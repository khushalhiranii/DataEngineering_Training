text_input = input()

with open('sample.txt', 'a+') as f:
    f.write(text_input)
    f.seek(0)
    print(f.readline())