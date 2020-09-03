# 2019/09/16
# Hongyu Tu
import subprocess
import PyPDF2

def main():
    print(' --- Program starts --- ')
    opt = int(input('Enter your choice: \n\t1. Process all pdf file in this directory\n\t2. Process one specific file\n'))

    if opt == 1: # multiple files
        raw = subprocess.check_output(['ls'])
        item = raw.split(b'\n')
        que = []
        # for tmp in item:
        #     print(tmp.decode('utf-8'))
        for tmp in item:
            # print('pdf is in {}: {}'.format(tmp,not b'.pdf' not in tmp))
            if b'.pdf' in tmp:
                que.append(tmp.decode('utf-8'))
        print('{} pdf files found in current directory: '.format(len(que)))
        for tmp in que:
            print(tmp)
        confirm = int(input('---\nContinue to process all of them?\n0 - No\n1 - yes\n'))
        if confirm:
            complete = 0
            for tmp in que:
                print('\n')
                print('Processing: {}'.format(tmp))
                test = process(tmp[0:len(tmp)-4])
                complete = complete + test
            print('\n{} out of {} files reversed!'.format(complete, len(que)))
        elif confirm == 0:
            print('Bye!')
            quit()
        else:
            print('No such option!')
            quit()

    elif opt == 2: # one single file
        name = str(input('Name of the PDF you want to reverse: \n'))
        i = process(name)
        if i:
            print('Done!')
    else:
        print('No such option!')


def process(name):
    try:
        pdfFileObj = open((name + '.pdf'), 'rb')
    except IOError:
        print('Could not read file: {}'.format(name + '.pdf'))
        print('bye')
        return 0
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfWriter = PyPDF2.PdfFileWriter()
    print('total page: {}'.format(pdfReader.numPages))
    p = pdfReader.numPages - 1
    curr = 1
    while p >= 0:
        pdfWriter.addPage(pdfReader.getPage(p))
        print('page {} set to page {}'.format(p+1, curr))
        p = p - 1
        curr = curr + 1
    print('Writing {} pages to {}'.format(pdfReader.numPages,(str(name) + '-rev.pdf')))
    newFile = open((name + '-rev.pdf'), 'wb')
    pdfWriter.write(newFile)
    pdfFileObj.close()
    newFile.close()
    return 1

main()
