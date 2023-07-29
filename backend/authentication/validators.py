from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


no_whitespace_validator = RegexValidator(
    regex=r'^\S+$',
    message='Esse campo não pode conter espaços em branco'
)

