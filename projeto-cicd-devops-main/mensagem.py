
def mensagem_personalizada(nome):
    return f"Olá, {nome}! Seja bem-vindo(a) ao seu primeiro projeto CI/CD no GitHub!"

if __name__ == '__main__':
    nome_usuario = input("Digite seu nome: ")
    print(mensagem_personalizada(nome_usuario))
