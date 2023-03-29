from tkinter import *

global test_page
test_page = False
while True:
    if test_page == False:
        test_page = True
        class Choice(Frame):
            def __init__(self, root):
                super(Choice, self).__init__(root)
                self.build()

            def build(self):
                self.formula = "0"
                self.lbl = Label(text=self.formula, font=("Times New Roman", 18, "bold"), bg="#000", foreground="#FFF")
                self.lbl.place(x=11, y=60)
                self.lbl2 = Label(text="Введите систему счисления", font=("Times New Roman", 18, "bold"), bg="#000",
                                  foreground="#FFF")
                self.lbl2.place(x=11, y=20)

                global btns

                btns = [
                    "1", "2", "3",
                    "4", "5", "6",
                    "7", "8", "9",
                    "C", "0", "→",
                ]

                x = 10
                y = 140
                for bt in btns:
                    com = lambda x=bt: self.logicalc(x)
                    Button(text=bt, bg="#000", foreground="#FFF",
                           font=("Times New Roman", 15, "bold"),
                           command=com).place(x=x, y=y,
                                              width=115,
                                              height=79)
                    x += 117
                    if x > 300:
                        x = 10
                        y += 81

            def logicalc(self, operation):
                if operation == "C":
                    self.formula = "0"
                    self.update()
                elif operation == "→":
                    if int(self.formula) < 36 and int(self.formula) > 1:
                        global nums
                        nums = int(self.formula)
                        root.destroy()
                    else:
                        self.formula = "Ошибка"
                        self.update()
                else:
                    if self.formula == "0" or self.formula == "Ошибка":
                        self.formula = ""
                    self.formula += operation
                    self.update()

            def update(self):
                if self.formula == "":
                    self.formula = "0"
                self.lbl.configure(text=self.formula)


        if __name__ == '__main__':
            root = Tk()
            root["bg"] = "#000"
            root.geometry("368x480+200+200")
            root.title("калькУлятор")
            root.resizable(False, False)
            app = Choice(root)
            app.pack()
            root.mainloop()


        class Calc(Frame):

            global a
            global reverse_words
            reverse_words = {
                10: 'A',
                11: 'B',
                12: 'C',
                13: 'D',
                14: 'E',
                15: 'F',
                16: 'G',
                17: 'H',
                18: 'I',
                19: 'J',
                20: 'K',
                21: 'L',
                22: 'M',
                23: 'N',
                24: 'O',
                25: 'P',
                26: 'Q',
                27: 'R',
                28: 'S',
                29: 'T',
                30: 'U',
                31: 'V',
                32: 'W',
                33: 'X',
                34: 'Y',
                35: 'Z'
            }
            a = [
                "c", "DEL", "×", "÷", "+", "-", "(", ")", "=", "back"
            ]
            for i in range(nums):
                newnumb = i
                if newnumb in reverse_words:
                    newnumb = reverse_words[i]
                a.append(str(newnumb))

            def __init__(self, root):
                super(Calc, self).__init__(root)
                self.build()

            def build(self):
                self.formula = "0"
                self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
                self.lbl.place(x=11, y=30)

                btns = a

                x = 10
                y = 100
                for bt in btns:
                    com = lambda x=bt: self.logicalc(x)
                    Button(text=bt, bg="#000", foreground="#FFF",
                           font=("Times New Roman", 15, "bold"),
                           command=com).place(x=x, y=y,
                                              width=100,
                                              height=79)
                    x += 100
                    if x > 450:
                        x = 10
                        y += 81

            def logicalc(self, operation):
                global test_page
                if operation == "c":
                    self.formula = ""
                elif operation == "DEL":
                    self.formula = self.formula[0:-1]
                elif operation == "=":
                    self.formula = self.calculation(self.formula, nums)
                elif operation == "back":
                    test_page = False
                else:
                    if self.formula == "0":
                        self.formula = ""
                    self.formula += operation
                if test_page == True:
                    self.update()
                else:
                    root.destroy()

            def update(self):
                if self.formula == "":
                    self.formula = "0"
                self.lbl.configure(text=self.formula)

            def calculation(self, line, nums):
                def up10(number):
                    words = {
                        'A': 10,
                        'B': 11,
                        'C': 12,
                        'D': 13,
                        'E': 14,
                        'F': 15,
                        'G': 16,
                        'H': 17,
                        'I': 18,
                        'J': 19,
                        'K': 20,
                        'L': 21,
                        'M': 22,
                        'N': 23,
                        'O': 24,
                        'P': 25,
                        'Q': 26,
                        'R': 27,
                        'S': 28,
                        'T': 29,
                        'U': 30,
                        'V': 31,
                        'W': 32,
                        'X': 33,
                        'Y': 34,
                        'Z': 35
                    }
                    number = list(number)
                    ten = 0
                    for i in range(len(number)):
                        if number[i] in words:
                            number[i] = words[number[i]]
                        ten = ten + int(number[i]) * (nums ** (len(number) - 1 - i))
                    return ten

                def below10(number):
                    reverse_words = {
                        10: 'A',
                        11: 'B',
                        12: 'C',
                        13: 'D',
                        14: 'E',
                        15: 'F',
                        16: 'G',
                        17: 'H',
                        18: 'I',
                        19: 'J',
                        20: 'K',
                        21: 'L',
                        22: 'M',
                        23: 'N',
                        24: 'O',
                        25: 'P',
                        26: 'Q',
                        27: 'R',
                        28: 'S',
                        29: 'T',
                        30: 'U',
                        31: 'V',
                        32: 'W',
                        33: 'X',
                        34: 'Y',
                        35: 'Z'
                    }
                    ten = ''
                    if number >= nums:
                        while number >= nums:
                            test = number - (number // nums) * nums
                            if (test in reverse_words) and (nums > 10):
                                test = reverse_words[test]
                            ten = ten + str(test)
                            number = number // nums
                        if number != 0:
                            ten = ten + str(number)
                        return ten[len(ten):: -1]
                    else:
                        if nums > 10 and number in reverse_words:
                            number = reverse_words[number]
                        return number

                num = sym = ''
                lnum = []
                lsym = []
                answ = ''
                line = line.replace('÷', '//')
                line = line.replace('×', '*')
                for i in range(len(line)):
                    if line[i].isalnum():
                        num = num + line[i]
                        if i == len(line) - 1:
                            lnum.append(num)
                    else:
                        if num != '':
                            lnum.append(num)
                            num = ''
                for i in range(len(line)):
                    if line[i].isalnum():
                        if sym != '':
                            lsym.append(sym)
                            sym = ''
                    else:
                        sym = sym + line[i]
                        if i == len(line) - 1:
                            lsym.append(sym)
                if nums != 10:
                    for i in range(len(lnum)):
                        lnum[i] = up10(lnum[i])
                if lsym[0] == '(':
                    for i in range(len(lnum) - 1):
                        answ = answ + str(lsym[i]) + str(lnum[i])
                    if lsym[-1] == ')':
                        answ += str(lsym[len(lsym) - 3])
                    else:
                        answ += str(lsym[-1])
                    answ += str(lnum[-1])
                else:
                    for i in range(len(lnum) - 1):
                        answ = answ + str(lnum[i]) + str(lsym[i])
                    answ = answ + str(lnum[-1])
                if lsym[-1] == ')':
                    answ = answ + str(lsym[-1])
                if nums != 10:
                    answ = below10(eval(answ))
                    return answ
                else:
                    return eval(answ)


        if __name__ == '__main__':
            root = Tk()
            root["bg"] = "#000"
            root.geometry("520x" + str(nums // 5 * 80 + 350))
            root.title("калькУлятор")
            root.resizable(False, False)
            app = Calc(root)
            app.pack()
            root.mainloop()
    else:
        break
