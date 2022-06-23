from project import db
from project.com.vo.ResultVO import ResultVO
from project.com.vo.TestVO import TestVO
from project.com.vo.TopicVO import TopicVO
from project.com.vo.StudentVO import StudentVO


class ResultDAO():
    def viewResult(self):
        resultList = db.session.query(ResultVO, TestVO, StudentVO, TopicVO)\
            .join(TestVO, ResultVO.result_testId == TestVO.testId)\
            .join(StudentVO, TestVO.test_LoginId == StudentVO.studentId)\
            .join(TopicVO, TestVO.test_TopicId == TopicVO.topicId).all()
        return resultList

    def insertResult(self, resultVO):
        db.session.add(resultVO)
        db.session.commit()

    def viewStudentResutl(self, resultVO):
        resultList = db.session.query(ResultVO, TestVO, StudentVO, TopicVO)\
            .join(TestVO, ResultVO.result_testId == TestVO.testId)\
            .join(StudentVO, TestVO.test_LoginId == StudentVO.studentId)\
            .join(TopicVO, TestVO.test_TopicId == TopicVO.topicId)\
            .filter(ResultVO.result_studentId == resultVO.result_studentId).all()
        return resultList
