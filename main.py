from math import gcd


def primeiro_divisor(numero):
    candidato = 2
    while candidato * candidato <= numero:
        if numero % candidato == 0:
            return candidato
        candidato += 1
    return None


def main():
    try:
        n = int(input("Digite o módulo RSA n (por exemplo, 35): "))
    except ValueError:
        print("Digite um número inteiro para o módulo n.")
        return

    if not 2 <= n <= 65536:
        print("O módulo n deve estar entre 2 e 65536.")
        return

    p = primeiro_divisor(n)
    if p is None:
        print(f"{n} é primo. O exercício pede o produto de dois primos distintos.")
        return

    q = n // p
    if p == q or primeiro_divisor(q) is not None:
        print(f"{n} = {p} × {q}. O exercício pede dois fatores primos distintos.")
        return

    print(f"Fatores encontrados: p = {p} e q = {q}.")
    print(f"Conferência: {p} × {q} = {n}.")

    phi = (p - 1) * (q - 1)
    print("\nBônus: calcular o expoente privado d.")
    print(f"φ(n) = ({p} - 1) × ({q} - 1) = {phi}.")

    if phi <= 2:
        print("Para este módulo, não existe um inteiro e entre 1 e φ(n), excluindo os extremos.")
        return

    print("O expoente público e é o segundo número da chave pública (n, e).")
    print(f"Escolha um inteiro de 2 a {phi - 1} que só tenha o divisor 1 em comum com {phi}.")

    while True:
        entrada = input(
            "Qual número você quer usar como expoente público? "
            "(Enter para encerrar): "
        ).strip()

        if not entrada:
            return

        try:
            e = int(entrada)
        except ValueError:
            print("Digite apenas o número que representa e.")
            continue

        if not 1 < e < phi:
            print(f"Escolha um número entre 2 e {phi - 1}.")
            continue

        divisor_comum = gcd(e, phi)
        if divisor_comum != 1:
            print(f"{e} e {phi} são divisíveis por {divisor_comum}. Tente outro número.")
            continue

        break

    for d in range(1, phi):
        if (e * d) % phi == 1:
            print(f"Expoente privado: d = {d}")
            print(f"Chave privada (n, d) = ({n}, {d})")
            print(f"Conferência: ({e} × {d}) % {phi} = 1")
            return


if __name__ == "__main__":
    main()