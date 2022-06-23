from flask import request, render_template, url_for, redirect, session

from project import app
from project.com.controller.LoginController import adminLoginSession
from project.com.dao.QuestionTypeDAO import QuestionTypeDAO
from project.com.vo.QuestionTypeVO import QuestionTypeVO


@app.route('/admin/loadQuestionType', methods=['get'])
def adminLoadQuestionType():
    try:
        if adminLoginSession() == 'admin':
            return render_template('admin/addQuestionType.html')
        else:
            return redirect(url_for('adminLoadLogin'))
    except Exception as ex:
        print(ex)


@app.route('/admin/insertQuestionType', methods=['post'])
def adminInsertQuestionType():
    try:
        if adminLoginSession() == 'admin':
            questionTypeName = request.form['questionTypeName']
            questionTypeDescription = request.form['questionTypeDescription']

            questionTypeVO = QuestionTypeVO()
            questionTypeDAO = QuestionTypeDAO()

            questionTypeVO.questionTypeName = questionTypeName
            questionTypeVO.questionTypeDescription = questionTypeDescription

            questionTypeDAO.insertQuestionType(questionTypeVO)

            return redirect(url_for('adminViewQuestionType'))

        else:
            return redirect('/')

    except Exception  as ex:
        print(ex)


@app.route('/admin/viewQuestionType', methods=['GET'])
def adminViewQuestionType():
    try:
        if adminLoginSession() == 'admin':
            questionTypeDAO = QuestionTypeDAO()
            questionTypeVOList = questionTypeDAO.viewQuestionType()

            return render_template('admin/viewQuestionType.html', questionTypeVOList=questionTypeVOList)

        else:
            return redirect('/')

    except Exception as ex:
        print(ex)


@app.route('/admin/deleteQuestionType', methods=['GET'])
def adminDeleteQuestionType():
    try:
        if adminLoginSession() == 'admin':
            questionTypeVO = QuestionTypeVO()
            questionTypeDAO = QuestionTypeDAO()

            questionTypeId = request.args.get('questionTypeId')

            questionTypeVO.questionTypeId = questionTypeId

            # delete questionType by its object
            questionTypeDAO.deleteQuestionType(questionTypeVO)

            return redirect(url_for('adminViewQuestionType'))
        else:
            return redirect('/')

    except Exception as ex:
        print(ex)


@app.route('/admin/editQuestionType', methods=['GET'])
def adminEditQuestionType():
    try:
        if session['session_loginRole'] == 'admin':
            questionTypeVO = QuestionTypeVO()
            questionTypeDAO = QuestionTypeDAO()

            questionTypeId = request.args.get('questionTypeId')

            questionTypeVO.questionTypeId = questionTypeId
            questionTypeVOList = questionTypeDAO.editQuestionType(questionTypeVO)

            return render_template('admin/editQuestionType.html', questionTypeVOList=questionTypeVOList)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/admin/updateQuestionType', methods=['POST'])
def adminUpdateQuestionType():
    try:
        if adminLoginSession() == 'admin':
            questionTypeId = request.form['questionTypeId']
            questionTypeName = request.form['questionTypeName']
            questionTypeDescription = request.form['questionTypeDescription']

            questionTypeVO = QuestionTypeVO()
            questionTypeDAO = QuestionTypeDAO()

            questionTypeVO.questionTypeId = questionTypeId
            questionTypeVO.questionTypeName = questionTypeName
            questionTypeVO.questionTypeDescription = questionTypeDescription

            questionTypeDAO.updateQuestionType(questionTypeVO)

            return redirect(url_for('adminViewQuestionType'))
        else:
            return redirect('/')

    except Exception as ex:
        print(ex)
