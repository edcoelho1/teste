import customtkinter as ctk #importar o q faz janelas
resultado="a" #valor inicial (nulo)
def botao_0():
    global resultado
    resultado= resultado+ "0"
    print(resultado[1:])
def botao_1():
    global resultado
    resultado= resultado + "1"
    print(resultado[1:])
def botao_2():
    global resultado
    resultado= resultado + "2"
    print(resultado[1:])
def botao_3():
    global resultado
    resultado= resultado + "3"
    print(resultado[1:])
def botao_4():
    global resultado
    resultado= resultado + "4"
    print(resultado[1:])
def botao_5():
    global resultado
    resultado= resultado + "5"
    print(resultado[1:])
def botao_6():
    global resultado
    resultado= resultado + "6"
    print(resultado[1:])
def botao_7():
    global resultado
    resultado= resultado + "7"
    print(resultado[1:])
def botao_8():
    global resultado
    resultado= resultado + "8"
    print(resultado[1:])
def botao_9():
    global resultado
    resultado= resultado + "9"
    print(resultado[1:])
def botao_soma():
    global resultado
    resultado= resultado + "+"
    print(resultado[1:])
def botao_subtração():
    global resultado
    resultado= resultado + "-"
    print(resultado[1:])
def botao_multiplicação():
    global resultado
    resultado= resultado + "*"
    print(resultado[1:])
def botao_divisão():
    global resultado
    resultado= resultado + "/"
def botao_exp():
    global resultado
    resultado= resultado + "**"
def botao_igual():
    global resultado
    resultado=resultado.replace("a","")
    try:
        while resultado[0] == '0' and resultado[1] not in {"+", "-", "*", "/", "**"}:
            resultado=resultado[1:]
        print(eval(resultado))
    except ZeroDivisionError:
        print("Não é possível dividir por 0.")
    except IndexError:
        print("Por favor, insira ao menos 2 dígitos e uma operação!")
    resultado="a" #Retornando ao valor inicial


ctk.set_appearance_mode("dark") #criar e configurar
ctk.set_default_color_theme("blue")

janela=ctk.CTk()
janela.geometry("700x200")#Dimensões da janela

botão_0=ctk.CTkButton(janela , text="0", command=botao_0)
botão_0.grid(row=4, column=0, padx=10, pady=10)

botão_1=ctk.CTkButton(janela , text="1", command=botao_1)
botão_1.grid(row=3, column=0, padx=10, pady=10)

botão_2=ctk.CTkButton(janela , text="2", command=botao_2)
botão_2.grid(row=3, column=2, padx=10, pady=10)

botão_3=ctk.CTkButton(janela , text="3", command=botao_3)
botão_3.grid(row=3, column=3, padx=10, pady=10)

botão_4=ctk.CTkButton(janela , text="4", command=botao_4)
botão_4.grid(row=2, column=0, padx=10, pady=10)

botão_5=ctk.CTkButton(janela , text="5", command=botao_5)
botão_5.grid(row=2, column=2, padx=10, pady=10)

botão_6=ctk.CTkButton(janela , text="6", command=botao_6)
botão_6.grid(row=2, column=3, padx=10, pady=10)

botão_7=ctk.CTkButton(janela , text="7", command=botao_7)
botão_7.grid(row=0, column=0, padx=10, pady=10)

botão_8=ctk.CTkButton(janela , text="8", command=botao_8)
botão_8.grid(row=0, column=2, padx=10, pady=10)

botão_9=ctk.CTkButton(janela , text="9", command=botao_9)
botão_9.grid(row=0, column=3, padx=10, pady=10)

botão_so=ctk.CTkButton(janela , text="+", command=botao_soma)
botão_so.grid(row=0, column=4, padx=10, pady=10)

botão_su=ctk.CTkButton(janela , text="-", command=botao_subtração)
botão_su.grid(row=2, column=4, padx=10, pady=10)

botão_mu=ctk.CTkButton(janela , text="*", command=botao_multiplicação)
botão_mu.grid(row=3, column=4, padx=10, pady=10)

botão_di=ctk.CTkButton(janela , text="/", command=botao_divisão)
botão_di.grid(row=4, column=2, padx=10, pady=10)

botão_exp=ctk.CTkButton(janela , text="^", command=botao_exp)
botão_exp.grid(row=4, column=3, padx=10, pady=10)

botão_i=ctk.CTkButton(janela , text="=", command=botao_igual)
botão_i.grid(row=4, column=4, padx=10, pady=10)

janela.mainloop() #Rodar a janela