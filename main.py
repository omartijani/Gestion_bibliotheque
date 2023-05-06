
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
import mysql.connector as connector
import re,  base64, sys, res
from PyQt5.QtCore import QByteArray
mydb = connector.connect(
        host="localhost",
        user="root",
        password="",
        database="libraru"
        )
mycursor = mydb.cursor()

class Login(QMainWindow):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        
        self.login.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.singup.clicked.connect(self.gotocreate)
        self.ErrorLabel = QtWidgets.QLabel()
        self.error.addWidget(self.ErrorLabel)
        self.forgot.clicked.connect(self.forget)

    def loginfunction(self):
     email = self.email.text()
     password = self.password.text()
     self.ErrorLabel.setText('')


    
     sql = "SELECT * FROM user WHERE email = %s AND password = %s"
     val = (email, password)
     mycursor.execute(sql, val)
     result = mycursor.fetchone()

     if result:
        
        mainp=Page()
        widget.addWidget(mainp)
        widget.setCurrentIndex(widget.currentIndex()+1)
     else:
        self.ErrorLabel.setText("Invalid email or password")
        self.ErrorLabel.setStyleSheet("color: red; border: 2px solid red;  font-size: 20px;")
        self.ErrorLabel.setAlignment(QtCore.Qt.AlignCenter)

    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def forget(self):
     email = self.email.text()
     self.ErrorLabel.setText('')
    
     sql = "SELECT * FROM user WHERE email = %s"
     val = (email,)
     mycursor.execute(sql, val)
     result = mycursor.fetchone()

     if result:
        change_password = forgetpass(email)
        widget.addWidget(change_password)
        widget.setCurrentIndex(widget.currentIndex()+1)
     else:
        self.ErrorLabel.setText("This email does not exist in our db. \n If you are new, please sign up.")
        self.ErrorLabel.setStyleSheet("color: red; border: 2px solid red;  font-size: 20px;")

class forgetpass(QMainWindow):
   def __init__(self,email):
        super(forgetpass,self).__init__()
        loadUi("forgetpass.ui",self)
        
        self.email = email
        self.chp.hide()
        self.submit.clicked.connect(self.check)
        self.changep.clicked.connect(self.change)
        self.newp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Errorp = QtWidgets.QLabel()
        self.Errorc = QtWidgets.QLabel()
        self.erp.addWidget(self.Errorp)
        self.erc.addWidget(self.Errorc)
        self.wlcm = QtWidgets.QLabel()
        self.qstio = QtWidgets.QLabel()
        self.welcome.addWidget(self.wlcm)
        self.qst.addWidget(self.qstio)
        sql = "SELECT name, qst FROM user WHERE email = %s"
        val = (email,)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        name = result[0]
        qst = result[1]
        self.wlcm.setText("welcome "+name+"")
        self.wlcm.setStyleSheet("background: rgb(133, 94, 66); font-size: 20px;border-top-left-radius: 10%;font-family: 'Script MT Bold';")
        self.qstio.setText("the question is : \n \n \n"+qst+"")
        self.qstio.setStyleSheet("background: rgb(133, 94, 66);font-size: 16px;border-top-left-radius: 10%;font-family: 'Script MT Bold';")
        self.wlcm.setAlignment(QtCore.Qt.AlignCenter)
        self.qstio.setAlignment(QtCore.Qt.AlignCenter)
   def check(self):
       answer = self.rep.text()
       email = self.email
       sql = "SELECT * FROM user WHERE email = %s AND answer = %s"
       val = (email, answer)
       mycursor.execute(sql, val)
       result = mycursor.fetchone()

       if result:
           self.chp.show()
        

   def change(self):
        
        confirmpassword = self.confirm.text()
        password = self.newp.text()
        email = self.email
        if not re.match(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}$", password):
            self.Errorp.setText('lenght >=8,\n[a-z],[A-Z],[0-9],[?@*#]')
            self.Errorp.setStyleSheet("color: red; border: 2px solid red;  font-size: 20px;")
        if password != confirmpassword:
            self.Errorc.setText('Password confirmation \n does not match the password')
            self.Errorc.setStyleSheet("color: red; border: 2px solid red;  font-size: 20px;")
        if self.Errorp.text() == '' and \
            self.Errorc.text() == '' :

            sql = "UPDATE user SET password = %s WHERE email = %s"
            val = (password, email)
            mycursor.execute(sql, val)
            mydb.commit()
            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)
            QMessageBox.information(self, "success", "passwor changed successfuly")
class CreateAcc(QMainWindow):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi("singup.ui", self)
        
        self.singup.clicked.connect(self.validation)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.emailErrorLabel = QtWidgets.QLabel()
        self.passwordErrorLabel = QtWidgets.QLabel()
        self.nameErrorLabel = QtWidgets.QLabel()
        self.answerErrorLabel = QtWidgets.QLabel()
        self.confirmPasswordErrorLabel = QtWidgets.QLabel()
        self.emr.addWidget(self.emailErrorLabel)
        self.par.addWidget(self.passwordErrorLabel)
        self.nar.addWidget(self.nameErrorLabel)
        self.anr.addWidget(self.answerErrorLabel)
        self.cor.addWidget(self.confirmPasswordErrorLabel)

    

    def validation(self):
        email = self.email.text()
        name = self.name.text()
        password = self.password.text()
        confirmpassword = self.confirmpassword.text()
        answer = self.answer.text()
        self.emailErrorLabel.setText('')
        self.passwordErrorLabel.setText('')
        self.nameErrorLabel.setText('')
        self.answerErrorLabel.setText('')
        self.confirmPasswordErrorLabel.setText('')
        
        sql = "SELECT * FROM user WHERE email = %s"
        val = (email,)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        if result or\
            not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.emailErrorLabel.setText("email invalid format ou l'email already token")
            self.emailErrorLabel.setStyleSheet("color: red;  font-size: 20px;")
            self.emailErrorLabel.setAlignment(QtCore.Qt.AlignCenter)
        if not re.match(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}$", password):
            self.passwordErrorLabel.setText('lenght >=8,[a-z],[A-Z],[0-9],[?@*#]')
            self.passwordErrorLabel.setStyleSheet("color: red;  font-size: 20px;")
            self.passwordErrorLabel.setAlignment(QtCore.Qt.AlignCenter)
        if not name:
            self.nameErrorLabel.setText('Please enter your name')
            self.nameErrorLabel.setStyleSheet("color: red;  font-size: 20px;")
            self.nameErrorLabel.setAlignment(QtCore.Qt.AlignCenter)
        if not answer:
            self.answerErrorLabel.setText('Please enter an answer to the security question')
            self.answerErrorLabel.setStyleSheet("color: red;  font-size: 20px;")
            self.answerErrorLabel.setAlignment(QtCore.Qt.AlignCenter)
        if password != confirmpassword:
            self.confirmPasswordErrorLabel.setText('Password confirmation does not match the password')
            self.confirmPasswordErrorLabel.setStyleSheet("color: red;  font-size: 20px;")
            self.confirmPasswordErrorLabel.setAlignment(QtCore.Qt.AlignCenter)

        if  self.emailErrorLabel.text() == '' and \
            self.passwordErrorLabel.text() == '' and \
            self.nameErrorLabel.text() == '' and \
            self.answerErrorLabel.text() == '' and \
            self.confirmPasswordErrorLabel.text() == '':
        
            self.createaccfunction()
    def createaccfunction(self):
        email = self.email.text()
        name = self.name.text()
        password = self.password.text()
        answer = self.answer.text()
        qst = self.qst.currentText()
        print("Successfully created account with email:", email, "and password:", password)
        

        sql = "INSERT INTO user (email, password, name, qst, answer ) VALUES (%s, %s, %s, %s, %s)"
        val = (email, password, name, qst, answer)
        mycursor.execute(sql, val)
        mydb.commit()
        login=Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        QMessageBox.information(self, "singup successfuly", "The account was added")


class CustomTableWidgetItem(QTableWidgetItem):
    def __init__(self, pixmap, *args, **kwargs):
        super(CustomTableWidgetItem, self).__init__(*args, **kwargs)
        self.pixmap = pixmap

    def data(self, role):
        if role == QtCore.Qt.BackgroundRole:
            icon_size = QtCore.QSize(200, 200) 
            return QBrush(self.pixmap.scaled(icon_size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        return super(CustomTableWidgetItem, self).data(role)
class Page(QMainWindow):   
     def __init__(self):
        super(Page, self).__init__()
        loadUi("home.ui", self)
        self.add.clicked.connect(self.goadd)
        self.search.clicked.connect(self.searchf)
        self.all.clicked.connect(self.Showb)
        self.dlt.clicked.connect(self.delete_row)
        self.Showb()

     def Showb(self):
        sql = "SELECT * FROM books"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        if data:
            self.list.setRowCount(0)
            self.list.setColumnCount(5)
            for row, form in enumerate(data):
                self.list.insertRow(row)
                for column, item in enumerate(form):
                    if column == 4:  
                        pixmap = QPixmap()
                        pixmap.loadFromData(item)
                        label = QLabel()
                        label.setPixmap(pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
                        label.setAlignment(QtCore.Qt.AlignCenter)
                        self.list.setCellWidget(row, column, label)
                        self.list.setRowHeight(row, 200)  
                    else:
                        self.list.setItem(row, column, QTableWidgetItem(str(item)))
            self.list.setColumnWidth(4, 220)
                
     

     def searchf(self):
        title = self.title.text()
        author = self.author.text()
        year = self.year.text()

        query = "SELECT * FROM books"
        conditions = []
        if title:
            conditions.append("title LIKE '%" + title + "%'")
        if author:
            conditions.append("auteur LIKE '%" + author + "%'")
        if year:
            conditions.append("year = '" + year + "'")

        if conditions:
            query += " WHERE " + " AND ".join(conditions)


        mycursor.execute(query)
        data = mycursor.fetchall()
        if data:
            self.list.setRowCount(0)
            self.list.setColumnCount(5)
            for row, form in enumerate(data):
                self.list.insertRow(row)
                for column, item in enumerate(form):
                    if column == 4: 
                        pixmap = QPixmap()
                        pixmap.loadFromData(item)
                        label = QLabel()
                        label.setPixmap(pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
                        label.setAlignment(QtCore.Qt.AlignCenter)
                        self.list.setCellWidget(row, column, label)
                        self.list.setRowHeight(row, 200)  # Set the row height
                    else:
                        self.list.setItem(row, column, QTableWidgetItem(str(item)))
            self.list.setColumnWidth(4, 220)
        QMessageBox.warning(self, "No Book", "there is no book with those attributs")
     def goadd(self):
        page=Page2()
        widget.addWidget(page)
        widget.setCurrentIndex(widget.currentIndex()+1)
     def delete_row(self):
        selected_row = self.list.currentRow()
        
        if selected_row >= 0:
            id = self.list.item(selected_row, 0).text()
            title = self.list.item(selected_row, 1).text()
            author = self.list.item(selected_row, 2).text()
            year = self.list.item(selected_row, 3).text()

            reply = QMessageBox.question(self, "Delete Book", f"Are you sure you want to delete '{title}' by '{author}' ({year})?", QMessageBox.Yes | QMessageBox.No)
            
            if reply == QMessageBox.Yes:
                
                self.list.removeRow(selected_row)

                
                mycursor.execute("DELETE FROM books WHERE idbook = %s ", (id,))
                mydb.commit()
        else:
            QMessageBox.warning(self, "No Row Selected", "Please select a row to delete.")




class Page2(QMainWindow):   
    def __init__(self):
        super(Page2, self).__init__()
        loadUi("add.ui", self)
        self.add.clicked.connect(self.add_book)
        self.imgc.clicked.connect(self.choose_cover_image)
       
        self.Errort = QtWidgets.QLabel()
        self.Errora = QtWidgets.QLabel()
        self.Errory = QtWidgets.QLabel()
        self.Errorc = QtWidgets.QLabel()
        self.titler.addWidget(self.Errort)
        self.authorr.addWidget(self.Errora)
        self.yearr.addWidget(self.Errory)
        self.coverr.addWidget(self.Errorc)
        self.filename = None  

    def choose_cover_image(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Choose Image", "", "Images (*.png *.xpm *.jpg *.jpeg *.bmp)")
        if filename:
            pixmap = QPixmap(filename)
            self.cover.setPixmap(pixmap)
            self.cover.setScaledContents(True)
            self.filename=filename
        

    def add_book(self):
        title = self.title.text().strip()
        author = self.author.text().strip()
        year = self.year.value()

        if not title:
            self.Errort.setText('Please enter title')
            self.Errort.setStyleSheet("color: red;  font-size: 20px;background : rgb(0,0,0,0)")
            self.Errort.setAlignment(QtCore.Qt.AlignCenter)
        else:
            self.Errort.clear()    

        if not author:
            self.Errora.setText('Please enter author')
            self.Errora.setStyleSheet("color: red;  font-size: 20px;background : rgb(0,0,0,0)")
            self.Errora.setAlignment(QtCore.Qt.AlignCenter)
        else:
            self.Errora.clear()    

        if year == 0:
            self.Errory.setText('Please enter a year ')
            self.Errory.setStyleSheet("color: red;  font-size: 20px;background : rgb(0,0,0,0)")
            self.Errory.setAlignment(QtCore.Qt.AlignCenter)
        else:
            self.Errory.clear()    

        if not self.filename:
            self.Errorc.setText('Please enter a cover image')
            self.Errorc.setStyleSheet("color: red;  font-size: 20px;background : rgb(0,0,0,0)")
            self.Errorc.setAlignment(QtCore.Qt.AlignCenter)
        else:
            self.Errorc.clear()
        if  self.Errora.text() == '' and \
            self.Errorc.text() == '' and \
            self.Errort.text() == '' and \
            self.Errory.text() == '' :

            with open(self.filename, 'rb') as file:
                image_data = file.read()
            try:
                sql = "INSERT INTO books (title, auteur, year, cover) VALUES (%s, %s, %s, %s)"
                mycursor.execute(sql, (title, author, year, image_data))
                mydb.commit()
                QMessageBox.information(self, "Success", "Book added successfully.")
                page = Page()
                widget.addWidget(page)
                widget.setCurrentIndex(widget.currentIndex() + 1)
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "Error", "Failed to add book. Please try again later.")
                page = Page()
                widget.addWidget(page)
                widget.setCurrentIndex(widget.currentIndex() + 1)
            
app = QApplication(sys.argv)
mainwindow = Login()
widget = QStackedWidget()
widget.addWidget(mainwindow)


widget.setFixedWidth(1200)
widget.setFixedHeight(1000)


screenGeometry = app.desktop().screenGeometry()
x = (screenGeometry.width() - widget.width()) // 2
y = (screenGeometry.height() - widget.height()) // 2
widget.setGeometry(x, y, widget.width(), widget.height())

widget.show()
sys.exit(app.exec_())