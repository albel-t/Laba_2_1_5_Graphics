from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_UNDERLINE
from docx.shared import Inches, Cm, Pt
import glob
import os

def addCode(name, paragraph):
    p = paragraph.add_run(name)
    p.font.name = 'Consolas'
    p.font.size = Pt(12)
    return p

def addTask(task, paragraph):
    p = paragraph.add_run(task)
    p.font.name = 'Times_New_Roman'
    p.font.size = Pt(14)
    return p

def addCodeTitle(code, paragraph):
    p = addTask(code, paragraph)
    p.font.bold = True
    return p

def addTaskTitle(text, paragraph):
    p = addTask(text, paragraph)
    p.font.bold = True
    return p


def addImage(path_to_image, paragraph):
    addTask(path_to_image.join('\\')[-1], paragraph)
    doc.add_picture(path_to_image, width=Inches(4.0))

#visual studio
# path_to_project = input()

path_to_this_document = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_to_template_document = "D:\projects\Templates\шаблон отчета Кафедра САПР.docx"
path_to_imgs = path_to_this_document + '\\img'
name_laba = "laba_1"

doc = Document(path_to_template_document)


style = doc.styles['Normal']
style.font.name = 'Times_New_Roman'
style.font.size = Pt(14)
p = doc.add_paragraph(" ")

addTaskTitle("Цель работы:\n", p)
print("Purpose of the work:")
addTask(input() + "\n", p)

addTaskTitle("Заданиe:\n", p)
print("Exercise:")
addTask(input() + "\n", p)


file_text = open(laba_file, "r", encoding="utf8").read()

addTaskTitle("Решение:\n", p)


# print(file_text, file_text.find("/***") , file_text.find("***/"), file_text[file_text.find("/***") : file_text.find("***/")])
addTask(file_text[file_text.find("/****")+5 : file_text.find("****/")], p) 
print("main file: - ", laba_file)

addCodeTitle("Code: " + name_solution + '.cpp\n', p)
addCode(file_text[file_text.find("****/")+5 : ], p)
print("write: ", name_solution + '.cpp')


laba_file = path_to_project + '/' + name_solution + '/' + name_laba
for filename in glob.glob(laba_file + ".*"):  
    addCodeTitle("\nCode: " + filename[filename.find(name_laba) : ] + '\n', p)
    addCode(open(filename, "r").read(), p)
    print("write: ", filename)

laba_file = path_to_project + '/' + name_solution + '\\'

for filename in glob.glob(laba_file + "*.cpp"):
    print("filename:", filename)
    if (filename not in glob.glob(laba_file + "laba_*.cpp")) and (filename not in glob.glob(laba_file + "ConsoleAlgorithms.cpp")):
        addCodeTitle("\nCode: " + filename[filename.find('\\') : ] + '\n', p)
        addCode(open(filename, "r").read(), p)
        print("_write: ", filename)

for filename in glob.glob(laba_file + "*.h"):
    print("filename:", filename)
    if  filename not in glob.glob(laba_file + "laba_*.h"):
        addCodeTitle("\nCode: " + filename[filename.find('\\') : ] + '\n', p)
        addCode(open(filename, "r").read(), p)
        print("_write:", filename)




for item in os.listdir(path_to_imgs):
    addImage(path_to_imgs, p)

doc.save(path_to_this_document + '/Oтчет_'+name_laba+'.docx') 