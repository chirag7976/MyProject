from datetime import datetime

from flask import render_template, redirect, url_for, session, request

from project import app
from project.com.controller.LoginController import adminLoginSession
from project.com.dao.FeedbackDAO import FeedbackDAO
from project.com.vo.FeedbackVO import FeedbackVO


# admin url patterns
@app.route('/admin/viewFeedback', methods=['GET'])
def adminViewFeedback():
    try:
        if adminLoginSession() == 'admin':
            feedbackDAO = FeedbackDAO()
            feedbackVOList = feedbackDAO.viewFeedback()
            return render_template('admin/viewFeedback.html', feedbackVOList=feedbackVOList)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/admin/deleteFeedback', methods=['GET'])
def adminDeleteFeedback():
    try:
        if adminLoginSession() == 'admin':
            feedbackVO = FeedbackVO()
            feedbackDAO = FeedbackDAO()

            feedbackVO.feedbackId = request.args.get('feedbackId')

            feedbackDAO.deleteFeedback(feedbackVO)

            return redirect(url_for('facultyViewFeedback'))
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/admin/reviewedFeedback', methods=['GET'])
def adminReviewedFeedback():
    try:
        if adminLoginSession() == 'admin':
            feedbackId = request.args.get('feedbackId')

            feedbackVO = FeedbackVO()
            feedbackDAO = FeedbackDAO()

            feedbackVO.feedbackId = feedbackId

            feedbackVO.feedbackTo_LoginId = session['session_loginId']
            feedbackDAO.changeFeedbackStatus(feedbackVO)

            return redirect(url_for('adminViewFeedback'))

        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


# faculty url patterns
@app.route('/faculty/loadFeedback', methods=['GET'])
def facultyLoadFeedback():
    try:
        if adminLoginSession() == 'faculty':
            return render_template('faculty/addFeedback.html')
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/faculty/insertFeedback', methods=['POST'])
def facultyInsertFeedback():
    try:
        if adminLoginSession() == 'faculty':
            feedbackVO = FeedbackVO()
            feedbackDAO = FeedbackDAO()

            feedbackVO.feedbackSubject = request.form['feedbackSubject']
            feedbackVO.feedbackDescription = request.form['feedbackDescription']
            feedbackVO.feedbackRating = request.form['feedbackRating']
            feedbackVO.feedbackDate = datetime.now().strftime('%d/%m/%Y')
            feedbackVO.feedbackTime = datetime.now().strftime('%H:%M')
            feedbackVO.feedbackFrom_LoginId = session['session_loginId']
            feedbackVO.feedbackStatus = 'pending'

            feedbackDAO.insertFeedback(feedbackVO)
            return redirect(url_for('facultyViewFeedback'))
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/faculty/viewFeedback', methods=['GET'])
def facultyViewFeedback():
    try:
        if adminLoginSession() == 'faculty':
            feedbackFrom_LoginId = session['session_loginId']

            feedbackVO = FeedbackVO()
            feedbackDAO = FeedbackDAO()

            feedbackVO.feedbackFrom_LoginId = feedbackFrom_LoginId

            feedbackVOList = feedbackDAO.viewFeedbackFaculty(feedbackVO)

            return render_template('faculty/viewFeedback.html', feedbackVOList=feedbackVOList)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


@app.route('/faculty/deleteFeedback', methods=['GET'])
def facultyDeleteFeedback():
    try:
        if adminLoginSession() == 'faculty':
            feedbackVO = FeedbackVO()
            feedbackDAO = FeedbackDAO()

            feedbackVO.feedbackId = request.args.get('feedbackId')

            feedbackDAO.deleteFeedback(feedbackVO)
            return redirect(url_for('facultyViewFeedback'))
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)
