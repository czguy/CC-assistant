import assistant
print("loading...")
print("PassManager V1.0")

def writefile():
    print("you can leave any of the fields, in case you don't remember\nor have. (for example email)")
    inpnm = input("Password is for: ")
    inpusrnm = input("Username: ")
    inppsswd = input("Password: ")
    inpmail = input("Email: ")

    with open("/home/codecube/CC-assistant/assistant/pass.txt", "a") as fileap:
        fileap.write(inpnm)
        fileap.write("---")
        fileap.write(inpusrnm)
        fileap.write("---")
        fileap.write(inppsswd)
        fileap.write("---")
        fileap.write(inpmail)

def readfile():
    with open("/home/codecube/CC-assistant/assistant/pass.txt", "r") as filerd:
        storenum = []
        k=-1

        for i in range(0, len(filerd.readlines())):
            storenum.append(i)

        filerd.seek(0)
        for j in filerd.readlines():
            filerd.seek(0)
            k+=1
            print(storenum[k]+1,"\b.", j)
def passman():
    while True:
        inppassman = input("passmanager-> ")         
        if inppassman == "/r":
            readfile()
        elif inppassman == "/w":
            writefile()
        elif inppassman == "/cls":
            assistant.clear()
        elif inppassman == "/e":
            assistant.startassistant()
        else:
            print("command doesn't exist!")