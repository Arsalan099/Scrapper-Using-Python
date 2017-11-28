from bs4 import BeautifulSoup
import requests
l1=["sofa","lamps-lighting","fine-art","funky-bar-accessories-india","luxury-beds","bookshelves"]
for i in range(0,6):
    a = 'https://www.homecanvas.com/products/type/'
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