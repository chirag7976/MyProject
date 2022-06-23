from project import db
from project.com.vo.TopicVO import TopicVO


class TopicDAO:
    def insertTopic(self, topicVO):
        db.session.add(topicVO)
        db.session.commit()

    def viewTopic(self):
        topicList = TopicVO.query.all()

        return topicList

    def deleteTopic(self, topicVO):
        topicList = TopicVO.query.get(topicVO.topicId)
        db.session.delete(topicList)
        db.session.commit()

    def editTopic(self, topicVO):
        topicList = TopicVO.query.filter_by(topicId=topicVO.topicId).all()
        return topicList

    def updateTopic(self, topicVO):
        db.session.merge(topicVO)
        db.session.commit()
