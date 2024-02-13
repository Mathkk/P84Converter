import sys
import os

def hex_replacement(file_path, blasters_hex, normalbattle_hex):
    with open(file_path, 'rb') as file:
        content = file.read()

    content = content.replace(bytes.fromhex(blasters_hex), bytes.fromhex(normalbattle_hex))

    with open(file_path, 'wb') as file_write:
        file_write.write(content)

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
# Idle YKW2
        hex_replacement(full_path, "2F605CC8", "3C9C0F4C")
# Long Idle YKW2
        hex_replacement(full_path, "1794B02D", "B83275BC")
# Sleeping/Tired Animation YKW 2
        hex_replacement(full_path, "238F2C41", "30737FC5")
# Recovering Animation YKW2
        hex_replacement(full_path, "7E1540AB", "6DD8FD46")
#Attack Animation YKW2
        hex_replacement(full_path, "9812A99B", "CAA1A2CF")
#Guard
        hex_replacement(full_path, "B1014E48", "477AAA9D")
#Victory Pose 1
        hex_replacement(full_path, "56E44DEC", "DEE71A37")
#Victory Pose 2
        hex_replacement(full_path, "95B760C7", "B8CDC1CC")
#Victory Pose 3
        hex_replacement(full_path, "D4867BDE", "45181E68")
#Damage
        hex_replacement(full_path, "D6D68B14", "84658040")
#Death
        hex_replacement(full_path, "B18581B5", "7616E5FB")
#L. Death frame
        hex_replacement(full_path, "A9E0BB11", "29D3F514")
#Charge Animation
        hex_replacement(full_path, "04B7C0F9", "174B937D")
#Inspirit Animation
        hex_replacement(full_path, "4D03C3B7", "A68A266D")
#Soultimate Attack Animation
        hex_replacement(full_path, "0A8E77DE", "06E0502D")
#Miss/Dodge
        hex_replacement(full_path, "CD2AA7DA", "BFF13AD5")