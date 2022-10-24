import time
import pyrqlite.dbapi2 as dbapi2

with open('chinook.sql', 'r',  encoding="utf-8") as fp:
    chinookFile = fp.read()

chinookFile = chinookFile.replace('?','')
chinookFile = chinookFile.replace(':',' ')
chinookFile = chinookFile.replace('; ','')

commands = chinookFile.split(';\n')

commands.remove(commands[1])
cc = ';'.join(commands[:-2])
cc = cc.replace('\n','')

with open('commands.txt', 'w', encoding="utf-8") as fp:
    fp.write(cc)
# connection = dbapi2.connect(
#     host= '127.0.0.1',
#     port=4001,
# )

# start = time.time()
# with connection.cursor() as cursor:
#     for command in commands[:-2]:
#         cursor.execute(command)
# end = time.time() - start
# print('Time taken:',end, 'seconds')
    
    