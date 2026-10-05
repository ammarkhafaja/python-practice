# def convertToTitle(columnNumber: int):
#       if columnNumber <=26:
#               return chr(columnNumber+64)
#       else:
#             res=[]  
#             while columnNumber >=1:                        
#                   if columnNumber>26:
#                          if columnNumber%26==0:
#                               if columnNumber/26 >26:
#                                     res.append(chr((int((columnNumber/26)%26))+64))
#                               else:
#                                     res.append(chr((int(columnNumber%26))+64))
#                                     columnNumber=columnNumber//26
                        
                        
#                   else:
#                          res.append(chr(int(columnNumber)+64))
#                          break
#       res=res[::-1]
#       res="".join(res)
#       return res
def convertToTitle(columnNumber: int):
      if(columnNumber%26==0):
            return chr(int(columnNumber/2)+64)
      if columnNumber <=26:
            return chr(int(columnNumber)+64)
      return convertToTitle(columnNumber%26)+convertToTitle(columnNumber//26)

print(convertToTitle(52))
