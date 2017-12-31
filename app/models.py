from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))
    note = db.Column(db.String(128))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def this_query(self):
        return User.query.filter_by(username=self.username, password=self.password).first()

    def this_note(self):
        return self.note

    def this_add(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            print("User add error")
            db.session.rollback()
            return False
        else:
            print("User add %s" % self.username)
            return True
        finally:
            db.session.close()

    def this_del(self):
        try:
            db.session.delete(User.query.filter_by(username=self.username, password=self.password).first())
            db.session.commit()
        except:
            print("User del error")
            db.session.rollback()
            return False
        else:
            print("User del %s" % self.username)
            return True
        finally:
            db.session.close()

    def this_mod(self, password):
        try:
            User.query.filter_by(username=self.username, password=self.password).update({'password': password})
            self.password = password
            db.session.commit()
        except:
            print("User mod error")
            db.session.rollback()
            return False
        else:
            print("User mod %s" % self.username)
            return True
        finally:
            db.session.close()

    def __repr__(self):
        return '<User %r>' % self.username
