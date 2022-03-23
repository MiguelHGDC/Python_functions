#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#pyversion:python3.5
 
import hashlib
import string
# ######## md5 ########
 
string = "contrasenia"
 
def _md5():
    md5 = hashlib.md5()
    md5.update (string.encode ('utf-8')) #Preste atención a la transcodificación
    res = md5.hexdigest()
    print ("resultado de cifrado md5:", res)

# ######## sha1 ########
def _sha1():
    sha1 = hashlib.sha1()
    sha1.update(string.encode('utf-8'))
    res = sha1.hexdigest()
    print ("resultado de cifrado sha1:", res)

# ######## sha256 ######## MUY SEGURO
def _sha256():
    string = 'beyongjie'
    sha256 = hashlib.sha256()
    sha256.update(string.encode('utf-8'))
    res = sha256.hexdigest()
    print ("resultado de cifrado sha256:", res)


# ######## sha384 ########
def _sha384():
    sha384 = hashlib.sha384()
    sha384.update(string.encode('utf-8'))
    res = sha384.hexdigest()
    print ("resultado de cifrado sha384:", res)

# ######## sha512 ######## MUY SEGURO
def _sha512(): 
    sha512= hashlib.sha512()
    sha512.update(string.encode('utf-8'))
    res = sha512.hexdigest()
    print ("resultado de cifrado sha512:", res)

if __name__ == "__main__":
    try:
        _md5()
    except:
        print("Error: md5 no se ha podido realizar")
    try:
        _sha1()
    except:
        print("Error: sha1 no se ha podido realizar")
    try:
        _sha256()
    except:
        print("Error: sha256 no se ha podido realizar")
    try:
        _sha384()
    except:
        print("Error: sha384 no se ha podido realizar")
    try:
        _sha512()
    except:
        print("Error: sha512 no se ha podido realizar")
#BY Miguel Herencia