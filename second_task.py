import string
import random


def generate_random_key(length):
    key = ''
    for i in range(length):
        key += chr(random.randint(0, 255))

    return key


def generate_strings(ikey, q=10):
    keys = {}
    for i in range(q):
        keys[i] = ''
        for j in range(len(ikey)):
            keys[i] += chr(random.randint(0, 255))

    return keys


def xor(string, other_string):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(string, other_string))


def generate_keys(ikey):
    keys = generate_strings(ikey)
    for i in range(len(keys)):
        keys[i] = xor(keys[i], ikey) + keys[i]
    return keys


def restore_key(key):
    c = int(len(key) / 2)
    return xor(key[:c], key[c:])


def encrypt(text, key_id, keys):
    key = restore_key(keys[key_id])
    encrypted_text = ''
    for symbol_text, symbol_key in zip(text, key):
        encrypted_text += chr(ord(symbol_text) ^ ord(symbol_key))

    return encrypted_text


def decrypt(encrypted_text, key_id, keys):
    key = restore_key(keys[key_id])
    restored_text = ''
    for symbol_text, symbol_key in zip(encrypted_text, key):
        restored_text += chr(ord(symbol_text) ^ ord(symbol_key))

    return restored_text


if __name__ == '__main__':
    ikey = generate_random_key(22)
    print('Первичный ключ : ' + ikey)
    keys = generate_keys(ikey)
    for elem in keys.values():
        print('Элемент группы : ' + elem)

    text = 'Лабораторная работа 3'
    encrypted_text = encrypt(text, 0, keys)
    print(encrypted_text)
    decrypted_text = decrypt(encrypted_text, 3, keys)
    print(decrypted_text)