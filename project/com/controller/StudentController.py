from flask import request, render_template, url_for, redirect

from project import app
from project.com.controller.LoginController import adminLoginSession
from project.com.dao.StudentDAO import StudentDAO
from project.com.vo.StudentVO import StudentVO





@app.route('/faculty/loadStudent', methods=['get'])
def facultyLoadStudent():
    try:
        if adminLoginSession() == 'faculty':
            return render_template('faculty/addStudent.html')
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/faculty/insertStudent', methods=['post'])
def facultyInsertStudent():
    try:
        if adminLoginSession() == 'faculty':
            studentFirstName = request.form['studentFirstName']
            studentLastName = request.form['studentLastName']
            studentEmail = request.form['studentEmail']
            studentGender = request.form['studentGender']
            studentContactNumber = request.form['studentContactNumber']

            studentVO = StudentVO()
            studentDAO = StudentDAO()

            studentVO.studentFirstName = studentFirstName
            studentVO.studentLastName = studentLastName
            studentVO.studentEmail = studentEmail
            studentVO.studentGender = studentGender
            studentVO.studentContactNumber = studentContactNumber
            studentVO.studentStatus = 'active'

            studentDAO.insertStudent(studentVO)

            return redirect(url_for('facultyViewStudent'))
        else:
            return redirect('/')
    except Exception  as ex:
        print(ex)


@app.route('/faculty/viewStudent', methods=['GET'])
def facultyViewStudent():
    try:
        if adminLoginSession() == 'faculty':
            studentDAO = StudentDAO()
            studentVOList = studentDAO.viewStudent()
            return render_template('faculty/viewStudent.html', studentVOList=studentVOList)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/faculty/blockStudent', methods=['GET'])
def facultyBlockStudent():
    try:
        if adminLoginSession() == 'faculty':
            studentVO = StudentVO()
            studentDAO = StudentDAO()

            studentId = request.args.get('studentId')

            studentVO.studentId = studentId
            studentVO.studentStatus = 'inactive'

            studentDAO.updateStudent(studentVO)

            return redirect(url_for('facultyViewStudent'))
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)

@app.route('/faculty/unblockStudent', methods=['GET'])
def facultyUnblockStudent():
    try:
        if adminLoginSession() == 'faculty':
            studentVO = StudentVO()
            studentDAO = StudentDAO()

            studentId = request.args.get('studentId')

            studentVO.studentId = studentId
            studentVO.studentStatus = 'active'

            studentDAO.updateStudent(studentVO)

            return redirect(url_for('facultyViewStudent'))
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/faculty/editStudent', methods=['GET'])
def facultyEditStudent():
    try:
        if adminLoginSession() == 'faculty':
            studentVO = StudentVO()
            studentDAO = StudentDAO()

            studentId = request.args.get('studentId')

            studentVO.studentId = studentId

            studentVOList = studentDAO.editStudent(studentVO)

            return render_template('faculty/editStudent.html', studentVOList=studentVOList)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/faculty/updateStudent', methods=['POST'])
def facultyUpdateStudent():
    try:
        if adminLoginSession() == 'faculty':
            studentId = request.form['studentId']
            studentFirstName = request.form['studentFirstName']
            studentLastName = request.form['studentLastName']
            studentGender = request.form['studentGender']
            studentEmail = request.form['studentEmail']
            studentContactNumber = request.form['studentContactNumber']

            studentVO = StudentVO()
            studentDAO = StudentDAO()

            studentVO.studentId = studentId
            studentVO.studentFirstName = studentFirstName
            studentVO.studentLastName = studentLastName
            studentVO.studentGender = studentGender
            studentVO.studetnEmail = studentEmail
            studentVO.studentContactNumber = studentContactNumber

            studentDAO.updateStudent(studentVO)

            return redirect(url_for('facultyViewStudent'))
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)
