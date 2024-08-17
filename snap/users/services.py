from django.db import transaction
from .models import BaseUser


def create_user(*, name, mobile_num, email: str, password: str) -> BaseUser:
    return BaseUser.objects.create_user(name=name, mobile_num=mobile_num, email=email, password=password)


def update_user(userid, name, mobile_num, email, password=None):
    the_user = BaseUser.objects.get(id=userid)
    the_user.name = name
    the_user.mobile_num = mobile_num
    the_user.email = email
    if password is not None:
        the_user.set_password(password)
    the_user.save()


# @transaction.atomic
# def register(*, email: str, password: str) -> BaseUser:
#     user = create_user(email=email, password=password)
#     return user
