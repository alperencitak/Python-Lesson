import sys

print(sys.version_info)
print(sys.version)

if "3.12" in sys.version:
    print("3.12 sürümündesiniz")

turkceAlfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
ingilizceAlfabe = "abcdefghijklmnopqrstuvwxyz"

for kontrol in turkceAlfabe:
    if not kontrol in ingilizceAlfabe:
        print(kontrol,end=" ")
print(" harfleri türkçede varken ingilizcede yoktur")
for kontrol in ingilizceAlfabe:
    if not kontrol in turkceAlfabe:
        print(kontrol,end=" ")
print(" harfleri ingilizcede varken türkçede yoktur")