import sys
import tkinter
import Bio
from tkinter import*
from tkinter import messagebox as mb
import requests
from Bio.SubsMat import MatrixInfo as matlist
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
import tkinter.scrolledtext as st

form = ''
BLOSUM62 = matlist.blosum62
PAM250 = matlist.pam250

doseq1 = 'MSLWQPLVLVLLVLGCCFAAPRQRQSTLVLFPGDLRTNLTDRQLAEEYLYRYGYTRVAEMRGESKSLGPALLLLQKQLSLPETGELDSATLKAMRTPRCGVPDLGRFQTFEGDLKWHHHNITYWIQNYSEDLPRAVIDDAFARAFALWSAVTPLTFTRVYSRDADIVIQFGVAEHGDGYPFDGKDGLLAHAFPPGPGIQGDAHFDDDELWSLGKGVVVPTRFGNADGAACHFPFIFEGRSYSACTTDGRSDGLPWCSTTANYDTDDRFGFCPSERLYTRDGNADGKPCQFPFIFQGQSYSACTTDGRSDGYRWCATTANYDRDKLFGFCPTRADSTVMGGNSAGELCVFPFTFLGKEYSTCTSEGRGDGRLWCATTSNFDSDKKWGFCPDQGYSLFLVAAHEFGHALGLDHSSVPEALMYPMYRFTEGPPLHKDDVNGIRHLYGPRPEPEPRPPTTTTPQPTAPPTVCPTGPPTVHPSERPTAGPTGPPSAGPTGPPTAGPSTATTVPLSPVDDACNVNIFDAIAEIGNQLYLFKDGKYWRFSEGRGSRPQGPFLIADKWPALPRKLDSVFEEPLSKKLFFFSGRQVWVYTGASVLGPRRLDKLGLGADVAQVTGALRSGRGKMLLFSGRRLWRFDVKAQMVDPRSASEVDRMFPGVPLDTHDVFQYREKAYFCQDRFYWRVSSRSELNQVDQVGYVTYDILQCPED'

doseq2 = 'MSPRQPLVLALLVLGCCSAAPRRRQPTLVVFPGELRTRLTDRQLAEEYLFRYGYTRVASMHGDSQSLRLPLLLLQKHLSLPETGELDNATLEAMRAPRCGVPDVGKFQTFEGDLKWHHHNITYWIQNYSEDLPRDVIDDAFARAFALWSAVTPLTFTRVYSRDADIVIQFGVAEHGDGYPFDGKDGLLAHAFPPGPGIQGDAHFDDEELWSLGKGVVVPTYFGNADGAPCHFPFTFEGRSYTACTTDGRSDGMAWCSTTADYDTDRRFGFCPSERLYTQDGNADGKPCEFPFIFQGRTYSACTTDGRSDGHRWCATTASYDKDKLYGFCPTRADSTVVGGNSAGELCVFPFVFLGKEYSSCTSEGRRDGRLWCATTSNFDSDKKWGFCPDKGYSLFLVAAHEFGHALGLDHSSVPERLMYPMYRYLEGSPLHEDDVRGIQHLYGPNPNPQPPATTTPEPQPTAPPTACPTWPATVRPSEHPTTSPTGAPSAGPTGPPTASPSAAPTASLDPAEDVCNVNVFDAIAEIGNKLHVFKDGRYWRFSEGSGRRPQGPFLIADTWPALPAKLDSAFEEPLTKKLFFFSGRQVWVYTGASVLGPRRLDKLGLGPEVPHVTGALPRAGGKVLLFGAQRFWRFDVKTQTVDSRSGAPVDQMFPGVPLNTHDVFQYREKAYFCQDRFFWRVSTRNEVNLVDQVGYVSFDILHCPED'

input_seq1 = ''
input_seq2 = ''


def jopa():
    if var.get() == '0':
        x = "needle_"
    elif var.get() == '1':
        x = "water_"
    return x


def jop():
    if var1.get() == '0':
        z = "blosum"

    elif var1.get() == '1':
        z = "pam"
    return z


def matrica():
    f = jopa() + jop()
    return f


def result(seq1, seq2, choise):
    global form
    if choise == 'needle_blosum':
        alignments = pairwise2.align.globalds(seq1, seq2, BLOSUM62, -10, -0.5)

        for alignment in alignments:

            form = (format_alignment(*alignment))
        return form
    elif choise == 'water_blosum':
        alignments = pairwise2.align.localds(seq1, seq2, BLOSUM62, -10, -0.5)

        for alignment in alignments:

            form = (format_alignment(*alignment))
        return form
    elif choise == 'needle_pam':
        alignments = pairwise2.align.globalds(seq1, seq2, PAM250, -10, -0.5)

        for alignment in alignments:

            form = (format_alignment(*alignment))
        return form
    elif choise == 'water_pam':
        alignments = pairwise2.align.localds(seq1, seq2, PAM250, -10, -0.5)

        for alignment in alignments:

            form = (format_alignment(*alignment))
        return form



def numbers(lens):
    n = 0
    nums = ''

    while len(nums) < len(lens) / 3:
        nums += str(n) + ' ' * 49
        n += 50

    return nums

def print_options(seq1,seq2):
    gaps = form.count('-')
    coincidence = form.count('|')
    total = max(len(seq1), len(seq2))
    similarity = coincidence + form.count(':')

    return f'''
            Программа использует стандартные настройки:           
                #    -datafile {matrica()}
                #    -gapopen 10.0
                #    -gapextend 0.5
                #    -endopen 10.0 
                #    -endextend 0.5
                
             Дополнительная информация:
             Длинна последовательностей - {total}
             Количество пробелов(gaps) -  {gaps}/{total} - {gaps/total*100}%
             Идентичность - {coincidence}/{total} - {coincidence/total*100}%
             Сходство - {similarity}/{total} - {similarity/total*100}%
             '''




def second_win(input1, input2):
    root = tkinter.Toplevel(win)
    root.resizable(width=False, height=False)
    root.iconbitmap('ico.ico')
    root.title('VishnyaProject result')
    root.geometry('760x400')
    scrollbar = Scrollbar(root,
                          orient=HORIZONTAL)
    scrollbar.pack(side="bottom", fill="x")
    Label(root, text='Результаты выравнивания', bg='green', fg='white', font=('Times New Roman', 18)).pack()
    Label(root, text='Если вы видете это, значит вы не применили настройки выравнивания', fg='#006A55', font=('Times New Roman', 10)).place(relx=.22, rely=.35)

    text = Text(root,
                state=NORMAL,
                wrap="none",
                xscrollcommand = scrollbar.set,
                width=730,
                height=380
                )


    text.insert('end',
                numbers(result(input1, input2, matrica())) + '\n' + result(input1, input2, matrica() ) + '\n' + str(print_options(input1, input2)))
    text.config(state=DISABLED)
    text.pack()
    scrollbar.config(command=text.xview)


    Label(root,
          text=print_options(input1, input2),
          anchor=W
          ).pack()

    root.mainloop()


def get1_entry():
    f = second_win(doseq1,doseq2)
    return f


def get_entry():
    value1 = text1.get()
    value2 = text2.get()

    if value1 and value2:
        input_seq1 = value1
        input_seq2 = value2
        text1.delete(0, 'end')
        text2.delete(0, 'end')
        second_win(input_seq1, input_seq2)

    else:
        msg = 'Введите последовательности в поля или воспользуйтесь готовым выравниванием (Ввод осуществляется только заглавными латинскими буквами)'
        mb.showwarning('внимание', msg)




def click_menu():
    about = '''
               Лабораторная работа №5
               Парное выравнивание нуклеиновых
               последовательностей
               Выполнил студент группы БиБ-201 
               Вишняков Сергей
                '''
    show = mb.showinfo('Справка', about)
    return show

win = Tk()
win.resizable(width=False, height=False)
win.iconbitmap('ico.ico')
win.title('VishnyaProject v2.0                  Выравнивание последовательностей по алгаритму Вунша и Ватермана')
win.geometry('800x420')
menu = Menu(win)
win.config(menu=menu)
menu.add_cascade(label='Справка', command=click_menu)


info1 = Label(win,
              text='тип выравнивания',
              font=14, bg='#34D1B2').place(relx=.07, rely=.085)
info2 = Label(win,
              text='матрица',
              font=14, bg='#34D1B2').place(relx=.34, rely=.085)
lb1 = Label(win,
            text=' Парное выравнивание последовательности белка MMP-9 человека и кролика',
            font='Arial 16',
            bg='#F93E58')
lb1.pack()


space = Label(win, text='___________________________________________________________________________________________'*2)
space.place(relx=0, rely=.33)
lb2 = Label(win,
            text='Выравнивание других последовательностей',
            font='Arial 18',
            bg='#F93E58')

lb2.place(rely=0.4,
          relx=.17)

Label(win, text='ПЕРВАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ',fg='#1F7A68', font="Roboto-BlackItalic 11").place(relx=.08, rely=.54)
text1 = Entry(win,
              textvariable=input_seq1,
              width=70,
              font=20)

text1.place(relx=0.08,
            rely=0.6)

Label(win, fg='#1F7A68', text='ВТОРАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ', font="Roboto-BlackItalic 11").place(relx=.08, rely=.66)
text2 = Entry(win,
              textvariable=input_seq2,
              width=70,
              font=20
              )

text2.place(relx=0.08,
            rely=0.72,
            height= 25,

            )

btn = Button(text='выполнить выравнивание',
             background="#739D00",
             foreground="#ccc",
             font=11,
             padx="20",
             pady="8",
             command=get1_entry)

btn.place(relx=.74,
          rely=.28,
          anchor="c",
          height=30,
          width=250,
          bordermode=OUTSIDE)

btn1 = Button(text='выполнить выравнивание',
              background="#739D00",
              foreground="#ccc",
              font=11,
              padx="20",
              pady="8",
              command=get_entry)

btn1.place(relx=.59,
           rely=.93,
           anchor="sw",
           height=30,
           width=250,
           bordermode=OUTSIDE)

var1 = StringVar()
var1.set(2)
var = StringVar()
var.set(2)
a1 = Radiobutton(win, font=10, fg='#1F7A68', text = 'глобальное', variable = var, value='0', command=jopa ).place(relx=.075, rely=.16)
a2 = Radiobutton(win, font=10, fg='#1F7A68', text = 'локальное', variable = var, value='1', command=jopa ).place(relx=.075, rely=.24)

b1 = Radiobutton(win, font=10, fg='#1F7A68', text = 'BLOSUM62', variable = var1, value='0', command=jop ).place(relx=.34, rely=.16)
b2 = Radiobutton(win, font=10, fg='#1F7A68', text = 'PAM250', variable = var1, value='1', command=jop ).place(relx=.34, rely=.24)

Label(win, text='перед применением установите настройки').place(relx=.584, rely=.19)
Label(win, text='перед применением установите настройки').place(relx=.59, rely=.8)


cum = Label(win, text='made by Sergey Vishnyakov')
cum.place(relx=.77, rely=.95)

bigass = Label(win, text='laboratory work №5 for Krylov P.A')
bigass.place(relx=.05, rely=.95)

win.mainloop()