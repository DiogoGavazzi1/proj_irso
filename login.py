from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # Importar Pillow para manipular imagens
import webbrowser  # Para redirecionar para uma página web


def check_login():
    username = user.get()
    password = code.get()

    if username == "Admin" and password == "Password":
        webbrowser.open("https://diogogavazzi1.github.io/proj_irso/")  # Substitua pela URL desejada
    else:
        messagebox.showerror("Erro", "Nome de utilizador ou senha incorretos.")


def on_enter_user(e):
    if user.get() == 'Username':
        user.delete(0, 'end')
        user.config(fg='black')


def on_leave_user(e):
    if user.get() == '':
        user.insert(0, 'Username')
        user.config(fg='grey')


def on_enter_code(e):
    if code.get() == 'Password':
        code.delete(0, 'end')
        code.config(fg='black', show='*')


def on_leave_code(e):
    if code.get() == '':
        code.insert(0, 'Password')
        code.config(fg='grey', show='')


root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.config(bg="#fff")
root.resizable(False, False)

# Redimensionar a imagem usando Pillow
original_image = Image.open("museu.png")  # Abrir a imagem original
resized_image = original_image.resize((300, 300), Image.Resampling.LANCZOS)  # Redimensionar a imagem
img = ImageTk.PhotoImage(resized_image)  # Converter para PhotoImage

Label(root, image=img, bg='White').place(x=50, y=50)  # Mostrar imagem no Tkinter

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

# Campo de utilizador
user = Entry(frame, width=25, fg='grey', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')  # Placeholder padrão
user.bind('<FocusIn>', on_enter_user)
user.bind('<FocusOut>', on_leave_user)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# Campo de senha
code = Entry(frame, width=25, fg='grey', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')  # Placeholder padrão
code.bind('<FocusIn>', on_enter_code)
code.bind('<FocusOut>', on_leave_code)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# Botão de login
Button(frame, width=39, pady=7, text='Sign In', bg='#57a1f8', fg='white', border=0, command=check_login).place(x=35, y=204)

root.mainloop()
