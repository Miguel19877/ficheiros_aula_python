lanche = ('Hamburguer', 'sumo', 'pizza', 'pudim')

#Todos os Elementos da tupla
print("Todos os elementos da tupla: ", lanche)
#ou
for comida in lanche:
    print(comida)

#A pizza
print("A pizza é: ", lanche[2])
#ou
#Independente da posição, a pizza
pizzaindex = lanche.index('pizza')
if pizzaindex != -1:
    print("A pizza está na posição: ", pizzaindex)
    print("A pizza é: ", lanche[pizzaindex])