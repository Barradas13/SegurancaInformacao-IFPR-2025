import tkinter as tk
from tkinter import messagebox
from KeyManipulation import cript, decript

def encrypt_message():
    password = password_entry.get()
    message = message_entry.get()
    
    if not password or not message:
        messagebox.showerror("Erro", "Por favor, preencha a senha e a mensagem.")
        return
    
    resultado = cript(message, password)

    result_label.config(text=f"Mensagem Criptografada: {resultado}")

def decrypt_message():
    password = password_entry.get()
    message = message_entry.get()
    
    if not password or not message:
        messagebox.showerror("Erro", "Por favor, preencha a senha e a mensagem.")
        return
    
    decrypted = decript(message, password)

    frase = ""

    for i in decrypted:
        frase += chr(int(i))

    result_label.config(text=f"Mensagem Descriptografada: {frase}")

# Configurar janela principal
root = tk.Tk()
root.title("Criptografia Simples")

# Campo para a senha
tk.Label(root, text="Senha:").grid(row=0, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=0, column=1, padx=10, pady=10)

# Campo para a mensagem
tk.Label(root, text="Mensagem:").grid(row=1, column=0, padx=10, pady=10)
message_entry = tk.Entry(root, width=40)
message_entry.grid(row=1, column=1, padx=10, pady=10)

# Botões de Cript e Uncript
encrypt_button = tk.Button(root, text="Cript", command=encrypt_message)
encrypt_button.grid(row=2, column=0, padx=10, pady=10)

decrypt_button = tk.Button(root, text="Uncript", command=decrypt_message)
decrypt_button.grid(row=2, column=1, padx=10, pady=10)

# Rótulo para exibir o resultado
result_label = tk.Label(root, text="Resultado aparecerá aqui", wraplength=400)
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Iniciar o loop da interface gráfica
root.mainloop()
