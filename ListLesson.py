markalar = ["BMW","OPEL","MAZDA","MERCEDES"]

print(markalar)
print(f"Liste {len(markalar)} elemanlıdır.")
print(f"Listenin ilk elemanı = {markalar[0]}",f"Listenin son elemanı = {markalar[len(markalar)-1]}",sep="\n")

markalar[markalar.index("MAZDA")] = "TOYOTA"
print(markalar)

if markalar.count("MAZDA") >= 1:
    print("'MAZDA' listenin bir elemanıdır")
else:
    print("'MAZDA' listenin bir elemanı değildir")

print(markalar[-2])
print(markalar[0:3]) # 0 dahil 3 dahil değil

markalar[-1] = "RENAULT"

markalar.append("AUDİ")
markalar.append("NİSSAN")
print(markalar)
markalar.pop(5)

print(markalar)
print(markalar[::-1])

ogrenciler = []
ogrenci1 = ["Ahmet", "Yılmaz","2001","70-60-70"]
ogrenci2 = ["AYŞE", "YAMAN","1999","80-80-70"]
ogrenci3 = ["MAHMUT", "TURLU","2001","80-70-90"]

ogrenciler.append(ogrenci1)
ogrenciler.append(ogrenci2)
ogrenciler.append(ogrenci3)
print(ogrenciler)