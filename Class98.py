""" f = open("E:/Python/Class98.txt", 'r+')
readData = f.read()

f.close()

def countWords(text):
    splitText = text.split(" ")
    print(splitText)
    return (len(splitText))

print(countWords(readData)) """

File1 = input('Enter File 1 name')
File2 = input('Enter File 2 name')

Ist_file = open(File1, 'r+')
readDataFromI = Ist_file.read()

IInd_file = open(File2, 'r+')
readDataFromII = IInd_file.read()

print(readDataFromII)

def exchangeText(text1, text2):
    Ist_file.write(text2)
    IInd_file.write(text1)

exchangeText(readDataFromI, readDataFromII)

Ist_file.close()
IInd_file.close()
