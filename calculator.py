from graphics import plotar_grafico  # Certifique-se de que a função plotar_grafico está no arquivo graphics.py

class Calculator():
    def __init__(self):
        self.montanteSemContribuicao = 0
        self.montanteContribuicao = 0
        self.capital = 0
        self.taxa = 0
        self.tempo = 0
        self.unidadeTempo = 'ano'

    def tipoTempo(self):
        try:
            self.unidadeTempo = input("Digite a unidade de tempo desejada (dias, mes, ano): ").strip().lower()
            if self.unidadeTempo not in ('dia', 'mes', 'ano'):
                raise ValueError("Tipo de tempo inválido. Escolha entre 'dia', 'mes' ou 'ano'.")
            return True
        except ValueError as e:
            print(e)
            return False
        
    def calcularMontanteFinal(self):
        try:
            self.capital = int(input("Defina o capital aplicado: "))
            self.taxa = int(input("Defina a taxa: "))
            self.tempo = int(input(f"Defina o tempo ({self.unidadeTempo}): "))

            if self.capital <= 0 or self.taxa <= 0 or self.tempo <= 0:
                raise ValueError("Os valores de capital, taxa e tempo devem ser positivos.")

            self.montanteSemContribuicao = self.capital * ((1 + (self.taxa)/100)**self.tempo)
        except ValueError as e:
            print(f"Erro ao calcular o montante: {e}")

    def simularContribuicoes(self):
        try:
            self.capital = int(input("Defina o capital aplicado: "))
            self.taxa = int(input("Defina a taxa: "))
            self.tempo = int(input(f"Defina o tempo ({self.unidadeTempo}): "))
            valorContribuicoes = int(input("Defina o valor das contribuições periódicas: "))

            if self.capital <= 0 or self.taxa <= 0 or self.tempo <= 0 or valorContribuicoes < 0:
                raise ValueError("Os valores de capital, taxa, tempo e contribuição devem ser positivos.")

            # Listas para armazenar o tempo e os montantes ao longo do tempo
            tempos = list(range(1, self.tempo + 1)) 
            montantes_com_contribuicoes = []
            montantes_sem_contribuicoes = []

            for t in tempos:
                # Calculando montante com contribuições periódicas
                montante_com_contribuicao = (self.capital * ((1 + self.taxa / 100) ** t)) + valorContribuicoes * (((1 + self.taxa / 100) ** t - 1) / (self.taxa / 100))
                montantes_com_contribuicoes.append(montante_com_contribuicao)

                # Calculando montante sem contribuições periódicas
                montante_sem_contribuicao = self.capital * ((1 + self.taxa / 100) ** t)
                montantes_sem_contribuicoes.append(montante_sem_contribuicao)

            return tempos, montantes_com_contribuicoes, montantes_sem_contribuicoes
        
        except ValueError as e:
            print(f"Erro ao simular contribuições: {e}")
            return [], [], []

    def mostrarDetalhes(self):
        try:
            if self.montanteSemContribuicao == 0:
                raise ValueError("O montante não foi calculado ainda. Por favor, calcule o montante final primeiro.")
            
            print("\nResumo do Cálculo:")
            print(f"Capital Inicial: {self.capital}")
            print(f"Taxa de Juros: {self.taxa}%")
            print(f"Tempo: {self.tempo} {self.unidadeTempo}")
            print(f"Montante Final: {self.montanteSemContribuicao:.2f} reais")
        
        except ValueError as e:
            print(f"Erro: {e}")
