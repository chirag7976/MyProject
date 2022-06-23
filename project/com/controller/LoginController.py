from flask import render_template, request, redirect, session, url_for
import random
import string
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from project import app
from project.com.dao.LoginDAO import LoginDAO
from project.com.dao.RegisterDAO import RegisterDAO
from project.com.dao.StudentDAO import StudentDAO
from project.com.vo.LoginVO import LoginVO
from project.com.vo.RegisterVO import RegisterVO
from project.com.vo.StudentVO import StudentVO


# check for default url pattern
@app.route('/', methods=['get'])
def adminLoadLogin():
    try:
        session.clear()
        print("in login")
        return render_template('admin/login.html')
    except Exception as ex:
        print(ex)


#student login url
@app.route('/student/loadLogin', methods=['get'])
def studentLoadLogin():
    try:
        session.clear()
        print("in student login")
        return render_template('student/studentLogin.html')
    except Exception as ex:
        print(ex)

#validate student username
@app.route('/student/validateUsername', methods=['post'])
def studentValidateLogin():
    try:
        print('hello')
        studentUsername = request.form['studentUsername']
        studentVO = StudentVO()
        studentDAO = StudentDAO()

        studentVO.studentEmail = studentUsername
        studentVO.studentStatus = 'active'

        studentList = studentDAO.validateUsername(studentVO)
        print('studentList at LoginController', studentList)

        if len(studentList) == 1  :
            if studentList[0].studentStatus == 'active':
                OTP = ''.join((random.choice(string.digits)) for i in range(4))
                # OTP = '3456'
                print(OTP)

                sender = "studentassistence.donotreply4@gmail.com"
                receiver = studentList[0].studentEmail
                msg = MIMEMultipart()

                msg['Form'] = sender
                msg['To'] = receiver
                msg['Subject'] = "OTP for Student Login"

                msg.attach(MIMEText(OTP, 'plain'))

                # smtp mail server setup
                server = smtplib.SMTP('smtp.gmail.com', 587)

                server.starttls()

                # login details for mail server
                server.login(sender, "cjp_@1234")
                text = msg.as_string()

                # send email
                server.sendmail(sender, receiver, text)

                # mail server quit.
                server.quit()


                session['session_stduentId'] = studentList[0].studentId
                session['session_studentUsername'] = studentList[0].studentEmail
                session['session_studentFirstName'] = studentList[0].studentFirstName
                session['session_studentLastName'] = studentList[0].studentLastName
                session['session_studentGender'] = studentList[0].studentGender
                session['session_studentContactNumber'] = studentList[0].studentContactNumber
                session['session_OTP'] = OTP
                session['session_studentLogin'] = 'inactive'

                return render_template('student/studentEnterOTP.html')
            else:
                session.clear()
                error = "Student temporary Blocked!"
                return render_template('student/studentLogin.html', error=error)

        else:
            session.clear()
            error = "Please ENTER correct Username!"
            return render_template('student/studentLogin.html', error = error)

    except Exception as ex:
        print(ex)

#validate student OTP
@app.route('/student/validateLogin', methods = ['post'])
def studentValidateOTP():
    try:
        print('In studentValidateOTP in Login Controller')
        studentOTP = request.form['studentOTP']
        print('studentOTP', studentOTP)
        if studentOTP == session['session_OTP'] :
            session['session_studentLogin'] = 'active'
            return redirect(url_for('studentLoadDashboard'))
        else:
            error = 'wrong OTP.'
            return render_template('student/studentEnterOTP.html', error = error)
    except Exception as ex:
        print(ex)




@app.route('/admin/validateLogin', methods=['post'])
def adminValidateLogin():
    try:
        # get values from login form
        loginUsername = request.form['loginUsername']
        loginPassword = request.form['loginPassword']

        # object of LoginVO() and LoginDAO()
        loginVO = LoginVO()
        loginDAO = LoginDAO()

        # store values in loginVO object
        loginVO.loginUsername = loginUsername
        loginVO.loginPassword = loginPassword

        loginVOList = loginDAO.validateLogin(loginVO)  # it returns serialized object values
        # print('********************loginVOList',loginVOList)

        loginDictList = [i.as_dict() for i in loginVOList]

        # print('*/**/*/*/*/*/*/*/*/*/*/*/loginDictList',loginDictList)
        lenLoginDictList = len(loginDictList)

        if lenLoginDictList == 0:
            msg = 'Username or Password is incorrect.'
            return render_template('admin/login.html', error=msg)
        elif loginDictList[0]['loginStatus'] == 'inactive':
            msg = 'You are temporary blocked by admin ! '
            return render_template('admin/login.html', error=msg)
        else:
            for i in loginDictList:
                # get data from dictionary
                loginId = i['loginId']
                loginUsername = i['loginUsername']
                loginRole = i['loginRole']

                # store in session
                session['session_loginId'] = loginId
                session['session_loginUsername'] = loginUsername
                session['session_loginRole'] = loginRole
                session.permanent = True

                # get detail of faclty from register master
                if loginRole == 'faculty':
                    registerVO = RegisterVO()
                    registerDAO = RegisterDAO()
                    registerVO.register_LoginId = loginId
                    registerVOList = registerDAO.getFacultyData(registerVO)
                    session['session_registerId'] = registerVOList[0].registerId
                    session['session_FirstName'] = registerVOList[0].registerFirstName
                    session['session_LastName'] = registerVOList[0].registerLastName
                    session['session_loginGender'] = registerVOList[0].registerGender
                    session['session_loginContactNumber'] = registerVOList[0].registerContactNumber

                if loginRole == 'admin':
                    # load admin dashboard
                    return redirect(url_for('adminLoadDashboard'))
                else:
                    # redirect to login page
                    return redirect(url_for('facultyLoadDashboard'))
    except Exception as ex:
        print(ex)


@app.route('/admin/loadDashboard')
def adminLoadDashboard():
    try:
        if adminLoginSession() == 'admin':
            return render_template('admin/index.html')
        else:
            return redirect(url_for('adminLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/faculty/loadDashboard')
def facultyLoadDashboard():
    try:
        if adminLoginSession() == 'faculty':
            return render_template('faculty/index.html')
        else:
            return redirect(url_for('facultyLogoutSession'))
    except Exception as ex:
        print(ex)


@app.route('/faculty/loadChangePassword')
def facultyLoadDashbhoard():
    try:
        if adminLoginSession() == 'faculty':
            return render_template('faculty/changePassword.html')
        else:
            return redirect(url_for('facultyLogoutSession'))
    except Exception as ex:
        print(ex)

@app.route('/faculty/updatePassword', methods=['post'])
def facultyUpadatePassword():
    try:
        if adminLoginSession() == 'faculty':
            currentPassword = request.form['currentPassword']
            newPassword = request.form['newPassword']
            loginId = session['session_loginId']

            loginVO = LoginVO()
            loginDAO = LoginDAO()

            loginVO.loginId = loginId
            loginVOList = loginDAO.viewLogin(loginVO)
            if len(loginVOList) == 0:
                error = "Something went worng Password can't be change. Please Try again."
                return render_template('faculty/changePassword.html', error = error)
            elif loginVOList[0].loginPassword == currentPassword :
                loginVO.loginPassword = newPassword
                loginDAO.updateLogin(loginVO)

                #send Email to password status.
                sender = "studentassistence.donotreply4@gmail.com"
                receiver = session['session_loginUsername']
                msg = MIMEMultipart()

                msg['Form'] = sender
                msg['To'] = receiver
                msg['Subject'] = "Your Password was changed for "

                msg.attach(MIMEText(receiver, 'plain'))

                # smtp mail server setup
                server = smtplib.SMTP('smtp.gmail.com', 587)

                server.starttls()

                # login details for mail server
                server.login(sender, "cjp_@1234")
                text = msg.as_string()

                # send email
                server.sendmail(sender, receiver, text)

                # mail server quit.
                server.quit()

                msg = 'Password has successfully Changed'
                return render_template('faculty/changePassword.html', msg = msg)
            else:
                error = "Your current password has not matched."
                return render_template('faculty/changePassword.html', error= error)
        else:
            return redirect(url_for('facultyLogoutSession'))
    except Exception as ex:
        print(ex)

@app.route('/student/loadDashboard')
def studentLoadDashboard():
    try:
        if studentLoginSession() == 'student':
            print('heeelo')
            return render_template('student/index.html')
        else:
            return redirect(url_for('studentLoadLogin'))
    except Exception as ex:
        print(ex)


@app.route('/admin/loginSession')
def adminLoginSession():
    try:
        if 'session_loginId' and 'session_loginUsername' in session:
            if session['session_loginRole'] == 'admin':
                return 'admin'
            elif session['session_loginRole'] == 'faculty':
                return 'faculty'
            print('<<<<<True>>>>>>')
        else:
            print('<<<<<<<False>>>>>>>')
            return False
    except Exception as ex:
        print(ex)

@app.route('/student/loginSession')
def studentLoginSession():
    try:
        if 'session_studentId' and 'session_studentLogin' in session:
            if session['session_studentLogin'] == 'active':
                return 'student'
            print('<<<<<True>>>>>')
        else:
            print('<<<<<False>>>>>')
            return False
    except Exception as ex:
        print(ex)


@app.route('/admin/logoutSession', methods=['GET'])
def adminLogoutSession():
    try:
        session.clear()
        return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/faculty/logoutSession', methods=['GET'])
def facultyLogoutSession():
    try:
        session.clear()
        return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/student/logoutSession', methods=['GET'])
def studentLogoutSession():
    try:
        session.clear()
        return redirect('/')
    except Exception as ex:
        print(ex)


