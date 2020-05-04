from django.contrib.auth import get_user_model

from factory import PostGenerationMethodCall, Sequence
from factory.django import DjangoModelFactory


class DemoUserFactory(DjangoModelFactory):
    username = Sequence(lambda n: "User %03d" % n)
    password = PostGenerationMethodCall("set_password", "password")
    is_staff = True
    is_active = True

    class Meta:
        model = get_user_model()


class ActiveListingOwnerFactory(DjangoModelFactory):
    username = Sequence(lambda n: "User %03d" % n)
    password = PostGenerationMethodCall("set_password", "password")
    is_staff = False
    is_active = True

    class Meta:
        model = get_user_model()
