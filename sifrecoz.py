from cryptography.fernet import Fernet

def keyUret():
    key=Fernet.generate_key()
    with open("key.txt","wb")as file:
        file.write(key)
def dosyaAc(dosya):
    with open(dosya,"rb")as dosya:
        return dosya.read()

def sifrele(key,dosya):
    f=Fernet(key)
    icerik=dosyaAc(dosya)
    sifreli=f.dencrypt(icerik)
    with open(dosya, "wb")as sifrele:
        sifrele.write(sifreli)
keyUret()
key=dosyaAc("C:\\Users\\ogr10\\Documents\\Gk\\key.txt")
