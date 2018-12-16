import logging
import io

def askMyName():
    name = input('please input your name: ')
    return name

def askGuestNames():
    names = list()
    for i in range(5):
        name = input("please give guest #{}'s name: ".format(i))
        names.append(name)
    return names

def returnMoreVars():
    name = 'name'
    age = 'age'
    return namem, age

def main():
    for i in range(1):
        '''
        logging.basicConfig(filename='test.log', level=logging.DEBUG)
        logging.warning("this is warning msg")
        logging.info("this is info msg")
        logging.debug("this is debug msg")
        name = 'Mr {}, my id is {}'.format('yalin',12)
        print('good morning ',name)
        '''
        logFile = open('test.log','r')
        print(logFile.read())
        logFile.close
        
        newFile = open('test_out.log', 'w')
        

        
        print('there are serveral guests coming')
        names = askGuestNames()
        print(" ".join(names))
        i = 1
        for name in names:
            print('guest #{}\'s name is '.format(i), name)
            i=i+1
        newFile.write(" ".join(names))
        newFile.close




main()