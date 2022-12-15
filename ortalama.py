import sys;
notlar=[]
sayı=0
print("Ortalamasını almak ve en küçük ile en büyük sayıyı bulmak için ard arda 5 sayı girin ve her defasında Enter'e basın.")
for x in range(0,5):
    try:
        c=int(input(" "+str(x+1)+". sayıyı girin: "))
        notlar.append(c)
        sayı=sayı+notlar[x]
    except ValueError:
        print("Lütfen sadece sayı girerek tekrar deneyin!")
        input("Çıkmak için Enter tuşuna basın...")
        sys.exit(0)
print("Sonuçlar:")
notlar.sort()
print("-en düşük: ",notlar[0])
print("-en yüksek: ",notlar[4])
ot=sayı/5
print("-ortalama: ",ot)
input("Çıkmak için Enter tuşuna basın...")
sys.exit(0)
