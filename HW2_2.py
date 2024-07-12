try:
    with open('input.txt','r',encoding='utf-8') as file, open ('output2.txt','w', encoding='utf-8') as dest:
        symbols = input ('Введите символы для удаления')
        lines = file.readlines()
        print(lines)
        for line in lines:
            line = line.strip()
            line = line.rstrip(symbols)
            line += ';'
            line = line[::-1]
            dest.write(line)
except FileNotFoundError:
    print("This file does not exist")