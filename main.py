import os
def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    clear = lambda: os.system('cls')
    clear()
    logo = open(dir_path + "\logo.txt", "r")
    print(logo.read())
    while(True):
        ch_main = int(input(">"))
        if ch_main == 1:
            print("\nACTIVE\nIntrusive reconnaissance that sends packets to the targeted system.")
            while(True):
                print("\n1. Yellow pages lookup\n2. Wifi Harvester\n3. Back")
                ch_active = int(input("\n>"))
                if ch_active == 1:
                    print("\nRetrieves information such as address, contact info, etc. of service providers / shops in the city\n")
                    import jimyellowpage as jp
                    jp.main()
                    input("Press any key to go home")
                    main()

                elif ch_active == 2:
                    print("\nRetrieves technical information about wifi networks and hotspots in the city\n")
                    import wigle 
                    wigle.main()
                    input("Press any key to go home")
                    main()

                else:
                    main()
            

        elif ch_main == 2:

            print("\nPASSIVE\nReconnaissance that either does not communicate directly to the targeted system or that uses commonly available public information.")
            
            while(True):

                print("\n1. Sock puppet\n2. Search Engine OSINT\n3. Organization OSINT\n4. Person OSINT\n5. Back")
                ch_active = int(input("\n>"))

                if ch_active == 1:
                    print("\nHelps create sock puppet accounts for various social media platforms.\n")
                    import sockpuppetmain as spm
                    spm.main()
                    input("Press any key to go home")
                    main()

                elif ch_active == 2:
                    print("\nThis module provides tools to search for information from the surface web and deep web.\n")
                    import searcheng as se
                    se.main()
                    input("Press any key to go home")
                    main()
                
                elif ch_active == 3:
                    print("\nTools to collect information and perform reconnaissance on an organization.\n")
                    import orgosintmain as oom
                    oom.main()
                    input("Press any key to go home")
                    main()

                elif ch_active == 4:
                    print("\nTools to collect information about a person.\n")
                    import personosintmain as pom
                    pom.main()
                    input("Press any key to go home")
                    main()

                else:
                    main()

        elif ch_main == 3:
            print("\nMITIGATION\nGeneral measures and guidelines to safeguard your information.")
            mitigation = open(dir_path + '\mitigation.txt', 'r')
            print(mitigation.read())
            input("Press any key to go home")
            main()
        else:
            print("\nChoose from the given options")

if __name__ == '__main__':
    main()
