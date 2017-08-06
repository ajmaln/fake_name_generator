from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
n = int(input("How many?"))
i=0
while i < n:
    req = Request('http://www.fakenamegenerator.com', headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, "lxml")
    #print (soup.prettify())
    name=soup.h3.string
    print(name)
    file=open("Details.txt",'a')
    file.write(name)
    img = soup.find_all('img')
    altag = [x.get("alt") for x in img]
    if 'Female' in altag:
        file.write("\n"+"F"+"\n")
        file.close()
    elif 'Male' in altag:
        file.write("\n" + "M" + "\n")
        file.close()
    i+=1


