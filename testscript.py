import os

def auto_execute_test():
    file_name = input('solutionNumber : ')
    print('execute test : ', file_name)
    os.system('python3 -m unittest -v solution' + file_name + '.Solution.doTest')


if __name__ == '__main__':
    auto_execute_test()

