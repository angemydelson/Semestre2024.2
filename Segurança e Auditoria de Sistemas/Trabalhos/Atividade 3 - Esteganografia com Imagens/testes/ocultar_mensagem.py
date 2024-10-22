from PIL import Image

def esconder_mensagem(imagem_caminho, mensagem, imagem_saida):
    # Carregar a imagem
    img = Image.open(imagem_caminho)
    img = img.convert('RGB')
    largura, altura = img.size
    pixels = img.load()
    
    # Converter a mensagem para binário
    mensagem_bin = ''.join(format(ord(c), '08b') for c in mensagem) + '1111111111111110'  # Marcador de fim
    
    # Verificar se a mensagem cabe na imagem
    if len(mensagem_bin) > largura * altura * 3:
        raise ValueError("Mensagem muito longa para a imagem fornecida.")
    
    mensagem_idx = 0
    
    # Ocultar a mensagem nos pixels
    for y in range(altura):
        for x in range(largura):
            r, g, b = pixels[x, y]
            if mensagem_idx < len(mensagem_bin):
                r = (r & ~1) | int(mensagem_bin[mensagem_idx])
                mensagem_idx += 1
            if mensagem_idx < len(mensagem_bin):
                g = (g & ~1) | int(mensagem_bin[mensagem_idx])
                mensagem_idx += 1
            if mensagem_idx < len(mensagem_bin):
                b = (b & ~1) | int(mensagem_bin[mensagem_idx])
                mensagem_idx += 1
            pixels[x, y] = (r, g, b)
    
    # Salvar a nova imagem com a mensagem oculta
    img.save(imagem_saida)
    print(f"Mensagem escondida na imagem {imagem_saida}")

# Exemplo de uso
if __name__ == "__main__":
    imagem_entrada = 'Teste.png'  # Coloque o caminho da imagem de entrada
    mensagem = 'Esta é uma mensagem secreta do Angemydelson.'  # A mensagem que você deseja esconder
    imagem_saida = 'imagem_saida.png'  # Nome da imagem de saída

    esconder_mensagem(imagem_entrada, mensagem, imagem_saida)
