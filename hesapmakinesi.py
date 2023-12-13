#kullanıcıdan değer aldığımız yer
islem = input('Lütfen Bir İşlem Seçin; (+,-,/,*) ')

s1 = int(input('Bir Sayı Girin; '))
s2 = int(input('Bir Sayı Girin; '))

#işlemlerin yapıldığı yer
toplama = s1+s2
cikarma = s1-s2
bölme = s1/s2
carpma = s1*s2

#if sistemi
if islem == "+" :print('İşlem Sonucu; {0}'.format(toplama))
if islem == "-" :print('İşlem Sonucu; {0}'.format(cikarma))
if islem == "/" :print('İşlem Sonucu; {0}'.format(bölme))
if islem == "*" :print('İşlem Sonucu; {0}'.format(carpma))

#Program xLiteChesy tarafından yapılmıştır