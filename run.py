from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import datetime

def table_gather():
    html = urlopen("https://covid19asi.saglik.gov.tr").read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    length = len(soup.find_all('div', class_='svg-turkiye-haritasi')[0].find_all('g'))
    assert length == 82
    df_ = []

    for i in range(length-1):
        city = soup.find_all('div', class_='svg-turkiye-haritasi')[0].find_all('g')[0].find_all("g")[i].get("data-adi")
        first_vac = soup.find_all('div', class_='svg-turkiye-haritasi')[0].find_all('g')[0].find_all("g")[i].get("data-birinci-doz")
        sec_vac = soup.find_all('div', class_='svg-turkiye-haritasi')[0].find_all('g')[0].find_all("g")[i].get("data-ikinci-doz")
        sum_vac = soup.find_all('div', class_='svg-turkiye-haritasi')[0].find_all('g')[0].find_all("g")[i].get("data-toplam")
        df_.append((city, first_vac, sec_vac, sum_vac))
    df = pd.DataFrame(df_, columns=["Sehir", "Ilk Doz", "Ikinci Doz", "Toplam Doz"])
    df["Ilk Doz"] = df["Ilk Doz"].str.replace(".", "").astype(int)
    df["Ikinci Doz"]= df["Ikinci Doz"].str.replace(".", "").astype(int)
    df["Toplam Doz"]= df["Toplam Doz"].str.replace(".", "").astype(int)
    df["Calisma Zamani"] = datetime.date.strftime(datetime.datetime.today(), format = "%d/%m/%Y %H:%S")
    
    dttime = datetime.date.strftime(datetime.datetime.today(), format = "%d-%m-%Y_%H_%S")
    date = datetime.date.strftime(datetime.datetime.today(), format = "%d/%m/%Y")
    
    return df, dttime, date
    
df, dttime, date = table_gather()
print("Data gathered")
name = "data/df-%s.json"%dttime
print(name)
print(date)
print(dttime)
df.to_json(name)
hs = open("data/files.txt","a")
hs.write(name + "\n")
hs.close() 
print("Done..!")

