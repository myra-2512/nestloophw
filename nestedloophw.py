dec=int(input("Enter a decimal number to convert to binary: "))

binary = ""
while dec > 0:
    binary = str(dec % 2)
    dec = dec // 2 
    print(binary, end="")

