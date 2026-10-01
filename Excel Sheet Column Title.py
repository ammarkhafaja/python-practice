def convertToTitle(columnNumber: int):
        if columnNumber <=26:
              return chr(columnNumber+64)
        else:
            numofchar=1
            while columnNumber>1:
                columnNumber/26
                numofchar+=1

print(convertToTitle(2))