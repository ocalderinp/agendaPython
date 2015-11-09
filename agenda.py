# -*- coding: utf-8 -*-
import os
import sqlite3
import re

# contactos = []
conexion = sqlite3.connect('agenda.s3db')
cursor = conexion.cursor()


class Contacto:
    nombre    = ""
    apellido  = ""
    telefono  = ""
    email     = ""

def limpiar():
    os.system('cls')

def addContact():
    limpiar()
    print "Agregando Nuevo Contacto"
    contacto = Contacto()

    pattern = re.compile("^([a-z ñáéíóú]{2,60})$")
    validName = False
    while validName == False:
        contacto.nombre = raw_input("Digite el nombre: ")
        if pattern.match(contacto.nombre) != None:
            validName = True
        else:
            print "Nombre Incorrecto. Debe contener solo letras"

    validLastName = False
    while validLastName == False:
        contacto.apellido = raw_input("Digite el apellido: ")
        if pattern.match(contacto.apellido) != None:
            validLastName = True
        else:
            print "Apellido Incorrecto. Debe contener solo letras"


    pattern = re.compile("^\+?\d{1,3}?[- .]?\(?(?:\d{2,3})\)?[- .]?\d\d\d[- .]?\d\d\d\d$")
    validPhone = False
    while validPhone == False:
        contacto.telefono = raw_input("Digite el telefono: ")
        if pattern.match(contacto.telefono) != None:
            validPhone = True
        else:
            print "Numero de Telefono Incorrecto. Debe contener 9 digitos"

    pattern = re.compile("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$")
    validMail = False
    while validMail == False:
        contacto.email = raw_input("Digite el email: ")
        if pattern.match(contacto.email) != None:
            validMail = True
        else:
            print "Direccion email invalida"

    reg = (contacto.nombre, contacto.apellido, contacto.telefono, contacto.email)
    cursor.execute('INSERT INTO Contactos (nombre, apellido, telefono, email) VALUES(?, ?, ?, ?)', reg)
    conexion.commit()
    menu()

def showContacts():
    limpiar()
    cursor.execute('SELECT * FROM Contactos')
    contactos = cursor.fetchall()
    print "Listado de Contactos"
    print 'Nombre \t\t\t Email \t\t\t Telefono'
    for c in contactos:
        contacto = str(c[1]) + " " + str(c[2]) + "\t\t\t" + str(c[4]) + "\t\t\t" + str(c[3])
        print contacto
    raw_input()
    menu()

def deleteContact():
    limpiar()
    email = raw_input("Entre el email: ")
    cursor.execute('DELETE FROM Contactos WHERE email=?',(email,))
    conexion.commit()
    menu()

def showContact():
    limpiar()
    nombre = raw_input("Entre el nombre: ")
    cursor.execute('SELECT * FROM Contactos WHERE nombre=?',(nombre,))
    contactos = cursor.fetchall()
    if len(contactos) != 0:
        for c in contactos:
            print "Nombre: " + str(c[1]) + " " + str(c[2])
            print "Telefono: " + str(c[3])
            print "Email: " + str(c[4])
            print "----------------------"
    else:
        print "No hay ningun contacto con el nombre " + nombre
    raw_input()
    menu()

def menu():
    limpiar()
    print "Mi Agenda v_0.1"
    print "---------------------"
    print "1- Agregar Contacto"
    print "2- Mostrar Contactos"
    print "3- Eliminar Contacto"
    print "4- Detalles Contacto"
    print "5- Salir"
    opcion = input('Digite una opcion: ')
    if opcion == 1:
        addContact()
    elif opcion == 2:
        showContacts()
    elif opcion == 3:
        deleteContact()
    elif opcion == 4:
        showContact()
    elif opcion == 5:
        conexion.close()
        os.system('exit')

    else:
        print 'Debe digitar una opcion valida'
        raw_input()
        menu()
menu()
