def generate(numRows: int) -> list[list[int]]:
        res=[]
        line=[]
        linenum=1
        if numRows==0:return res.append([])
        while linenum<=numRows:
            line=[1]
            if linenum==1:
                res.append(line)
            elif linenum==2:
                res.append([1,1])
            else:
                cur=res[-1]
                print(f"res= {res}")
                print(f"cur={cur}")
                for i in range(0,len(cur)-1):
                    line.append(cur[i]+cur[i+1])
                line.append(1)
                res.append(line)
            linenum+=1    
        return res
print(generate(5))