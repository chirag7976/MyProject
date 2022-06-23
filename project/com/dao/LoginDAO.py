from project import db
from project.com.vo.LoginVO import LoginVO


class LoginDAO:
    # insertLogin will insert login details in "loginmaster" table
    def insertLogin(self, loginVO):
        db.session.add(loginVO)
        db.session.commit()

    # function will check for vaild login details
    def validateLogin(self, loginVO):
        loginList = LoginVO.query.filter_by(loginUsername=loginVO.loginUsername, loginPassword=loginVO.loginPassword).all()
        print('***********/******/*loginList',loginList)
        return loginList

    def forgotLogin(self, loginVO):
        loginList = LoginVO.query.filter_by(loginUsername=loginVO.loginUsername).all()
        return loginList

    def viewLogin(self, loginVO):
        loginVOList = LoginVO.query.filter_by(loginId = loginVO.loginId).all()
        return loginVOList

    def updateLogin(self, loginVO):
        db.session.merge(loginVO)
        db.session.commit()
