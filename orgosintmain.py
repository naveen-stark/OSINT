from main import main as mn
def main():
    ch = int(input("\n1. Website OSINT\n2. Organization data\n3. Back\n>"))
    if ch == 1:    
        while(True):
            ch2 = int(input("\n1. Website reconnaissance\n2. IOT reconnaissance\n3. Wayback\n4. Reverse\n>"))
            if ch2 == 1:
                import osint_sh as osh
                osh.main()
                input("Press any key to go home")
                mn()

            elif ch2 == 2:
                import shodan 
                shodan.main()
                input("Press any key to go home")
                mn()

            elif ch2 == 3:
                import wayback 
                wayback.main()
                input("Press any key to go home")
                mn()

            elif ch2 == 4:
                import reverse 
                reverse.main()
                input("Press any key to go home")
                mn()
               
            else:
                continue


    elif ch == 2:
        ch2 = int(input("\n1. Business Records\n2. Email Breach Checker\n>"))
        if ch2 == 1:
            import businessrecords as br
            br.main()
            input("Press any key to go home")
            mn()
        elif ch2 == 2:
            import breachedata as bd
            bd.main()
            input("Press any key to go home")
            mn()
    else:
        import main
        main.main()



if __name__ == "__main__":
    main()