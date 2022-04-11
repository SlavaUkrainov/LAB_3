import string
import random


def encrypt(crypt_data):
    for i in range(length_data):
        crypt_data = (crypt_data[:i] +
                      chr(ord(crypt_data[i]) ^ ord(xor_key[i])) +
                      crypt_data[i + 1:])
        print(crypt_data[i], end="")
    return crypt_data


def decrypt(crypt_data):
    crypt_data = encrypt(crypt_data)
    return crypt_data


if __name__ == '__main__':
    input_data = input("Введите текст : ")
    lower_upper_letter = string.ascii_letters
    length_data = len(input_data)
    xor_key = list()
    for x in range(length_data):
        xor_key.append(random.choice(lower_upper_letter))

    print("Текст после шифрования: ")
    input_data = encrypt(input_data)
    print("\n")
    print("Текст до шифрования: ")
    decrypt(input_data)
    print("\n")
    print("Ключ шифрования:", xor_key)
