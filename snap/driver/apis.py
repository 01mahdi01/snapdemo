from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from snap.driver.services import creat_driver, driver_update, delete_driver
from snap.driver.models import Driver


class CreateDriver(APIView):
    class CreateDriverInputSerializer(serializers.Serializer):
        car_info = serializers.JSONField

    def post(self, request):
        serializer = self.CreateDriverInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        userid = request.user.id
        car_info = serializer.validated_data.get("car_info")
        creat_driver(userid, car_info)
        return Response({'message': '______temp_____driver created'})

    class DriverOutputSerializer(serializers.ModelSerializer):
        model = Driver
        fields = ("userid", "car")


class UpdateDriver(APIView):
    class UpdateDriverInputSerializer(serializers.Serializer):
        car_info = serializers.JSONField
        name = serializers.CharField
        mobile_num = serializers.CharField
        email = serializers.EmailField
        password = serializers.CharField

    def post(self, request):
        serializer = self.UpdateDriverInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        car_info = serializer.validated_data.get("car_info")
        name = serializer.validated_data.get("name")
        mobile_num = serializer.validated_data.get("mobile_num")
        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")
        driver_update(user, car_info, name, mobile_num, email, password)
        return Response({'message': '______temp_____driver updated'})

    class DriverOutputSerializer(serializers.ModelSerializer):
        model = Driver
        fields = ("user", "car")


class DeleteDriver(APIView):

    def post(self, request):
        userid = request.user.id
        driver = Driver.objects.get(userid=userid)
        delete_driver(driver.id)
