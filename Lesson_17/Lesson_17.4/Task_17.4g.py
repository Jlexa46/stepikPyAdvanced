def convert_time_to_minutes(__time_24_hour):
    hours, minutes = __time_24_hour.split(':')
    return int(hours) * 60 + int(minutes)


logs = []
with open('logfile.txt', 'rt', encoding='utf-8') as log:
    for line in log:
        logs.append(line.strip().split(','))

with open('output.txt', 'wt', encoding='utf-8') as file:
    for user in filter(lambda x: (convert_time_to_minutes(x[2]) - convert_time_to_minutes(x[1])) >= 60, logs):
        file.write(user[0] + '\n')
