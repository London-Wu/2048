from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import ui
import random

class MainWin(QtWidgets.QWidget, ui.Ui_Form):
    block_num = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    score = 0

    def __init__(self):
        super(MainWin, self).__init__()

        self.setupUi(self)
        self.replay_button.clicked.connect(self.replayGame)

        self.block_obj = [[self.l1_1, self.l1_2, self.l1_3, self.l1_4],
                          [self.l2_1, self.l2_2, self.l2_3, self.l2_4],
                          [self.l3_1, self.l3_2, self.l3_3, self.l3_4],
                          [self.l4_1, self.l4_2, self.l4_3, self.l4_4]]
        self.start()

    def changeBlock(self, block_x, block_y, num):  # 变换方块
        _translate = QtCore.QCoreApplication.translate
        if num == 0:
            self.block_obj[block_y][block_x].setStyleSheet("background-color: rgb(162, 152, 152);")
            self.block_obj[block_y][block_x].setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\"></span></p></body></html>"))
        elif num == 2:
            self.block_obj[block_y][block_x].setStyleSheet("background-color: rgb(238, 228, 218);")
            self.block_obj[block_y][block_x].setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#46413b;\">2</span></p></body></html>"))
        elif num == 4:
            self.block_obj[block_y][block_x].setStyleSheet("background-color: rgb(237, 224, 200);")
            self.block_obj[block_y][block_x].setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#46413b;\">4</span></p></body></html>"))
        elif num == 8:
            self.block_obj[block_y][block_x].setStyleSheet("background-color: rgb(242, 177, 121);")
            self.block_obj[block_y][block_x].setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#f9f6f2;\">8</span></p></body></html>"))
        elif num == 16:
            self.block_obj[block_y][block_x].setStyleSheet("background-color: rgb(245, 149, 99);")
            self.block_obj[block_y][block_x].setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#f9f6f2;\">16</span></p></body></html>"))
        elif num == 32:
            self.block_obj[block_y][block_x].setStyleSheet("background-color: rgb(246, 124, 95);")
            self.block_obj[block_y][block_x].setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#f9f6f2;\">32</span></p></body></html>"))
        elif num == 64:
            self.block_obj[block_y][block_x].setStyleSheet("background-color: rgb(246, 94, 59);")
            self.block_obj[block_y][block_x].setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#f9f6f2;\">64</span></p></body></html>"))
        elif num == 128:
            self.block_obj[block_y][block_x].setStyleSheet("background-color: rgb(237, 207, 114);")
            self.block_obj[block_y][block_x].setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#f9f6f2;\">128</span></p></body></html>"))
        elif num == 256:
            self.block_obj[block_y][block_x].setStyleSheet("background-color: rgb(237, 204, 97);")
            self.block_obj[block_y][block_x].setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#f9f6f2;\">256</span></p></body></html>"))
        elif num == 512:
            self.block_obj[block_y][block_x].setStyleSheet("background-color: rgb(237, 204, 79);")
            self.block_obj[block_y][block_x].setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#f9f6f2;\">512</span></p></body></html>"))
        elif num == 1024:
            self.block_obj[block_y][block_x].setStyleSheet("background-color: rgb(237, 204, 61);")
            self.block_obj[block_y][block_x].setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#f9f6f2;\">1024</span></p></body></html>"))
        elif num >= 2048:
            self.block_obj[block_y][block_x].setStyleSheet("background-color: rgb(237, 204, 43);")
            self.block_obj[block_y][block_x].setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#f9f6f2;\">" + str(num) + "</span></p></body></html>"))

    def start(self):  # 初始化
        # 产生两个格
        block1_x = random.randint(0, 3)
        block1_y = random.randint(0, 3)
        block1_num = random.choice((2, 4))
        block2_x = random.randint(0, 3)
        block2_y = random.randint(0, 3)
        while block1_x == block2_x and block1_y == block2_y:  # 防止出现初始化同一个格的情况
            return self.start()
        block2_num = random.choice((2, 4))
        self.block_num[block1_y][block1_x] = block1_num
        self.block_num[block2_y][block2_x] = block2_num
        self.changeBlock(block1_x, block1_y, block1_num)
        self.changeBlock(block2_x, block2_y, block2_num)

    def replayGame(self):  # 当重玩按钮被按下时
        answer = QtWidgets.QMessageBox.question(self, '重玩', '你确定要重玩吗?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if answer == QtWidgets.QMessageBox.Yes:
            self.replay()

    def replay(self):
        # 清除方格
        for i in range(4):
            for j in range(4):
                self.changeBlock(j, i, 0)
        self.block_num = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        # 清除分数
        self.score = 0
        self.score_label.setText('0')
        self.start()
    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:  # 检测按键
        if a0.key() == QtCore.Qt.Key_W:
            self.contralUp()
        if a0.key() == QtCore.Qt.Key_S:
            self.contralDown()
        if a0.key() == QtCore.Qt.Key_A:
            self.contralLeft()
        if a0.key() == QtCore.Qt.Key_D:
            self.contralRight()

    def contral(self, li: list) -> list:
        # 加
        ori = 0
        for i in range(1, 4):
            if li[i] == 0:
                continue
            elif li[i] == li[ori]:
                li[ori] *= 2
                li[i] = 0
                # 还要顺便加一下分
                self.score += li[ori]
                self.score_label.setText(str(self.score))
            ori = i
        # 推
        for i in range(3, -1, -1):
            if li[i] == 0:
                for j in range(i+1, len(li)):
                    li[j-1] = li[j]
                li[3] = 0

        return li

    def add_one(self):  # 加一个格
        add_able = []
        for i in range(4):
            for j in range(4):
                if self.block_num[i][j] == 0:
                    add_able.append((i, j))
        if len(add_able) == 0:
            return
        else:
            block = random.choice(add_able)
            block_num = random.choice((2, 4))
            self.block_num[block[0]][block[1]] = block_num
            self.changeBlock(block[1], block[0], block_num)

    def isover(self):  # 判断是否游戏结束
        for i in range(4):
            for j in range(4):
                if self.block_num[i][j] == 0:
                    return
        for i in range(4):
            for j in range(1,4):
                if self.block_num[i][j-1] == self.block_num[i][j]:
                    return
        for i in range(4):
            for j in range(1,4):
                if self.block_num[j-1][i] == self.block_num[j][i]:
                    return
        # 如果走到这里还没返回，那么你就over了
        answer = QtWidgets.QMessageBox.question(self, '游戏结束!', '无路可走了,是否再来一局?', QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        if answer == QtWidgets.QMessageBox.Yes:
            self.replay()

    def contralUp(self):
        li = []
        ori_block_num = [self.block_num[0][:], self.block_num[1][:], self.block_num[2][:], self.block_num[3][:]]# 这里给一个原来的格子的布局，以便判断是否为无效操作
        for i in range(4):  # x
            for j in range(4):  # y
                li.append(self.block_num[j][i])
            reli = self.contral(li)
            for k in range(4):  # y
                self.changeBlock(i, k, reli[k])
            # 写入到block_num
            for l in range(4):  # y
                self.block_num[l][i] = reli[l]
            li = []
        if ori_block_num != self.block_num:  # 非无效操作下
            # 加个格
            self.add_one()
            # 判断是不是over了
            self.isover()

    def contralDown(self):
        li = []
        ori_block_num = [self.block_num[0][:], self.block_num[1][:], self.block_num[2][:],
                         self.block_num[3][:]]  # 这里给一个原来的格子的布局，以便判断是否为无效操作
        for i in range(4):  # x
            for j in range(3, -1, -1):  # y^-1
                li.append(self.block_num[j][i])
            reli = self.contral(li)
            reli.reverse()
            for k in range(4):  # y
                self.changeBlock(i, k, reli[k])
            # 写入到block_num
            for l in range(4):  # y
                self.block_num[l][i] = reli[l]
            li = []
        if ori_block_num != self.block_num:  # 非无效操作下
            # 加个格
            self.add_one()
            # 判断是不是over了
            self.isover()

    def contralLeft(self):
        li = []
        ori_block_num = [self.block_num[0][:], self.block_num[1][:], self.block_num[2][:],
                         self.block_num[3][:]]  # 这里给一个原来的格子的布局，以便判断是否为无效操作
        for i in range(4):  # y
            for j in range(4):  # x
                li.append(self.block_num[i][j])
            reli = self.contral(li)
            for k in range(4):  # x
                self.changeBlock(k, i, reli[k])
            # 写入到block_num
            for l in range(4):  # x
                self.block_num[i][l] = reli[l]
            li = []
        if ori_block_num != self.block_num:  # 非无效操作下
            # 加个格
            self.add_one()
            # 判断是不是over了
            self.isover()

    def contralRight(self):
        li = []
        ori_block_num = [self.block_num[0][:], self.block_num[1][:], self.block_num[2][:],
                         self.block_num[3][:]]  # 这里给一个原来的格子的布局，以便判断是否为无效操作
        for i in range(4):  # y
            for j in range(3, -1, -1):  # x^-1
                li.append(self.block_num[i][j])
            reli = self.contral(li)
            reli.reverse()
            for k in range(4):  # x
                self.changeBlock(k, i, reli[k])
            # 写入到block_num
            for l in range(4):  # x
                self.block_num[i][l] = reli[l]
            li = []
        if ori_block_num != self.block_num:  # 非无效操作下
            # 加个格
            self.add_one()
            # 判断是不是over了
            self.isover()



app = QtWidgets.QApplication(sys.argv)
mainwin = MainWin()
mainwin.show()
sys.exit(app.exec_())