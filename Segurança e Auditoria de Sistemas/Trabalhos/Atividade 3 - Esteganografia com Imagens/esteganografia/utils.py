def string_to_binary(mensagem):
    """Converte uma string de texto em uma sequência binária."""
    return ''.join(format(ord(c), '08b') for c in mensagem)

def binary_to_string(mensagem_bin):
    """Converte uma sequência binária de volta para texto."""
    mensagem = ''
    for i in range(0, len(mensagem_bin), 8):
        byte = mensagem_bin[i:i+8]
        mensagem += chr(int(byte, 2))
    return mensagem

def apply_key(mensagem_bin, chave, decrypt=False):
    """Aplica uma chave para criptografar ou descriptografar uma mensagem binária."""
    chave_bin = string_to_binary(chave)
    mensagem_keyed = ''
    
    for i in range(len(mensagem_bin)):
        if decrypt:
            mensagem_keyed += str(int(mensagem_bin[i]) ^ int(chave_bin[i % len(chave_bin)]))  # XOR para descriptografia
        else:
            mensagem_keyed += str(int(mensagem_bin[i]) ^ int(chave_bin[i % len(chave_bin)]))  # XOR para criptografia
    
    return mensagem_keyed
