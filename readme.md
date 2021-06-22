## Türkiye Covid-19 Günlük Aşılama Tablosu

Github Actions kullanılarak [Sağlık Bakanlığı COVID-19 Aşısı Bilgilendirme Platformu](https://covid19asi.saglik.gov.tr/)'ndan günlük olarak (sabah ve akşam) çekilen veri görselleştirilmiştir. Veri [bs4](https://github.com/silverstone1903/covid-19-vaccine-report-tr/blob/main/run.py) kullanılarak data frame haline getirilerek elde edildiği tarih bilgisi ile *json* formatında `data` klasörüne yazılmaktadır. Bir gün içerisinde yapılan toplam aşıyı görmek adına sabah 7.55 ve gece 23.55'te çalışacak şekilde actions script'i düzenlenmiştir. Bir önceki güne ait dosya isimlerini alabilmek için de script [sonuna](https://github.com/silverstone1903/covid-19-vaccine-report-tr/blob/main/run.py#L58) yazılan dosya isimlerinin tutulduğu `files.txt` eklenmiştir. Böylece önceki güne ait veriler bu listeden okunabilmektedir. Github Pages kullanılarak repo pages haline getirilmiş ve böylece yazılan verilere github.io üzerinden ulaşılabilmektedir. 


```
$ curl https://silverstone1903.github.io/covid-19-vaccine-report-tr/data/files.txt
data/df-21_06_2021_08_00.json
data/df-21_06_2021_23_49.json
data/df-22_06_2021_08_03.json
```

Bu şekilde önceki güne ait ve sabah elde edilen veriler kullanılarak bir önceki gün şehirlere göre yapılan toplam aşılar görselleştirilmektedir. Sabah elde edilen veri de o güne kadar ki şehirlere göre yapılan toplam aşılamayı tablo olarak göstermektedir.

[Günlük Aşılama Raporu](https://silverstone1903.github.io/daily-covid19-data-table/tables/Covid19AsiTurkiye.html)

