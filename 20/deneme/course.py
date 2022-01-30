# f= open("file.txt")
# print(f)
# f.close()

# f= open("file.txt","r", encoding="utf-8")  
# text = f.read()
# print(text)



with open ("file.txt", "r",encoding="utf8")as f:
    Text = f.read()
    print(Text)
    