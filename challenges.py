#!/usr/bin/env python3

# 
#  * Crea un programa que invierta el orden de una cadena de texto
#  * sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
#  
def string_inverter(str):
    len_str = len(str)
    rever = ""
    for i in range(len_str):
        rever = str[i] + rever
    return rever

def other_way(txt):
    rever = ""
    for i in range(len(txt),0,-1):
        rever+= txt[i-1]
    return rever

# str = input("Enter String to revert :")
# print("Original String :", str)
# print("Reversing string :",string_inverter(str))
# print("Other way :",other_way(str))

# /*
#  * Crea un programa que cuente cuantas veces se repite cada palabra
#  * y que muestre el recuento final de todas ellas.
#  * - Los signos de puntuación no forman parte de la palabra.
#  * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#  * - No se pueden utilizar funciones propias del lenguaje que
#  *   lo resuelvan automáticamente.
#  */

import re, operator
 
def count_words(str):
    dic_w = {}
    pa = r"\w+"
    list_w = re.findall(pa,str)
    for i in list_w:
        dic_w[i] = list_w.count(i)
    dic_w = sorted(dic_w.items(),key=operator.itemgetter(1),reverse=True)
    return dic_w

# str = """ * Crea un programa que cuente cuantas veces se repite cada palabra
#             * y que muestre el recuento final de todas ellas.
#             * - Los signos de puntuación no forman parte de la palabra.
#             * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
#             * - No se pueden utilizar funciones propias del lenguaje que
#             *   lo resuelvan automáticamente."""
# # print(count_words(str))

# /*
#  * Crea un programa se encargue de transformar un número
#  * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#  */
 
def decimal_to_binary(binary):
    # convert binary number to string to know  its len
    binary_str = str(binary) 
    len_binary = len(binary_str)
     
    number = 0
    for i in range(len_binary):
        # get item 
        item = binary_str[i]
        # get index from right to left
        index = len_binary-i-1
        # sum value from 2^ index and * item 
        number =  number + 2**(index)*int(item)
        # print(int(i),2**i, binary_str[i],number)
    print("decimal",number)
    return number

def get_Maxindex(decimal):
    index =0 
    while True:
            x2= 2**index
            if  x2 < decimal:
                index+=1
            elif x2 == decimal:
                return index
            else:
                break
    return index-1
def list_to_binary(listb):
     binary = ["0" for x in range(listb[0]+1)]
      
     for i in range(len(listb)):
           binary[listb[i]] = "1"
     binary.reverse()
     print(binary)

def binary_to_decimal(decimal):
        binary =[]
        b1 = decimal
        i = 0
        while True:
            binary.append(get_Maxindex(b1))
            b1 = b1 - 2**binary[i]
            i+=1
            if b1 == 0:
                 break
        print(binary)
        list_to_binary(binary)  
        return binary     
    
def decimalBinary(decimal,rest):
     
     if not decimal:
          return rest
     div = decimal //2
     rest.insert(0,decimal % 2)
     return decimalBinary(div,rest)
# rest = []
# print(decimalBinary(682,rest))

# decimal_to_binary(1010101010)
# binary_to_decimal(682)


# /*
#  * Crea un programa que sea capaz de transformar texto natural a código
#  * morse y viceversa.
#  * - Debe detectar automáticamente de qué tipo se trata y realizar
#  *   la conversión.
#  * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
#  *   o símbolos y dos espacios entre palabras "  ".
#  * - El alfabeto morse soportado será el mostrado en
#  *   https://es.wikipedia.org/wiki/Código_morse.
#  */

# chak , is not working
def morse(code):
     alphabet_morse = {"A" : ".—", "N" : "—.", "0" : "—————",
                       "B" : "—...", "Ñ" : "——.——", "1" : ".————",
                       "C" : "—.—.", "O" : "———", "2" : "..———",
                       "CH" : "————", "P" : ".——.", "3" : "...——",
                       "D" : "—..", "Q" : "——.—", "4" : "....—",
                       "E" : ".", "R" : ".—.", "5" : ".....",
                        "F" : "..—.", "S" : "...", "6" : "—....",
                        "G" : "——.", "T" : "—", "7" : "——...",
                        "H" : "....", "U" : "..—", "8" : "———..",
                        "I" : "..", "V" : "...—", "9" : "————.",
                        "J" : ".———", "W" : ".——", "." : ".—.—.—",
                        "K" : "—.—", "X" : "—..—", "," : "——..——",
                        "L" : ".—..", "Y" : "—.——", "?" : "..——..",
                        "M" : "——", "Z" : "——.."," " :	"·—··—·" }
     print(alphabet_morse)
     morse_return = ""
     code = code.upper()
     for i in code:
          nnn = alphabet_morse.get(i,0)
          morse_return = morse_return + str(nnn)
          
     return morse_return

# morse("""A lo largo de tu formación recibirs asesoramiento para mejorar tu CV 
# y te prepararemos para realizar entrevistas con nuestras empresas colaboradoras. 
# Esta formacion es gratuita para ti y NO se te descontar nada del salario de la oferta de trabajo que consigas.""")


# /*
#  * Crea un programa que comprueba si los paréntesis, llaves y corchetes
#  * de una expresión están equilibrados.
#  * - Equilibrado significa que estos delimitadores se abren y cieran
#  *   en orden y de forma correcta.
#  * - Paréntesis, llaves y corchetes son igual de prioritarios.
#  *   No hay uno más importante que otro.
#  * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
#  * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
#  */

 
#  ******************************************************

person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_marred': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
        'street': 'Space street',
        'zipcode': '02210'
            }
}

def check_skills(dic,skill):
     if dic.get("skills",0):
          print("All skills")
          print(dic["skills"][len(dic["skills"])//2])
          if skill in dic["skills"]:
               print(skill)
          else:
               print(f"{skill} is not present")     
     else:
          raise Exception("ERROR")
     
check_skills(person,"Pythonsss")

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1 = {**dic1,**dic2}
dic1.update(dic3)
print(dic1)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dic = {}
for i in range(len(keys)):
     dic[keys[i]] = values[i]
dic_c = {x:j for x in keys for j in values}
print(dic)
print(dic_c)

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000} 

dic_r = {x:defaults for x in employees }
print(dic_r)

for i in employees:
     dic_r[i]=defaults
print(dic_r)

 
dic = {}.fromkeys(employees,defaults)
print(dic)

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]

re = {x:sample_dict[x] for x in keys}
print(re)
res = {}
for x in keys:
    res.update({x:sample_dict[x]})
print(res)

res = {}
for k,v in sample_dict.items():
     if k in keys:
         continue 
     res[k]=v
print(res)

res1 = {x:sample_dict[x] for x in sample_dict.keys() - keys}
print(res1)

sample_dict1 = {'a': 100, 'b': 200, 'c': 300}    

if 200 in sample_dict1.values():
     print("exist 200")

if sample_dict.get("city",0):
     sample_dict["location"] = sample_dict.pop("city")
print(sample_dict)

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'History': 75
}
import operator
menor = sorted(sample_dict.items(),key=operator.itemgetter(1))
print(menor[0][0])
menor1 = sorted(sample_dict.items(),key = lambda x:x[1])
print(menor1)
menor2 = min(sample_dict.items(),key=operator.itemgetter(1))
print(menor2)

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict["emp3"]["salary"] =1
print(sample_dict)

list1 = [100, 200, 300, 400, 500]
list2 = list1.copy()
list1.reverse()
list2 = list2[::-1]
print(list1, list2)

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]


list3 = [list1[x]+list2[x] for x in range(len(list1))]
list4 = [x+j for x,j in zip(list1, list2)]
print(list3)
print(list4)

numbers = [1, 2, 3, 4, 5, 6, 7]

square = [x**2 for x in numbers]
print(square)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

list3 = [x+j for x in list1 for j in list2 ]
print(list3)

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]


    
list4 = [print(x,j) for x ,j in zip(list1,list2[::-1])]
print(list4)
 
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list2 = [x for x in list1 if x]
print(list2)

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub list to add
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)

list1 = [5, 20, 15, 20, 25, 50, 20]
list2 = [x for x in list1 if x != 20]
print(list2)