def interface():
    print("   0   1   2  ")
    print("0 [{}] [{}] [{}]".format(tabuleiro [0][0], tabuleiro [0][1], tabuleiro [0][2]))
    print("1 [{}] [{}] [{}]".format(tabuleiro [1][0], tabuleiro [1][1], tabuleiro [1][2]))
    print("2 [{}] [{}] [{}]".format(tabuleiro [2][0], tabuleiro [2][1], tabuleiro [2][2]))

def validarVitoria(rodada):
    global parar 
    if(tabuleiro[0][0] == rodada and tabuleiro[0][1] == rodada and tabuleiro[0][2] == rodada):
        interface()
        print("O {} Venceu!".format(rodada))
        parar = True 
   

tabuleiro = [[" "," "," ",], [" "," "," ",], [" "," "," ",]]

parar = False
rodada = "x"
jogadas = 0

while parar == False:
    if jogadas == 9:
        interface()
        print("Empate!")
        parar = True 
    interface()

    linha = int(input("Digite a linha escolhida:"))
    coluna = int(input("Digite a coluna escolhida:"))

    if rodada == "x":
        tabuleiro[linha][coluna] = "x"
        jogadas += 1
        rodada = "O"


    elif rodada == "O":
        tabuleiro[linha][coluna] = "o"
        jogadas += 1 
        rodada = "x"

    

print ("Programa encerrado. ")        



