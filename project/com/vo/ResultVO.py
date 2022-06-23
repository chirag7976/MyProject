from project import db
from project.com.vo.TestVO import TestVO
from project.com.vo.LoginVO import LoginVO
from project.com.vo.StudentVO import StudentVO

class ResultVO(db.Model):
    __tablename__ = 'resultmaster'
    resultId = db.Column('resultId', db.Integer, primary_key=True, autoincrement=True)
    result_testId = db.Column('result_testId', db.Integer, db.ForeignKey(TestVO.testId), nullable=False)
    result_loginId = db.Column('result_loginId', db.Integer, db.ForeignKey(LoginVO.loginId), nullable=False)
    result_studentId =db.Column('result_studentId', db.Integer, db.ForeignKey(StudentVO.studentId), nullable=False)
    resultDate = db.Column('resultDate', db.String(10), nullable=False)
    resultTime = db.Column('resultTime', db.String(10), nullable=False)
    resultScore = db.Column('resultScore', db.Float)

    def as_dict(self):
        return {
            'resultId' : self.resultId,
            'result_testId' : self.result_testId,
            'result_loginId' : self.result_loginId,
            'result_studentId': self.result_studentId,
            'resultDate' : self.resultDate,
            'resultTime' : self.resultTime,
            'resultScore' : self.resultScore
        }

db.create_all()