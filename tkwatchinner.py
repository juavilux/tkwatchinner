import tkinter as tk
import time

def atualizar_relógio():
    hora_atual = time.strftime('%H:%M:%S')
    label_relogio.config(text=hora_atual)
    janela.after(1000, atualizar_relógio)

# Mock do clima (poderia vir de uma API depois)
def atualizar_clima():
    clima_mock = "☀️ 29°C"
    label_clima.config(text=clima_mock)

# Criação da janela
janela = tk.Tk()
janela.title("Relógio Digital")
janela.configure(bg="black")

# Fonte estilo relógio digital
fonte_relogio = ("DS-Digital", 60, "bold")  # Pode instalar essa fonte se não tiver

# Label do relógio
label_relogio = tk.Label(janela, font=fonte_relogio, fg="red", bg="black")
label_relogio.pack(side="left", padx=20, pady=20)

# Label do clima
label_clima = tk.Label(janela, font=("Arial", 20), fg="white", bg="black")
label_clima.pack(side="left", padx=10)

# Inicia atualização
atualizar_relógio()
atualizar_clima()

# Loop principal
janela.mainloop()
