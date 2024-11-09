from marshmallow import Schema, fields


class HabitSchema(Schema):
    id = fields.Int()
    habit = fields.Str()
    desc = fields.Str()
class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()

