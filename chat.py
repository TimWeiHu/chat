#讀取檔案
def read(input_file):
    data = []
    with open(input_file, 'r', encoding='utf-8-sig') as f:
        for line in f:
            data.append(line.strip())
    return data

# 以人名進行檢索，並將人名下的訊息加上發送者（name:）
def convert(names, data):
    chat_line = []
    speaker = None
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

#定義 main funtion
def main():
    data = read('input.txt')
    names = ['Allen', 'Tom']    #宣告此對話的參與者
    chat = convert(names, data)
    save('output.txt',chat)

    for line in chat:
        print(line)
    print('')

main()
