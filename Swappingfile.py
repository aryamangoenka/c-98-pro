def swapfiledata():
    txt1=input("Enter the file 1 name ")
    txt2=input("Enter the file 2 name ")

    with open(txt1,'r') as a:
        data_a=a.read()
    with open(txt2,'r') as b:
        data_b=b.read()
    with open(txt1,'w') as a:
        a.write(data_b)
    with open(txt2,'w') as b:
        b.write(data_a)
swapfiledata()