# Реализация приложения «Граббер».

import pathlib
import re
from chardet.universaldetector import UniversalDetector

def encoding(fb):
  detector = UniversalDetector()
  for line in fb:
    detector.feed(line)
    if detector.done:
      break
    detector.close()
  return detector.result['encoding']

fileDir = r"F:\\"
fileExt = input("Введите расширение файлов: ")
word = input("Введите слово для поиска: ")
pattern = r"'\b{}\b'".format(re.escape(word))
filePath = list(pathlib.Path(fileDir).glob('**\*.{}'.format(fileExt)))   #Список путей к файлам

for path in filePath:
    code = encoding(path.read_bytes().splitlines())   #Определение кодировки файла
    file_contents = path.read_text(encoding=code).splitlines()   #Считывание файла
    for line in file_contents:
        if re.search(pattern, line):   #Поиск слова в строке файла
            print(pathlib.Path(path).name)