# from app import db, login
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin
#
#
# # class User(UserMixin, db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     username = db.Column(db.String(64), index=True, unique=True)
# #     password_hash = db.Column(db.String(128))
# #     user_role = db.Column(db.Integer)
# #
# #     def __repr__(self):
# #         return '<User {} >' .format(self.username)
# #
# #     def set_password(self, password):
# #         self.password_hash = generate_password_hash(password)
# #
# #     def check_password(self, password):
# #         return check_password_hash(self.password_hash, password)
# #
# #
# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))
#
# class User(UserMixin, db.Document):
#     username = db.StringField()
#     password_hash = db.StringField()
#     user_role = db.IntField(required=False)
#
#     def __str__(self):
#         return 'User: %s' % self.username
#
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)
#
#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
#
#
# class Account(db.Document):
#     account_number = db.IntField()
#     balance = db.IntField(required=False)
#     firstname = db.StringField(required=False)
#     lastname = db.StringField(required=False)
#     age = db.IntField(required=False)
#     gender = db.StringField(required=False)
#     address = db.StringField(required=False)
#     employer = db.StringField(required=False)
#     email = db.StringField(required=False)
#     city = db.StringField(required=False)
#     state = db.StringField(required=False)
