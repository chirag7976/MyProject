import random
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import request, render_template, session, redirect, url_for

from project import app
from project.com.dao.LoginDAO import LoginDAO
from project.com.dao.RegisterDAO import RegisterDAO
from project.com.vo.LoginVO import LoginVO
from project.com.vo.RegisterVO import RegisterVO


@app.route('/faculty/loadRegister', methods=['GET'])
def adminLoadRegister():
    try:
        return render_template('faculty/register.html')
    except Exception as ex:
        print(ex)


@app.route('/faculty/insertRegister', methods=['POST'])
def facultyInsertRegister():
    try:
        loginUsername = request.form['loginUsername']
        registerFirstName = request.form['registerFirstName']
        registerLastName = request.form['registerLastName']
        registerGender = request.form['gender']
        registerContactNumber = request.form['registerContactNumber']

        loginVO = LoginVO()
        loginDAO = LoginDAO()

        registerVO = RegisterVO()
        registerDAO = RegisterDAO()

        loginPassword = ''.join((random.choice(string.ascii_letters + string.digits)) for i in range(8))

        # Email Account Setup


        sender = "studentassistence.donotreply4@gmail.com"
        receiver = loginUsername
        msg = MIMEMultipart()

        msg['Form'] = sender
        msg['To'] = receiver
        msg['Subject'] = "Python Password"

        msg.attach(MIMEText(loginPassword, 'plain'))

        # smtp mail server setup
        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()

        # login details for mail server
        server.login(sender, "cjp_@1234")
        text = msg.as_string()

        # send email
        server.sendmail(sender, receiver, text)

        # push login deatils in "loginmaster" table
        loginVO.loginUsername = loginUsername
        loginVO.loginPassword = loginPassword
        loginVO.loginRole = "faculty"
        loginVO.loginStatus = "active"
        loginDAO.insertLogin(loginVO)

        # push details in "registermaster" table
        registerVO.registerFirstName = registerFirstName
        registerVO.registerLastName = registerLastName
        registerVO.registerGender = registerGender
        registerVO.registerContactNumber = registerContactNumber
        registerVO.register_LoginId = loginVO.loginId

        registerDAO.insertRegister(registerVO)

        # mail server quit.
        server.quit()
        message = 'You are succesfully regsted!  Please check Email for password'
        return render_template("admin/login.html", msg=message)
    except Exception as ex:
        print(ex)


# forgot Passwords


@app.route('/faculty/loadForgotPassword', methods=['GET'])
def facultyLoadForgotPassword():
    try:
        return render_template('faculty/forgotPassword.html')
    except Exception as ex:
        print(ex)


@app.route('/faculty/forgotPassword', methods=['POST'])
def facultyForgotPassword():
    try:
        forgotEmail = request.form['forgotEmail']

        loginVO = LoginVO()
        loginDAO = LoginDAO()

        loginVO.loginUsername = forgotEmail

        loginList = loginDAO.forgotLogin(loginVO)

        if len(loginList) == 0:
            message = "You not registered with this email id."
            return render_template('faculty/forgotPassword.html', error=message)
        else:
            OTP = ''.join((random.choice(string.digits)) for i in range(4))
            # OTP = '3456'
            print(OTP)

            sender = "studentassistence.donotreply4@gmail.com"
            receiver = loginList[0].loginUsername
            msg = MIMEMultipart()

            msg['Form'] = sender
            msg['To'] = receiver
            msg['Subject'] = "Enter OTP for Forgot Password : "

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

            # store forgotOTP in session
            session['session_forgotPasswordOTP'] = OTP
            session['session_forgotEmail'] = forgotEmail

            message = "Details sent! Enjoy."

            return render_template('faculty/forgotPasswordOTP.html', msg=message)
    except Exception as ex:
        print(ex)


@app.route('/faculty/validateForgotPasswordOTP', methods=['post'])
def facultyForgotPasswordOTP():
    try:
        forgotOTP = request.form['forgotOTP']

        if session['session_forgotPasswordOTP'] == forgotOTP:

            forgotEmail = session['session_forgotEmail']

            loginVO = LoginVO()
            loginDAO = LoginDAO()

            loginVO.loginUsername = forgotEmail

            loginList = loginDAO.forgotLogin(loginVO)
            print('dsafsags',loginList)

            # Email Account Setup
            sender = "studentassistence.donotreply4@gmail.com"
            receiver = loginList[0].loginUsername
            msg = MIMEMultipart()

            msg['Form'] = sender
            msg['To'] = receiver
            msg['Subject'] = "Python Forgot Password"

            msg.attach(MIMEText(loginList[0].loginPassword, 'plain'))

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

            message = "Details sent! Login agin. Enjoy. "

            return render_template('faculty/forgotPassword.html', msg=message)
        else:

            return redirect(url_for('facultyForgotPassword'))

    except Exception as ex:
        print(ex)

