from project import db
from project.com.vo.FeedbackVO import FeedbackVO
from project.com.vo.LoginVO import LoginVO
from project.com.vo.RegisterVO import RegisterVO


class FeedbackDAO():
    def insertFeedback(self, feedbackVO):
        db.session.add(feedbackVO)
        db.session.commit()

    def viewFeedback(self):
        feedbackList = db.session.query(FeedbackVO, LoginVO, RegisterVO) \
            .join(LoginVO, FeedbackVO.feedbackFrom_LoginId == LoginVO.loginId) \
            .join(RegisterVO, FeedbackVO.feedbackFrom_LoginId == RegisterVO.register_LoginId).all()
        return feedbackList

    def viewFeedbackFaculty(self, feedbackVO):
        feedbackList = FeedbackVO.query.filter_by(feedbackFrom_LoginId=feedbackVO.feedbackFrom_LoginId).all()
        return feedbackList

    def editFeedback(self, feedbackVO):
        feedbackList = FeedbackVO.query.filter_by(feedbackId=feedbackVO.feedbackId).all()
        return feedbackList

    def changeFeedbackStatus(self, feedbackVO):
        db.session.merge(feedbackVO)
        db.session.commit()

    def deleteFeedback(self, feedbackVO):
        feedbackList = FeedbackVO.query.get(feedbackVO.feedbackId)
        db.session.delete(feedbackList)
        db.session.commit()
