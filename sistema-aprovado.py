aprovados_vestibular = []

quantos_passaram = int(input("quantos foram aprovados: "))

#Laço de repetição que adiciona nomes que foram aprovados no vestibular
for cont_passaram in range(quantos_passaram):
    aprovados_vestibular.append(input("Nome do aprovado: "))

#variavel que ira armazenar um valor para finalizar a pesquisa
finalizar_pesquisa = 0

#Laço de repetição para realisar a pesquisa do nome
while True:
    if finalizar_pesquisa == 1:
        break
    pesquisa = input("digite o nome que deseja ver se foi aprovado: ")
    achou_aprovado = False
    for cont_passaram in range(len(aprovados_vestibular)):
        if pesquisa == aprovados_vestibular[cont_passaram]:
            print("Parabens o ", aprovados_vestibular[cont_passaram]," foi aprovado")
            achou_aprovado = True
            break
    if achou_aprovado == False:
        print("Infelizmente está pessoa não foi aprovado")
    finalizar_pesquisa = int(input("Se deseja finalzar sua pesquisa aperte a tecla 1, se deseja continuar aperte a tecla 0: "))