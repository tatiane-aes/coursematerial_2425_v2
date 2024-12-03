def count_lines_in_file(path):
    with open(path, encoding='utf-8') as file:
        return len(file.readlines())

print(count_lines_in_file('/Users/tatianesanto/Library/CloudStorage/GoogleDrive-riddletati@gmail.com/Meu Drive/University/UCLL/Programming 1/coursematerial_2425_v2/13-file-io/03-assignment-count-lines/test.txt'))