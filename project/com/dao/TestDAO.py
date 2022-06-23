from project import db
from project.com.vo.TestVO import TestVO
from project.com.vo.TopicVO import TopicVO
from project.com.vo.StudentVO import StudentVO
from project.com.vo.QuestionVO import QuestionVO


class TestDAO():
    #viewTest: get test details for perticular testId
    def viewTest(self, testVO):
        print('in viewTest at testDAO')
        testVOList = db.session.query(TestVO, TopicVO, StudentVO) \
            .join(TopicVO, TestVO.test_TopicId == TopicVO.topicId) \
            .join(StudentVO, TestVO.test_LoginId == StudentVO.studentId) \
            .filter(TestVO.testId == testVO.testId).all()
        print('testVOList', testVOList)
        return testVOList

    #viewPendingTest: only return pending test for perticular student
    def viewPendingTest(self, testVO):
        print('in testDAO')
        testList = db.session.query(TestVO, TopicVO)\
            .join(TopicVO, TestVO.test_TopicId == TopicVO.topicId)\
            .filter(db.and_(TestVO.test_LoginId == testVO.test_LoginId,
                            TestVO.test_AnswerSeven == testVO.test_AnswerSeven)).all()
        print('testVOList', testList)
        return testList

    #viewTestForStudent
    def viewTestForStudent(self, testVO):
        testList = db.session.query(TestVO, TopicVO, StudentVO) \
            .join(TopicVO, TestVO.test_TopicId == TopicVO.topicId) \
            .join(StudentVO, TestVO.test_LoginId == StudentVO.studentId)\
            .filter(TestVO.test_LoginId == testVO.test_LoginId).all()
        return testList

    #viweTestList: all test list
    def viewTestList(self):
        print('in viewTestList at TestDAO')
        testList = db.session.query(TestVO, TopicVO, StudentVO) \
            .join(TopicVO, TestVO.test_TopicId == TopicVO.topicId) \
            .join(StudentVO, TestVO.test_LoginId == StudentVO.studentId).all()
        return testList

    #insertTestData: insert test data in testmaster
    def insertTestData(self, testVO):
        db.session.merge(testVO)
        db.session.commit()

    #viewTestQuestion: get question for particular questionId
    def viewTestQuestion(self, questionVO):
        print('in viewTestData at TestDAO')
        testQestionVOList = QuestionVO.query.filter_by(questionId=questionVO.questionId)
        return testQestionVOList


    #viewPendingResult
    def viewPendingResult(self, testVO):
        print('viewPendingResults')
        testVOList = db.session.query(TestVO, TopicVO, StudentVO) \
            .join(TopicVO, TestVO.test_TopicId == TopicVO.topicId) \
            .join(StudentVO, TestVO.test_LoginId == StudentVO.studentId)\
            .filter(TestVO.test_ResultStatus == testVO.test_ResultStatus).all()
        print('testVOList at genrteresult')
        return testVOList

