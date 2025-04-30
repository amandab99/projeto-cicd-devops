def saudacao(hora):
    if 6 <= hora < 12:
        return "Bom dia!"
    elif 12 <= hora < 18:
        return "Boa tarde!"
    elif 18 <= hora <= 23:
        return "Boa noite!"
    else:
        return "Boa madrugada!"
