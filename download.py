tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_internet_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))

velocidade_internet_mbs = velocidade_internet_mbps * 0.125
tempo_download_minutos = tamanho_arquivo_mb / velocidade_internet_mbs / 60

print(f"O tempo aproximado de download do arquivo é de {tempo_download_minutos:.2f} minutos.")
