import ast

def decodeHuffman(inputFile):
    decodedText = ""
    currentCode = ""
    try:
        with open(inputFile, "r", encoding="utf-8") as file:
            data = file.readlines()
    except Exception as error:
        print(f"Błąd odczytu pliku: {error}")
        return

    dictionary = data[0].strip().replace("Słownik: ", "")
    huffmanCodes = ast.literal_eval(dictionary)
    text = data[1].strip().replace("Skompresowany tekst: ", "")


    for code in text:
        currentCode += code
        for char, code in huffmanCodes.items():
            if code == currentCode:
                decodedText += char
                currentCode = ""
                break

    try:
        with open("deszyfr.txt", "w", encoding="utf-8") as fileOutput:
            fileOutput.write(decodedText)
    except Exception as error:
        print(f"Błąd: {error}")


inputFile = input("Podaj plik z kodem huffmana: ")
decodeHuffman(inputFile)
