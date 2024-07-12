# with open ("input.txt",'r') as file:
#     a = file.readlines()
#     print(a)
try:
    with open ("input.txt",'r') as file:
        grades = {}
        for line in file:
            line_list = line.strip().split(',')
            # grades['Anton'] = 83
            grades[line_list[0]] = int(line_list[1])

        mean = sum(grades.values()) / len(grades)
        print(mean)
except FileNotFoundError:
    print("This file does not exist")
with open ('output.txt','w') as file:
    # В переменную Х будут записываться ключи словаря:
    for name in grades:
        # print(grades[name])
        # grades['Anton'] == 83
        if grades[name] > mean:
            print (name, file=file)


