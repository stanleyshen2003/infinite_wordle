import requests
import bs4
words=[]
url = "https://douze.pixnet.net/blog/post/398218087"
file = requests.get(url)
objsoup = bs4.BeautifulSoup(file.text, 'lxml')
tag = objsoup.find_all('p')
for data in tag:
    if((data.text[0]=="*" or ord(data.text[0])>122) and len(data.text)>6 and data.text[6]==" "):
        words.append(data.text[1:6])
    if(data.text[0]!="*" and ord(data.text[0])<=122):
        if(len(data.text)>6 and data.text[5]==" "):
            words.append(data.text[0:5])

words = sorted(words)
realwords =[]
q=0
i=0
popped=False
while(i<len(words)):
    q=0
    while(q<5):
        if (ord(words[i][q])<97 or ord(words[i][q])>122):
            words.pop(i)
            popped=True
            break
        q+=1
    i+=1
    if(popped==True):
        popped=False
        i-=1
print("{",end="{'")
print(words[0][0],end="'")
i=1
while(i<5):
    print(',',end="'")
    print(words[0][i],end="'")
    i+=1
print("}",end='')
i=1
while(i<len(words)):
    q=1;
    print(",",end="{'")
    print(words[i][0],end="'")
    while(q<5):
         print(',',end="'")
         print(words[i][q],end="'")
         q+=1
    print("}",end='')
    i+=1
print("}")

