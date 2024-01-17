import os
import datetime

def ler_arquivos_por_usuario_e_data(diretorio, usuario, data):
    # Lista para armazenar as linhas encontradas
    linhas_encontradas = []

    # Percorre todos os arquivos no diretório
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            # Verifica se o arquivo termina com "item.txt"
            if file.endswith("item.txt"):
                caminho_arquivo = os.path.join(root, file)

                # Abre o arquivo e lê suas linhas
                with open(caminho_arquivo, 'r') as arquivo:
                    for linha in arquivo:
                        # Divide a linha usando espaço como delimitador
                        partes = linha.split(" ")

                        # Extrai a data e o usuário
                        data_log = partes[0][1:]  # [15-01-24 -> 15-01-24
                        usuario_log = partes[3][1:-1]  # "Tranduir" -> Tranduir

                        # Verifica se a linha contém o usuário e a data dentro do range
                        if (data_log == data) and (usuario_log == usuario):
                            linhas_encontradas.append(linha)

    # Escreve as linhas encontradas em um novo arquivo
    with open('resultado.txt', 'w') as resultado_file:
        for linha_encontrada in linhas_encontradas:
            resultado_file.write(linha_encontrada)

# INPUTS
usuario = input("Digite o nome do usuário: ")
data = input("Digite a data do LOG (DD-MM-AA): ")

diretorio_logs = r"C:\Users\Paulo-PC\Zomboid\Logs"

ler_arquivos_por_usuario_e_data(diretorio_logs, usuario, data)
print("Resultado salvo em resultado.txt")
