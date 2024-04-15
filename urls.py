from django.contrib import admin
from django.urls import path

from post.views import postest1, dashBoard



urlpatterns = [

    path('', postest1),
    path('admin/', admin.site.urls),
    path('pos1/', postest1 ),
    path('pos1/dashBoard/', dashBoard ),
]
