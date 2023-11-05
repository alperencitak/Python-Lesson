dosya = open("deneme.txt", "w")
print("Bu bir deneme dosyasidir.", file=dosya)
dosya.close()

import os
print(os.getcwd()) #4-5 satırı dosyanın konumunu gösterir.

dosya2 = open("deneme2.txt", "w")
print("Bu bir deneme 2 dosyasidir.", file=dosya2, flush=True) #normal değeri false'dur.
#flush false ise dosya yazılan tamponda bekler.True ise beklemeden dosyaya yazılır.Kapatılma ihtiyacı yok.

import sys
f = open("dosya.txt", "w")
sys.stdout, f = f, sys.stdout
print("deneme123", flush=True)
sys.stdout = f
print("deneme12345")

"""
newfile = open("newtextfile.txt","w")
import sys
backupsys = sys.stdout
sys.stdout = newfile
print("Yeni metin dosyasi", flush=True)
sys.stdout = backupsys
print("Dosya yazma bitmistir sys.stdout eski haline getirildi \n"
      "Dosya kapanmadı bu sebeple yazmaya devam edilebilir.")
print("Dosya hala acik", end=".", file=newfile)
"""