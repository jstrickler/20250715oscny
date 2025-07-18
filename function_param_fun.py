def read_files1(search_term, file_path):
    with open(file_path) as file_in:
        for line in file_in:
            if search_term in line:
                print(line.rstrip())

read_files1('Dormouse', 'DATA/alice.txt')
read_files1(file_path='DATA/mary.txt', search_term='lamb')
print('-' * 60)

def read_files2(search_term, *file_paths):
    for file_path in file_paths:
        with open(file_path) as file_in:
            for line in file_in:
                if search_term in line:
                    print(line.rstrip())

read_files2('wombat', 'DATA/words.txt')
read_files2('pepper', 'DATA/alice.txt', 'DATA/words.txt')
read_files2('lizard', 'DATA/alice.txt', 'DATA/words.txt')

def read_files3(search_term, *file_paths, show_file_name=False):
    for file_path in file_paths:
        with open(file_path) as file_in:
            for line in file_in:
                if search_term in line:
                    if show_file_name:
                        print(file_path, end=" ")
                    print(line.rstrip())

read_files3('wombat', 'DATA/words.txt')
read_files3('pepper', 'DATA/alice.txt', 'DATA/words.txt', show_file_name=True)
read_files3('lizard', 'DATA/alice.txt', 'DATA/words.txt')