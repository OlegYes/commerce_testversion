from django.urls import path

from commerce import settings
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_lot", views.addlot, name="create_lot"),
    path("my_lots", views.my_lots, name="my_lots"),
    path("<int:my_lot_id>", views.LotData, name="my_lot"),
    path("testhtml", views.testhtml, name="testhtml")
]


