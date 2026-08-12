import io
import random
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from faker import Faker
from PIL import Image, ImageTk
import requests

fake = Faker("pt_BR")


class BancoApp:

    def __init__(self, root):
        self.root = root
        self.root.title("PyBank - Sistema Bancário")
        self.root.geometry("450x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#1E1E2E")

        self.nome_cliente = fake.name()
        self.agencia = "0001"
        self.conta = fake.bank_country() + "-" + str(fake.random_digit())
        self.saldo = round(random.uniform(1500.00, 10000.00), 2)

        self.historico = [
            {"tipo": "Depósito Inicial", "valor": self.saldo, "data": "Hoje"}
        ]

        self._setup_styles()
        self._criar_header()
        self._criar_card_saldo()
        self._criar_painel_acoes()
        self._criar_historico_view()

    def _setup_styles(self):
        """Configura estilos dos widgets ttk"""
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Bank.TButton",
            font=("Helvetica", 11, "bold"),
            foreground="#FFFFFF",
            background="#89B4FA",
            padding=10,
            borderwidth=0,
        )
        self.style.map("Bank.TButton", background=[("active", "#74C7EC")])

    def _carregar_avatar(self):
        """Carrega uma imagem da web via Requests e exibe via PIL"""
        url_avatar = f"https://api.dicebear.com/7.x/bottts/png?seed={self.nome_cliente.replace(' ', '')}"
        try:
            response = requests.get(url_avatar, timeout=5)
            if response.status_code == 200:
                image_data = response.content
                image = Image.open(io.BytesIO(image_data))
                image = image.resize((60, 60), Image.Resampling.LANCZOS)
                return ImageTk.PhotoImage(image)
        except Exception:
            pass

        img_fallback = Image.new("RGB", (60, 60), color="#B4BEFE")
        return ImageTk.PhotoImage(img_fallback)

    def _criar_header(self):
        """Painel superior com avatar e dados do cliente"""
        header_frame = tk.Frame(self.root, bg="#181825")
        header_frame.pack(fill="x", padx=15, pady=(15, 5))

        self.avatar_img = self._carregar_avatar()
        avatar_label = tk.Label(
            header_frame, image=self.avatar_img, bg="#181825"
        )
        avatar_label.pack(side="left", padx=(5, 15))

        info_frame = tk.Frame(header_frame, bg="#181825")
        info_frame.pack(side="left")

        lbl_boas_vindas = tk.Label(
            info_frame,
            text=f"Olá, {self.nome_cliente.split()[0]}!",
            font=("Helvetica", 14, "bold"),
            fg="#CDD6F4",
            bg="#181825",
        )
        lbl_boas_vindas.pack(anchor="w")

        lbl_conta = tk.Label(
            info_frame,
            text=f"Ag: {self.agencia} | CC: {self.conta}",
            font=("Helvetica", 9),
            fg="#A6ADC8",
            bg="#181825",
        )
        lbl_conta.pack(anchor="w")

    def _criar_card_saldo(self):
        """Card central para visualização do saldo"""
        card = tk.Frame(self.root, bg="#313244", bd=0, relief="flat")
        card.pack(fill="x", padx=15, pady=10, ipady=10)

        lbl_titulo_saldo = tk.Label(
            card,
            text="Saldo Disponível",
            font=("Helvetica", 10),
            fg="#BAC2DE",
            bg="#313244",
        )
        lbl_titulo_saldo.pack(anchor="w", padx=15, pady=(10, 0))

        self.lbl_saldo = tk.Label(
            card,
            text=f"R$ {self.saldo:,.2f}".replace(",", "X")
            .replace(".", ",")
            .replace("X", "."),
            font=("Helvetica", 22, "bold"),
            fg="#A6E3A1",
            bg="#313244",
        )
        self.lbl_saldo.pack(anchor="w", padx=15, pady=(0, 10))

    def _criar_painel_acoes(self):
        """Botões de ação principal"""
        actions_frame = tk.Frame(self.root, bg="#1E1E2E")
        actions_frame.pack(fill="x", padx=15, pady=5)

        btn_deposito = ttk.Button(
            actions_frame,
            text="➕ Depósito",
            style="Bank.TButton",
            command=self._acao_deposito,
        )
        btn_deposito.pack(side="left", expand=True, fill="x", padx=(0, 5))

        btn_transferir = ttk.Button(
            actions_frame,
            text="💸 PIX / Transferir",
            style="Bank.TButton",
            command=self._acao_transferencia,
        )
        btn_transferir.pack(side="right", expand=True, fill="x", padx=(5, 0))

    def _criar_historico_view(self):
        """Seção com extrato rápido"""
        lbl_extrato = tk.Label(
            self.root,
            text="Últimas Movimentações",
            font=("Helvetica", 11, "bold"),
            fg="#CDD6F4",
            bg="#1E1E2E",
        )
        lbl_extrato.pack(anchor="w", padx=15, pady=(15, 5))

        frame_list = tk.Frame(self.root, bg="#1E1E2E")
        frame_list.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        self.listbox = tk.Listbox(
            frame_list,
            bg="#181825",
            fg="#CDD6F4",
            selectbackground="#45475A",
            bd=0,
            highlightthickness=0,
            font=("Helvetica", 10),
        )
        self.listbox.pack(fill="both", expand=True)

        self._atualizar_historico_listbox()

    def _atualizar_historico_listbox(self):
        """Atualiza o conteúdo da caixa de extrato"""
        self.listbox.delete(0, tk.END)
        for t in reversed(self.historico):
            sinal = "+" if "Depósito" in t["tipo"] else "-"
            item = f"{t['tipo']}: {sinal}R$ {t['valor']:.2f}"
            self.listbox.insert(tk.END, item)

    def _atualizar_saldo_label(self):
        """Atualiza o texto do saldo formatado"""
        texto_formatado = (
            f"R$ {self.saldo:,.2f}".replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )
        self.lbl_saldo.config(text=texto_formatado)

    def _acao_deposito(self):
        """Janela popup/dialog para depósitos"""
        val = simpledialog.askfloat(
            "Depósito", "Digite o valor do depósito (R$):", parent=self.root
        )
        if val is not None:
            if val > 0:
                self.saldo += val
                self.historico.append({"tipo": "Depósito", "valor": val})
                self._atualizar_saldo_label()
                self._atualizar_historico_listbox()
                messagebox.showinfo(
                    "Sucesso",
                    f"Depósito de R$ {val:.2f} realizado com sucesso!",
                )
            else:
                messagebox.showerror(
                    "Erro", "Digite um valor maior que zero."
                )

    def _acao_transferencia(self):
        """Janela popup/dialog para transferências"""
        chave_destino = fake.cpf()

        val = simpledialog.askfloat(
            "Transferência PIX",
            f"Chave PIX de Destino (Exemplo): {chave_destino}\n\nDigite o valor da transferência (R$):",
            parent=self.root,
        )

        if val is not None:
            if val <= 0:
                messagebox.showerror(
                    "Erro", "Digite um valor válido para transferência."
                )
            elif val > self.saldo:
                messagebox.showwarning(
                    "Saldo Insuficiente",
                    "Você não tem saldo suficiente para realizar esta operação.",
                )
            else:
                self.saldo -= val
                self.historico.append({"tipo": "PIX enviado", "valor": val})
                self._atualizar_saldo_label()
                self._atualizar_historico_listbox()
                messagebox.showinfo(
                    "PIX Realizado",
                    f"Transferência de R$ {val:.2f} enviada com sucesso!",
                )


if __name__ == "__main__":
    root = tk.Tk()
    app = BancoApp(root)
    root.mainloop()