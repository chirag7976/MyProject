# complainController for all complain Url Patterns

import os
from datetime import datetime

from flask import redirect, render_template, request, url_for, session
from werkzeug.utils import secure_filename

from project import app
from project.com.controller.LoginController import adminLoginSession
from project.com.dao.ComplainDAO import ComplainDAO
from project.com.vo.ComplainVO import ComplainVO

# upload foldder location and config
UPLOAD_FOLDER = 'project/static/facultyResources/complainAttachement/'
REPLY_UPLOAD_FOLDER = 'project/static/facultyResources/replyAttachment/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['REPLY_UPLOAD_FOLDER'] = REPLY_UPLOAD_FOLDER


# admin viewComplain URL pattern
@app.route('/admin/viewComplain', methods=['GET'])
def adminViewComplain():
    try:
        if adminLoginSession() == 'admin':
            complainDAO = ComplainDAO()
            complainVOList = complainDAO.viewComplain()
            return render_template('admin/viewComplain.html', complainVOList=complainVOList)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


# admin: load complain reply form
@app.route('/admin/loadComplainReply', methods=['GET'])
def adminLoadComplainReply():
    try:
        if adminLoginSession() == 'admin':
            # get complainId from url
            complainId = request.args.get('complainId')

            return render_template('admin/addComplainReply.html', complainId=complainId)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


# admin: submit complain reply form
@app.route('/admin/insertComplainReply', methods=['POST'])
def adminInsertComplainReply():
    try:
        if adminLoginSession() == 'admin':
            complainVO = ComplainVO()
            complainDAO = ComplainDAO()

            complainId = request.form['complainId']
            complainStatus = 'replied'
            complainTo_LoginId = session['session_loginId']
            replySubject = request.form['replySubject']
            replyMessage = request.form['replyMessage']
            replyDate = datetime.now().strftime('%d/%m/%Y')
            replyTime = datetime.now().strftime('%H:%M')

            replyFile = request.files['replyFile']

            # complain attachment file name
            replyFileName = secure_filename(replyFile.filename)

            # file path
            replyFilePath = os.path.join(app.config['REPLY_UPLOAD_FOLDER'])

            # save file at location
            replyFile.save(os.path.join(replyFilePath, replyFileName))

            complainVO.complainId = complainId
            complainVO.complainStatus = complainStatus
            complainVO.replySubject = replySubject
            complainVO.replyMessage = replyMessage
            complainVO.replyDate = replyDate
            complainVO.replyTime = replyTime
            # store filename and filepath in complainVO
            complainVO.replyFileName = replyFileName
            complainVO.replyFilePath = replyFilePath.replace("project", "..")
            complainVO.complainTo_LoginId = complainTo_LoginId

            complainDAO.insertComplainReply(complainVO)

            return redirect(url_for('adminViewComplain'))
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


# admin: view complain replys
@app.route('/admin/viewComplainReply', methods=['GET'])
def adminViewComplainReply():
    try:
        if adminLoginSession() == 'admin':
            complainId = request.args.get('complainId')

            complainVO = ComplainVO()
            complainDAO = ComplainDAO()

            complainVO.complainId = complainId

            complainReplyVOList = complainDAO.viewComplainReply(complainVO)

            return render_template('admin/viewComplainReply.html', complainReplyVOList=complainReplyVOList)

        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


# faculty url patterns

# faculty: load addComplain form
@app.route('/faculty/loadComplain', methods=['GET'])
def facultyLoadComplain():
    try:
        if adminLoginSession() == 'faculty':
            return render_template('faculty/addComplain.html')
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


# faculty: submit addcomplain form
@app.route('/faculty/insertComplain', methods=['POST'])
def facultyInsertComplain():
    try:
        if adminLoginSession() == 'faculty':

            complainVO = ComplainVO()
            complainDAO = ComplainDAO()

            complainSubject = request.form['complainSubject']
            complainDescription = request.form['complainDescription']
            complainDate = datetime.now().strftime('%d/%m/%Y')
            complainTime = datetime.now().strftime('%H:%M')
            complainStatus = 'pending'

            complainFrom_LoginId = session['session_loginId']

            # request file from user
            complainFile = request.files['complainFile']

            # complain attachment file name
            complainFileName = secure_filename(complainFile.filename)

            # file path
            complainFilePath = os.path.join(app.config['UPLOAD_FOLDER'])

            # save file at location
            complainFile.save(os.path.join(complainFilePath, complainFileName))

            # store filename and filepath in complainVO
            complainVO.complainFileName = complainFileName
            complainVO.complainFilePath = complainFilePath.replace("project", "..")

            complainVO.complainSubject = complainSubject
            complainVO.complainDescription = complainDescription
            complainVO.complainDate = complainDate
            complainVO.complainTime = complainTime

            complainVO.complainStatus = complainStatus
            complainVO.complainFrom_LoginId = complainFrom_LoginId

            # insert data in "complainmaster" table by "complainVO" object
            complainDAO.insertComplain(complainVO)

            return redirect(url_for('facultyViewComplain'))
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/faculty/viewComplain', methods=['GET'])
def facultyViewComplain():
    try:
        if adminLoginSession() == 'faculty':

            complainFrom_LoginId = session['session_loginId']
            complainVO = ComplainVO()
            complainDAO = ComplainDAO()
            complainVO.complainFrom_LoginId = complainFrom_LoginId
            complainVOList = complainDAO.viewComplainFaculty(complainVO)

            return render_template('faculty/viewComplain.html', complainVOList=complainVOList)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/faculty/deleteComplain', methods=['GET'])
def facultyDeleteComplain():
    try:
        if adminLoginSession() == 'faculty':

            complainVO = ComplainVO()
            complainDAO = ComplainDAO()

            complainVO.complainId = request.args.get('complainId')

            complainList = complainDAO.deleteComplain(complainVO)

            path = complainList.complainFilePath.replace('..', 'project') + complainList.complainFileName

            os.remove(path)

            if complainList.complainStatus == 'replied':
                complainReplyFilePath = complainList.replyFilePath.replace('..', 'project') + complainList.replyFileName
                # delete admin ComplainReply File
                os.remove(complainReplyFilePath)

            return redirect(url_for('facultyViewComplain'))
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/faculty/viewComplainReply', methods=['GET'])
def facultyViewComplainReply():
    try:
        if adminLoginSession() == 'faculty':
            complainId = request.args.get('complainId')

            complainVO = ComplainVO()
            complainDAO = ComplainDAO()

            complainVO.complainId = complainId

            complainReplyVOList = complainDAO.viewComplainReply(complainVO)

            return render_template('faculty/viewComplainReply.html', complainReplyVOList=complainReplyVOList)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)
