from project import db
from project.com.vo.TopicVO import TopicVO
from project.com.vo.StudentVO import StudentVO


class TestVO(db.Model):
    __tablename__ = 'testmaster'
    testId = db.Column('testId', db.Integer, primary_key=True, autoincrement=True)
    test_TopicId = db.Column(db.Integer, db.ForeignKey(TopicVO.topicId))
    test_LoginId = db.Column(db.Integer, db.ForeignKey(StudentVO.studentId))
    test_AnswerOne = db.Column(db.String(100))
    test_AnswerTwo = db.Column(db.String(100))
    test_AnswerThree = db.Column(db.String(100))
    test_AnswerFour = db.Column(db.String(100))
    test_AnswerFive = db.Column(db.String(100))
    test_AnswerSix = db.Column(db.String(100))
    test_AnswerSeven = db.Column(db.String(5000))
    test_QuestionsId = db.Column(db.String(100))
    test_Time = db.Column(db.String(20))
    test_Date = db.Column(db.String(20))
    test_ResultStatus = db.Column(db.String(20))
    
    def as_dict(self):
        return {
            'topicId': self.topicId,
            'test_TopicId': self.test_TopicId,
            'test_LoginId': self.test_LoginId,
            'test_AnswerOne': self.test_AnswerOne,
            'test_AnswerTwo': self.test_AnswerTwo,
            'test_AnswerThree': self.test_AnswerThree,
            'test_AnswerFour': self.test_AnswerFour,
            'test_AnswerFive': self.test_AnswerFive,
            'test_AnswerSix': self.test_AnswerSix,
            'test_AnswerSeven': self.test_AnswerSeven,
            'test_QuestionsId': self.test_QuestionsId,
            'test_Time': self.test_Time,
            'test_Date': self.test_Date,
            'test_ResultStatus':self.test_ReportStatus
        }


db.create_all()
