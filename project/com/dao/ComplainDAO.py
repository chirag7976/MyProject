from project import db
from project.com.vo.ComplainVO import ComplainVO
from project.com.vo.LoginVO import LoginVO
from project.com.vo.RegisterVO import RegisterVO


class ComplainDAO():
    def insertComplain(self, complainVO):
        db.session.add(complainVO)
        db.session.commit()

    def viewComplain(self):
        complainList = db.session.query(ComplainVO, LoginVO, RegisterVO) \
            .join(LoginVO, ComplainVO.complainFrom_LoginId == LoginVO.loginId) \
            .join(RegisterVO, ComplainVO.complainFrom_LoginId == RegisterVO.register_LoginId).all()
        return complainList

    def viewComplainFaculty(self, complainVO):
        complainList = ComplainVO.query.filter_by(complainFrom_LoginId=complainVO.complainFrom_LoginId).all()
        return complainList

    def deleteComplain(self, complainVO):
        complainList = complainVO.query.get(complainVO.complainId)
        db.session.delete(complainList)
        db.session.commit()
        return complainList

    def editComplain(self, complainVO):
        complainList = ComplainVO.query.filter_by(complainId=complainVO.complainId).all()
        return complainList

    def insertComplainReply(self, complainVO):
        db.session.merge(complainVO)
        db.session.commit()

    def viewComplainReply(self, complainVO):
        complainReplyList = ComplainVO.query.filter_by(complainId=complainVO.complainId).all()
        return complainReplyList


'''
    def editComplain(self, complainVO):
        complainList = ComplainVO.query.filter_by(complainId = complainVO.complainId).all()
        return complainList

    def updateComplain(self, complainVO):
        db.session.merge(complainVO)
        db.session.commit()

    def viewComplainReply(self):
        complainReplyList = db.session.query(ComplainVO).all()
        return complainReplyList
'''
