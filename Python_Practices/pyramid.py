# string ="hello world"
string =input ("Enter a Word : ")
x=0
for i in string:
    x+=1
    print(string[0:x])

for i in string :
    x-=1
    print(string[0:x])