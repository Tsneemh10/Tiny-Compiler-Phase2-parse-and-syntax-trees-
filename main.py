
import re
from random import random

from PyQt5 import QtCore, QtGui, QtWidgets
import networkx as nx
from PyQt5.QtWidgets import QMessageBox
from networkx.drawing.nx_pydot import graphviz_layout
import matplotlib.pyplot as plt


process = [[], [], []]
HEGIHT = 120
WIDTH = 150
counter = 0
stack = []
Input = []
Input_for_ast=''
nodes = []
Input_to_match = []
Graph = nx.DiGraph()
flag_is_accepted= False
token_error=False





class Point:
    def __init__(self, label, index):
        self.children = []
        self.index = index
        self.is_mark = False
        self.label = label


# gui
class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 160, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 20, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 90, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 230, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.click_enter())
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(60, 210, 621, 22))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.lineEdit = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit.setObjectName("lineEdit")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setGeometry(QtCore.QRect(490, 180, 140, 19))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")

        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.label_3 = QtWidgets.QLabel(self.splitter_4)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.splitter_6 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_6.setGeometry(QtCore.QRect(280, 310, 232, 89))
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_6)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.widget = QtWidgets.QWidget(self.splitter_2)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_PT = QtWidgets.QPushButton(self.widget)
        self.pushButton_PT.clicked.connect(lambda: self.draw_parse_tree())

        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(14)
        self.pushButton_PT.setFont(font)
        self.pushButton_PT.setObjectName("pushButton_PT")
        self.verticalLayout.addWidget(self.pushButton_PT)
        self.pushButton_AST = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(14)
        self.pushButton_AST.setFont(font)
        self.pushButton_AST.setObjectName("pushButton_AST")
        self.pushButton_AST.clicked.connect(lambda: self.draw_ast(Input_for_ast))
        self.verticalLayout.addWidget(self.pushButton_AST)
        self.splitter_5 = QtWidgets.QSplitter(self.splitter_6)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.pushButton_DFA = QtWidgets.QPushButton(self.splitter_5)
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(14)
        self.pushButton_DFA.setFont(font)
        self.pushButton_DFA.setObjectName("pushButton_DFA")
        self.pushButton_DFA.clicked.connect(lambda: self.clear_text_box())
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(14)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Enter your string below"))
        self.label.setText(_translate("MainWindow", "Compilers Final Project "))
        self.label_2.setText(_translate("MainWindow", "PHASE(2)"))
        self.pushButton.setText(_translate("MainWindow", "Enter"))
        self.pushButton_PT.setText(_translate("MainWindow", "PARSE TREE"))
        self.pushButton_AST.setText(_translate("MainWindow", "ABSTRACT SYNTAX TREE"))
        self.pushButton_DFA.setText(_translate("MainWindow", "clear"))


    def clear_text_box(self):
        self.lineEdit.clear()

    def click_enter(self):
        global stack, Input_to_match, nodes, flag_is_accepted, Input_for_ast
        nodes.clear()
        stack.clear()
        Input_to_match.clear()
        Graph.clear()
        flag_is_accepted= False
        Input_for_ast=''
        root = Point('exp', 1)
        process[0].append("$ exp")
        nodes.append(root)
        stack.append(Point('$', 0))
        stack.append(root)
        val = self.lineEdit.text()
        Input_for_ast=val
        temp_tokens = self.tokenize(val)
        temp_tokens.reverse()
        Input_to_match.append('$')
        for i in range(len(temp_tokens)):
            Input_to_match.append(temp_tokens[i])
        str_input = ' '
        for i in range(len(Input_to_match)):
            str_input = str_input + Input_to_match[len(Input_to_match) - i - 1] + ' '

        process[1].append(str_input)
        process[2].append(" ")
        if (token_error):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Your string is not accepted")
            msg.setWindowTitle("Failure!")
            msg.exec_()
            return
        else:
            self.parse()

        for i in range(len(process[0])):
            if (i + 1 == len(process[0])):
                print(process[0][i], "\t\t", process[1][i], "\t\t", "Done!")
                break
            print(process[0][i], "\t\t", process[1][i], "\t\t", process[2][i + 1])

        if (stack[-1].label == '$' and Input_to_match[-1] == '$'):
            print("valid string")
            flag_is_accepted=True
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Your string is accepted")
            msg.setWindowTitle("Success!")
            msg.exec_()


        else:
            print("Invalid string")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Your string is not accepted")
            msg.setWindowTitle("Failure!")
            msg.exec_()

    def draw_parse_tree(self):
        global nodes, Graph
        if (flag_is_accepted):
            nodes_labels = {point.index: point.label for point in nodes if point.index != 0}

            for i in range(0, len(nodes)):
                for j in range(len(nodes[i].children)):
                    Graph.add_edge(nodes[i].index, nodes[i].children[j].index)
            nx.draw_networkx(Graph, pos=graphviz_layout(Graph, prog="dot"), labels=nodes_labels,
                             node_size=[len(nodes_labels[node]) * 260 for node in list(Graph.nodes)], node_color="Yellow")
            plt.tight_layout()
            plt.show()
        else:
            print("warning")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Parsing error!")
            msg.setInformativeText("Your string is not accepted!!")
            msg.setWindowTitle("Error")
            msg.exec_()

    def hierarchy_pos(self, G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):

        if not nx.is_tree(G):
            raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

        if root is None:
            if isinstance(G, nx.DiGraph):
                root = next(iter(nx.topological_sort(G)))  # allows back compatibility with nx version 1.11
            else:
                root = random.choice(list(G.nodes))

        def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):

            if pos is None:
                pos = {root: (xcenter, vert_loc)}
            else:
                pos[root] = (xcenter, vert_loc)
            children = list(G.neighbors(root))
            if not isinstance(G, nx.DiGraph) and parent is not None:
                children.remove(parent)
            if len(children) != 0:
                dx = width / len(children)
                nextx = xcenter - width / 2 - dx / 2
                for child in children:
                    nextx += dx
                    pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                         vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                         pos=pos, parent=root)
            return pos

        return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)

    def draw_ast(self, text: str, verbose=False):
        if flag_is_accepted:
            tree = nx.DiGraph()
            nodes = []
            text = self.tokenize(text)
            labels = dict()
            for index, element in enumerate(text): labels[index] = [element, element]
            for index in range(0, len(text)): nodes.append(index)
            while True:
                if verbose:
                    print(labels)
                    print(nodes)
                if len(nodes) == 1:
                    act_labels = dict()
                    for node in list(tree.nodes):
                        if node in list(tree.nodes): act_labels[node] = labels[node][1]
                    if verbose: print(labels)
                    pos = self.hierarchy_pos(tree)
                    nx.draw_networkx(tree, pos=pos, labels=act_labels,node_size=[len(act_labels[node]) * 300 for node in list(tree.nodes)], node_color= "Yellow")
                    plt.get_current_fig_manager().set_window_title("Syntax Tree")
                    plt.tight_layout()
                    plt.show()
                    break
                flag = False
                for index in range(0, len(nodes)):
                    if labels[nodes[index]][0] == "!":
                        child = nodes[index + 1]
                        if labels[child][0] == "!": continue
                        parent = max(nodes) + 1
                        labels[parent] = ["! " + labels[child][1], "!"]
                        tree.add_edge(parent, child)
                        nodes.pop(index)
                        nodes.pop(index)
                        nodes.insert(index, parent)
                        flag = True
                        break
                if flag: continue
                flag = False
                for index in range(0, len(nodes)):
                    if labels[nodes[index]][0] == ">":
                        left = nodes[index - 1]
                        right = nodes[index + 1]
                        parent = max(nodes) + 1
                        labels[parent] = [labels[left][1] + " > " + labels[right][1], ">"]
                        tree.add_edge(parent, left)
                        tree.add_edge(parent, right)
                        nodes.pop(index - 1)
                        nodes.pop(index - 1)
                        nodes.pop(index - 1)
                        nodes.insert(index - 1, parent)
                        break
                    elif labels[nodes[index]][0] == "<":
                        left = nodes[index - 1]
                        right = nodes[index + 1]
                        parent = max(nodes) + 1
                        labels[parent] = [labels[left][1] + " < " + labels[right][1], "<"]
                        tree.add_edge(parent, left)
                        tree.add_edge(parent, right)
                        nodes.pop(index - 1)
                        nodes.pop(index - 1)
                        nodes.pop(index - 1)
                        nodes.insert(index - 1, parent)
                        break
                    elif labels[nodes[index]][0] == "=":
                        left = nodes[index - 1]
                        right = nodes[index + 1]
                        parent = max(nodes) + 1
                        labels[parent] = [labels[left][1] + " = " + labels[right][1], "="]
                        tree.add_edge(parent, left)
                        tree.add_edge(parent, right)
                        nodes.pop(index - 1)
                        nodes.pop(index - 1)
                        nodes.pop(index - 1)
                        nodes.insert(index - 1, parent)
                        break
                if flag: continue
                flag = False

                for index in range(0, len(nodes)):
                    if labels[nodes[index]][0] == "&&":
                        left = nodes[index - 1]
                        right = nodes[index + 1]
                        parent = max(nodes) + 1
                        labels[parent] = [labels[left][1] + " && " + labels[right][1], "&&"]
                        tree.add_edge(parent, left)
                        tree.add_edge(parent, right)
                        nodes.pop(index - 1)
                        nodes.pop(index - 1)
                        nodes.pop(index - 1)
                        nodes.insert(index - 1, parent)
                        flag = True
                        break
                if flag: continue
                for index in range(0, len(nodes)):
                    if labels[nodes[index]][0] == "||":
                        left = nodes[index - 1]
                        right = nodes[index + 1]
                        parent = max(nodes) + 1
                        labels[parent] = [labels[left][1] + " || " + labels[right][1], "||"]
                        tree.add_edge(parent, left)
                        tree.add_edge(parent, right)
                        nodes.pop(index - 1)
                        nodes.pop(index - 1)
                        nodes.pop(index - 1)
                        nodes.insert(index - 1, parent)
                        break


        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Syntax error!")
            msg.setInformativeText("Your string is not accepted!!")
            msg.setWindowTitle("Error")
            msg.exec_()


    def tokenize(self, input):
        global token_error
        token_error= False
        current = 0
        tokens = []
        alphabet = re.compile(r'[a-zA-Z_][a-zA-Z0-9_]*', re.I)
        space = re.compile(r"\s")

        while current < len(input):
            char = input[current]
            if re.match(space, char):
                current = current + 1   # x<y || y
                continue
            elif char == '<':
                tokens.append("<")
                current = current + 1
                continue
            elif char == '>':
                tokens.append(">")
                current = current + 1
                continue
            elif char == '=':
                tokens.append("=")
                current = current + 1
                continue
            elif char == '!':
                tokens.append("!")
                current = current + 1
                continue
            elif char == '|':
                if (current + 1 < len(input)):
                    if input[current + 1] == "|":
                        tokens.append("||")
                        current = current + 2
                        continue
                else:
                    token_error= True
                    return tokens
            elif char == '&':
                if (current+1 < len(input)):
                    if input[current + 1] == "&":
                        tokens.append("&&")
                        current = current + 2
                        continue
                else:
                    token_error = True
                    return tokens
            elif re.match(alphabet, char):
                value = ''
                while re.match(alphabet, char):
                    value += char
                    current = current + 1
                    if current < len(input):
                        char = input[current]
                    else:
                        break
                tokens.append("ID")
                continue
            token_error= True
            print(token_error)
            return tokens
        return tokens

    def get_max_index(self):
        return max([point.index for point in nodes]) + 1

    def parse(self):
        global stack, nodes, Input_to_match
        action = ''

        while stack[-1].label != '$' and Input_to_match != '$':
            fixed_In = ''
            fixed_st = ''

            if stack[-1].label == Input_to_match[-1]:
                print("match")
                stack.pop()
                Input_to_match.pop()
                for i in range(len(Input_to_match)):
                    fixed_In = fixed_In + Input_to_match[len(Input_to_match) - i - 1] + ' '

                for i in range(len(stack)):
                    fixed_st = fixed_st + stack[i].label + ' '

                process[0].append(fixed_st)
                process[1].append(fixed_In)
                process[2].append("match!")
                # print(fixed_st,fixed_Ins)

            elif stack[-1].label == 'exp':
                if Input_to_match[-1] == '!' or Input_to_match[-1] == 'ID':
                    action = ("exp -> term exp'")
                    node_temp = stack.pop()
                    child1 = Point('term', self.get_max_index())
                    nodes.append(child1)
                    child2 = Point("exp'", self.get_max_index())
                    nodes.append(child2)
                    node_temp.children.append(child1)
                    node_temp.children.append(child2)

                    stack.append(child2)
                    stack.append(child1)

                else:
                    print("No rule to match!!!!")
                    break


            elif stack[-1].label == "exp'":
                if Input_to_match[-1] == '||':
                    action = ("exp' -> || term exp'")

                    node_temp = stack.pop()
                    child1 = Point('||', self.get_max_index())
                    nodes.append(child1)
                    child2 = Point("term", self.get_max_index())
                    nodes.append(child2)
                    child3 = Point("exp'", self.get_max_index())
                    nodes.append(child3)
                    node_temp.children.append(child1)
                    node_temp.children.append(child2)
                    node_temp.children.append(child3)
                    stack.append(child3)
                    stack.append(child2)
                    stack.append(child1)


                elif Input_to_match[-1] == '$':
                    action = ("exp' -> ∈")
                    node_temp = stack.pop()
                    child1 = Point('∈', self.get_max_index())
                    nodes.append(child1)
                    node_temp.children.append(child1)

                else:
                    print("No rule to match!!!!")
                    break


            elif stack[-1].label == "term":
                if Input_to_match[-1] == '!' or Input_to_match[-1] == 'ID':
                    action = ("term -> factor term'")
                    node_temp = stack.pop()
                    child1 = Point('factor', self.get_max_index())
                    nodes.append(child1)
                    child2 = Point("term'", self.get_max_index())

                    nodes.append(child2)
                    node_temp.children.append(child1)
                    node_temp.children.append(child2)

                    stack.append(child2)
                    stack.append(child1)

                else:
                    print("No rule to match!!!!")
                    break

            elif stack[-1].label == "term'":
                if Input_to_match[-1] == '&&':
                    action = ("term' -> && factor term'")

                    node_temp = stack.pop()
                    child1 = Point('&&', self.get_max_index())
                    nodes.append(child1)
                    child2 = Point("factor", self.get_max_index())
                    nodes.append(child2)
                    child3 = Point("term'", self.get_max_index())

                    nodes.append(child3)
                    node_temp.children.append(child1)
                    node_temp.children.append(child2)
                    node_temp.children.append(child3)
                    stack.append(child3)
                    stack.append(child2)
                    stack.append(child1)

                elif Input_to_match[-1] == '||' or Input_to_match[-1] == '$':
                    node_temp = stack.pop()
                    child1 = Point('∈', self.get_max_index())
                    nodes.append(child1)
                    node_temp.children.append(child1)

                else:
                    print("No rule to match!!!!")
                    break

            elif stack[-1].label == "factor":
                if Input_to_match[-1] == '!' or Input_to_match[-1] == 'ID':
                    action = ("factor -> operand factor'")
                    node_temp = stack.pop()
                    child1 = Point('op', self.get_max_index())
                    nodes.append(child1)
                    child2 = Point("factor'", self.get_max_index())

                    nodes.append(child2)
                    node_temp.children.append(child1)
                    node_temp.children.append(child2)

                    stack.append(child2)
                    stack.append(child1)


                else:
                    print("No rule to match!!!!")
                    break

            elif stack[-1].label == "factor'":
                if Input_to_match[-1] == '>' or Input_to_match[-1] == '<' or Input_to_match[-1] == '=':
                    action = ("factor' -> && comp op factor'")

                    node_temp = stack.pop()
                    child1 = Point('comp', self.get_max_index())
                    nodes.append(child1)
                    child2 = Point("op", self.get_max_index())
                    nodes.append(child2)
                    child3 = Point("factor'", self.get_max_index())

                    nodes.append(child3)
                    node_temp.children.append(child1)
                    node_temp.children.append(child2)
                    node_temp.children.append(child3)
                    stack.append(child3)
                    stack.append(child2)
                    stack.append(child1)
                elif Input_to_match[-1] == '||' or Input_to_match[-1] == '&&' or Input_to_match[-1] == '$':
                    node_temp = stack.pop()
                    child1 = Point('∈', self.get_max_index())
                    nodes.append(child1)
                    node_temp.children.append(child1)


                else:
                    print("No rule to match!!!!")
                    break
            elif stack[-1].label == "comp":
                if Input_to_match[-1] == '>':
                    action = ("comp -> >")
                    node_temp = stack.pop()
                    child1 = Point('>', self.get_max_index())
                    nodes.append(child1)
                    node_temp.children.append(child1)

                    stack.append(child1)

                elif Input_to_match[-1] == '<':
                    action = ("comp -> <")
                    node_temp = stack.pop()
                    child1 = Point('<', self.get_max_index())
                    nodes.append(child1)
                    node_temp.children.append(child1)

                    stack.append(child1)

                elif Input_to_match[-1] == '=':
                    action = ("comp -> =")
                    node_temp = stack.pop()
                    child1 = Point('=', self.get_max_index())
                    nodes.append(child1)
                    node_temp.children.append(child1)

                    stack.append(child1)


                else:
                    print("No rule to match!!!!")
                    break


            elif stack[-1].label == "op":
                if Input_to_match[-1] == 'ID':
                    action = ("operand -> ID")
                    node_temp = stack.pop()
                    child1 = Point('ID', self.get_max_index())
                    nodes.append(child1)
                    node_temp.children.append(child1)

                    stack.append(child1)


                elif Input_to_match[-1] == '!':
                    action = ("operand -> ! operand")
                    node_temp = stack.pop()
                    child1 = Point('!', self.get_max_index())
                    nodes.append(child1)
                    child2 = Point("op", self.get_max_index())

                    nodes.append(child2)
                    node_temp.children.append(child1)
                    node_temp.children.append(child2)

                    stack.append(child2)
                    stack.append(child1)

                else:
                    print("No rule to match!!!!")
                    break
            fixed_Input = str('')
            fixed_stack = str('')
            for i in range(len(Input_to_match)):
                fixed_Input = fixed_Input + Input_to_match[len(Input_to_match) - i - 1] + ' '

            for i in range(len(stack)):
                fixed_stack = fixed_stack + stack[i].label + ' '

            fixed_Input = "{0:>40}".format(fixed_Input)
            process[0].append(fixed_stack)
            process[1].append(fixed_Input)
            process[2].append(action)




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

    # print(fixed_stack, fixed_Input, action)



