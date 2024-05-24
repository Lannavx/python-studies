"""
    Faça um programa que peça o tamanho de um arquivo para download (em MB) 
    e a velocidade de um link de Internet (em Mbps), calcule e informe o 
    tempo aproximado de download do arquivo usando este link (em minutos).
"""

tamanho = float(input('Informe o tamanho do seu arquivo para download: '))
velocidade = int(input('Informe a velocidade do link: '))

#calculo do tempo de download
#converte a velocidade de Mbps para MBps e calcula o tempo em minutos

tempo_download = tamanho / (velocidade / 8 ) / 60
print(f'O tempo aproximado de download do arquivo é de {tempo_download:.2f} minutos')