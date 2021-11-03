print(" ------------------------------------------------")
print("|                                                |")
print("|    09EncodeAString                             |")
print("|    Name : Leo                                  |")
print("|    Version : 01                                |")
print("|                                                |")
print(" ------------------------------------------------")
string = input("What is your string? ")
message = ""
for element in string:
    x = chr(ord(element)+1)
    print(element,"=",x)
    message += x
    print(message)