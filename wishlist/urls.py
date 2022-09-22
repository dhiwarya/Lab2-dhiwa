from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_xml #customize to the name of the function created
from wishlist.views import show_json # adjust the name of the function created
from wishlist.views import show_json_by_id
from wishlist.views import show_xml_by_id
from wishlist.views import register
from wishlist.views import login_user
from wishlist.views import logout_user

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'), #customize the name of the function 
    path('json/', show_json, name='show_json'), #customise the name of the function created
    path('html/', show_wishlist, name='show_wishlist'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]