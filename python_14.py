def texter(text1, text2, text3) :
    print(f"{text2} {text3} {text1}")

def texter(text1, text2, text3) :
    print(f"{text2} {text3} {text1}")
texter(text1="you", text2="i", text3="love")
texter(text2="i", text3="love", text1="you")

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue' ):
    print(" -- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print(" -- Lovely plumage, the", type)
    print(" -- It's", state, "!")

parrot(1000)
# argument
parrot(voltage=1000)
parrot (voltage=1000000, action='V00000M' )
parrot(action='VOOOOOM', voltage=1000000)
parrot('a million', 'bereft of life', 'jump' )
# arguments
parrot('a thousand' , state='pushing up the daisies' ) # 1 positional, 1


def selam(isim, soyad, meslek, sehir):
    print(f'benim adim {isim} soyadim {soyad}. {sehir} sehrinde yasiyorum. meslegim {meslek}')
selam('ali', 'guzel', 'developer', 'izmir' )
selam(sehir='izmir',meslek='develper', soyad = 'guzel', isim = 'ali')
selam('ali', sehir='izmir', meslek='develper', soyad = 'guzel' )

def selam(isim, soyad, meslek ='developer' , ulke = 'Turkiye' ):
    print(f'benim adim {isim} soyadim {soyad}. {ulke} ulkesinde yasiyorum. meslegim {meslek}')
selam('ali' , 'guzel')

def selam(isim, soyad, meslek ='developer' , ulke = 'Turkiye' ):
    print(f'benim adim {isim} soyadim {soyad}. {ulke} ülkesinde yasiyorum. meslegim {meslek}')
selam('ahmet', 'nazik', 'Netherlands')
selam('ahmet', 'nazik', ulke = 'Netherlands')

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue' ):
    print(" -- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print(" -- Lovely plumage, the", type)
    print(" -- It's", state, "!")
parrot(1000)

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue' ) :
    print(" -- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print(" -- Lovely plumage, the", type)
    print(" -- It's", state, "!")
parrot(voltage=1000)
parrot('million', 'alive')
parrot('million', action = "BAAAAAAAM")
parrot(voltage=1000000, action='VOOOOM' )

parrot(action='VOOOOOM',voltage=1000000)
parrot ('a million', 'bereft of life', 'jump' )
parrot ('a thousand', state='pushing up the daisies') # 1 positional, 1 keyword

def city(capital, continent='Europe' ) :
    print(capital, 'in', continent)
city('Athens') # we don't have to pass any arguments into 'continent'
city ('Ulaanbaatar', continent='Asia' ) # we can change the default value by kwargs
city('Cape Town', 'Africa') # we can change the default value by positional args.


def fruiterer(fruit1, fruit2) :
    print('I want to get', fruit1, 'and', fruit2)
fruiterer('orange', 'banana' )

def fruiterer(*fruit) :
    print ('I want to get : ' )
    for i in fruit :
        print('-', i)
fruiterer('orange', 'banana', 'melon', 'ananas' )

def toplama(a,b):
    print(a+b)
toplama(3,4)

def toplama(*a):
    print(sum(a))

toplama(5)
toplama(5,7,9,2,4)

def toplama(*a):
    toplam = 0
    for i in a:
        toplam+=1
    print(toplam)

def slicer(*x):
    even = []
    odd = []
    for i in x:
        if i%2 == 0 :
            even.append(i)
        else:
            odd.append(i)
    print(even)
    print(odd)
slicer(5,6,7,4,3,8,9,2,1,0,9,8,7,6,7)
slicer(*[5,6,7,4,3,8,9,2,1,0,9,8,7,6,7])
listem = [5,6,7,4,3,8,9,2,1,0,9,8,7,6,7]
slicer(*listem)

print(listem)
print(*listem)

def toplama(*a):
    print(sum(a))
toplama(2,3)
toplama(3,4,5)

def animals( ** kwargs):
    for key, value in kwargs.items():
        print(value, "are", key)
animals(Carnivores="Lions", Omnivores="Bears", Herbivores ="Deers", Nomnivores="Human")

def slicer(*x):
    print([i for i in x if i%2 == 0])
    print([i for i in x if i%2 == 1])
slicer(5,6,7,4,3,8,9,2,1,0,9,8,7,6,7)


def ulke_baskent( ** kwargs):
    for u,b in kwargs. items():
        print(f'{u} ulkesinin baskenti {b} dir. ')
ulke_baskent(ingiltere = 'London', usa = 'washington')

def organizer( ** itop):
    isimler = []
    yaslar = []
    for i in itop:
        print(i)
organizer(ali = 25, veli = 40, zeki = 50)

def organizer( ** itop):
    isimler = []
    yaslar = []
    for i in itop. values():
        print(i)
organizer(ali = 25, veli = 40, zeki = 50)

def organizer( ** itop):
    isimler = []
    yaslar = []
    for i,j in itop.items():
        isimler.append(i)
        yaslar.append(j)
    print(isimler)
    print(yaslar)

organizer(ali = 25, veli = 40, zeki = 50)

def organizer( ** people):
    names = []
    ages = []
    for key, value in people. items():
        names . append(key)
        ages. append(value)
    print(names, ages, sep="\n")
organizer(ali = 25, veli = 40, zeki = 50)

def brothers(bro1, bro2, bro3):
    print ('Here are the names of brothers : ')
    print(bro1, bro2, bro3, sep='\n' )
family = ['tom', 'sue', 'tim' ]
brothers(*family)

def toplama(a,b,c):
    print(a+b+c)
    
toplama(3,4,5)
listem = [4,5,6]
toplama(*listem)

def merger(arg1, arg2, arg3, arg4):
    print(f"For me, {arg1} {arg4} and {arg3} {arg2} are geniuses.")
genius = ('Bill', 'Rossum', 'Guido van', "Gates")
merger(*genius)

def gene(x, y): # defined by positional args
    print(x, "belongs to Generation X")
    print(y, "belongs to Generation Y")
dict_gene = {'y' : "Marry", 'x' : "Fred"}
gene( ** dict_gene) # we call the function by a single
# argument(variable)

def meaner (Alfred, Joseph, Eric) :
    avg = (Alfred + Joseph + Eric) / 3
    print("The average of their ages is :", avg)
friends = {'Alfred': 44, 'Joseph': 39, 'Eric': 55}
meaner( ** friends)

int('45')

a = '55'
try:
    int(a)
    print('try blogu calisti')
except :
    print('bir hata ile karsilasildi')

# a = 'xy'
# try:
#     int(a)
#     print('try blogu calisti')
# except :
#     print('bir hata ile karsilasildi')

# try:
#     a = int(input("Bir sayi giriniz"))
#     b = int(input("Ikinci sayiyi giriniz"))
#     print(a/b)
# except ValueError:
#     print('Kardesim bu sayiyi ben nasil integer a cevireyim. bi kontrol et bakalim')
# except ZeroDivisionError:
#     print('Kardesim bir sayi hic sifira bolunurmu hic mi matemati gormedim')
# print('Bittiiiiii')

# try:
#     a = int(input("Bir sayi giriniz"))
#     b = int(input("Ikinci sayiyi giriniz"))
#     print(a/b)
# except ValueError:
#     print('Kardesim bu sayiyi ben nasil integer a cevireyim. bi kontrol et bakalim')
# except ZeroDivisionError:
#     print('Kardesim bir sayi hic sifira bolunurmu hic mi matemati gormedim')
#     print('Bittiiiiii')
# else:
#     print('Hic bir hata ile karsilasmadan try blogu calisti')

# try:
#     a = int(input("Bir sayi giriniz"))
#     b = int(input("Ikinci sayiyi giriniz"))
#     print(a/b)
# except ValueError:
#     print('Kardeşim bu sayiyi ben nasil integer a cevireyim. bi kontrol et bakalim')
# except ZeroDivisionError:
#     print('Kardesim bir sayi hic sifira bolunurmu hic mi matemati gormedin')
# else:
#     print('Hic bir hata ile karsilasmadan try blogu calisti')
# finally:
#     print('Bu hata olsa da olmasa da calisir' )

import math
dir(math)
math. factorial(5)

import math as m
m. factorial(5)

import math
print(dir(math) ) # you can find out all names defined in this module

dir(math)
# help(math)
m.pi

from math import pi, factorial, log10 # we'll use the functions directly
print(pi) # it also contains several arithmetic constants
print(factorial(4)) # gives the value of 4!
print(log10(1000)) # prints the common logarithm of 1000

import string
dir(string)
# help(string)
string.ascii_uppercase

a = string.ascii_uppercase
for i in a:
    print(i)

import string as stg # we've used alias for 'string' module
print(stg.punctuation) # prints all available punctuation marks
print(stg.digits) # prints all the digits

import datetime
print(datetime. date.today()) # prints today's date (yyyy-mm-dd)
print(datetime. datetime.now()) # prints the current time in microseconds

from random import choice
city = ['Stockholm', 'Istanbul', 'Seul', 'Cape Town' ]
print(choice(city))

# def selam(isim):
#     '''bu fonksiyonun aciklamasi'''
#     print('Merhaba', isim)

# def toplama(a,b):
#     print(a+b)

# def cikarma(a,b):
#     print(a-b)

# def carpma(a,b):
#     print(a*b)

# def bolme(a,b):
#     print(a/b)

# import islemler
# help(islemler)
# dir(islemler)
# islemler.selam('Yasin')
# islemler.toplama(4,6)

# import islemler as isl
# isl. toplama(4,5)

# from islemler import selam
# selam('yasin')

# kendi modulunu yazma