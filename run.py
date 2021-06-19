from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import datetime

def month_replacer_list(l):
    l = (l.replace("Ocak", "/01/").replace("Şubat", "/02/").replace(
        "Mart",
        "/03/").replace("Nisan", "/04/").replace("Mayıs", "/05/").replace(
            "Haziran", "/06/").replace("Temmuz", "/07/").replace(
                "Ağustos", "/08/").replace("Eylül", "/09/").replace(
                    "Ekim",
                    "/10/").replace("Kasım",
                                    "/11/").replace("Aralık",
                                                    "/12/")).replace(" ", "")
    return datetime.date.strftime(pd.to_datetime(l), format="%d/%m/%Y")

def table_gather():
    html = urlopen("https://covid19asi.saglik.gov.tr").read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    length = len(
        soup.find_all('div', class_='svg-turkiye-haritasi')[0].find_all('g'))
    assert length == 82
    df_ = []

    for i in range(length - 1):
        city = soup.find_all('div', class_='svg-turkiye-haritasi')[0].find_all(
            'g')[0].find_all("g")[i].get("data-adi")
        first_vac = soup.find_all(
            'div', class_='svg-turkiye-haritasi')[0].find_all('g')[0].find_all(
                "g")[i].get("data-birinci-doz")
        sec_vac = soup.find_all(
            'div', class_='svg-turkiye-haritasi')[0].find_all('g')[0].find_all(
                "g")[i].get("data-ikinci-doz")
        sum_vac = soup.find_all('div',
                                class_='svg-turkiye-haritasi')[0].find_all(
                                    'g')[0].find_all("g")[i].get("data-toplam")
        df_.append((city, first_vac, sec_vac, sum_vac))

    df = pd.DataFrame(df_,
                      columns=["Sehir", "Ilk Doz", "Ikinci Doz", "Toplam Doz"])
    df["Ilk Doz"] = df["Ilk Doz"].str.replace(".", "").astype(int)
    df["Ikinci Doz"] = df["Ikinci Doz"].str.replace(".", "").astype(int)
    df["Toplam Doz"] = df["Toplam Doz"].str.replace(".", "").astype(int)
    dates = str(soup.find_all('div', class_='container')[2]).split(
        "var asisayisiguncellemesaati =")[1].split(' \\')[0].strip().split(
            "\\")[0].split(";")[0].replace("'", "")
    dod = dates.split(",")[0]
    tod = dates.split(", ")[1].split(" ")[1]
    date_time = dod + str(" ") + tod
    df["Calisma Zamani"] = date_time
    df["Tarih"] = pd.to_datetime(tod)
    dttime = df.Tarih.dt.strftime("%d_%m_%Y_%H_%S")[0]

    return df, dttime, date_time
    
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

