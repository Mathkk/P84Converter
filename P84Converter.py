import sys
import os


# Replaces hex sequences in the binary file
def hex_replacement(file_path, to_replace, replace_with):
    with open(file_path, 'rb') as file:
        content= file.read()
        content = content.replace(bytes.fromhex(to_replace), bytes.fromhex(replace_with))
    with open(file_path, 'wb') as file_write:
        file_write.write(content)


hex_codes = {
    # idle
    "3C9C0F4C": "2F605CC8",
    # Long idle
    "B83275BC": "1794B02D",
    # Sleeping/Tired
    "30737FC5": "238F2C41",
    # Recovering
    "6DD8FD46": "7E1540AB",
    # Attack
    "CAA1A2CF": "9812A99B",
    # Guard
    "477AAA9D": "B1014E48",
    # Victory Pose 1
    "DEE71A37": "AB007C21",
    # Victory Pose 2
    "B8CDC1CC": "115175B8",
    # Victory Pose 3
    "45181E68": "876172CF",
    # Damage
    "84658040": "D6D68B14",
    # Death
    "7616E5FB": "B18581B5",
    # L. Death Frame
    "29D3F514": "A9E0BB11",
    # Charge Animation
    "174B937D": "04B7C0F9",
    # Inspirit Animation
    "A68A266D": "4D03C3B7",
    # Soultimate attack animation
    "06E0502D": "0A8E77DE",
    # Dodge/Miss
    "BFF13AD5": "CD2AA7DA"
}
def Main():
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        print("Usage: P84Converter.exe [blasters if you want to convert to blasters and normal if you want to convert to normal battle] [folder]");
        sys.exit(0);
    elif len(sys.argv) != 3:
        print("Usage: P84Converter.exe [blasters if you want to convert to blasters and normal if you want to convert to normal battle] [folder]");
        sys.exit(1);
    else:
        mode: str = sys.argv[1];
        folder_path: str = sys.argv[2];

        if not os.path.exists(folder_path):
            print(f"Folder does not exist: {folder_path}");
            sys.exit(1);

        # K is Blasters, V is normal battle
        if mode == "normal":
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                for k, v in hex_codes.items():
                    hex_replacement(file_path, k, v)
        elif mode == "blasters":
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                for k, v in hex_codes.items():
                    hex_replacement(file_path, v, k)
        else:
            print(f"Invalid mode: {mode}. Please refer to the help menu by running `P84Converter.exe -h`. ")
Main();