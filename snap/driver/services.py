from snap.users.models import BaseUser
from snap.users.services import update_user
from snap.driver.models import Driver
from django.shortcuts import get_object_or_404


def creat_driver(user, car_info):
    return Driver.objects.create(user=user, car=car_info)


def get_driver_detail(driver_id):
    the_driver = Driver.objects.get(id=driver_id)
    return the_driver


def driver_update(driver_id, car_info, name, mobile_num, email, password):
    # ___update the driver table
    the_driver = Driver.objects.select_related("user").filter(id=driver_id)[0]
    the_driver.car = car_info
    user = the_driver.user
    user.name = name
    user.mobile_num = mobile_num
    user.email = email
    user.password = password
    the_driver.save()
    user.save()


def delete_driver(driver_id):
    the_driver = Driver.objects.get(id=driver_id)
    return the_driver.delete()
