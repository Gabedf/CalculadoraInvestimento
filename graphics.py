import matplotlib.pyplot as plt

def plotar_grafico(tempos, montantes_com_contribuicoes, montantes_sem_contribuicoes, unidadeTempo):
    plt.figure(figsize=(14, 8))  # Aumentando o tamanho da figura

    # Linha para o montante com contribuições periódicas
    plt.plot(tempos, montantes_com_contribuicoes, label="Montante com Contribuições Periódicas", color='#007acc', marker='o', linestyle='-', linewidth=3, markersize=8, zorder=3)
    
    # Linha para o montante sem contribuições periódicas
    plt.plot(tempos, montantes_sem_contribuicoes, label="Montante sem Contribuições Periódicas", color='#ff7f0e', marker='s', linestyle='--', linewidth=3, markersize=8, zorder=3)

    # Personalizando o gráfico
    plt.title("Evolução do Montante ao Longo do Tempo", fontsize=20, fontweight='bold', color='darkslategray', pad=20)
    plt.xlabel(f"Tempo ({unidadeTempo.capitalize()})", fontsize=16, color='darkgreen', labelpad=15)
    plt.ylabel("Montante Final (R$)", fontsize=16, color='darkgreen', labelpad=15)

    # Ajustando o fundo e a grade
    plt.grid(True, linestyle='-', linewidth=0.5, alpha=0.7, color='gray')  # Grade mais suave
    plt.gca().set_facecolor('whitesmoke')  # Fundo do gráfico mais suave
    
    # Ajustando a visibilidade da legenda
    plt.legend(loc='upper left', fontsize=14, frameon=True, shadow=True, fancybox=True, title="Tipos de Montante", title_fontsize=14, bbox_to_anchor=(1.05, 1), borderaxespad=0.)

    # Ajustando os limites dos eixos para melhorar a visualização
    plt.xlim(min(tempos), max(tempos))
    plt.ylim(min(min(montantes_sem_contribuicoes), min(montantes_com_contribuicoes)) * 0.9, max(max(montantes_sem_contribuicoes), max(montantes_com_contribuicoes)) * 1.1)

    # Exibindo o gráfico
    plt.tight_layout()  # Ajustando para evitar sobreposição
    plt.show()
