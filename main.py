with open('example.txt', 'w') as file:
    file.write('Hello world.\n')
    file.write('!!!\n')

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

#exercise 6
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
