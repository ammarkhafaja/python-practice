def outer():
    global out
    out = "outer"
    inn=""
    print(out)


    def inner():
        nonlocal inn
        inn = "inner"
        print(inn)
        print(out)
    inner()
    print(inn)
print(out)
outer()

