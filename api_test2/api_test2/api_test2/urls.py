from django.contrib import admin
from django.urls import path, include

from api1.urls import router as api1_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api1/', include(api1_router.urls))
]
