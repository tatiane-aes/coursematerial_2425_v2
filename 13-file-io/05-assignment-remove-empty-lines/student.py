# with open('input.txt', 'w', encoding='utf-8') as file:
#     file.writelines(['a\n', 'b\n', 'c\n', '\n', 'c\n', '\n', 'c\n'])

def remove_empty_lines(source, destination):
    with open(source, 'r', encoding='utf-8') as file:
        linhas_original = file.readlines()

    with open(destination, 'w+', encoding='utf-8') as file:
        for linha in linhas_original: 
            if len(linha.replace("\n", "")) > 0:
                file.write(linha)

remove_empty_lines('/Users/tatianesanto/Library/CloudStorage/GoogleDrive-riddletati@gmail.com/Meu Drive/University/UCLL/Programming 1/coursematerial_2425_v2/13-file-io/05-assignment-remove-empty-lines/input.txt',
'/Users/tatianesanto/Library/CloudStorage/GoogleDrive-riddletati@gmail.com/Meu Drive/University/UCLL/Programming 1/coursematerial_2425_v2/13-file-io/05-assignment-remove-empty-lines/output.txt')

with open('/Users/tatianesanto/Library/CloudStorage/GoogleDrive-riddletati@gmail.com/Meu Drive/University/UCLL/Programming 1/coursematerial_2425_v2/13-file-io/05-assignment-remove-empty-lines/output.txt',
encoding='utf-8') as file:
    print(file.read())

# foi quase. porque tem uma linha a mais? 