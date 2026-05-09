# Message Bus Distribuído com Relógios Lógicos de Lamport

## 📖 Sobre o Projeto

Este projeto implementa um **Message Bus (Barramento de Mensagens)** inspirado nos conceitos de sistemas distribuídos apresentados por Deitel.

A aplicação utiliza um **Message Buffer centralizado** para intermediar a comunicação entre produtores e consumidores, garantindo desacoplamento entre os processos e controle da ordenação lógica das mensagens.

Além disso, o sistema implementa:

- Comunicação distribuída via TCP
- Relógios Lógicos de Lamport
- Criptografia de mensagens
- Auditoria de eventos
- Modos de envio Unicast, Multicast e Broadcast

---

# 🧠 Tecnologias Utilizadas

- Python 3
- Sockets TCP
- Biblioteca `cryptography`
- Relógios Lógicos de Lamport

---

# ⚙ Pré-requisitos

Antes de executar o projeto, certifique-se de possuir:

- Python 3 instalado
- Pip instalado

---

# 📦 Instalação da Dependência

Abra o terminal na pasta do projeto e execute:

```bash
pip install cryptography
```

---

# 🚀 Como Executar o Projeto

Para simular corretamente um ambiente distribuído, o sistema deve ser executado em **3 terminais diferentes**.

---

# 🖥 Passo 1 — Iniciar o Servidor

No primeiro terminal, execute:

```bash
python src/tester.py
```

Depois escolha a opção:

```text
1 - Iniciar Servidor
```

## ✅ O que acontece?

O servidor (`MsgQMgr`) será iniciado utilizando TCP na porta 5000.

Ele será responsável por:

- Gerenciar o Message Buffer
- Receber mensagens
- Controlar a ordenação lógica
- Gerenciar exclusão mútua

## ✅ Exemplo esperado

```text
Servidor iniciado na porta 5000...
Aguardando conexões...
```

---

# 🖥 Passo 2 — Iniciar o Produtor

No segundo terminal, execute:

```bash
python src/tester.py
```

Depois escolha:

```text
2 - Iniciar Produtor
```

O sistema solicitará:

## 🔹 ID do produtor

Exemplo:

```text
Produtor_Alpha
```

## 🔹 Tipo de envio

Escolha uma opção:

```text
1 - Unicast
2 - Multicast
3 - Broadcast
```

## 🔹 Mensagem

Digite a mensagem desejada:

```text
Olá consumidor!
```

## ✅ O que acontece?

O produtor:

1. Criptografa a mensagem
2. Adiciona um timestamp lógico de Lamport
3. Envia os dados ao barramento central

## ✅ Exemplo esperado

```text
Mensagem enviada com sucesso.
Lamport Clock: 3
```

---

# 🖥 Passo 3 — Iniciar o Consumidor

No terceiro terminal, execute:

```bash
python src/tester.py
```

Depois escolha:

```text
3 - Iniciar Consumidor
```

## ✅ O que acontece?

O consumidor:

1. Solicita mensagens ao servidor
2. Recebe os dados
3. Decifra a mensagem
4. Atualiza o relógio lógico local

## ✅ Exemplo esperado

```text
Mensagem recebida:
Olá consumidor!

Lamport Clock sincronizado: 4
```

---

# 📋 Auditoria do Sistema

Para visualizar os logs do sistema, execute novamente:

```bash
python src/tester.py
```

Escolha:

```text
4 - Exibir Auditoria
```

## ✅ O que será exibido?

O arquivo `audit.log` mostrará todos os eventos registrados no sistema.

## ✅ Exemplo esperado

```text
[Lamport: 1] Servidor iniciado
[Lamport: 3] Produtor_Alpha enviou mensagem
[Lamport: 4] Consumidor recebeu mensagem
```

---

# 🔄 Fluxo Geral do Sistema

```text
Produtor
   ↓
Criptografia + Timestamp Lamport
   ↓
Message Buffer (Servidor)
   ↓
Consumidor
   ↓
Decifragem + Sincronização Lógica
```

---

# 🔒 Segurança

O sistema utiliza criptografia para proteger as mensagens transmitidas pela rede, garantindo:

- Confidencialidade
- Integridade da comunicação
- Segurança entre os processos distribuídos

---

# 📚 Conceitos Aplicados

Este projeto aplica conceitos fundamentais de:

- Sistemas Distribuídos
- Comunicação Cliente-Servidor
- Exclusão Mútua
- Relógios Lógicos
- Middleware
- Segurança da Informação

---

# 📌 Fluxo Correto de Execução

```text
1° Terminal → Servidor
2° Terminal → Produtor
3° Terminal → Consumidor
4° Terminal (Opcional) → Auditoria
```

---

# ⚠ Observações Importantes

- O servidor deve ser iniciado antes do produtor e consumidor.
- Todos os terminais devem estar na pasta do projeto.
- Certifique-se de possuir Python 3 instalado.
- O sistema utiliza comunicação TCP na porta 5000.

---

# 👨‍💻 Objetivo Acadêmico

O objetivo deste projeto é demonstrar, na prática, o funcionamento de um barramento de mensagens distribuído com ordenação lógica e comunicação segura utilizando conceitos clássicos de sistemas distribuídos.
