from flask import request, render_template, url_for, redirect, session, jsonify
from project import app
from datetime import datetime
# import speech_recognition as sr
from project.com.controller.LoginController import studentLoginSession, adminLoginSession
from project.com.dao.TestDAO import TestDAO
from project.com.vo.TestVO import TestVO
from project.com.vo.QuestionVO import QuestionVO

#facultyViewTest: get List of All tests.
@app.route('/faculty/viewTest', methods=['get'])
def facultyViewTest():
    try:
        if adminLoginSession() == 'faculty':
            print('in faculty viewTest at TestController')
            studentId = request.args.get('studentId')
            print(studentId)
            testVO = TestVO()
            testVO.test_LoginId = studentId
            testDAO = TestDAO()
            if testVO.test_LoginId == None:
                testList = testDAO.viewTestList()
                print(testList)
            else:
                testList = testDAO.viewTestForStudent(testVO)
            return render_template('faculty/viewTest.html', testList=testList)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)



#facultyViewTestDetails: get details about perticular testId
@app.route('/faculty/viewTestDetails', methods=['get'])
def facultyViewTestDetails():
    try:
        if adminLoginSession() == 'faculty':
            print('in faculty viewStudent at TestController')
            testId = request.args.get('testId')
            print(testId)
            testVO = TestVO()
            testDAO = TestDAO()

            testVO.testId = testId

            testVOList = testDAO.viewTest(testVO)

            # testQuestionList =
            print('testVOList', testVOList)

            testQuestionsId = testVOList[0][0].test_QuestionsId
            testQuestionsIdList = testQuestionsId.split(',')

            questionVOList = []
            for i in testQuestionsIdList:
                questionVO = QuestionVO()
                questionVO.questionId = i
                questionVOList += (testDAO.viewTestQuestion(questionVO))


            print('testQuestionsId', testQuestionsId)
            print('testQuestionsIdList', testQuestionsIdList)
            print('testQuestionsList', questionVOList)


            return render_template('faculty/viewTestDetails.html', testVOList=testVOList, questionVOList=questionVOList)
        else:
            return redirect('/')
    except Exception as ex:
        print(ex)


#get List of all pending test for particular studnet
@app.route('/student/viewPendingTest')
def studentViewPendingTest():
    try:
        if studentLoginSession() == 'student':
            testVO = TestVO()
            testDAO = TestDAO()
            testVO.test_LoginId = session['session_stduentId']
            testVO.test_AnswerSeven = 'none'

            testVOList = testDAO.viewPendingTest(testVO)

            return render_template('student/viewPendingTest.html', testVOList = testVOList)
        else:
            return redirect(url_for('studentLoadLogin'))
    except Exception as ex:
        print(ex)

#viewLoadTest will load question seven test
@app.route('/student/viewLoadTest', methods=['get'])
def studentLoadTest():
    try:
        if studentLoginSession() == 'student':
            testId = request.args.get('testId')
            print('testId' , testId)

            testVO = TestVO()
            testDAO = TestDAO()


            testVO.testId = testId

            testVOList = testDAO.viewTest(testVO)

            #get Question Seven
            testQuestionsId = testVOList[0][0].test_QuestionsId
            testQuestionsIdList = testQuestionsId.split(',')

            questionSevenId = testQuestionsIdList.pop()

            questionVO = QuestionVO()
            questionVO.questionId = questionSevenId

            questionVOList = testDAO.viewTestQuestion(questionVO)

            print('viewtest', testVOList, questionVOList)

            return render_template('student/viewLoadTest.html', testVOList = testVOList, questionVOList = questionVOList)
        else:
            return redirect(url_for('studentLoadLogin'))
    except Exception as ex:
        print(ex)

#ajax request: start and handle the recording , 'speech reconigation'
# @app.route("/student/ajaxStartRecording", methods=['GET'])
# def studentAjaxStartRecording():
#     try:
#         if studentLoginSession() == "student":
#             test_AnswerSeven = ''
#             # r = sr.Recognizer()
#             # mic = sr.Microphone()
#             with mic as source:
#                 print("recording", datetime.now().time())
#                 audio = r.record(source, duration=120)
#                 print("Time Over ", datetime.now().time())
#                 try:
#                     answer = r.recognize_google(audio)
#                     test_AnswerSeven = answer
#                     print(test_AnswerSeven)
#                 except Exception as ex:
#                     print('recording Exception', ex)
#
#             print("Answer is -----", test_AnswerSeven)
#             testDAO = TestDAO()
#             testVO = TestVO()
#             print('hefeafflf')
#             testId = request.args.get('testId')
#             print('testID', testId)
#             testVO.testId = testId
#             testVO.test_AnswerSeven = test_AnswerSeven
#             testVO.resultStatus = "pending"
#             testDAO.insertTestData(testVO)
#             answerJson = {'text':test_AnswerSeven}
#             testStatus = {'status':'submitted'}
#             print(answerJson)
#
#             return jsonify(testStatus)
#         else:
#             return None
#     except Exception as ex:
#         print(ex)


#after complate student description test
@app.route("/student/finishTest")
def studentFinishTest():
    try:
        if studentLoginSession() == 'student':
            print('test completed')
            return redirect(url_for('studentViewPendingTest'))
        else:
            print('wrong hit')
            return redirect(url_for('studentLoadLogin'))
    except Exception as ex:
        print(ex)




