#kalkulator
print("KALKULATOR")

def dodawanie(x, y):
    return x + y
def odejmowanie(x, y):
    return x - y
def mnozenie(x, y):
    return x * y
def dzielenie(x, y):
    return x / y
def potegowanie(x, y):
    return x ** y

wyjscie = False
while wyjscie == False:

    print("::Menu::")
    print("1 - dodawanie")
    print("2 - odejmowanie")
    print("3 - mnozenie")
    print("4 - dzielenie")
    print("5 - potegowanie")
    print("6 - wyjscie")

    choice = input("Wybierz (1/2/3/4/5/6):")

    if choice == '6':
        pytanie = input("Wyjść z programu? (Tak/Nie): ")
        if pytanie == 'Tak':
            wyjscie = True
            print('Koniec programu!')
            exit()
        elif pytanie == 'Nie':
            wyjscie = False
            print('Powrót do programu')
            choice = input("Wybierz (1/2/3/4/5/6):")

    x = float(input("Podaj pierwszą liczbę: "))
    y = float(input("Podaj drugą liczbę: "))

    if choice == '1':
        print("Suma wynosi: "x, "+", y, "=", dodawanie(x, y))

    elif choice == '2':
        print("Różnica wynosi: "x, "-", y, "=", odejmowanie(x, y))

    elif choice == '3':
        print("Iloczyn wynosi: "x, "*", y, "=", mnozenie(x, y))

    elif choice == '4':
        print("Iloraz wynosi: "x, "/", y, "=", dzielenie(x, y))

    elif choice == '5':
        print("Wynik potęgowania: "x, "**", y, "=", potegowanie(x, y))

    else:
        print("Kalkulator nie obejmuje takiej operacji")
