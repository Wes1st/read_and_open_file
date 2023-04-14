import os


def get_sorted_file():
    current = os.getcwd()
    folder = 'sorted'
    list_files_in_dir = ['1.txt', '2.txt', '3.txt']
    string_file = []
    for file_name in list_files_in_dir:
        full_path = os.path.join(current, folder, file_name)
        with open(full_path, 'r', encoding='utf-8') as file:
            temp = []
            for line in file:
                temp.append(line.strip())
            temp.insert(0, str(len(temp)))
            temp.insert(0, file_name)
            string_file.append(temp)
    string_file.sort(key=len)

    file_name = 'sorted_file.txt'
    full_path = os.path.join(current, folder, file_name)
    with open(full_path, 'w', encoding='utf-8') as file:
        for string in string_file:
            for line in string:
                file.writelines(line + '\n')


get_sorted_file()
