from django_registration.forms import RegistrationForm
from users.models import CustomUser
from crispy_forms.helper import FormHelper

class CustomUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = CustomUser
        