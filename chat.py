#讀取檔案
def read(input_file):
    data = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(line.strip())
    return data

# 以人名進行檢索，並將人名下的訊息加上發送者（name:）
def speak(names, data):
    chat_line = []
    speaker = ''
    for line in data:
        for name in names:
            if name == line:
                speaker = name
                break
        if speaker != line:
            chat_line.append(speaker + '：' + line)
    return chat_line

# 將結果存成TXT檔
def save(output_file, chat):
    with open(output_file, 'w', encoding='utf-8') as f:
        for c in chat:
            f.write(c + '\n')


data = read('input.txt')

# 去除 ufeff
data[0] = data[0].encode('utf-8').decode('utf-8-sig')

names = ['Allen', 'Tom']

chat = speak(names, data)

save('output.txt',chat)


for line in data:
    print(line)
print('')
# print(data)

print(chat)