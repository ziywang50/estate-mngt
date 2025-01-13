from django.apps import AppConfig
from django.utils.translation import gettextlazy as _

class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.profiles"
    verbose_name = _("Profiles")