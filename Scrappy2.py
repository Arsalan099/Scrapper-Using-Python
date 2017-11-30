from bs4 import BeautifulSoup
import requests
l1=[]
l2=[]
a='https://www.homecanvas.com/furniture-online/'
r=requests.get(a)
soup=BeautifulSoup(r.text,'lxml')
links=soup.findAll("div", class_="checkbox checkbox-circle")
for i in range(0, len(links)):
    if (links[i].find('a').string) not in l2:
        l1.append(str(links[i].find('a').get('href')))
        l2.append(links[i].find('a').string)
for i in range(0,len(l1)):
    a = 'https://www.homecanvas.com'
    a=a+l1[i]
    r=requests.get(a)
    soup=BeautifulSoup(r.text,'lxml')
    td1=soup.findAll("div", class_="productt-name")
    td2=soup.findAll("img", class_="productt-img img-responsive lazy")
    td3=soup.findAll("div", class_="price")
    td4=soup.findAll("div", class_="vendorr")
    for i in range(0,len(td1)):
        j=str(td3[i])
        td4[i]=td4[i].find('a').string
        k=j.replace('<div class="price">', '').replace('</div>', '').replace('<img class="rupee-icon" src="/assets/images/icons/rupee.svg"/>', '').replace('\n', '')
        print(td1[i].string,k,td4[i])
        print(td2[i].get('data-src'))
    print(l2[i]+" Finished")
