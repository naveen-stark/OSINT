from main import main as mn
import os
def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    ch = int(input("\n1. Sock puppet check-list\n2. Persona creation\n3. ID and Password Manager\n4. Back\n>"))
    if ch == 2:    
        while(True):
            ch2 = int(input("\n1. Social media accounts\n2. Fake face generator\n3. Back\n>"))

            if ch2 == 1:
                ch3 = int(input("\n1. Twitter\n2. Tumblr\n3. Instagram\n4. Pinterest\n5. Back\n>"))

                if ch3 == 1:
                    import Twitter_sock_puppet as tsp
                    tsp.main()
                    input("Press any key to go home")
                    mn()
                elif ch3 == 2:
                    import tumblr
                    tumblr.main()
                    input("Press any key to go home")
                    mn()
                elif ch3 == 3:
                    import Instagram_sock_puppet as isp
                    isp.main()
                    input("Press any key to go home")
                    mn()
                elif ch3 == 4:
                    import pinterest as psp
                    psp.main()
                    input("Press any key to go home")
                    mn()
                elif ch3 == 5:
                    import main
                    main.main()
                    input("Press any key to go home")
                    mn()
        
            elif ch2 == 2:
                import thispersondoesnotexist as tpdne
                tpdne.main()
                input("Press any key to go home")
                mn()

            else:
                import main
                main.main()

    elif ch == 1:
        checklist = open(dir_path + '\guidelinestxt.txt', 'r')
        print(checklist.read())
        input("Press any key to go home")
        mn()

    elif ch == 3:
        try:
            iapm = open(dir_path + '\Sock account details.txt', 'r')
            print(iapm.read())
            input("Press any key to go home")
            mn()
        except:
            print("No sock puppet created")
    
    else:
        import main
        main.main()

if __name__ == "__main__":
    main()