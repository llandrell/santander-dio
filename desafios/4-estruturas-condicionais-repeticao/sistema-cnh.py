MAIOR_IDADE = 18  # Define a idade mínima para tirar a CNH.

try:
    idade = int(input("Informe sua idade: "))
    idade_falta = MAIOR_IDADE - idade

    if idade >= MAIOR_IDADE:
        print("Vamos dar entrada na CNH.")
        laudo = input("Você já possui laudo? Digite 1 para sim, 0 para não: ").strip().lower()
        if laudo in ["1", "sim", "s"]: 
            print("Laudo confirmado!")
        else:
            print("Vá até o SAC e compre o laudo")
    elif idade_falta == 1:
        print(f"Infelizmente, você ainda não possui idade para tirar a habilitação. Falta {idade_falta} anos.")
    else:
        print(f"Infelizmente, você ainda não possui idade para tirar a habilitação. Faltam {idade_falta} anos.")

except ValueError:
    print("Por favor, digite um número válido.")