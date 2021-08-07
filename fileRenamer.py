import os

def Directory():
    os.system('cls')
    directory = input(r"Input the location of the directory containing the files you want to be neatened: ")
    if os.path.isdir(directory):
        os.chdir(directory)
        print(os.getcwd())
        Neatening()
    else:
        print("That location does not exist, try again")
        Directory()

def Neatening():
    os.system('cls')
    for files in os.listdir():
        indexCount = -1
        CharList = []
        Year = ""
        newName = ""

        file_name, file_extension = os.path.splitext(files)
        file_name = file_name.replace("."," ")

        for i in file_name:
            indexCount += 1
            CharList.append(i)
            if i.isdigit():
                Year += str(i)
                if Year == str(720) or Year == str(480):
                    CharList = CharList[:-3]
                    break
                if len(Year) == 4:
                    if Year == 1080:
                        CharList = CharList[:-4]
                        break  
                    if CharList[indexCount-4] != "(":
                        CharList.insert(indexCount-3,"(")
                    CharList.append(")") 
                    break
            else:
                Year = ""
        for i in CharList:
            newName += i
        newName = newName.strip()
        newName += file_extension
        os.rename(files,newName)

Directory()