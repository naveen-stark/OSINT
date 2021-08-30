from main import main as mn
def main():
    ch = int(input("\n1. EXIF extractor\n2. Email\n3. Username OSINT\n4. Social media\n5. Back\n>"))
    if ch == 1:    
        import exif 
        exif.main()
    
    elif ch == 2:
        ch2 = int(input("1. Find emails\n2. Email checker\n3. Back\n>"))
        if ch2 == 1:
            import Phonebook as pb 
            pb.main()
            input("Press any key to go home")
            mn()

        elif ch2 == 2:
            import emailverify as ev
            ev.main()
            input("Press any key to go home")
            mn()

        else:
            import main
            main.main()
    
    elif ch == 3:
        import usernamechecker as uc
        uc.main()
        input("Press any key to go home")
        mn()
    
    elif ch == 4:
        ch3 = int(input("\n1. Facebook\n2. Twitter\n3. Reddit\n4. Telegram\n5. Back\n>"))
        if ch3 == 1:
            ch4 = int(input("\n1. Facebook Image Extractor\n2. Facebook Data Extractor\n3. Back\n"))
            if ch4 == 1:
                import facebookimage as fbi 
                fbi.main()
                input("Press any key to go home")
                mn()
            elif ch4 == 2:
                import facescrape as fs 
                fs.main()
                input("Press any key to go home")
                mn()
            else:
                import main 
                main.main()

        elif ch3 == 2:
            import person_twitter as pt 
            pt.main()
            input("Press any key to go home")
            mn()
        
        elif ch3 == 4:
            import telegago as tg 
            tg.main()
            input("Press any key to go home")
            mn()

        elif ch3 == 3:
            import reddit2 
            reddit2.main()
            input("Press any key to go home")
            mn()

        else:
            import main
            main.main()
    else:
        import main
        main.main()

if __name__ == '__main__':
    main()



    
    