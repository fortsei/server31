from django.db.models import Sum, Avg, Count, Max, Min
from django.db.models import Count, Sum, Avg, Max, F, Q
from .models import Passenger, Flight, Ticket, Booking, Aircraft, Airport

from django.db.models.functions import TruncMonth
from core.models import (
    Airport,
    Aircraft,
    Flight,
    Passenger,
    Booking,
    Crew,
    FlightCrew,
    Ticket
)


class BaseRepository:
    def __init__(self, model):
        self.model = model
    def get_all(self):
        return self.model.objects.all()
    def get_by_id(self, entity_id):
        try:
            return self.model.objects.get(pk=entity_id)  
        except self.model.DoesNotExist:
            return None                                  
    def create(self, **kwargs):
        return self.model.objects.create(**kwargs)
    
    def delete(self, id):
        instance = self.get_by_id(id)
        if instance:
            instance.delete()
            return instance
        else:
            return None
        
    def update(self, id, **kwargs):
        instance = self.get_by_id(id)
        if instance:
            for k, v in kwargs.items():
                setattr(instance, k ,v)
            instance.save()
        return instance


class AirportRepository(BaseRepository):
    def __init__(self):
        super().__init__(Airport)


class AircraftRepository(BaseRepository):
    def __init__(self):
        super().__init__(Aircraft)


class FlightRepository(BaseRepository):
    def __init__(self):
        super().__init__(Flight)


class PassengerRepository(BaseRepository):
    def __init__(self):
        super().__init__(Passenger)


class BookingRepository(BaseRepository):
    def __init__(self):
        super().__init__(Booking)


class CrewRepository(BaseRepository):
    def __init__(self):
        super().__init__(Crew)


class FlightCrewRepository(BaseRepository):
    def __init__(self):
        super().__init__(FlightCrew)


class TicketRepository(BaseRepository):
    def __init__(self):
        super().__init__(Ticket)

class RepositoryManager:
    def __init__(self):
        self.airports = AirportRepository()
        self.aircrafts = AircraftRepository()
        self.flights = FlightRepository()
        self.passengers = PassengerRepository()
        self.bookings = BookingRepository()
        self.crews = CrewRepository()
        self.flight_crews = FlightCrewRepository()
        self.tickets = TicketRepository()


repo = RepositoryManager()




class AnalyticsRepository:
    
    def get_flights_by_airport(self):
        return Flight.objects.values('airport__name') \
            .annotate(total_flights=Count('flight_id')) \
            .order_by('-total_flights')

    def get_revenue_by_aircraft_type(self):
        return Booking.objects.values('flight__aircraft__model') \
            .annotate(total_revenue=Sum('price'), avg_price=Avg('price')) \
            .order_by('-total_revenue')

    def get_frequent_flyers(self):
        return Passenger.objects.annotate(booking_count=Count('booking')) \
            .filter(booking_count__gt=1) \
            .values('first_name', 'last_name', 'booking_count') \
            .order_by('-booking_count')

    def get_avg_ticket_price_by_nationality(self):
        return Passenger.objects.values('nationality') \
            .annotate(avg_spend=Avg('booking__price')) \
            .exclude(avg_spend__isnull=True) \
            .order_by('-avg_spend')

    def get_low_occupancy_flights(self):
        return Flight.objects.annotate(sold_tickets=Count('booking')) \
            .filter(sold_tickets__lt=50) \
            .values('flight_number', 'sold_tickets', 'airport__name')

    def get_passenger_age_distribution(self):
        return Passenger.objects.values('birth_date__year') \
            .annotate(count=Count('passenger_id')) \
            .order_by('birth_date__year')

analytics_repo = AnalyticsRepository()