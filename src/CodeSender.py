from PyQt5 import QtCore, QtGui, QtWidgets
from Classes import MainWindow, uGecko, Verification


class CodeSender_Main(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super(CodeSender_Main, self).__init__()

        # Set up base GUI parameters
        self.setupUi(self)
        self.Set_Functions()

        # Run verification functions
        self.Verify_IPv4()
        self.Verify_Code(self.Input_plainTextEdit.toPlainText(), self.Input_plainTextEdit)
        self.Verify_Code(self.Input_plainTextEdit_2.toPlainText(), self.Input_plainTextEdit_2)

        # Set vars & states
        self.restore = 0
        self.connected = False
        self.Send_pushButton.setEnabled(False)
        self.Send_pushButton_2.setEnabled(False)

    def Set_Functions(self):
        self.Connection_lineEdit.textChanged.connect(self.Verify_IPv4)
        self.Input_plainTextEdit.textChanged.connect(self.On_Input_Changed)
        self.Input_plainTextEdit_2.textChanged.connect(self.On_Input_Changed)
        self.Format_pushButton.clicked.connect(self.On_Format_Clicked)
        self.Format_pushButton_2.clicked.connect(self.On_Format_Clicked)
        self.Connection_pushButton.clicked.connect(self.Connect)
        self.Send_pushButton.clicked.connect(self.On_Send_Clicked)
        self.Send_pushButton_2.clicked.connect(self.On_Send_Clicked)

    def On_Input_Changed(self):
        input_text = self.sender().toPlainText()
        self.Verify_Code(input_text, self.sender())

    def On_Format_Clicked(self):
        input_text = self.sender().parent().findChild(QtWidgets.QPlainTextEdit).toPlainText()
        formatted_text = self.Format_Code(input_text)
        self.sender().parent().findChild(QtWidgets.QPlainTextEdit).setPlainText(formatted_text)

    def Verify_IPv4(self):
        if Verification.IP_Verification(self.Connection_lineEdit.text()):
            self.Connection_lineEdit.setStyleSheet("selection-background-color: rgb(0, 255, 0);")
            self.Connection_pushButton.setEnabled(True)
        else:
            self.Connection_lineEdit.setStyleSheet("selection-background-color: rgb(255, 0, 0);")
            self.Connection_pushButton.setEnabled(False)

    def Verify_Code(self, code, used_object):
        if Verification.Code_Verification(code):
            used_object.setStyleSheet("background-color: rgb(0, 255, 0);")
            used_object.verticalScrollBar().setStyleSheet("background-color: rgb(239, 239, 239);")
        else:
            used_object.setStyleSheet("background-color: rgb(255, 0, 0);")
            used_object.verticalScrollBar().setStyleSheet("background-color: rgb(239, 239, 239);")

    def Format_Code(self, code):
        input_string = code.replace(" ", "").replace("\n", "")
        output_string = ""
        for i, c in enumerate(input_string):
            if i % 17 == 16:
                output_string += c + "\n"
            else:
                output_string += c

        new_output_string = []
        for i, line in enumerate(output_string.split("\n")):
            if line.startswith("#"):
                new_output_string.append("#" + line[1:9] + " " + line[9:])
            elif line:
                new_output_string.append(line[:8] + " " + line[8:])

        return "\n".join(new_output_string).upper()

    def Connect(self):
        if not self.connected:
            self.tcp_con = uGecko.uGecko(self.Connection_lineEdit.text())
            self.tcp_con.connect()
            self.Send_pushButton.setEnabled(True)
            self.Send_pushButton_2.setEnabled(True)
            self.Connection_pushButton.setText("Disconnect")
            self.connected = True
        else:
            self.Connection_pushButton.setText("Connect")
            self.Disconnect()
            self.connected = False

    def Disconnect(self):
        self.tcp_con.disconnect()
        self.Send_pushButton.setEnabled(False)
        self.Send_pushButton_2.setEnabled(False)

    def On_Send_Clicked(self):
        input_text = self.sender().parent().findChild(QtWidgets.QPlainTextEdit).toPlainText()
        method = "RAM" if self.sender() == self.Send_pushButton else "CAFE"
        if method not in ["RAM","CAFE"]:
            print("Invalid Send() method. Program will now exit")
            sys.exit(1)
        self.Send(input_text, method)

    def Send(self, code_str, method):
        if method == "RAM":
            commands = code_str.split("\n")
            for command in commands:
                if "#" not in command:
                    addr, value = command.split()
                    self.tcp_con.kernelWrite(int(addr, 16), int(value, 16), True)
        elif method == "CAFE":
            cafe_code = ""
            for line in code_str.split("\n"):
                if not line.startswith("#"):
                    cafe_code += line.replace(" ", "")

            self.tcp_con.s.send(bytes.fromhex('03'))
            self.tcp_con.s.send(bytes.fromhex('10014CFC00000000'))

            for x in range(self.restore):
                address = '{:08X}'.format(0x01133000 + x * 4)
                self.tcp_con.s.send(bytes.fromhex('03'))
                self.tcp_con.s.send(bytes.fromhex(address + '00000000'))

            for x in range(0, len(cafe_code), 8):
                address = '{:08X}'.format(0x01133000 + (x // 8) * 4)
                data = cafe_code[x:x+8]
                self.tcp_con.s.send(bytes.fromhex('03'))
                self.tcp_con.s.send(bytes.fromhex(address + data))
    
            self.tcp_con.s.send(bytes.fromhex('03'))
            self.tcp_con.s.send(bytes.fromhex('10014CFC00000001'))
            self.restore = x
        else:
            print("Invalid Send() method. Program will now exit")
            sys.exit(1)


if __name__ == "__main__":
    import sys
    CodeSender_App = QtWidgets.QApplication(sys.argv)
    CodeSender_Var = CodeSender_Main()
    CodeSender_Var.show()
    sys.exit(CodeSender_App.exec_())
