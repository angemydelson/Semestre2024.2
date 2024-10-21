from PIL import Image

def extrair_mensagem(imagem_caminho):
    # Carregar a imagem
    img = Image.open(imagem_caminho)
    img = img.convert('RGB')
    largura, altura = img.size
    pixels = img.load()
    
    mensagem_bin = ''
    
    # Extrair os bits da mensagem dos pixels
    for y in range(altura):
        for x in range(largura):
            r, g, b = pixels[x, y]
            mensagem_bin += str(r & 1)
            mensagem_bin += str(g & 1)
            mensagem_bin += str(b & 1)
    
    # Converter os bits em caracteres
    mensagem = ''
    for i in range(0, len(mensagem_bin), 8):
        byte = mensagem_bin[i:i+8]
        if byte == '11111111':  # Marcador de fim
            break
        mensagem += chr(int(byte, 2))
    
    return mensagem

# Exemplo de uso
if __name__ == "__main__":
    imagem_oculta = 'imagem_saida.png'  # Coloque o caminho da imagem com a mensagem oculta
    mensagem_oculta = extrair_mensagem(imagem_oculta)
    print(f"Mensagem extraída: {mensagem_oculta}")
