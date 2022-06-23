from project import db


class StudentVO(db.Model):
    __tablename__ = 'studentmaster'
    studentId = db.Column('studentId', db.Integer, primary_key=True, autoincrement=True)
    studentFirstName = db.Column('studentFirstName', db.String(50), nullable=False)
    studentLastName = db.Column('studentLastName', db.String(50), nullable=False)
    studentGender = db.Column('studentGender', db.String(10), nullable=False)
    studentEmail = db.Column('studentEmail', db.String(40), nullable=False)
    studentContactNumber = db.Column('studentContactNumber', db.Integer, nullable=False)
    studentStatus = db.Column('studentStatus', db.String(10), nullable=False)

    def as_dict(self):
        return {
            'studentId': self.studentId,
            'studentFirstName': self.studentFirstName,
            'studentLastName': self.studentLastName,
            'studentGender': self.studentGender,
            'studentEmail': self.studentEmail,
            'studentContactNumber': self.studentContactNumber,
            'studentStatus': self.studentStatus
        }


db.create_all()
