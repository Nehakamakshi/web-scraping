from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://clutch.co/directory/mobile-application-developers').text
soup = BeautifulSoup(source, 'lxml')

ls = []
ls1 = []
ls2 = []
for heading in soup.find_all('h3'):
    ls.append(heading.text.strip())
    # print(heading.text.strip())
    # print()
print(ls)
# companyName = heading.text
# print(companyName)
for detail in soup.find_all('div', class_="module-list"):
     detail1= detail.text.split("\n")
     while("" in detail1):
        detail1.remove("")
     ls1.append(detail1)
print(ls1)
ls.pop()
print(len(ls))
print(len(ls1))
for detail3 in soup.find_all('div', class_="rating-reviews"):
     detail2 = detail3.text.split()
     while("" in detail2) :
        detail2.remove("")
     ls2.append(detail2)
print(ls2)

ls3 = []
src1 = []
ls4 = []

source1 = requests.get('htstps://clutch.co/directory/mobile-application-developer').text
soup1 = BeautifulSoup(source, 'lxml')
for anchor in soup1.findAll('h3', class_='company_info'):
    ls3.append(anchor.find('a')['href'])
    # print(anchor.find('a')['href'])
print(len(ls3))
for i in range(len(ls3)):
    src = 'https://clutch.co' + ls3[i]
    src1.append(src)
for i in range(len(ls3)):
    source2 = requests.get(src1[i]).text
    soup1 = BeautifulSoup(source2, 'lxml')
    website = soup1.find('section', class_='quick-menu').find('a', class_='web_icon')['href']
    contact = soup1.find('section', class_='quick-menu').find('a', class_='phone_icon').text
    contact = contact.strip().split('.')
    contact = ''.join(contact)
    ls4.append([contact, website])

csv_file = open('scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['company','website', 'contact', 'min project size', 'hourly rate', 'employee size', 'location', 'Rating', 'Review Count'])
for i in range(len(ls)):
    csv_writer.writerow([ls[i], ls4[i][1], ls4[i][0], ls1[i][0], ls1[i][1], ls1[i][2], ls1[i][3], ls2[i][0], ls2[i][1]])
csv_file.close()




