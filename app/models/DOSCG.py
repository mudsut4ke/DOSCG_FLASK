from app import db


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(20))
    value = db.Column(db.Integer)


class DOSCG(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    func_no = db.Column(db.Integer, nullable=False)
    answer = db.relationship("Answer")

    def __repr__(self):
        return "<DOSCG func_no %r>" % self.func_no
