def dictutil():
    import assistant
    while True:
        j = False
        dictinp = input("Word: ")
        with open("/home/codecube/CC-assistant/assistant/dictionary.txt", "r") as file:
            #command check
            if dictinp == "/exit" or dictinp == "/e":
                assistant.startassistant()
                j = True
            elif dictinp == "/read" or dictinp == "/r":
                print(file.read())
                j = True
            elif dictinp == "/clear" or dictinp == "/cls":
                assistant.clear()
                j = True
            elif "/" in dictinp:
                    j = True
            elif dictinp == " ":
                pass
            #dictionary check
            with open("/home/codecube/CC-assistant/assistant/dictionary.txt", "r") as file:
                for i in file.readlines(): 
                    if dictinp in i:
                        print(i)
                        j = True
                if j != True:
                    print("Word didn't found")
                    enttransinp = input("Translation: ")
                    if enttransinp == "/c":
                        print("you canceled the word addition.")
                    else:
                        with open("/home/codecube/CC-assistant/assistant/dictionary.txt", "a") as fileap:
                            fileap.write("\n")
                            fileap.write(dictinp)
                            fileap.write(" - ")
                            fileap.write(enttransinp)
                        print("word added successfully!")
