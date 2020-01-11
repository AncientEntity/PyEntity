
def Debug(text,debugType=0):
    #0 warning, 1 error, 2 fatal
    if debugType == 0:
        print("[Warning] "+text)
    elif debugType == 1:
        print("[Error] "+text)
    else:
        print("[Fatal] "+text)