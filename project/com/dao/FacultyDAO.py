from project import db
from project.com.vo.LoginVO import LoginVO
from project.com.vo.RegisterVO import RegisterVO


class FacultyDAO():
    def viewFaculty(self):
        facultyList = db.session.query(RegisterVO, LoginVO).join(LoginVO,
                                                                 RegisterVO.register_LoginId == LoginVO.loginId).all()
        return facultyList

    # change loginStatus : block or unblock
    def changeStatusFaculty(self, loginVO):
        db.session.merge(loginVO)
        db.session.commit()

    #update faculty profile details
    def updateFacultyProfile(self, registerVO):
        db.session.merge(registerVO)
        db.session.commit()
