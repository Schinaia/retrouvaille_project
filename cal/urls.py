
from django.urls import path, include
from cal.views import CalendarView



from . import views

app_name = 'cal'
urlpatterns = [
#    path(r'^index/$', views.index, name='index'),
   path("cal/calendar/", CalendarView.as_view(), name='calendar'),
   path("event/new/", views.event, name='event_new'),
   path("event/edit/<int:event_id>/", views.event, name='event_edit'),
#    path("kalender/", kalender_view, name="kalender"),
#    path("kalender/<int:year>/<int:month>/", kalender_view, name="kalender_met_datum"),
]

