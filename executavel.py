import tkinter
import tkinter as Tk
import sqlite3
import pandas as pd

# conexao = sqlite3.connect("banco_clientes.db")
#
# c = conexao.cursor()
#
# c.execute("""CREATE TABLE clientes(
#     nome text,
#     sobrenome text,
#     email text,
#     telefone text
#     )
#     """)
#
# conexao.commit()
#
# conexao.close()

def cadastrar_cliente():
    conexao = sqlite3.connect("banco_clientes.db")

    c = conexao.cursor()

    c.execute("INSERT INTO Clientes VALUES (:nome , :sobrenome , :email , :telefone)",
              {
                  'nome' :entry_nome.get(),
                  'sobrenome':entry_sobrenome.get(),
                  'email':entry_email.get(),
                  'telefone':entry_telefone.get()
              }
              )
    conexao.commit()

    conexao.close()

    entry_nome.delete(0,"end")
    entry_sobrenome.delete(0, "end")
    entry_telefone.delete(0, "end")
    entry_email.delete(0, "end")


def exporta_cliente():
    conexao = sqlite3.connect("banco_clientes.db")

    c = conexao.cursor()

    c.execute("SELECT*,oid FROM clientes")
    clientes_cadastrados = c.fetchall()
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados , columns=['nome','sobrenome','email','telefone','Id_Banco'])
    clientes_cadastrados.to_excel('banco_clientes.xlsx')
    conexao.commit()


    conexao.close()





janela = Tk.Tk()
janela.title('Cadastro de Clientes ')

# labels:

label_nome = Tk.Label(janela, text='Nome')
label_nome.grid(row=0 , column=0 , padx=10 , pady=10)

label_sobrenome = Tk.Label(janela, text='Sobrenome')
label_sobrenome.grid(row=1 , column=0 , padx=10 , pady=10)

label_email = Tk.Label(janela, text='Email')
label_email.grid(row=2 , column=0 , padx=10 , pady=10)

label_telefone = Tk.Label(janela, text='Telefone')
label_telefone.grid(row=3 , column=0 , padx=10 , pady=10)

#campo de preencimento

entry_nome = Tk.Entry(janela, text='Nome', width=30)
entry_nome.grid(row=0 , column=1 , padx=10 , pady=10)

entry_sobrenome = Tk.Entry(janela, text='Sobrenome',width=30)
entry_sobrenome.grid(row=1 , column=1 , padx=10 , pady=10)

entry_email = Tk.Entry(janela, text='Email', width=30)
entry_email.grid(row=2 , column=1 , padx=10 , pady=10)

entry_telefone = Tk.Entry(janela, text='Telefone', width=30)
entry_telefone.grid(row=3 , column=1 , padx=10 , pady=10)

#botoes

botao_cadastrar= Tk.Button(janela , text='Cadastrar Cliente' , command=cadastrar_cliente)
botao_cadastrar.grid(row=4, column= 0 , padx= 10 , pady= 10 , columnspan=2, ipadx=80)

botao_exportar= Tk.Button(janela , text='Exportar Base de clientes' , command=exporta_cliente)
botao_exportar.grid(row=5, column= 0 , padx= 10 , pady= 10 , columnspan=2 , ipadx=80)

janela.mainloop()