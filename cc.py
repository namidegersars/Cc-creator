#tool created by Sars
import random
import pyfiglet

sars = pyfiglet.figlet_format("Sars")
print(sars)

user_count = int(input("Oluşturulacak cc miktarını giriniz(Max:100) : "))
if user_count > 100:
    print("Fazla miktar girdin,lütfen tekrar dene")
def generate_card_number():
    card_number = "4169"
    for _ in range(12):
        digit = random.randint(0, 9)
        card_number += str(digit)
    return card_number

def generate_cvv():
    cvv = ""
    for _ in range(3):
        digit = random.randint(0, 9)
        cvv += str(digit)
    return cvv

def generate_expiry_date():
    month = random.randint(1, 12)
    year = random.randint(23, 30)
    expiry_date = str(month).zfill(2) + "/" + str(year)
    return expiry_date
if user_count <= 100:
 for _ in range(user_count):
    card_number = generate_card_number()
    cvv = generate_cvv()
    expiry_date = generate_expiry_date()
    print("Kart Numarası:", card_number)
    print("CVV:", cvv)
    print("Bitiş Tarihi:", expiry_date)
    print("--------------------------------")