from project import db
from project.com.vo.QuestionTypeVO import QuestionTypeVO
from project.com.vo.QuestionVO import QuestionVO
from project.com.vo.TopicVO import TopicVO


class QuestionDAO:
    def insertQuestion(self, questionVO):
        db.session.add(questionVO)
        db.session.commit()

    def viewQuestion(self):
        questionList = db.session.query(QuestionVO, TopicVO, QuestionTypeVO).join(TopicVO,
                                                                                  QuestionVO.question_TopicId == TopicVO.topicId).join(
            QuestionTypeVO, QuestionVO.question_QuestionTypeId == QuestionTypeVO.questionTypeId).all()
        return questionList

    def deleteQuestion(self, questionId):
        questionList = QuestionVO.query.get(questionId)
        db.session.delete(questionList)
        db.session.commit()

    def editQuestion(self, questionVO):
        questionList = QuestionVO.query.filter_by(questionId=questionVO.questionId)
        print(questionList)
        return questionList

    def updateQuestion(self, questionVO):
        db.session.merge(questionVO)
        db.session.commit()

