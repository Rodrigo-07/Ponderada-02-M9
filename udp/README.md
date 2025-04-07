# Implementação UDP

['HOW TO RUN' criado com o GPT]


# How to Run

## 1. Iniciar o Servidor

No primeiro terminal, execute:

```bash
python3 server.py
```

- O servidor usa `socket.SOCK_DGRAM` (UDP normal).
- Ele ficará escutando na porta (por exemplo, 6565) e imprimirá qualquer mensagem recebida.

---

## 2. Iniciar o Cliente (Raw Socket)

Em outro terminal, execute:

```bash
sudo python3 client.py
```

- É necessário `sudo` porque o cliente usa um *raw socket* (`socket.SOCK_RAW`), que requer privilégios de root.
- No terminal do servidor, deve aparecer a mensagem recebida.

---

## 3. Capturar Pacotes com `tcpdump` (Opcional)

Se quiser ver os pacotes em formato hexadecimal, abra um terceiro terminal:

```bash
sudo tcpdump -i lo -nn -X udp port 6565
```

- `-i lo`: captura na interface de loopback (`127.0.0.1`).
- `-nn`: evita a conversão de IP/porta em nomes.
- `-X`: mostra o hexdump do pacote.

Assim que você executar novamente o cliente, o `tcpdump` exibirá o pacote UDP (com cabeçalho IP e payload).

Obs: esse projeto só foi testado com Linux