from rest_framework.routers import SimpleRouter,DefaultRouter
from .views import *
router=SimpleRouter()

router.register('login',LoginViewSet,basename="login")
# router.register('logout', LogoutViewSet, basename='logout')
router.register('teacher',TeacherViewSet,basename="teacher")
router.register('student',StudentViewSet,basename="student") 
router.register('updateprofile',ProfileUpdateViewSet,basename="updateprofile")
router.register('changepassword',UserChangepasswordViewSet,basename="changepassword")
router.register('forgetpassword',ResetPasswordEmailViewSet,basename="forgetpassword")
router.register('search',SearchViewSet,basename="search")
router.register('job',CreateJobViewSet,basename="job")
# router.register('searchjob',SearchJobViewSet,basename="searchjob")
router.register('gallery',GalleryViewSet,basename="Gallery")
router.register('event',EventViewSet,basename="Event")
router.register('chat',ChatViewSet,basename="chat")