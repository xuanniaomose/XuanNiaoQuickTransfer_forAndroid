# Form implementation generated from reading ui file 'XuanNiaoTR.ui'
#
# Created by: PyQt6 UI code generator 6.0.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import re
import sys
import json
import time
import socket
import threading
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow


class Ui_XuanNiaoTR(object):

    def __init__(self):
        super(Ui_XuanNiaoTR, self).__init__()

        self.input_stream = None
        self.XuanNiaoTR = None
        self.button_send = None
        self.frame_bottom = None
        self.s_entry = None
        self.checkBox_connect = None
        self.lineEdit_port = None
        self.label_port = None
        self.lineEdit_ipv4 = None
        self.label_ipv4 = None
        self.frame_medium = None
        self.ChartBrowser = None
        self.frame_chart = None
        self.window = None
        self.s = None
        self.addr = None
        self.client = None
        self.receive_buffer = str()  # 接收区缓冲
        self.send_buffer = str()  # 发送区缓冲
        self.Server_ipv4 = self.get_host_auto()
        self.Server_port = int(9999)
        self.receive_str = None
        self.send_str = None
        self.ip = None
        # self.contact()

    def setupUi(self, XuanNiaoTR):
        XuanNiaoTR.setObjectName("XuanNiaoTR")
        # XuanNiaoTR.setEnabled(True)
        XuanNiaoTR.resize(400, 536)
        # XuanNiaoTR.setSizeGripEnabled(False)
        # XuanNiaoTR.setModal(False)

        self.frame_chart = QtWidgets.QFrame(XuanNiaoTR)
        self.frame_chart.setGeometry(QtCore.QRect(0, 0, 400, 530))
        self.frame_chart.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_chart.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_chart.setObjectName("frame_chart")
        # 聊天收发文本显示
        self.ChartBrowser = QtWidgets.QTextBrowser(self.frame_chart)
        self.ChartBrowser.setGeometry(QtCore.QRect(0, 0, 400, 330))
        self.ChartBrowser.setObjectName("ChartBrowser")
        self.ChartBrowser.append(self.receive_str)
        # 中部框体
        self.frame_medium = QtWidgets.QFrame(self.frame_chart)
        self.frame_medium.setGeometry(QtCore.QRect(0, 329, 400, 40))
        self.frame_medium.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_medium.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_medium.setObjectName("frame_medium")
        # 电脑端ipv4地址 端口号 是否开启连接
        self.label_ipv4 = QtWidgets.QLabel(self.frame_medium)
        self.label_ipv4.setGeometry(QtCore.QRect(0, 10, 71, 21))
        self.label_ipv4.setObjectName("label_ipv4")

        self.lineEdit_ipv4 = QtWidgets.QLineEdit(self.frame_medium)
        self.lineEdit_ipv4.setGeometry(QtCore.QRect(70, 10, 100, 21))
        self.lineEdit_ipv4.setText(self.Server_ipv4)
        self.lineEdit_ipv4.setFrame(True)
        self.lineEdit_ipv4.setReadOnly(True)
        self.lineEdit_ipv4.setObjectName("lineEdit_ipv4")
        # ipv4 = self.lineEdit_port.text()
        # self.Server_ipv4 = int(ipv4)

        self.label_port = QtWidgets.QLabel(self.frame_medium)
        self.label_port.setGeometry(QtCore.QRect(180, 10, 71, 21))
        self.label_port.setObjectName("label_port")

        self.lineEdit_port = QtWidgets.QLineEdit(self.frame_medium)
        self.lineEdit_port.setGeometry(QtCore.QRect(250, 10, 50, 21))
        self.lineEdit_port.setInputMask("9999")
        self.lineEdit_port.setText("9999")
        self.lineEdit_port.setObjectName("lineEdit_port")
        port = self.lineEdit_port.text()
        self.Server_port = int(port)

        self.checkBox_connect = QtWidgets.QCheckBox(self.frame_medium)
        self.checkBox_connect.setGeometry(QtCore.QRect(330, 10, 71, 21))
        self.checkBox_connect.setChecked(True)
        self.checkBox_connect.setObjectName("checkBox_connect")
        self.checkBox_connect.stateChanged.connect(self.check_connect)
        # 聊天输入框
        self.s_entry = QtWidgets.QLineEdit(self.frame_chart)
        self.s_entry.setGeometry(QtCore.QRect(0, 370, 401, 141))
        self.s_entry.setText("这里是电脑端")
        self.s_entry.setObjectName("s_entry")
        self.s_entry.returnPressed.connect(self.sending)
        # 底部框体
        self.frame_bottom = QtWidgets.QFrame(self.frame_chart)
        self.frame_bottom.setGeometry(QtCore.QRect(0, 510, 401, 31))
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_bottom.setObjectName("frame_bottom")

        self.button_send = QtWidgets.QPushButton(self.frame_bottom)
        self.button_send.setGeometry(QtCore.QRect(300, 0, 75, 24))
        self.button_send.setObjectName("button_send")
        self.button_send.clicked.connect(self.sending)

        self.connecting()
        self.retranslateUi(XuanNiaoTR)
        self.lineEdit_ipv4.editingFinished.connect(self.lineEdit_ipv4.update)
        self.button_send.clicked.connect(self.s_entry.update)
        QtCore.QMetaObject.connectSlotsByName(XuanNiaoTR)
        print("主界面创建完成")

    def retranslateUi(self, XuanNiaoTR):
        _translate = QtCore.QCoreApplication.translate
        XuanNiaoTR.setWindowTitle(_translate("XuanNiaoTR", "Dialog"))
        self.label_ipv4.setText(_translate("XuanNiaoTR", "电脑端ipv4:"))
        self.label_port.setText(_translate("XuanNiaoTR", "电脑端口号:"))
        self.checkBox_connect.setText(_translate("XuanNiaoTR", "连接状态"))
        self.button_send.setText(_translate("XuanNiaoTR", "发送"))

    def check_connect(self):
        print("状态改变")
        status = self.checkBox_connect.isChecked()
        if status:
            self.connect()
            print("已连接")

    # 自动获取本机host
    def get_host_auto(self):
        # 函数 gethostname() 返回当前正在执行 Python 的系统主机名
        host = str(socket.gethostbyname(socket.gethostname()))
        return host

    # 建立连接
    def connect(self):
        self.s = socket.socket()
        host = self.get_host_auto()
        self.s.bind((host, self.Server_port))
        self.s.listen(1)
        self.ChartBrowser.append('等待手机接入...\n')
        self.client, self.addr = self.s.accept()
        self.ChartBrowser.append(time.strftime('%H:%M:%S') + ' 连接手机IP为'
                                 + str(self.addr[0]) + '手机端口' + str(self.addr[1]) + '\n\n')
        try:
            self.receiving()
        except Exception as e:
            print(e)
        return

    # 发送数据
    def send_data(self):
        self.send_buffer = self.s_entry.text()
        if self.send_buffer is not None:
            # 特别注意：数据的结尾加上换行符才可让客户端的readline()停止阻塞
            self.client.send(bytes(self.send_buffer, 'utf8'))
            self.ChartBrowser.append(time.strftime('%H:%M:%S') + ' 服务器:\n' + self.send_buffer + '\n\n')
            # self.client.shutdownOutput()
            # self.s_entry.clear()
        return

    # 接收数据
    def receive_data(self):
        while True:
            try:
                self.input_stream = self.client.recv(1024)
                self.receive_buffer = str(self.input_stream, 'utf8')
                msg_type = re.search(r"@\w{3}Mark@", self.receive_buffer, re.MULTILINE)
                if self.receive_buffer != "":
                    print(self.receive_buffer)
                    if self.receive_buffer == "@EndMark@\n":
                        self.ChartBrowser.append(time.strftime('%H:%M:%S') + ' 手机端:断开连接' + '\n\n')
                    # 用正则表达式判定接收内容是“断开”、“消息”还是“文件”
                    elif msg_type is not None:
                        # 传输类型为文件
                        if msg_type.group(0) == "@FilMark@":
                            # server_head_msg = json.loads(self.client.recv(1024))
                            file_name = re.findall(r"@FilMark@(.*)@FName@", self.receive_buffer, re.M)[0]
                            self.ChartBrowser.append(time.strftime('%H:%M:%S') + '手机端:\n' + str(file_name))
                            print(file_name)
                            file_path = 'E:/test/'
                            file_len = int(re.findall(r"@FName@(.*)@FLen@", self.receive_buffer, re.M)[0])
                            print(file_len)
                            self.client.send(bytes("接收到：" + file_name, 'utf8'))
                            print(isinstance(file_len, int))

                            self.input_stream = self.client.recv(file_len)
                            print(str(self.input_stream))
                            print(str(self.input_stream))
                            file_data = self.input_stream
                            with open(file_path + file_name, 'wb') as f:
                                f.write(file_data)
                                f.close()
                    else:
                        self.receive_str = self.receive_buffer
                        self.ChartBrowser.insertPlainText(
                            time.strftime('%H:%M:%S') + ' 客户端:\n' + self.receive_str + '\n')
            except Exception as e:
                print(e)

    # connecting(),sending()和receiving()分别开启一个线程
    def connecting(self):
        threading.Thread(target=self.connect).start()
        return

    def sending(self):
        threading.Thread(target=self.send_data).start()
        return

    def receiving(self):
        sleep_time = 5
        t_r = threading.Thread(target=self.receive_data(), args=(sleep_time,))
        t_r.setDaemon(True)
        t_r.start()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__ui = Ui_XuanNiaoTR()
        self.__ui.setupUi(self)
        self.setWindowTitle('玄鸟快传')  # 设置窗口标题要在窗口ui创建之后


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exit(app.exec())
