import sys
import os

def substituir_sequencia(arquivo, sequencia_antiga, sequencia_nova):
    with open(arquivo, 'rb') as file:
        conteudo = file.read()

    conteudo = conteudo.replace(bytes.fromhex(sequencia_antiga), bytes.fromhex(sequencia_nova))

    with open(arquivo, 'wb') as file:
        file.write(conteudo)

if len(sys.argv) != 2:
    print("""You have to use: python BlastersToNormalBattle.py [your_folder_name], ur nerd🤓""")
    sys.exit(1)

nome_da_pasta = sys.argv[1]

# Obter o diretório atual
diretorio_atual = os.getcwd()

# Combinar o diretório atual com o nome da pasta
caminho_da_pasta = os.path.join(diretorio_atual, nome_da_pasta)

# Verificar se o diretório existe
if not os.path.exists(caminho_da_pasta):
    print("There is no such folder:", caminho_da_pasta)
    sys.exit(1)

# Iterar sobre todos os arquivos na pasta
for arquivo in os.listdir(caminho_da_pasta):
    caminho_completo = os.path.join(caminho_da_pasta, arquivo)
    if os.path.isfile(caminho_completo):
# Idle
        substituir_sequencia(caminho_completo, "3C9C0F4C", "2F605CC8")
# Long Idle
        substituir_sequencia(caminho_completo, "B83275BC", "1794B02D")
# Sleeping/Tired Animation
        substituir_sequencia(caminho_completo, "30737FC5", "238F2C41")
# Recovering Animation
        substituir_sequencia(caminho_completo, "6DD8FD46", "7E1540AB")
#Attack Animation
        substituir_sequencia(caminho_completo, "CAA1A2CF", "9812A99B")
#Guard
        substituir_sequencia(caminho_completo, "477AAA9D", "B1014E48")
#Victory Pose 1
        substituir_sequencia(caminho_completo, "DEE71A37", "AB007C21")
#Victory Pose 2
        substituir_sequencia(caminho_completo, "B8CDC1CC", "115175B8")
#Victory Pose 3
        substituir_sequencia(caminho_completo, "45181E68", "876172CF")
#Damage
        substituir_sequencia(caminho_completo, "84658040", "D6D68B14")
#Death
        substituir_sequencia(caminho_completo, "7616E5FB", "B18581B5")
#L. Death frame
        substituir_sequencia(caminho_completo, "29D3F514", "A9E0BB11")
#Charge Animation
        substituir_sequencia(caminho_completo, "174B937D", "04B7C0F9")
#Inspirit Animation
        substituir_sequencia(caminho_completo, "A68A266D", "4D03C3B7")
#Soultimate Attack Animation
        substituir_sequencia(caminho_completo, "06E0502D", "0A8E77DE")
#Miss/Dodge
        substituir_sequencia(caminho_completo, "BFF13AD5", "CD2AA7DA")