from flask import request, render_template, url_for, redirect

from project import app
from project.com.controller.LoginController import adminLoginSession
from project.com.dao.TopicDAO import TopicDAO
from project.com.vo.TopicVO import TopicVO


@app.route('/faculty/loadTopic', methods=['get'])
def facultyLoadTopic():
    try:
        if adminLoginSession() == 'faculty':
            return render_template('faculty/addTopic.html')
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/faculty/insertTopic', methods=['post'])
def facultyInsertTopic():
    try:
        if adminLoginSession() == 'faculty':
            topicName = request.form['topicName']
            topicDescription = request.form['topicDescription']

            topicVO = TopicVO()
            topicDAO = TopicDAO()

            topicVO.topicName = topicName
            topicVO.topicDescription = topicDescription

            topicDAO.insertTopic(topicVO)

            return redirect(url_for('facultyViewTopic'))
        else:
            return redirect('/')
    except Exception  as ex:
        print(ex)


@app.route('/faculty/viewTopic', methods=['GET'])
def facultyViewTopic():
    try:
        if adminLoginSession() == 'faculty':
            topicDAO = TopicDAO()
            topicVOList = topicDAO.viewTopic()
            return render_template('faculty/viewTopic.html', topicVOList=topicVOList)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/faculty/deleteTopic', methods=['GET'])
def facultyDeleteTopic():
    try:
        if adminLoginSession() == 'faculty':
            topicVO = TopicVO()
            topicDAO = TopicDAO()

            topicId = request.args.get('topicId')

            topicVO.topicId = topicId

            topicDAO.deleteTopic(topicVO)

            return redirect(url_for('facultyViewTopic'))
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/faculty/editTopic', methods=['GET'])
def facultyEditTopic():
    try:
        if adminLoginSession() == 'faculty':
            topicVO = TopicVO()
            topicDAO = TopicDAO()

            topicId = request.args.get('topicId')

            topicVO.topicId = topicId

            topicVOList = topicDAO.editTopic(topicVO)

            return render_template('faculty/editTopic.html', topicVOList=topicVOList)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/faculty/updateTopic', methods=['POST'])
def facultyUpdateTopic():
    try:
        if adminLoginSession() == 'faculty':
            topicId = request.form['topicId']
            topicName = request.form['topicName']
            topicDescription = request.form['topicDescription']

            topicVO = TopicVO()
            topicDAO = TopicDAO()

            topicVO.topicId = topicId
            topicVO.topicName = topicName
            topicVO.topicDescription = topicDescription

            topicDAO.updateTopic(topicVO)

            return redirect(url_for('facultyViewTopic'))
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)
