from project import db
from project.com.vo.RegisterVO import RegisterVO


class RegisterDAO():
    def insertRegister(self, registerVO):
        db.session.add(registerVO)
        db.session.commit()

    def getFacultyData(self, registerVO):
        registerVOList = RegisterVO.query.filter_by(register_LoginId = registerVO.register_LoginId).all()
        return registerVOList