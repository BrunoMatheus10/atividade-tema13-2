# Solicita ao usuário que insira um e-mail para validação
email = input("Digite o e-mail para validação: ")

# Inicializa variáveis de controle
arroba_encontrado = False  # Indica se o caractere '@' foi encontrado
ponto_encontrado = False   # Indica se o caractere '.' foi encontrado no domínio
parte_local = ""           # Parte local do e-mail (antes do '@')
dominio = ""               # Parte do domínio do e-mail (depois do '@')
valido = True              # Indica se o e-mail é válido

# Percorre cada caractere do e-mail
i = 0
while i < len(email):
    try:
        if email[i] == '@':
            if arroba_encontrado:
                # Se já encontrou um '@', o e-mail é inválido
                valido = False
            else:
                arroba_encontrado = True  # Marca que encontrou o '@'
        elif arroba_encontrado:
            dominio += email[i]  # Adiciona o caractere ao domínio
        else:
            parte_local += email[i]  # Adiciona o caractere à parte local
    except IndexError:
        valido = False  # Captura possíveis erros de índice
    i += 1

# Verifica se o domínio contém um ponto
for char in dominio:
    if char == '.':
        ponto_encontrado = True  # Marca que encontrou um ponto no domínio

# Verifica se todas as condições foram atendidas
if valido and arroba_encontrado and ponto_encontrado and parte_local and dominio and len(dominio) >= 3 and dominio[-2] != '.':
    print(email," é um e-mail válido.")  # E-mail é válido
else:
    print(email," é um e-mail inválido.")  # E-mail é inválido
