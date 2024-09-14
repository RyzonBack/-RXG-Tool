import os
import fade
from fade import *

# Banner et menu
banner = """
                                    ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
                                    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                                    ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒▒▓███▓▒░ 
                                    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
                                         Discord.gg/r4xgt-community                                                                                                                 
"""
banner = fade.fire(banner)

menu = """                              
                              ╔════════════════════════════════════════════╗
                              ║  [1] 𝐈𝐃 𝐓𝐎 𝐓𝐎𝐊𝐄𝐍         [6] Loading       ║
                              ║  [2] 𝐓𝐎𝐊𝐄𝐍 𝐂𝐇𝐄𝐂𝐊𝐄𝐑       [7] Loading       ║
                              ║  [3] 𝐈𝐏 𝐋𝐨𝐨𝐤𝐮𝐩           [8] Loading       ║
                              ║  [4] 𝐎𝐛𝐟𝐮𝐬𝐜𝐚𝐭𝐨𝐫          [9] Loading       ║
                              ║  [5] Loading             [§] 𝐌𝐀𝐃𝐄 𝐁𝐘 𝐑✗𝐆   ║
                              ║        Discord.gg/r4xgt-community          ║
                              ╚════════════════════════════════════════════╝"""

menu = fade.fire(menu)

def main():
    while True:  
        os.system("cls")  
        print(banner)
        print()
        print(menu)
        choice = input("Choix : ")

        if choice == "1":
            os.system("python prgm/FIRST-TOKEN.py")
            input("\nAppuyez sur Entrée pour continuer...") 
        elif choice == "2":
            os.system("python prgm/TOKEN-CHECK.py")
            input("\nAppuyez sur Entrée pour continuer...")  
        elif choice == "3":
            os.system("python prgm/IP-LOOKUP.py")
            input("\nAppuyez sur Entrée pour continuer...") 
        elif choice == "4":
            os.system("python prgm/OBSTRUCATOR.py")
            input("\nAppuyez sur Entrée pour continuer...")  
        else:
            print("Merci de rentrer un nombre valide.")
            input("Appuyez sur Entrée pour revenir au menu...")  

if __name__ == "__main__":
    main()
