from project import db


class TopicVO(db.Model):
    __tablename__ = 'topicmaster'
    topicId = db.Column('topicId', db.Integer, primary_key=True, autoincrement=True)
    topicName = db.Column('topicName', db.String(50), nullable=False)
    topicDescription = db.Column('topicDescription', db.String(500), nullable=False)

    def as_dict(self):
        return {
            'topicId': self.topicId,
            'topicName': self.topicName,
            'topicDescription': self.topicDescription
        }


db.create_all()
