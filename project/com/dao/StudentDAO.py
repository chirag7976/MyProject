from project import db
from project.com.vo.StudentVO import StudentVO


class StudentDAO():
    def insertStudent(self, studentVO):
        db.session.add(studentVO)
        db.session.commit()

    def viewStudent(self):
        studentList=StudentVO.query.all()
        print('viewstudentList',studentList)
        return studentList

    def deleteStudent(self, studentVO):
        studentList = StudentVO.query.get(studentVO.studentId)
        db.session.delete(studentList)
        db.session.commit()

    def editStudent(self, studentVO):
        studentList = StudentVO.query.filter_by(studentId=studentVO.studentId).all()
        return studentList

    def updateStudent(self, studentVO):
        db.session.merge(studentVO)
        db.session.commit()

    def validateUsername(self, studentVO):
        print(studentVO)
        studentList = StudentVO.query.filter_by(studentEmail = studentVO.studentEmail).all()
        print(studentList)
        return studentList
