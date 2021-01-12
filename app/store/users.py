from app.models import Users


def add_user_mongo(user):
    user = Users.from_dict(user)
    user.save()
    return user
