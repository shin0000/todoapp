from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from api1.urls import router as api1_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api1/', include(api1_router.urls)),
    path('login/', obtain_jwt_token),
    path('api2/', include('user.urls')),
]
