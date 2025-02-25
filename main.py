from calculator import *  
from graphics import *

calc = Calculator()

# Inicialização de variáveis para armazenar dados necessários para o gráfico
tempos = []
montantes_com_contribuicoes = []
montantes_sem_contribuicoes = []

while True:
    try:
        mensagem = ("\n#------ESCOLHA UMA OPCAO------#\n"
                    + "1) Definir unidade de tempo (ano, mes, dia)\n" 
                    + "2) Calcular montante final\n"
                    + "3) Calcular montante levando em conta contribuições periódicas\n"
                    + "4) Mostrar gráfico do investimento pelo tempo\n"
                    + "0) Encerrar programa\n"
                    + "Escolha) ")

        opcao = int(input(mensagem))  # Tenta ler a opção do menu

        if opcao == 1:
            if not calc.tipoTempo(): 
                print("Tipo de tempo incorreto.")
        elif opcao == 2: 
            calc.calcularMontanteFinal()
            print(f"Montante sem contribuições: {calc.montanteSemContribuicao:.2f}")
        elif opcao == 3:
            # Simular os montantes com e sem contribuições
            tempos, montantes_com_contribuicoes, montantes_sem_contribuicoes = calc.simularContribuicoes()
            print(f"Último montante com contribuições periódicas: {montantes_com_contribuicoes[-1]:.2f}")
            print(f"Último montante sem contribuições periódicas: {montantes_sem_contribuicoes[-1]:.2f}")
        elif opcao == 4:
            # Verifica se os dados necessários para o gráfico foram calculados
            if tempos and montantes_com_contribuicoes and montantes_sem_contribuicoes:
                plotar_grafico(tempos, montantes_com_contribuicoes, montantes_sem_contribuicoes, calc.unidadeTempo)
            else:
                print("É necessário calcular os montantes antes de mostrar o gráfico.")
        elif opcao == 0:
            encerrar = input("Encerrando o programa...\nDigite enter para encerrar) ")
            break  # Sai do loop e encerra o programa
        else:
            print("Opção inválida. Tente novamente.")
    
    except ValueError as e:
        # Captura e trata exceções de entradas inválidas, como se o usuário digitar texto quando for esperado um número
        print(f"Erro de entrada: {e}. Por favor, insira um número válido.")

    except Exception as e:
        # Captura outros tipos de exceções inesperadas
        print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.")
