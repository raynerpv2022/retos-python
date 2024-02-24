

# * Reto #1
#  * ¿ES UN ANAGRAMA?
#  * Fecha publicación enunciado: 03/01/22
#  * Fecha publicación resolución: 10/01/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
#  * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
#  * NO hace falta comprobar que ambas palabras existan.
#  * Dos palabras exactamente iguales no son anagrama.

def is_anagram(str, name):
    str = str.lower()
    name = name.lower()
    if str == name:
        return False
    
    return sorted(str) == sorted(name)
    # other way 

    # if len(str) != len(name) or str == name:
    #     return False
    # for i in range(len(str)):
    #      print(str[i], name[i])
    #      if str[i] not in name or name[i] not in str:
    #          return False
        
    # return True
         