from scrumboard.api import CardViewSet,ListViewSet
from rest_framework.routers import DefaultRouter

"""
"""

router = DefaultRouter() #instead of urlpatterns list
router.register(r'lists',ListViewSet)
router.register(r'cards', CardViewSet)

#calling a bad url shows a lot of urls created automaticallyt
urlpatterns = router.urls