import sys

def get_mean_size(ls_output: list) ->float:
    summ_file = 0
    count = 0
    for line in ls_output:
        count += 1 # считаем число строк
        summ_file += int(line.split()[4]) # суммируется значение из 4 столбца
    return summ_file / count

if __name__ == '__main__':
    data: list = sys.stdin.readlines()[1:] # принимаем данные из стандартного потока ввода начиная с 1 строки
    if not data:
        print('данная директория пуста или к ней нет доступа.')
    else:
        mean_size: float = get_mean_size(data) # отправляем данные для обработки в функцию
        print(f':Средний размер файлов в данной директории{mean_size}байт')