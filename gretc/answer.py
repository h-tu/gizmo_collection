import os
import numpy as np

# get_answer(34,10)

def get_answer(sec, question):
    text = 'section {} question {} -- [ '.format(sec, question) + answer[sec-1][question-1] + ' ]'
    return text

answer = []

if not os.path.exists("key.npy"):
    print('Creating key.npy...')
    f = open("TCkey.txt", "r", encoding="utf8")
    raw = f.read()

    lst = raw.split('\n')

    while("" in lst) : 
        lst.remove("") 

    for idx,ele in enumerate(lst):
        if "参考答案" in ele:
            line = lst[idx+1].split(' ')[1] + '/' + lst[idx+2].split(' ')[1]
            answer.append(line.split('/'))

    f.close()
    
    answer = np.array(answer)
    np.save('key.npy', answer)
else:
    print('Loading key.npy...')
    answer = np.load('key.npy')

a, b = input("Enter section and number: ").split() 
section = int(a)
question = int(b)


while True:
    print(get_answer(section, question))
    if question  == 10:
        section += 1
        question = 0
    tmp = input()
    if len(tmp):
        print('Bye')
        break
    else:
        question += 1