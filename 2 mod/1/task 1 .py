import os.path


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(BASE_DIR, 'output_file.txt')

def get_summary_rss(ps_output_file_path: str) ->str:
    with open (ps_output_file_path,'r') as file:
        lines = file.readlines()[1:]  # считываются все строки начиная с 1
    summ_memory = 0                    # здесь хранится объем памяти
    for line in lines:                #  считыываются все строки
        columns = line.split()        # строки переводим в список
        summ_memory += int(columns[5]) #  5ый столбец приводим к int  и суммируем
        # после расчета цикла в кб будем осуществлен перевод в читабельные велечины
        thousand = 1024
        label = 0
        labels = {0: 'кило', 1: 'мега', 2: 'гига', 3: 'тера'}
    while summ_memory > thousand:
        summ_memory /= thousand
        label += 1
    return f'объем используемой памяти {round(summ_memory, 3)} {labels[label]}байт'

if __name__ =='__main__':
    path: str = OUTPUT_FILE
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)


