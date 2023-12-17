# Otwarcie pliku tekstowego w trybie odczytu ('r' - read)
with open('kalimba.txt', encoding = 'utf-8') as file:
    zawartosc = file.read()
    print(zawartosc)

    zawartosc = zawartosc.replace('1', 'C')
    zawartosc = zawartosc.replace('2', 'D')
    zawartosc = zawartosc.replace('3', 'E')
    zawartosc = zawartosc.replace('4', 'F')
    zawartosc = zawartosc.replace('5', 'G')
    zawartosc = zawartosc.replace('6', 'A')
    zawartosc = zawartosc.replace('7', 'B')
    zawartosc = zawartosc.replace('xD', 'x2')
    zawartosc = zawartosc.replace('’','*')
    zawartosc = zawartosc.replace('*','°')
    print(zawartosc)

with open('kalimba2.txt', 'w', encoding='utf-8') as file:
    file.write(zawartosc)

#test github