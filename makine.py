# Önceliğimiz burada işlemleri tanımlıyoruz
def add(x,y):
     return x + y

def  multiply(x,y):
     return x - y

def subtract(x,y):
     return x * y

def divide(x,y):
     return x / y

# Seçim menüsü hazırlıyoruz
print("Bir işlem türü seçiniz :")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")

# Seçim ve işlem menüsü
while True:
     choice = input("Yukarıdan seçim yapmak için işlemlerin yanındaki sayıyı yazınız: ")
     if choice in ('1', '2', '3', '4'):
          try:
               num1 = float(input("İlk sayıyı giriniz: "))
               num2 = float(input("İkinci sayıyı giriniz: "))
          except ValueError:
               print("Sadece rakamlar girebilirsiniz, lütfen tekrar dener misiniz?")
               continue
          
          # İşlem yapıldıktan sonra aldığımız çıktı
     if choice == '1':
          print("Sonuç: ", num1, "+", num2, "=", add(num1, num2))
     elif choice == '2':
          print("Sonuç: ", num1, "-", num2, "=", multiply(num1, num2))
     elif choice == '3':
          print("Sonuç: ", num1, "*", num2, "=", subtract(num1, num2))
     elif choice == '4':
          print("Sonuç: ", num1, "/", num2, "=", divide(num1, num2))
     
     # Son kısımda çıkan tatlı bir mesaj 
     hesaplama_sonrası = input("Artık yeni hesap makinen benim! :) ")
