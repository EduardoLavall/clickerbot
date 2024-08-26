import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")

def click():
    print("pauzão gordo")

texto = customtkinter.CTkLabel(janela, text="text1")
email = customtkinter.CTkEntry(janela, placeholder_text="input1")
botao = customtkinter.CTkButton(janela, text="button", command=click)

texto.pack(padx= 10, pady= 10)
email.pack(padx= 10, pady= 10)
botao.pack(padx= 10, pady= 10)

janela.mainloop()