from django.urls import path
from .views import AircraftRevenueAnalyticsView, PassengerAnalyticsView, GeneralReportView
from .views import (
    PassengerListView, PassengerDetailView, 
    PassengerCreateView, PassengerUpdateView, PassengerDeleteView
)
from core.views import (
    AirportListCreateAPIView,
    AirportDetailAPIView,

    AircraftListCreateAPIView,
    AircraftDetailAPIView,

    FlightListCreateAPIView,
    FlightDetailAPIView,

    PassengerListCreateAPIView,
    PassengerDetailAPIView,

    BookingListCreateAPIView,
    BookingDetailAPIView,

    TicketListCreateAPIView,
    TicketDetailAPIView,

    CrewListCreateAPIView,
    CrewDetailAPIView,

    FlightCrewListCreateAPIView,
    FlightCrewDetailAPIView,
)
from .dashboard_views import (dashboard_plotly, dashboard_bokeh)
urlpatterns = [

 
    path('airports/', AirportListCreateAPIView.as_view(), name='airport-list'),
    path('airports/<int:pk>/', AirportDetailAPIView.as_view(), name='airport-detail'),

   
    path('aircrafts/', AircraftListCreateAPIView.as_view(), name='aircraft-list'),
    path('aircrafts/<int:pk>/', AircraftDetailAPIView.as_view(), name='aircraft-detail'),

  
    path('flights/', FlightListCreateAPIView.as_view(), name='flight-list'),
    path('flights/<int:pk>/', FlightDetailAPIView.as_view(), name='flight-detail'),

    
    path('passengers/', PassengerListCreateAPIView.as_view(), name='passenger-list'),
    path('passengers/<int:pk>/', PassengerDetailAPIView.as_view(), name='passenger-detail'),

    
    path('bookings/', BookingListCreateAPIView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingDetailAPIView.as_view(), name='booking-detail'),

    
    path('tickets/', TicketListCreateAPIView.as_view(), name='ticket-list'),
    path('tickets/<int:pk>/', TicketDetailAPIView.as_view(), name='ticket-detail'),

 
    path('crew/', CrewListCreateAPIView.as_view(), name='crew-list'),
    path('crew/<int:pk>/', CrewDetailAPIView.as_view(), name='crew-detail'),

   
    path('ui/flight-crews/', FlightCrewListCreateAPIView.as_view(), name='flight-crew-list'),
    path('ui/flight-crews/<int:pk>/', FlightCrewDetailAPIView.as_view(), name='flight-crew-detail'),
    path('ui/passengers/', PassengerListView.as_view(), name='passenger_list'),
    path('ui/passengers/<int:pk>/', PassengerDetailView.as_view(), name='passenger_detail'),
    path('ui/passengers/add/', PassengerCreateView.as_view(), name='passenger_add'),
    path('ui/passengers/<int:pk>/edit/', PassengerUpdateView.as_view(), name='passenger_edit'),
    path('ui/passengers/<int:pk>/delete/', PassengerDeleteView.as_view(), name='passenger_delete'),
    path('analytics/aircraft-revenue/', AircraftRevenueAnalyticsView.as_view()),
    path('analytics/passengers/', PassengerAnalyticsView.as_view()),
    path('analytics/general/', GeneralReportView.as_view()),
    path('dashboard/v1/', dashboard_plotly, name='dashboard_plotly'),
    path('dashboard/v2/', dashboard_bokeh, name='dashboard_bokeh'),
]

