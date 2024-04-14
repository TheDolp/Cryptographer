# Cryptographer MIPT. Python project 
Описание проекта:  

Программа позволяет зашифровать и дешифровать текстовые файлы, состоящие только из букв русского или английского алфавита.  

Функционал: 

Текст для шифровки/дешифровки программа берет из файла, путь к которому указывает пользователь. Результат также записывается в отдельный файл. 

Шифрование: для каждого из шифров программа может сама подобрать фразу(букву), с помощью которой зашифрует файл, в таком случае будет запрошен путь к файлу для записи этой фразы.

Дешифровка: для каждого из шифров необходимо предоставить файл для дешифровки и файл с кодовой фразой(буквой). Для шифра Цезаря есть возможность автоматической дешифровки с помощью частотного анализа.

Архитектура: 

Данные от пользователя получаются через класс getter. Его методы - "узнай эти данные, проверь корректность, верни их мне":
  get_path() - запрашивает у пользователя путь, пока не получит корректный путь до файла .txt
  get_number(min_elem, max_elem) - число из диапазона 


Взаимодействие ведется через специальный класс communicator. У него есть методы:
  run() - запуск взаимодействия. Будет запускать new_cypher пока пользователь не захочет завершить работу.
  new_cypher() - запуск новой шифровки или дешифровки. Узнает у пользователя с каким шифром он хочет работать. Узнает какой вид взаимодействия выбирает пользователь и запускает соответствующую функцию класса-шифра. 

Разница описанных выше классов в том, что getter - инструмент, который communicator использует, решая, какие данные и в каком порядке запрашивать, а getter включается на момент получения определенных данных.

Отдельно будут созданы классы алфавиты. Классы предположительно будут лежать в отдельном файле data. Методы:
  is_in_alph(char)->bool - принадлежит ли символ алфавиту.
  move_symb(char, int)->char - сдвиг на некоторое число
  get_nubmer(char)->int - номер буквы
  get_lower_char(int)->char - прописная буква по номеру
  get_upper_char(int)->char - заглавная буква по номеру
  who_is_who(list)->map - по парам "буква-встречаемость", зная, что это шифр цезаря, предполагает какая буква была изначально для каждой буквы
  Возможны дополнения

Для каждого шифра будет создан класс, взаимодействующий класс будет использовать методы классов-шифров. Класс сможет зашифровать, расшифровать и сгенерировать ключ для шифрования. Основные функции классов будут получать строку и ключ(да, тоже строка) и возвращать зашифрованный или расшифрованный вариант.
В общем виде для класса-шифра методы выглядят так:
  code(path_in, path_out, path_code = none) - вызываемая функция шифрования
  decode(path_in, path_out, path_code) - вызываемая функция дешифровки
  code_str(str_in, str_code) - шифрование 
  decode_str(str_in, str_code) - дешифровка
Для шифра Цезаря существует отдальная функция для автоматической дешифровки
  auto_decode(path_in, path_out)
