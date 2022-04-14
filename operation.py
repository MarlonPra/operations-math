import random
from tkinter import *
import tkinter as tk

i = 0
correct = 0
# Ventana GUI
root = Tk()  # definimos que root es TK()
root.title("Math Operations")  # Cambiar el nombre de la ventana
root.geometry("720x480")  # Configurar tamaño
root.iconbitmap("math.ico")  # Cambiar el icono
root.config(bg="#fcd46c")  # Cambiar color de fondo
root.resizable(0, 0)  # obliga a que la ventana no se pueda cambiar de tamaño

texto1 = tk.Label(root, text="Introduce tu nombre",
                  font="robot 30 bold", justify="center")
texto1.config(bg="#fcd46c")
cajatexto = tk.Entry(root, font="robot 30", justify="center")
boton1 = tk.Button(root, text="Enviar", padx="30",
                   pady="30", justify="center", command=lambda: (calculator()))
texto1.pack(pady="10")
cajatexto.pack(pady="50")
boton1.pack(pady="100")


def calculator():
    global nombre
    nombre = cajatexto.get()
    texto1.pack_forget()
    cajatexto.pack_forget()
    boton1.pack_forget()
    global texto2
    global textdescr
    texto2 = tk.Label(root, font="robot 30 bold", justify="center")
    texto2.pack(pady="10")
    texto2.config(bg="#fcd46c")
    texto2["text"] = "Hola " + nombre
    textdescr = tk.Label(root, font="robot 30 bold",
                         justify="center", text="Porfavor resuelve las operaciones")
    textdescr.pack(pady="10")
    textdescr.config(bg="#fcd46c")
    operaciones()


def operaciones():
    global texto3
    global cajatexto2
    global boton2
    texto3 = tk.Label(root, font="robot 30", justify="center")
    texto3.pack(pady="50")
    texto3.config(bg="#fcd46c")
    cajatexto2 = tk.Entry(root, font="robot 30", justify="center")
    cajatexto2.pack()
    seleccion = random.randint(1, 2)  # seleccionamos la suma o resta
    if seleccion == 1:
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        resultado = a + b
        # suma = print()
        texto3["text"] = str(a) + " + " + str(b)
    elif seleccion == 2:
        a = random.randint(50, 99)
        b = random.randint(1, 49)
        resultado = a - b
        # resta = print(a + " - "+ b)
        texto3["text"] = str(a) + " - " + str(b)
    boton2 = tk.Button(root, text="Enviar", padx="30",
                       pady="10", command=lambda: (validar(resultado, cajatexto2)))
    boton2.pack(pady="20")


def validar(resultado, cajatexto2):
    respuesta = int(cajatexto2.get())
    global i
    global correct
    if resultado == respuesta:
        global verd
        verd = Toplevel(root)
        verd.title("CORRECTO")
        verd.geometry("250x150")
        verd.config(bg="#1AE128")
        verd.iconbitmap("math.ico")
        verd.resizable(0, 0)
        textval = tk.Label(verd, font="robot 18",
                           justify="center", text="Respuesta Correcta")
        textval2 = tk.Label(verd, font="robot 20", justify="center")
        textval2["text"] = resultado
        textval.pack(pady="10")
        textval.config(bg="#1AE128")
        textval2.pack(pady="10")
        textval2.config(bg="#1AE128")
        botonval = tk.Button(verd, text="Cerrar", padx="20",
                             pady="5", command=lambda: (resetverd()))
        botonval.pack()
        #print("Respuesta correcta")
        #print(resultado)
        #print(respuesta)
        i = i + 1
        correct = correct + 1
        #print("i= ", i)
        #print("correct= ", correct)
    else:
        global fal
        fal = Toplevel(root)
        fal.title("INCORRECTO")
        fal.geometry("250x150")
        fal.config(bg="#F43131")
        fal.iconbitmap("math.ico")
        fal.resizable(0, 0)
        textfal = tk.Label(fal, font="robot 18",
                           justify="center", text="Respuesta Incorrecta")
        textfal2 = tk.Label(fal, font="robot 20", justify="center")
        textfal2["text"] = resultado
        textfal.pack(pady="10")
        textfal.config(bg="#F43131")
        textfal2.pack(pady="10")
        textfal2.config(bg="#F43131")
        botonfal = tk.Button(fal, text="Cerrar", padx="20",
                             pady="5", command=lambda: (resetfal()))
        botonfal.pack()
        #print("Respuesta Incorrecta")
        #print(resultado)
        #print(respuesta)
        i += 1
        correct = correct
        #print("i= ", i)
        #print("correct= ", correct)


def resetverd():
    verd.destroy()
    if i != 10:
        texto2.pack_forget()
        texto3.pack_forget()
        cajatexto2.pack_forget()
        boton2.pack_forget()
        textdescr.pack_forget()
        calculator()
    else:
        #print("A")
        texto2.pack_forget()
        texto3.pack_forget()
        cajatexto2.pack_forget()
        boton2.pack_forget()
        textdescr.pack_forget()
        textofin = tk.Label(root, font="robot 40 bold", justify="center")
        textofin.pack(pady="60")
        textofin.config(bg="#fcd46c")
        textofin["text"] = nombre
        textofin2 = tk.Label(root, font="robot 20 bold", justify="center")
        textofin2.config(bg="#fcd46c")
        textofin2.pack(pady="50")
        if correct >= 1:
            textofin2["text"] = "Usted tuvo " + str(
                correct) + " operacion(es) correctas de 10"
        else:
            textofin2["text"] = "Usted no tuvo ninguna bien, esfuerzate mas"
        botoncerrar = tk.Button(
            root, text="Salir", font="robot 20", padx="20", pady="5", command=lambda: (root.destroy()))
        botoncerrar.pack(pady="30")


def resetfal():
    fal.destroy()
    if i != 10:
        texto2.pack_forget()
        texto3.pack_forget()
        cajatexto2.pack_forget()
        boton2.pack_forget()
        textdescr.pack_forget()
        calculator()
    else:
        #print("A")
        texto2.pack_forget()
        texto3.pack_forget()
        cajatexto2.pack_forget()
        boton2.pack_forget()
        textdescr.pack_forget()
        textofin = tk.Label(root, font="robot 40 bold", justify="center")
        textofin.config(bg="#fcd46c")
        textofin.pack(pady="60")
        textofin["text"] = nombre
        textofin2 = tk.Label(root, font="robot 20 bold", justify="center")
        textofin2.config(bg="#fcd46c")
        textofin2.pack(pady="50")
        if correct >= 1:
            textofin2["text"] = "Usted tuvo " + str(
                correct) + " operacion(es) correctas de 10"
        else:
            textofin2["text"] = "Usted no tuvo ninguna bien, esfuerzate más"
        botoncerrar = tk.Button(
            root, text="Salir", font="robot 20", padx="20", pady="5", command=lambda: (root.destroy()))
        botoncerrar.pack(pady="30")


root.mainloop()
