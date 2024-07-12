try:
    with open('input1.txt','r') as text_file:
        store_dict = dict(eval(text_file.read()))
except FileNotFoundError:
    print("This file does not exist")
#print(store_dict)
new_dict = {}
for element1 in store_dict.values():
    #print(element1)
    for element2 in dict(element1).items():
        if element2[0] not in new_dict:
            new_dict[element2[0]] = element2[1]
        else:
            new_dict[element2[0]] += element2[1]
#print(new_dict)
with open('output1.txt','w') as text_file:
    for element in new_dict.items():
        text_file.write(f'{element[0]}:{element[1]} \n')
    text_file.close()