def parse_bold(markdown):
    x=0
    y=0
    new=""
    x = markdown.find("**")
    while x != -1:

        if x==-1:
            break
        else:
            y=markdown.find("**",x+2)
            if markdown[x+2]!=" " and markdown[y-1]!=" ":
                new+= markdown[:x]+" <b>"+markdown[x+2:y]+"</b> "+markdown[y+2:]
            x=y+2
    return new
print(parse_bold("**This is bold**"))