while True:
    print("""
NOKIA 3310 MENU

1. Phone Book
2. Messages
3. Chat
4. Call Register
5. Tones
6. Settings
7. Call Divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM Services
14. Exit
""")

    menu = int(input("Enter Menu 1 - 14: "))

    match menu:

        case 1:
            while True:
                print("PHONE BOOK")
                print("1. Search")
                print("2. Service Nos.")
                print("3. Add Name")
                print("4. Erase")
                print("5. Edit")
                print("6. Assign Tone")
                print("7. Send B'card")
                print("8. Options")
                print("9. Speed Dials")
                print("10. Voice Tags")
                print("0. Back")

                phone_book = int(input("Enter Option 1 - 10 or 0 to go back: "))

                if phone_book == 0:
                    break

                match phone_book:
                    case 1:
                        print("Search")
                    case 2:
                        print("Service Nos.")
                    case 3:
                        print("Add Name")
                    case 4:
                        print("Erase")
                    case 5:
                        print("Edit")
                    case 6:
                        print("Assign Tone")
                    case 7:
                        print("Send B'card")
                    case 8:
                        while True:
                            print("OPTIONS")
                            print("1. Type of View")
                            print("2. Memory Status")
                            print("0. Back")

                            option = int(input("Enter Option 1 - 2 or 0 to go back: "))

                            if option == 0:
                                break

                            match option:
                                case 1:
                                    print("Type of View")
                                case 2:
                                    print("Memory Status")
                                case _:
                                    print("Invalid Option")

                    case 9:
                        print("Speed Dials")
                    case 10:
                        print("Voice Tags")
                    case _:
                        print("Invalid Option")

        case 2:
            while True:
                print("MESSAGES")
                print("1. Write Messages")
                print("2. Inbox")
                print("3. Outbox")
                print("4. Picture Messages")
                print("5. Templates")
                print("6. Smileys")
                print("7. Message Settings")
                print("8. Info Service")
                print("9. Voice Mailbox Number")
                print("10. Service Command Editor")
                print("0. Back")

                message = int(input("Enter Option 1 - 10 or 0 to go back: "))

                if message == 0:
                    break

                match message:
                    case 1:
                        print("Write Messages")
                    case 2:
                        print("Inbox")
                    case 3:
                        print("Outbox")
                    case 4:
                        print("Picture Messages")
                    case 5:
                        print("Templates")
                    case 6:
                        print("Smileys")
                    case 7:
                        while True:
                            print("MESSAGE SETTINGS")
                            print("1. Set 1")
                            print("2. Common")
                            print("0. Back")

                            settings = int(input("Enter Option 1 to 2 or 0 to go back: "))

                            if settings == 0:
                                break

                            match settings:
                                case 1:
                                    print("SET 1")
                                    print("1. Message Centre Number")
                                    print("2. Messages Sent As")
                                    print("3. Message Validity")
                                case 2:
                                    print("COMMON")
                                    print("1. Delivery Reports")
                                    print("2. Reply Via Same Centre")
                                    print("3. Character Support")
                                case _:
                                    print("Invalid Option")

                    case 8:
                        print("Info Service")
                    case 9:
                        print("Voice Mailbox Number")
                    case 10:
                        print("Service Command Editor")
                    case _:
                        print("Invalid Option")

        case 3:
            print("CHAT")

        case 4:
            while True:
                print("CALL REGISTER")
                print("1. Missed Calls")
                print("2. Received Calls")
                print("3. Dialled Numbers")
                print("4. Erase Recent Call Lists")
                print("5. Show Call Duration")
                print("6. Show Call Costs")
                print("7. Call Cost Settings")
                print("8. Prepaid Credit")
                print("0. Back")

                call = int(input("Enter Option 1 - 8 or 0 to go back: "))

                if call == 0:
                    break

                match call:
                    case 1:
                        print("Missed Calls")
                    case 2:
                        print("Received Calls")
                    case 3:
                        print("Dialled Numbers")
                    case 4:
                        print("Erase Recent Call Lists")
                    case 5:
                        print("Show Call Duration")
                    case 6:
                        print("Show Call Costs")
                    case 7:
                        print("Call Cost Settings")
                    case 8:
                        print("Prepaid Credit")
                    case _:
                        print("Invalid Option")

        case 5:
            while True:
                print("TONES")
                print("1. Ringing Tone")
                print("2. Ringing Volume")
                print("3. Incoming Call Alert")
                print("4. Composer")
                print("5. Message Alert Tone")
                print("6. Keypad Tones")
                print("7. Warning Tones")
                print("8. Vibrating Alert")
                print("9. Screen Saver")
                print("0. Back")

                tones = int(input("Enter Option 1 - 9 or 0 to go back: "))

                if tones == 0:
                    break

                match tones:
                    case 1:
                        print("Ringing Tone")
                    case 2:
                        print("Ringing Volume")
                    case 3:
                        print("Incoming Call Alert")
                    case 4:
                        print("Composer")
                    case 5:
                        print("Message Alert Tone")
                    case 6:
                        print("Keypad Tones")
                    case 7:
                        print("Warning Tones")
                    case 8:
                        print("Vibrating Alert")
                    case 9:
                        print("Screen Saver")
                    case _:
                        print("Invalid Option")

        case 6:
            while True:
                print("SETTINGS")
                print("1. Call Settings")
                print("2. Phone Settings")
                print("3. Security Settings")
                print("4. Restore Factory Settings")
                print("0. Back")

                setting = int(input("Enter Option 1 - 4 or 0 to go back: "))

                if setting == 0:
                    break

                match setting:
                    case 1:
                        print("CALL SETTINGS")
                        print("1. Automatic Redial")
                        print("2. Speed Dialling")
                        print("3. Call Waiting Options")
                        print("4. Own Number Sending")
                        print("5. Phone Line In Use")
                        print("6. Automatic Answer")

                    case 2:
                        print("PHONE SETTINGS")
                        print("1. Language")
                        print("2. Cell Info Display")
                        print("3. Welcome Note")
                        print("4. Network Selection")
                        print("5. Lights")
                        print("6. Confirm SIM Service Actions")

                    case 3:
                        print("SECURITY SETTINGS")
                        print("1. PIN Code Request")
                        print("2. Call Barring Service")
                        print("3. Fixed Dialling")
                        print("4. Closed User Group")
                        print("5. Phone Security")
                        print("6. Change Access Codes")

                    case 4:
                        print("Restore Factory Settings")

                    case _:
                        print("Invalid Option")

        case 7:
            print("CALL DIVERT")

        case 8:
            print("GAMES")

        case 9:
            print("CALCULATOR")

        case 10:
            print("REMINDERS")

        case 11:
            while True:
                print("CLOCK")
                print("1. Alarm Clock")
                print("2. Clock Settings")
                print("3. Date Setting")
                print("4. Stopwatch")
                print("5. Countdown Timer")
                print("6. Auto Update Date and Time")
                print("0. Back")

                clock = int(input("Choose Option 1 - 6 or 0 to go back: "))

                if clock == 0:
                    break

                match clock:
                    case 1:
                        print("Alarm Clock")
                    case 2:
                        print("Clock Settings")
                    case 3:
                        print("Date Setting")
                    case 4:
                        print("Stopwatch")
                    case 5:
                        print("Countdown Timer")
                    case 6:
                        print("Auto Update Date and Time")
                    case _:
                        print("Invalid Option")

        case 12:
            print("PROFILES")

        case 13:
            print("SIM SERVICES")

        case 14:
            print("Exit")
            break

        case _:
            print("Invalid Menu")
