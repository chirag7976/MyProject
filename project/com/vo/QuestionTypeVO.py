from project import db


class QuestionTypeVO(db.Model):
    __tablename__ = 'questiontypemaster'
    questionTypeId = db.Column('questionTypeId', db.Integer, primary_key=True, autoincrement=True)
    questionTypeName = db.Column('questionTypeName', db.String(50), nullable=False)
    questionTypeDescription = db.Column('questionTypeDescription', db.String(200), nullable=False)

    def as_dict(self):
        return {
            'questionTypeId': self.questionTypeId,
            'questionTypeName': self.questionTypeName,
            'questionTypeDescription': self.questionTypeDescription
        }


db.create_all()
