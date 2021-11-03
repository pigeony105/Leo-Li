string = input("What is your string? ")
message = ""
for element in string:
    x = chr(ord(element)+1)
    print(element,"=",x)
    message += x
    print(message)