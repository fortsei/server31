from rest_framework import serializers
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


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = '__all__'


class FlightCrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightCrew
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
