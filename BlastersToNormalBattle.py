import sys
import os

def hex_replacement(file, blasters_hex, normalbattle_hex):
    with open(file, 'rb') as file:
        content = file.read()

    content = content.replace(bytes.fromhex(blasters_hex), bytes.fromhex(normalbattle_hex))

    with open(file, 'wb') as file:
        file.write(content)

if len(sys.argv) != 2:
    print("""You have to use: python BlastersToNormalBattle.py [your_folder_name], ur nerd🤓""")
    sys.exit(1)

folder_name = sys.argv[1]

# Get the current directory
current_directory = os.getcwd()

# Combine the current directory with the folder name
folder_path = os.path.join(current_directory, folder_name)

# Check if the directory exists
if not os.path.exists(folder_path):
    print("There is no such folder:", folder_path)
    sys.exit(1)

# Iterate over all the files in the folder
for file in os.listdir(folder_path):
    full_path = os.path.join(folder_path, file)
    if os.path.isfile(full_path):
# Idle
        hex_replacement(full_path, "3C9C0F4C", "2F605CC8")
# Long Idle
        hex_replacement(full_path, "B83275BC", "1794B02D")
# Sleeping/Tired Animation
        hex_replacement(full_path, "30737FC5", "238F2C41")
# Recovering Animation
        hex_replacement(full_path, "6DD8FD46", "7E1540AB")
#Attack Animation
        hex_replacement(full_path, "CAA1A2CF", "9812A99B")
#Guard
        hex_replacement(full_path, "477AAA9D", "B1014E48")
#Victory Pose 1
        hex_replacement(full_path, "DEE71A37", "AB007C21")
#Victory Pose 2
        hex_replacement(full_path, "B8CDC1CC", "115175B8")
#Victory Pose 3
        hex_replacement(full_path, "45181E68", "876172CF")
#Damage
        hex_replacement(full_path, "84658040", "D6D68B14")
#Death
        hex_replacement(full_path, "7616E5FB", "B18581B5")
#L. Death frame
        hex_replacement(full_path, "29D3F514", "A9E0BB11")
#Charge Animation
        hex_replacement(full_path, "174B937D", "04B7C0F9")
#Inspirit Animation
        hex_replacement(full_path, "A68A266D", "4D03C3B7")
#Soultimate Attack Animation
        hex_replacement(full_path, "06E0502D", "0A8E77DE")
#Miss/Dodge
        hex_replacement(full_path, "BFF13AD5", "CD2AA7DA")