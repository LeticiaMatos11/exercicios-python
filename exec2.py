while True: 
    comando = input ("Digite um comando (ou 'sair' para encerrar): ")
    if comando.lower() == 'sair' :
        print("Encerrando p programa...")
        break # A trava de segurança foi acionada!
    else:
        print("O motor continua a roda...")