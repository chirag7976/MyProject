from project import db
from project.com.vo.LoginVO import LoginVO


class RegisterVO(db.Model):
    __tablename__ = 'registermaster'
    registerId = db.Column('registerId', db.Integer, primary_key=True, autoincrement=True)
    registerFirstName = db.Column('registerFirstName', db.String(50), nullable=False)
    registerLastName = db.Column('registerLastName', db.String(50), nullable=False)
    registerGender = db.Column('registerGender', db.String(50), nullable=False)
    registerContactNumber = db.Column('registerContactNumber', db.Integer, nullable=False)
    register_LoginId = db.Column('register_LoginId', db.Integer, db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'registerId': self.registerId,
            'registerFirstName': self.registerFirstName,
            'registerLastName': self.registerLastName,
            'registerGender': self.registerGender,
            'registerContactNumber': self.registerContactNumber,
            'register_LoginId': self.register_LoginId
        }


db.create_all()
