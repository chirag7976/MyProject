from flask import request, render_template, url_for, redirect
from project import app
from project.com.controller.LoginController import adminLoginSession
from project.com.dao.QuestionDAO import QuestionDAO
from project.com.dao.QuestionTypeDAO import QuestionTypeDAO
from project.com.dao.TopicDAO import TopicDAO
from project.com.vo.QuestionVO import QuestionVO


@app.route('/faculty/loadQuestion', methods=['GET'])
def facultyLoadQuestion():
    try:
        if adminLoginSession() == 'faculty':
            topicDAO = TopicDAO()
            topicVOList = topicDAO.viewTopic()

            questionTypeDAO = QuestionTypeDAO()
            questionTypeVOList = questionTypeDAO.viewQuestionType()

            return render_template('faculty/addQuestion.html', topicVOList=topicVOList,
                                   questionTypeVOList=questionTypeVOList)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/faculty/insertQuestion', methods=['POST'])
def facultyInsertQuestion():
    try:
        if adminLoginSession() == 'faculty':
            # get values from html form
            question = request.form['question']
            keyword = request.form['keyword']
            question_TopicId = request.form['question_TopicId']
            question_QuestionTypeId = request.form['question_QuestionTypeId']

            # QuestionVO and QuestionDAO objects created
            questionVO = QuestionVO()
            questionDAO = QuestionDAO()

            print('keyword', keyword)

            # pass value to VO by questionVO object
            questionVO.question = question
            questionVO.keyword = keyword
            questionVO.question_TopicId = question_TopicId
            questionVO.question_QuestionTypeId = question_QuestionTypeId

            # run query by questionDAO object
            questionDAO.insertQuestion(questionVO)

            return redirect(url_for('facultyViewQuestion'))
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/faculty/viewQuestion', methods=['GET'])
def facultyViewQuestion():
    try:
        if adminLoginSession() == 'faculty':
            questionDAO = QuestionDAO()
            questionVOList = questionDAO.viewQuestion()

            return render_template('faculty/viewQuestion.html', questionVOList=questionVOList)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/faculty/deleteQuestion', methods=['GET'])
def facultyDeleteQuestion():
    try:
        if adminLoginSession() == 'faculty':
            questionDAO = QuestionDAO()

            questionId = request.args.get('questionId')

            questionDAO.deleteQuestion(questionId)

            return redirect(url_for('facultyViewQuestion'))
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/faculty/editQuestion', methods=['GET'])
def facultyEditQuestion():
    try:
        if adminLoginSession() == 'faculty':
            questionVO = QuestionVO()
            questionDAO = QuestionDAO()

            topicDAO = TopicDAO()
            questionTypeDAO = QuestionTypeDAO()

            questionId = request.args.get('questionId')

            questionVO.questionId = questionId

            questionVOList = questionDAO.editQuestion(questionVO)

            topicVOList = topicDAO.viewTopic()

            questionTypeVOList = questionTypeDAO.viewQuestionType()

            return render_template('faculty/editQuestion.html', topicVOList=topicVOList, questionVOList=questionVOList,
                                   questionTypeVOList=questionTypeVOList)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/faculty/updateQuestion', methods=['POST'])
def facultyUpdateQuestion():
    try:
        if adminLoginSession() == 'faculty':
            question = request.form['question']
            keyword = request.form['keyword']
            question_TopicId = request.form['question_TopicId']
            question_QuestionTypeId = request.form['question_QuestionTypeId']
            questionId = request.form['questionId']

            questionVO = QuestionVO()
            questionDAO = QuestionDAO()

            questionVO.questionId = questionId
            questionVO.question = question
            questionVO.keywords = keyword
            print('keyword', keyword)
            questionVO.question_TopicId = question_TopicId
            questionVO.question_QuestionTypeId = question_QuestionTypeId

            questionDAO.updateQuestion(questionVO)

            return redirect(url_for('facultyViewQuestion'))
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)
