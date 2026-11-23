# Importa as bibliotecas necessárias
import cv2
import time
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from ultralytics import YOLO

# 1. Carrega a rede neural pré-treinada YOLOv8 (Deep Learning)
modelo = YOLO("yolov8n.pt")

# 2. Liga a webcam padrão do computador
video_capture = cv2.VideoCapture(0)

# Variáveis para controlar tempos, infrações e pausas entre fotografias
tempo_focado = 0.0
tempo_distraido = 0.0
infracoes = 0
ultima_foto = 0
tempo_anterior = time.time()

# 3. Loop infinito para analisar o vídeo em tempo real
while True:
    # Captura um frame (imagem) da câmara
    ret, frame = video_capture.read()
    if not ret:
        break

    # Calcula quanto tempo passou desde o último frame
    tempo_atual = time.time()
    diferenca = tempo_atual - tempo_anterior
    tempo_anterior = tempo_atual

    # Envia a imagem para a IA detetar objetos (confiança mínima de 50%)
    resultados = modelo(frame, conf=0.5, verbose=False)

    # Verifica se existe algum telemóvel entre os objetos detetados
    smartphone_detetado = False
    for caixa in resultados[0].boxes:
        id_classe = int(caixa.cls[0])
        nome_objeto = modelo.names[id_classe]

        if nome_objeto == "cell phone":
            smartphone_detetado = True

    # Atualiza os cronómetros consoante o estado atual
    if smartphone_detetado:
        tempo_distraido += diferenca
    else:
        tempo_focado += diferenca

    # Desenha as caixas automáticas do YOLOv8 na imagem
    frame_ia = resultados[0].plot()
    altura, largura, _ = frame_ia.shape

    # Desenha o painel preto no canto superior esquerdo
    cv2.rectangle(frame_ia, (15, 15), (470, 130), (0, 0, 0), -1)

    # Mostra os cronómetros e o número de infrações no ecrã
    cv2.putText(frame_ia, f"Focado: {int(tempo_focado)}s | Distraido: {int(tempo_distraido)}s",
                (25, 48), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(frame_ia, f"Infracoes registadas: {infracoes}",
                (25, 82), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    # Se detetar telemóvel: ativa o alarme vermelho, tira foto e guarda no relatório
    if smartphone_detetado:
        cv2.rectangle(frame_ia, (5, 5), (largura - 5, altura - 5), (0, 0, 255), 10)
        cv2.putText(frame_ia, "ALERTA: Smartphone detetado!",
                    (25, 118), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

        # Só tira uma nova foto a cada 5 segundos (para não encher o computador de fotos)
        if tempo_atual - ultima_foto > 5:
            infracoes += 1
            ultima_foto = tempo_atual
            hora = datetime.now().strftime("%H:%M:%S")
            nome_foto = f"prova_{infracoes}.jpg"

            # Guarda a fotografia da infração na pasta do projeto
            cv2.imwrite(nome_foto, frame_ia)

            # Regista a hora da infração num ficheiro de texto
            with open("relatorio_foco.txt", "a", encoding="utf-8") as ficheiro:
                ficheiro.write(f"Infração #{infracoes} às {hora} - Foto: {nome_foto}\n")
    else:
        cv2.putText(frame_ia, "Estado: Focado no trabalho",
                    (25, 118), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    # Mostra o vídeo no ecrã
    cv2.imshow("FocusGuard AI - Pressione 'q' para terminar", frame_ia)

    # Encerra o loop quando a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 4. Liberta a câmara e fecha a janela do vídeo
video_capture.release()
cv2.destroyAllWindows()

# 5. Gera automaticamente o gráfico final de produtividade com Matplotlib
if tempo_focado + tempo_distraido > 0:
    valores = np.array([tempo_focado, tempo_distraido])
    etiquetas = ["Tempo Focado", "Tempo Distraído"]
    cores = ["#2ecc71", "#e74c3c"]

    plt.pie(valores, labels=etiquetas, colors=cores, autopct="%1.1f%%", startangle=90)
    plt.title(f"Relatório FocusGuard AI (Infrações: {infracoes})")
    plt.legend()
    plt.savefig("grafico_produtividade.png")
    plt.show()