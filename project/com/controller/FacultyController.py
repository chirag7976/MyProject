from flask import request, render_template, redirect, url_for, session

from project import app
from project.com.controller.LoginController import adminLoginSession
from project.com.dao.FacultyDAO import FacultyDAO
from project.com.vo.LoginVO import LoginVO
from project.com.vo.RegisterVO import RegisterVO


@app.route('/admin/viewFaculty', methods=['GET'])
def adminViewFaculty():
    try:
        if adminLoginSession() == 'admin':
            facultyDAO = FacultyDAO()
            facultyVOList = facultyDAO.viewFaculty()
            return render_template('admin/viewFaculty.html', facultyVOList=facultyVOList)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/admin/blockFaculty', methods=['GET'])
def adminBlockFaculty():
    try:
        if adminLoginSession() == 'admin':
            loginId = request.args.get('loginId')
            loginStatus = 'inactive'

            loginVO = LoginVO()
            facultyDAO = FacultyDAO()

            loginVO.loginId = loginId
            loginVO.loginStatus = loginStatus

            facultyDAO.changeStatusFaculty(loginVO)
            return redirect(url_for('adminViewFaculty'))
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/admin/unblockFaculty', methods=['GET'])
def adminUnblockFaculty():
    try:
        if adminLoginSession() == 'admin':
            loginId = request.args.get('loginId')
            loginStatus = 'active'

            loginVO = LoginVO()
            facultyDAO = FacultyDAO()

            loginVO.loginId = loginId
            loginVO.loginStatus = loginStatus

            facultyDAO.changeStatusFaculty(loginVO)
            return redirect(url_for('adminViewFaculty'))

        else:
            return redirect('/')
    except Exception as ex:
        print(ex)

#facultyViewProfile: view Faculty prfile details page
@app.route('/faculty/viewProfile', methods=['get'])
def facultyViewProfile():
    try:
        if adminLoginSession() == 'faculty':
            return render_template('faculty/viewProfile.html')
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


#facultyEditProfile: edit profile details by faculty
@app.route('/faculty/editProfile', methods=['get'])
def facultyEditProfile():
    try:
        if adminLoginSession() == 'faculty':
            return render_template('faculty/editProfile.html')
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)

@app.route('/faculty/updateProfile', methods=['POST'])
def facultyUpdateProfile():
    try:
        if adminLoginSession() == 'faculty':
            registerId = request.form['registerId']
            print('dsafa', registerId)
            loginFirstName = request.form['loginFirstName']
            loginLastName = request.form['loginLastName']
            loginGender = request.form['loginGender']
            loginContactNumber = request.form['loginContactNumber']

            registerVO = RegisterVO()
            registerVO.registerId = registerId
            registerVO.registerFirstName = loginFirstName
            registerVO.registerLastName = loginLastName
            registerVO.registerGender = loginGender
            registerVO.registerContactNumber =loginContactNumber

            facultyDAO = FacultyDAO()
            facultyDAO.changeStatusFaculty(registerVO)

            session['session_registerId'] = registerId
            session['session_FirstName'] = loginFirstName
            session['session_LastName'] = loginLastName
            session['session_loginGender'] = loginGender
            session['session_loginContactNumber'] = loginContactNumber

            return redirect(url_for('facultyViewProfile'))
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)