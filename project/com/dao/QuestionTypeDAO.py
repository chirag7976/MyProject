from project import db
from project.com.vo.QuestionTypeVO import QuestionTypeVO


class QuestionTypeDAO:
    def insertQuestionType(self, questionTypeVO):
        db.session.add(questionTypeVO)
        db.session.commit()

    def viewQuestionType(self):
        typeList = db.session.query(QuestionTypeVO).all()

        return typeList

    def deleteQuestionType(self, questionTypeVO):
        typeList = QuestionTypeVO.query.get(questionTypeVO.questionTypeId)
        db.session.delete(typeList)
        db.session.commit()

    def editQuestionType(self, questionTypeVO):
        typeList = QuestionTypeVO.query.filter_by(questionTypeId=questionTypeVO.questionTypeId).all()
        return typeList

    def updateQuestionType(self, questionTypeVO):
        db.session.merge(questionTypeVO)
        db.session.commit()
