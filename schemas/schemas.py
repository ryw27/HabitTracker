from marshmallow import Schema, fields


class HabitSchema(Schema):
    id = fields.int()
    habit = fields.Str()
    desc = fields.Str()
class UserSchema(Schema):
    id = fields.int()
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()

