from PIL import Image
import logging
from esteganografia.utils import string_to_binary, binary_to_string, apply_key

# Configurando o logger
logging.basicConfig(filename='logs/esteganografia.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def verificar_espaco(imagem_caminho, mensagem):
    """Verifica se a imagem tem espaço suficiente para ocultar a mensagem."""
    img = Image.open(imagem_caminho)
    largura, altura = img.size
    max_bits = largura * altura * 3
    mensagem_bin = ''.join(format(ord(c), '08b') for c in mensagem) + '1111111111111110'
    
    if len(mensagem_bin) > max_bits:
        logging.error("A mensagem é muito grande para a imagem fornecida.")
        raise ValueError("A mensagem é muito grande para a imagem fornecida.")
    else:
        logging.info("Espaço suficiente disponível para ocultar a mensagem.")
        return True

def esconder_mensagem(imagem_caminho, mensagem, imagem_saida, chave=None):
    """Oculta uma mensagem em uma imagem, com uma chave opcional para criptografia."""
    img = Image.open(imagem_caminho)
    img = img.convert('RGB')
    largura, altura = img.size
    pixels = img.load()

    # Converter a mensagem para binário e aplicar a chave se houver
    mensagem_bin = string_to_binary(mensagem)
    if chave:
        mensagem_bin = apply_key(mensagem_bin, chave)
    mensagem_bin += '1111111111111110'  # Marcador de fim

    mensagem_idx = 0
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
    
    img.save(imagem_saida)
    logging.info(f"Mensagem escondida na imagem {imagem_saida}")
    print(f"Mensagem escondida com sucesso na imagem: {imagem_saida}")

def extrair_mensagem(imagem_caminho, chave=None):
    """Extrai a mensagem oculta de uma imagem, com uma chave opcional para descriptografia."""
    img = Image.open(imagem_caminho)
    img = img.convert('RGB')
    largura, altura = img.size
    pixels = img.load()

    mensagem_bin = ''
    for y in range(altura):
        for x in range(largura):
            r, g, b = pixels[x, y]
            mensagem_bin += str(r & 1)
            mensagem_bin += str(g & 1)
            mensagem_bin += str(b & 1)

    # Remover marcador de fim e descriptografar se chave for fornecida
    marcador_fim = mensagem_bin.find('1111111111111110')
    mensagem_bin = mensagem_bin[:marcador_fim]
    
    if chave:
        mensagem_bin = apply_key(mensagem_bin, chave, decrypt=True)

    mensagem = binary_to_string(mensagem_bin)
    logging.info("Mensagem extraída com sucesso.")
    return mensagem
