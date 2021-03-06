# Файловый ввод и вывод
# Программы, которые мы писали до сих пор, требовали повторного ввода данных при каждом запуске, потому что, как только
# программа заканчивает свою работу, данные для переменных исчезают из оперативной памяти. Если их нужно сберечь между
# выполнениями программы, требуется запись. Данные записываются в файл, обычно сохраняющийся на диске компьютера.

# Файл (англ. file) — именованная область данных на носителе информации.

# Сохраненные в файле данные обычно остаются в нем после завершения работы программы, их можно позже извлечь и
# использовать.

# Когда программе нужно сохранить данные для дальнейшего использования, она пишет их в файл. Из файла записанные данные
# можно считать.

# Программисты называют такой процесс сохранения данных — запись данных в файл. Когда часть данных пишется в файл, она
# копируется из переменной, находящейся в оперативной памяти. Файл, куда сохраняются данные, называется файл вывода,
# потому что программа помещает в него выходные данные.

# Процесс извлечения данных из файла называется чтением данных из файла. Данные считываются из файла ввода. Программа
# извлекает входные данные из этого файла. Когда порция данных считывается из файла, она копируется в оперативную
# память, где на нее ссылается переменная.


# Работа с файлами
# Когда в программе используется файл, как правило требуется выполнить три шага:
#     1. Открыть файл. В процессе открытия файла создается связь между файлом и программой. Открытие файла вывода обычно
#       создает файл на диске и позволяет программе записать в него данные. Открытие файла ввода позволяет программе
#       прочитать данные из файла.
#     2. Обработать файл. На этом шаге данные либо записываются в файл (если это файл вывода), либо считываются из файла
#       (если это файл ввода).
#     3. Закрыть файл. После использования файла программой его нужно закрыть, тем самым освободить ресурс и разорвать
#       связь файла с программой.


# Типы файлов
# Существует два типа файлов: текстовые и двоичные (бинарные). Текстовый файл содержит данные, которые были закодированы
# в виде текста при помощи такой схемы кодирования, как ASCII или Юникод. Даже если файл содержит числа, эти числа в
# файле хранятся как набор символов. В результате файл можно открыть и просмотреть в текстовом редакторе, таком как
# Блокнот.

# Двоичный файл содержит данные, которые не были преобразованы в текст. Данные, которые помещены в двоичный файл,
# предназначены только для чтения программой, и такой файл невозможно просмотреть в текстовом редакторе.

# Python позволяет работать и с текстовыми, и с двоичными файлами, но в рамках этого курса мы будем работать с
# текстовыми файлами, чтобы вы могли использовать текстовый редактор для исследования файлов, создаваемых вашими
# программами.

# Разделение файлов на текстовые и бинарные искусственное, так как любой текстовый файл бинарен.


# Методы доступа к файлам
# Большинство языков программирования обеспечивает два способа получения доступа к данным в файле:
#     последовательный,
#     прямой или произвольный.

# Последовательный, как при проигрывании кассет с записью на пленке, выдает порции информации одну за другой. При работе
# с таким файлом не получится перескочить сразу к нужной части данных, сначала придется прочитать все предыдущие.
# При работе с файлом с прямым или произвольным доступом можно перескочить непосредственно к любой порции данных, не
# читая предыдущие. Как проигрыватель компакт-дисков или МР3-плеер перескакивает сразу к любой песне.


# Имена файлов
# Большинство пользователей компьютеров привыкли, что файлы определяются по имени. Когда создаете документ с помощью
# текстового редактора и сохраняете его в файле, указываете имя файла. Если исследуете содержимое диска с помощью
# проводника Windows, видите список имен файлов.

# У каждой операционной системы собственные правила именования файлов. Многие системы поддерживают использование
# расширений файлов, т.е. коротких последовательностей символов, которые расположены в конце имени файла и предваряются
# точкой. Расширение обычно говорит о типе данных в файле. Например, расширение jpg сообщает, что файл содержит
# графическое изображение, сжатое согласно стандарту JPEG. Расширение txt свидетельствует, что в файле текст. Расширение
# docx информирует о наличии в файле документа Microsoft Word.

# Кодировка файлов
# В прошлом курсе мы говорили о том, как строки текста хранятся в памяти компьютера, таблицах символов ASCII и Юникод,
# а также о кодировке UTF-8.

# Кодировка UTF-8 самая распространенная, рекомендуем использовать именно ее в качестве кодировки по умолчанию для
# текстовых файлов.

# UTF-8 — сложная кодировка, на обозначение одного символа в ней может использоваться от одного до шести байт.
# Подробнее про эту кодировку можно почитать в википедии.

# В операционной системе Windows до сих пор используется однобайтовая кодировка Windows-1251. Чтобы избежать проблем при
# работе с текстовыми файлами в Windows нужно явно указывать кодировку. В редакторе Notepad («Блокнот») можно указывать
# кодировку при сохранении файла.

# При работе с ОС Linux и MacOS таких проблем не возникает вовсе, поскольку в них кодировка UTF-8 применяется
# по умолчанию.


# Относительные и абсолютные пути
# Путь файла (или путь к файлу) — последовательное указание имен папок, через которые надо пройти, чтобы добраться до
# объекта.
# Пути к файлу бывают двух типов:
#     абсолютные;
#     относительные.

# Абсолютный путь – полный путь к файлу, показывающий точное место его расположения. Он всегда один и тот же, пока файл
# не перемещен.
# Примеры абсолютного пути:
#     D:\Data\MyFiles\picture.png;
#     С:\MyPrograms\Python\script.py;
#     C:\Users\timur\YandexDisk\BeeGeek\Python\book.pdf.

# Указывая абсолютный путь на компьютере, обязательно нужно указывать диск, а также использовать \ (для Windows) в
# качестве разделителя имен папок.
# В unix-подобных ОС, например, в Linux и Mac OS для отделения имен папок используется прямой слеш /, а не обратный,
# как в Windows.

# Относительный путь – привязан к какой-либо "отправной точке" и указан по отношению к ней.
# Например, у нас есть картинка picture.png, которая хранится на диске D. Абсолютный путь к ней будет
# D:\Data\MyFiles\picture.png, а относительно папки Data можно указывать MyFiles\picture.png.

# Абсолютный путь показывает точное местонахождение файла, а относительный показывает путь к файлу от какой-либо
# "отправной точки".


# Примечания
# Примечание 1. Конкретная физическая организация файлов, их группировка по папкам, устройство процедур доступа к
# информации, механизмы кеширования очень сильно зависят от операционной системы и применяемой в ней файловой системы.
# Как правило, при работе с файлами прикладные программисты работают на верхнем уровне абстракции.

# Примечание 2. Файлы обычно располагаются на носителях, работающих медленнее, чем оперативная память. Поэтому работа с
# ними идет в буферизированном режиме. Даже если вы запросите один байт из файла, считается целый блок (до нескольких
# килобайт). Он переместится в буфер оперативной памяти. Дальше файл читается оттуда, поскольку это быстрее и экономит
# ресурсы чтения/записи внешних носителей.

# Примечание 3. Примеры однобайтовых кодировок:
# Windows-1251;     # https://ru.wikipedia.org/wiki/Windows-1251
# cp-866;           # https://ru.wikipedia.org/wiki/CP866
# КОИ-8.            # https://ru.wikipedia.org/wiki/%D0%9A%D0%9E%D0%98-8

# Примечание 4. Прочитать про относительные и абсолютные пути можно тут и тут.
# http://phpfaq.ru/newbie/paths
# https://ru.wikipedia.org/wiki/%D0%9F%D1%83%D1%82%D1%8C_%D0%BA_%D1%84%D0%B0%D0%B9%D0%BB%D1%83
