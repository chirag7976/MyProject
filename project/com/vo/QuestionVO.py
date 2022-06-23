from project import db
from project.com.vo.QuestionTypeVO import QuestionTypeVO
from project.com.vo.TopicVO import TopicVO


class QuestionVO(db.Model):
    __tablename__ = 'questionmaster'
    questionId = db.Column('questionId', db.Integer, primary_key=True, autoincrement=True)
    question = db.Column('question', db.String(300), nullable=False)
    keyword = db.Column('keyword', db.String(4000), nullable=False)
    question_TopicId = db.Column('question_TopicId', db.Integer, db.ForeignKey(TopicVO.topicId), nullable=False)
    question_QuestionTypeId = db.Column('question_QuestionTypeId', db.Integer,
                                        db.ForeignKey(QuestionTypeVO.questionTypeId), nullable=False)

    def as_dict(self):
        return {
            'questionId': self.questionId,
            'question': self.question,
            'keyword': self.keyword,
            'question_TopicId': self.question_TopicId,
            'question_QuestionTypeId': self.question_QuestionTypeId
        }


db.create_all()
