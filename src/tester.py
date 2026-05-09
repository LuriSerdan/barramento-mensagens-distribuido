import threading
import time
import os
from msg_q_mgr import MsgQMgr
from middleware_stub import MessageStub

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    while True:
        limpar_tela()
        print("=== SISTEMA DE MENSAGERIA DISTRIBUÍDO ===")
        print(f"Projeto: {os.path.basename('DESENVOLVIMENTO DE UM BARRAMENTO DE MENSAGENS DISTRIBUÍDO')}")
        print("1. Iniciar Servidor (Middleware/MsgQMgr)")
        print("2. Iniciar Produtor (Simulação de Envio)")
        print("3. Iniciar Consumidor (Simulação de Recebimento)")
        print("4. Ver Log de Auditoria (audit.log)")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            print("\nIniciando Servidor... (Pressione Ctrl+C para parar)")
            try:
                server = MsgQMgr()
                server.start()
            except KeyboardInterrupt:
                pass
        
        elif opcao == '2':
            id_prod = input("Digite o ID do Produtor (ex: Produtor_01): ")
            stub = MessageStub(client_id=id_prod)
            msg = input("Mensagem a enviar: ")
            print("Modos: 1. Unicast | 2. Multicast (Grupo) | 3. Broadcast")
            modo_op = input("Escolha o modo: ")
            
            modo = "broadcast"
            alvo = None
            if modo_op == '1':
                modo = "unicast"
                alvo = input("ID do Destinatário: ")
            elif modo_op == '2':
                modo = "multicast"
                alvo = input("Nome do Canal/Grupo: ")

            res = stub.send_message(msg, mode=modo, target=alvo)
            print(f"\nStatus: {res['status']} | Mensagem enviada com sucesso!")
            input("\nPressione Enter para voltar...")

        elif opcao == '3':
            id_cons = input("Digite o ID do Consumidor (ex: Consumidor_A): ")
            stub = MessageStub(client_id=id_cons)
            print(f"Aguardando mensagens para {id_cons}...")
            res = stub.receive_message()
            
            if res.get("status") == "EMPTY":
                print("\nNenhuma mensagem pendente no buffer.")
            else:
                print("\n--- Mensagem Recebida ---")
                print(f"De: {res['producer']}")
                print(f"Conteúdo (Decifrado): {res['payload']}")
                print(f"Timestamp Lógico: {res['timestamp']}")
                print(f"Modo Original: {res['mode']}")
            input("\nPressione Enter para voltar...")

        elif opcao == '4':
            if os.path.exists("audit.log"):
                with open("audit.log", "r") as f:
                    print("\n=== LOG DE AUDITORIA ===")
                    print(f.read())
            else:
                print("\nArquivo de log ainda não criado.")
            input("\nPressione Enter para voltar...")

        elif opcao == '0':
            break

if __name__ == "__main__":
    menu_principal()