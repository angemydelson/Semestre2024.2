from esteganografia.esteganografia import extrair_mensagem

if __name__ == "__main__":
    imagem_oculta = 'img_geradas/imagem_saida.png'
    chave = input("Digite a chave para descriptografar a mensagem (opcional): ")

    try:
        mensagem = extrair_mensagem(imagem_oculta, chave if chave else None)
        print(f"Mensagem extraída: {mensagem}")
    except ValueError as e:
        print(f"Erro: {e}")
