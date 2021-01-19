from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, _user_has_perm
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class AccountManager(BaseUserManager):
    def create_user(self, request_data, **kwargs):
        now = timezone.now()
        if not request_data['email']:
            raise ValueError('Users must have an email address.')

        profile = ""
        if request_data.get('profile'):
            profile = request_data['profile']

        user = self.model(
            username=request_data['username'],
            email=self.normalize_email(request_data['email']),
            is_active=True,
            last_login=now,
            date_joined=now,
            profile=profile
        )

        user.set_password(request_data['password'])
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        request_data = {
            'username': username,
            'email': email,
            'password': password
        }
        user = self.create_user(request_data)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username    = models.CharField(_('username'), max_length=30, unique=True)
    first_name  = models.CharField(_('first name'), max_length=30, blank=True)
    last_name   = models.CharField(_('last name'), max_length=30, blank=True)
    email       = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    profile     = models.CharField(_('profile'), max_length=255, blank=True)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    is_admin    = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def user_has_perm(user, perm, obj):
        return _user_has_perm(user, perm, obj)

    def has_perm(self, perm, obj=None):
        return _user_has_perm(self, perm, obj=obj)

    def has_module_perms(self, app_label):
        return self.is_admin

    def get_short_name(self):
        return self.first_name

    @property
    def is_superuser(self):
        return self.is_admin

    class Meta:
        db_table = 'api_user'
        swappable = 'AUTH_USER_MODEL'

# settingの設定
# get_user_modelを用いる
# appnameはuser(?)


# curl -X POST -H "Content-Type: application/json" -d '{"username": "shinji", "email": "a@a.com", "password": "1118aaad"}' localhost:8000/login/
# {"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFAYS5jb20iLCJleHAiOjE2MTA5ODQ4MDAsImVtYWlsIjoiYUBhLmNvbSJ9.RxHqYrHb80G3rmIfPVb-d1S8rwoZASUNy26hLqt1wMs"} 

# curl -X GET -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFAYS5jb20iLCJleHAiOjE2MTA5ODQ4MDAsImVtYWlsIjoiYUBhLmNvbSJ9.RxHqYrHb80G3rmIfPVb-d1S8rwoZASUNy26hLqt1wMs" -H "Content-Type: application/json" localhost:8000/api/mypage/
# curl -X POST -H "Content-Type: application/json" -d '{"username": "shinji", "email": "a@a.com", "password": "1118aaad"}' localhost:8000/api/register/

# curl -X PUT -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFAYS5jb20iLCJleHAiOjE2MTA5ODQ4MDAsImVtYWlsIjoiYUBhLmNvbSJ9.RxHqYrHb80G3rmIfPVb-d1S8rwoZASUNy26hLqt1wMs" -H "Content-Type: application/json" -d '{"username": "shinji2", "email": "b@b.com", "password": "1118aaad"}' localhost:8000/api/auth_update/

# curl -X POST -H "Content-Type: application/json" -d '{"username": "shinji3", "email": "c@c.com", "password": "1118aaad"}' localhost:8000/api/register/
# curl -X POST -H "Content-Type: application/json" -d '{"username": "shinji3", "email": "c@c.com", "password": "1118aaad"}' localhost:8000/login/
# {"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImNAYy5jb20iLCJleHAiOjE2MTA5ODU3MzIsImVtYWlsIjoiY0BjLmNvbSJ9.0s1rx2xZMnBp2GRP551CMLzGpKW4X0qFv0YD-t6FsmE"}

# curl -X GET -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImNAYy5jb20iLCJleHAiOjE2MTA5ODU3MzIsImVtYWlsIjoiY0BjLmNvbSJ9.0s1rx2xZMnBp2GRP551CMLzGpKW4X0qFv0YD-t6FsmE" -H "Content-Type: application/json" localhost:8000/api/mypage/
# curl -X DELETE -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImNAYy5jb20iLCJleHAiOjE2MTA5ODU3MzIsImVtYWlsIjoiY0BjLmNvbSJ9.0s1rx2xZMnBp2GRP551CMLzGpKW4X0qFv0YD-t6FsmE" -H "Content-Type: application/json" localhost:8000/api/delete/
# curl -X GET -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImNAYy5jb20iLCJleHAiOjE2MTA5ODU3MzIsImVtYWlsIjoiY0BjLmNvbSJ9.0s1rx2xZMnBp2GRP551CMLzGpKW4X0qFv0YD-t6FsmE" -H "Content-Type: application/json" localhost:8000/api/mypage/
