import random
import string

ID_NUM_LEN = 2
ID_NUM_CHARS = 6

def id_generator():
    deck_chars = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    deck_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    id_part2 = random.sample(deck_num,ID_NUM_LEN)
    id_part1 = random.sample(deck_chars,ID_NUM_CHARS)
    print("Baraja_num:",deck_num)
    print("Baraja_letras:",deck_chars)
    print("Letras aleatorias:",id_part1)
    print("Numeros aleatorios:",id_part2)
    print("------- CONCATENAMOS --------")
    id_final = id_part1 + id_part2
    #Pasamos a string mediante lista de comprehension
    id_final = ''.join([str(elem) for elem in id_final])
    print("ID FINAL: ",id_final," cant: ",len(id_final))
    return id_final


if __name__ == "__main__":
    id_generator()

#BY Miguel Herencia