import os
import re
from tqdm import tqdm

pattern = r"[A-Za-z]+(?:[-_][A-Za-z]+)*|\d+(?:[-_]\d+)*"
ignore_extension = ['py', 'ipynb']

def fix_name(i):
    tmp = i.split('.')
    end = '.' + tmp[-1]
    new_name = ''.join(tmp[:-1])

    if '@' in new_name:
        new_name = new_name.split('@')[1]

    if ' ' in new_name:
        new_name = new_name.split()[0]

    # tmp = new_name.split('-')
    # if len(tmp) > 2:
    #     new_name = tmp[0] + tmp[1]

    matches = re.findall(pattern, new_name)
    new_name = '-'.join(matches).upper() + end

    return new_name

def main():
    change_lst = []
    
    for i in os.listdir():
        if i[0] == '.':
            os.system('rm ' + i)
        else:
            if 'py' not in i and 'ipynb' not in i:
                new_name = fix_name(i)
        
                if new_name != i:
                    print(i + '\t' + new_name)
                    change_lst.append((i, new_name))
    
    if len(change_lst) > 0:
        print('\nFix?')
        if input() == 'y':
            print('Fixing')
            for _ in tqdm(change_lst):
                i, new_name = _
                os.system('mv \'' + i + '\' \'' + new_name + '\'')
            
            print('Done')
    else:
        print('No need to fix')


if __name__=="__main__":
    main()