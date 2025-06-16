p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscibe this"
p4 = "click this"

message = input("Enter your coment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this is spam")
else:
    print("not spam")