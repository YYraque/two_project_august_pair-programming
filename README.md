🐍 Projetos Educacionais em Python - Finanças, História e GUI
Este repositório contém uma coleção de aplicações gráficas desenvolvidas em Python utilizando Tkinter e componentes modernos. Os projetos foram elaborados com foco didático para alunos do programa Jovem Aprendiz, integrando conceitos de programação procedural e orientada a objetos, educação financeira e história do Brasil.

🎯 Objetivos Didáticos
Evolução de Paradigmas: Transição da programação procedural (uso de funções, parâmetros e escopo global) para a Programação Orientada a Objetos - POO (classes, encapsulamento e gerenciamento de estado via self).

Interfaces Gráficas (GUI): Construção de telas interativas com tkinter e ttk utilizando Frame, Label, Entry, Button, Listbox, ttk.Notebook e personalização de temas com ttk.Style.

Tratamento de Exceções e Validação: Uso de blocos try/except para prevenção de falhas no parser numérico (ValueError) e controle de lógica de negócios (saldo insuficiente).

Consumo de APIs e Imagens HTTP: Integração com serviços Web (requests), geração de dados fictícios em português (faker) e processamento de imagens em memória (Pillow).

🚀 Projetos Incluídos
1. 🏛️ PyBank - Sistema Bancário Moderno em POO (pybank_app.py)
Aplicação bancária completa escrita sob o paradigma de Programação Orientada a Objetos (POO) e com visual moderno baseado na paleta Catppuccin.

Destaques:

Estruturação modular usando classe BancoApp.

Gerador de dados fictícios via Faker (pt_BR) para cliente, agência e CPF.

Integração com a API DiceBear para download e renderização dinâmica do avatar do cliente.

Histórico de transações em tempo real com extrato formatado.

2. 📜 Linha do Tempo: Eufrásia Teixeira Leite (historia_financas_eufrasia.py)
Uma interface interativa sobre Eufrásia Teixeira Leite (1850–1930), a primeira investidora global do Brasil.

Destaques:

Download e exibição da foto histórica via requisição HTTP (requests + Pillow).

Tratamento de erros de rede com fallback gracioso para manter a aplicação funcional offline.

Botões interativos que disparam janelas de informação (messagebox) com fatos da história financeira nacional.

3. 💵 Simulador de Aportes (simulador_aportes.py)
Uma calculadora de fluxo de caixa simplificada em estilo procedural para ensinar operações básicas de depósito e saque.

Destaques:

Controle de saldo em tempo real via variáveis globais.

Travas de segurança para impedimento de depósitos zerados/negativos e saques acima do saldo disponível.

Limpeza automática dos campos de entrada (Entry.delete) após a execução das operações.

4. 📊 Dashboard Financeiro - Padrão B3 (dashboard_bankb3.py)
Um painel completo simulando o ambiente visual e operacional da Bolsa de Valores brasileira (B3).

Destaques:

Navegação entre seções utilizando Abas (ttk.Notebook): Conta Corrente, Criptoativos e Extrato.

Módulo de simulação para compra de frações de criptomoedas (Bitcoin - BTC).

Componente tk.Listbox para exibição cronológica das movimentações.

🛠️ Pré-requisitos e Instalação
Para executar os projetos, você precisará do Python 3.10+ instalado em sua máquina.

1. Instalação das dependências
Abra o terminal ou prompt de comando e instale as bibliotecas necessárias:

Bash
pip install requests pillow faker
Ou, caso esteja utilizando múltiplos ambientes Python:

Bash
python -m pip install requests pillow faker
Nota para usuários Linux (Ubuntu/Debian): O tkinter pode não vir instalado por padrão na distribuição Python do SO. Caso necessário, instale com:
sudo apt-get install python3-tkinter

💻 Como Executar as Aplicações
Navegue até a pasta do projeto no seu terminal e execute o arquivo desejado:

Bash
# 1. Executar o PyBank (POO + API de Avatares)
python pybank_app.py

# 2. Executar a Linha do Tempo de Eufrásia
python historia_financas_eufrasia.py

# 3. Executar o Simulador de Aportes
python simulador_aportes.py

# 4. Executar o Dashboard B3
python dashboard_bankb3.py
🗂️ Estrutura do Repositório
Plaintext
.
├── pybank_app.py                 # Sistema bancário orientado a objetos (Faker + DiceBear API)
├── historia_financas_eufrasia.py  # Aplicação interativa sobre Eufrásia Teixeira Leite
├── simulador_aportes.py          # Simulador procedural de depósitos e saques
├── dashboard_bankb3.py           # Dashboard financeiro com abas estilo B3
└── README.md                     # Documentação do repositório

💙 Projeto desenvolvido para fins educacionais e de capacitação profissional.