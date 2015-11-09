import os
import sqlite3

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
    contacto.nombre = raw_input("Digite el nombre: ")
    contacto.apellido = raw_input("Digite el apellido: ")
    contacto.telefono = raw_input("Digite el telefono: ")
    contacto.email = raw_input("Digite el email: ")
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
