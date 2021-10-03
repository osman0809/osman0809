import os 
moderator = input('Wat is u moderator code: ')
test = open('tweets.txt' , 'r')

zinnen = test.readlines()

test1 = open('goedgekeurd.txt', 'a')
test2 = open('afgekeurd.txt', 'a')



for zin in zinnen:
    print(zin)
    moderator_NS = input('Is deze zin gepast Y/N ')
    if moderator_NS == 'Y':
        test1.write(f'beoordeeld door moderator {moderator} - {zin} \n')
    else:
        test2.write(f'beoordeeld door moderator {moderator} - {zin} \n') 
test.close()
#os.remove('tweets.txt')
test1.close()
test2.close()
