def convertToTitle(columnNumber: int):
      if columnNumber <=26:
              return chr(columnNumber+64)
      else:
            res=[]  
            res.append(chr(columnNumber%26))
            columnNumber-=columnNumber%26
            while columnNumber >1:
                  x=columnNumber/26
                  if x>26:
                         res.append("A")
                         columnNumber=columnNumber/26
                  else:
                         res.append(chr(columnNumber+64))
      res=res[::-1]
      res=res.join()
      return res

print(convertToTitle(701))
