from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.db.models import Q

class AadhaarPhoneBackend(BaseBackend):
    """
    Authenticate using phone number or Aadhaar number as username,
    and Aadhaar number as password.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        from .models import Registration
        print(f"Authenticating username: {username} with password: {password}")
        try:
            registration = Registration.objects.get(
                Q(contact=username) | Q(aadhar_number=username)
            )
            print(f"Found registration: {registration}")
            if registration.aadhar_number == password:
                if registration.user:
                    print(f"Returning user: {registration.user}")
                    return registration.user
                else:
                    print("Registration has no linked user")
            else:
                print("Password does not match Aadhaar number")
        except Registration.DoesNotExist:
            print("Registration does not exist")
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
