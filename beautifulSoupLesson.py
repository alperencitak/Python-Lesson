html_doc = """
    <!DOCTYPE html>
<html lang="tr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formlar</title>
</head>

<body>
    <form>
        <p>
            <b>Ad :</b> <input type="text" name="ad">
        </p>
        <p>
            <b>Soyad :</b> <input type="text" name="soyad">
        </p>
        <p>
            <b>Cinsiyetiniz :</b>
            <span style="color: blue;">Erkek</span> <input type="radio" name="cinsiyet">
            <span style="color: fuchsia;">Kadın</span> <input type="radio" name="cinsiyet">
        </p>
        <p>
            <b>Doğum yeri :</b> <select name="dogumyeri">
                <option>Eskişehir</option>
                <option>İstanbul</option>
                <option>Ankara</option>
            </select>
        </p>
        <p>
            <b>Hobileriniz :</b><br> <select multiple name="dogumyeri">
                <option>Spor</option>
                <option>Müzik</option>
                <option>Resim</option>
            </select>
        </p>
        <p>
            <b>E-posta :</b> <input type="email" name="email">
        </p>
        <p>
            <b>Şifre :</b> <input type="password" name="password">
        </p>
        <p>
            <b>Şifre onay :</b> <input type="password" name="password" id="">
        </p>
        <p style="color: chartreuse;">
            <input type="checkbox" name="checkbox"> I agree terms of service.
        </p>
        <p style="color: rgb(255, 179, 0);">
            <input type="checkbox"> Bilgilerimi hatırla.
        </p>
    </form>
</body>

</html>
"""

from bs4 import BeautifulSoup

if __name__ == '__main__':
    soup = BeautifulSoup(html_doc, 'html.parser')
    result = soup.prettify()  # düzeltilmiş şekilde html kodlarını verir.
    result = soup.title  # title etiketini verir
    result = soup.body  # body etiketini verir
    result = soup.title.name  # title etiket ismini verir.
    result = soup.title.string  # title ismini verir.
    result = soup.p  # ilk p etiketini verir.
    result = soup.find_all('p')  # tüm p etiketlerini liste şeklinde getirir.
    result = soup.find_all('select')[0].find_all('option')
    result = soup.p.findChildren()  # ilk p etiketinin içindekileri getirir.
    result = soup.p.findNextSibling()  # 2. p etkiketinin içindekileri getirir.
    result = soup.p.findNextSibling().findNextSibling()  # 3. p etkiketinin içindekileri getirir.

    print(result)