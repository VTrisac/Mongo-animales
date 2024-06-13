# -*- coding: utf-8 -*-

from pymongo import MongoClient
conexion = MongoClient("mongodb://localhost:27017/")
        
basedatos = conexion.ejercicios
colecc = basedatos.animales

def agregar():
    salir = ""
    tipo = input("Tipo de animal: ")
    diccio = {"tipo": tipo}
    while salir != "n":
        campo = input("Nombre del campo: ")
        valor = input("Valor para " + campo + ": ")
        salir = input("Añadir otro campo? (s/n) ")
        diccio[campo]=valor
    nuevo = colecc.insert_one(diccio)
    print(tipo, "Agregado. Identificador del nuevo documento:", nuevo.inserted_id)

def listado():
    tipo = input("Tipo de animal: ")
    result = colecc.find_one({"tipo": tipo})
    if result:
        for animal in colecc.find({"tipo": tipo},{"_id":0, "tipo": 0}):
            print("-".center(30, "-"))
            for dato in animal.items():
                print((dato[0]+":").ljust(15), dato[1])
    else:
        print("El tipo", tipo,"no se ha encontrado.")


def consultas():
    campo = input("Nombre del campo: ")
    valor = input("Valor para " + campo + ": ")
    result = colecc.find_one({campo: valor})
    if result:
        for animal in colecc.find({campo: valor},{"_id":0,campo:0}):
            print("-".center(30, "-"))
            for dato in animal.items():
                print((dato[0]+":").ljust(15), dato[1])
    else:
        print("El campo '", campo,"' con el valor '", valor, "' no se ha encontrado.")
        

oper = ""
while(oper != "0"):
    print("\nOPCIONES:\n1- Agregar animal\n2-Listado\n3-Consultas\n\n0-Salir")
    oper = input("Indique la opción: ")
    if oper == "1":
        agregar()
    if oper == "2":
        listado()
    if oper == "3":
        consultas()
print("Gracias por usar pymongo.")
