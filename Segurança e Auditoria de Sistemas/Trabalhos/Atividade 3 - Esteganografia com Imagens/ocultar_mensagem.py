from esteganografia.esteganografia import esconder_mensagem, verificar_espaco

if __name__ == "__main__":
    imagem_entrada = 'img/image1.png'
    mensagem = 'Mensagem secreta de teste do Angemydelson. Je suis lá, me voilá'
    imagem_saida = 'img_geradas/imagem_saida.png'
    chave = input("Digite a chave para criptografia (opcional): ")

    try:
        verificar_espaco(imagem_entrada, mensagem)
        esconder_mensagem(imagem_entrada, mensagem, imagem_saida, chave if chave else None)
    except ValueError as e:
        print(f"Erro: {e}")
