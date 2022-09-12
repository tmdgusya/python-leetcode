import os

def auto_execute_test():
    file_name = input('file name : ')

    print('execute test : ', file_name)

    os.system('python3 -m unittest -v ' + file_name)


if __name__ == '__main__':
    auto_execute_test()

