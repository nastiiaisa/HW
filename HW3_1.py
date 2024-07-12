try:
    with open('cities.txt','r') as text_file:
        text = text_file.read()
except FileNotFoundError:
    print("This file does not exist")
#print(text)
text = text.split('\n')
population = int(input("Enter amount of population "))
new_list = []

for lines in text:
    name = lines[:lines.index(':')]
    number = lines[lines.index(':')+1:]
    #print(name)
    #print(number)
    if int(number) > population:
        new_list.append(lines)
#print (new_list)
print(sorted(new_list))
#print(sorted(new_list))
with open('filtered_cities.txt','w') as text_file:
    for element in sorted(new_list):
        text_file.write(element + '\n')
    text_file.close()
