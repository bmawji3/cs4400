class User():
    # id = db.Column(db.Integer, primary_key=True)
    # nickname = db.Column(db.String(64), index=True, unique=True)
    # email = db.Column(db.String(120), index=True, unique=True)
    # posts = db.relationship('Post', backref='author', lazy='dynamic')
    username = ""
    password = ""
    id = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)