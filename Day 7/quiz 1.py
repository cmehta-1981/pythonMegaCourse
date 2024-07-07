#What will be the content of logs.txt this time?

file = open('log.txt', 'w')
file.write('101.102.103.222 GET 01.988')
file.close()

file = open('log.txt', 'w')
file.write('171.131.104.108 POST 2.143')
file.close()