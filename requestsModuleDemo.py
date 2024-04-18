import json
import requests



if __name__ == '__main__':
    api_key="5424facf11bba4e90acf6f8b"
    api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

    bozulan_doviz = input("Bozulan döviz türü: ") #USD
    alinan_döviz = input("Alınan döviz türü: ") # TRY
    miktar = input(f"Ne kadar {alinan_döviz} bozdurmak istiyorsunuz: ")
    conversion = requests.get(api_url + bozulan_doviz)
    conversion = json.loads(conversion.text)
    sonuc = int(miktar) * conversion["conversion_rates"][alinan_döviz]
    print(f"{miktar} {bozulan_doviz} = {sonuc} {alinan_döviz}")