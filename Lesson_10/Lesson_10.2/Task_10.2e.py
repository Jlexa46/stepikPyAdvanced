courses = {'CS101': ['3004', 'Хайнс', '8:00'], 'CS102': ['4501', 'Альварадо', '9:00'], 'CS103': ['6755', 'Рич', '10:00'], 'NT110': ['1244', 'Берк', '11:00'], 'CM241': ['1411', 'Ли', '13:00']}
course = input()
if course in courses:
    print(course + ': ' + courses[course][0] + ', ' + courses[course][1] + ', ' + courses[course][2])
