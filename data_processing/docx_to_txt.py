import os
import glob
import docx


def getText(docx_path):
    doc = docx.Document(docx_path)
    fullText = []
    for par in doc.paragraphs:
        fullText.append(par.text)
    return '\n'.join(fullText)


if __name__ == '__main__':
    file_list = glob.glob('../data/raw_data/books/docx/*')
    txt_location = '../data/raw_data/books/txt/'

    for file_path in file_list:
        if not 'PROCESSED' in file_path:
            file_name = file_path.split('/')[-1][:-5]
            with open(txt_location + file_name + '.txt', 'w') as output_file:
                text = getText(file_path)
                output_file.write(text)
                os.rename(file_path, file_path[:-5] + '_PROCESSED.docx')
