#Nicola Batty
#10/10/2014
#ASCII python Task 1

print("Hello user")

text_or_ascii = "hi"
while text_or_ascii == "a-t" or text_or_ascii == "t-a":
    text_or_ascii = input("please staet wether you want ascii to text (a-t) or text to ascii (t-a): ")
    if text_or_ascii == "a-t":
        ascii_code = int(input("please input ascii code: "))
        text = chr(ascii_code)
        print("{0}".format(text))
    elif text_or_ascii == "t-a":
        ascii_code = input("please input ascii code: ")
        text = ord(ascii_code)
        print("{0}".format(text))
    else:
        print("Try again")
        
    
