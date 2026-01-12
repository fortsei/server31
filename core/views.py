import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from core.repositories import analytics_repo
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Passenger
from .forms import PassengerForm
from rest_framework import viewsets 
from core.serializers import (
    AirportSerializer,
    AircraftSerializer,
    FlightSerializer,
    PassengerSerializer,
    BookingSerializer,
    CrewSerializer,
    FlightCrewSerializer,
    TicketSerializer
)

from core.repositories import repo

class AirportListCreateAPIView(APIView):

    def get(self, request):
        airports = repo.airports.get_all()
        serializer = AirportSerializer(airports, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AirportSerializer(data=request.data)
        if serializer.is_valid():
            airport = repo.airports.create(**serializer.validated_data)
            return Response(
                AirportSerializer(airport).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class AirportDetailAPIView(APIView):

    def get(self, request, pk):
        airport = repo.airports.get_by_id(pk)
        if not airport:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(AirportSerializer(airport).data)

    def put(self, request, pk):
        serializer = AirportSerializer(data=request.data)
        if serializer.is_valid():
            airport = repo.airports.update(pk, **serializer.validated_data)
            if not airport:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(AirportSerializer(airport).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        airport = repo.airports.delete(pk)
        if not airport:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

class FlightListCreateAPIView(APIView):

    def get(self, request):
        flights = repo.flights.get_all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            flight = repo.flights.create(**serializer.validated_data)
            return Response(
                FlightSerializer(flight).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class FlightDetailAPIView(APIView):

    def get(self, request, pk):
        flight = repo.flights.get_by_id(pk)
        if not flight:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(FlightSerializer(flight).data)

    def put(self, request, pk):
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            flight = repo.flights.update(pk, **serializer.validated_data)
            if not flight:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(FlightSerializer(flight).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        flight = repo.flights.delete(pk)
        if not flight:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

class AircraftListCreateAPIView(APIView):

    def get(self, request):
        aircrafts = repo.aircrafts.get_all()
        serializer = AircraftSerializer(aircrafts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AircraftSerializer(data=request.data)
        if serializer.is_valid():
            aircraft = repo.aircraft.create(**serializer.validated_data)
            return Response(
                AirportSerializer(aircraft).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class AircraftDetailAPIView(APIView):

    def get(self, request, pk):
        aircraft = repo.aircrafts.get_by_id(pk)
        if not aircraft:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(AircraftSerializer(aircraft).data)

    def put(self, request, pk):
        serializer = AirportSerializer(data=request.data)
        if serializer.is_valid():
            aircraft = repo.aircrafts.update(pk, **serializer.validated_data)
            if not aircraft:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(AircraftSerializer(aircraft).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        aircraft = repo.aircrafts.delete(pk)
        if not aircraft:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PassengerListCreateAPIView(APIView):

    def get(self, request):
        passengers = repo.passengers.get_all()
        serializer = PassengerSerializer(passengers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PassengerSerializer(data=request.data)
        if serializer.is_valid():
            passenger = repo.passengers.create(**serializer.validated_data)
            return Response(
                PassengerSerializer(passenger).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PassengerDetailAPIView(APIView):

    def get(self, request, pk):
        passenger = repo.passengers.get_by_id(pk)
        if not passenger:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(PassengerSerializer(passenger).data)

    def put(self, request, pk):
        serializer = PassengerSerializer(data=request.data)
        if serializer.is_valid():
            passenger = repo.passengers.update(pk, **serializer.validated_data)
            if not passenger:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(PassengerSerializer(passenger).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        passenger = repo.passengers.delete(pk)
        if not passenger:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookingListCreateAPIView(APIView):

    def get(self, request):
        bookings = repo.bookings.get_all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            booking = repo.bookings.create(**serializer.validated_data)
            return Response(
                BookingSerializer(booking).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingDetailAPIView(APIView):

    def get(self, request, pk):
        booking = repo.bookings.get_by_id(pk)
        if not booking:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(BookingSerializer(booking).data)

    def put(self, request, pk):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            booking = repo.bookings.update(pk, **serializer.validated_data)
            if not booking:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(BookingSerializer(booking).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        booking = repo.bookings.delete(pk)
        if not booking:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)

class TicketListCreateAPIView(APIView):

    def get(self, request):
        tickets = repo.tickets.get_all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            ticket = repo.tickets.create(**serializer.validated_data)
            return Response(
                TicketSerializer(ticket).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketDetailAPIView(APIView):

    def get(self, request, pk):
        ticket = repo.tickets.get_by_id(pk)
        if not ticket:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(TicketSerializer(ticket).data)

    def put(self, request, pk):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            ticket = repo.tickets.update(pk, **serializer.validated_data)
            if not ticket:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(TicketSerializer(ticket).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ticket = repo.tickets.delete(pk)
        if not ticket:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CrewListCreateAPIView(APIView):

    def get(self, request):
        crew = repo.crews.get_all()
        serializer = CrewSerializer(crew, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CrewSerializer(data=request.data)
        if serializer.is_valid():
            crew_member = repo.crews.create(**serializer.validated_data)
            return Response(
                CrewSerializer(crew_member).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CrewDetailAPIView(APIView):

    def get(self, request, pk):
        crew = repo.crews.get_by_id(pk)
        if not crew:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(CrewSerializer(crew).data)

    def put(self, request, pk):
        serializer = CrewSerializer(data=request.data)
        if serializer.is_valid():
            crew = repo.crews.update(pk, **serializer.validated_data)
            if not crew:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(CrewSerializer(crew).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        crew = repo.crews.delete(pk)
        if not crew:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class FlightCrewListCreateAPIView(APIView):

    def get(self, request):
        flight_crews = repo.flight_crews.get_all()
        serializer = FlightCrewSerializer(flight_crews, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlightCrewSerializer(data=request.data)
        if serializer.is_valid():
            flight_crew = repo.flight_crews.create(**serializer.validated_data)
            return Response(
                FlightCrewSerializer(flight_crew).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlightCrewDetailAPIView(APIView):

    def get(self, request, pk):
        flight_crew = repo.flight_crews.get_by_id(pk)
        if not flight_crew:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(FlightCrewSerializer(flight_crew).data)

    def delete(self, request, pk):
        flight_crew = repo.flight_crews.delete(pk)
        if not flight_crew:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
 



class PassengerListView(ListView):
    model = Passenger
    template_name = 'core/passenger_list.html'
    context_object_name = 'passengers'


class PassengerDetailView(DetailView):
    model = Passenger
    template_name = 'core/passenger_detail.html'
    context_object_name = 'passenger'


class PassengerCreateView(CreateView):
    model = Passenger
    form_class = PassengerForm
    template_name = 'core/passenger_form.html'
    success_url = reverse_lazy('passenger_list')


class PassengerUpdateView(UpdateView):
    model = Passenger
    form_class = PassengerForm
    template_name = 'core/passenger_form.html'
    success_url = reverse_lazy('passenger_list')


class PassengerDeleteView(DeleteView):
    model = Passenger
    success_url = reverse_lazy('passenger_list')
   
class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer



class BaseAnalyticsView(APIView):
   
    def process_dataframe(self, queryset):
       
        data = list(queryset)
        df = pd.DataFrame(data)
        
        if df.empty:
            return None, None
            
        return df, data


class AircraftRevenueAnalyticsView(BaseAnalyticsView):
    def get(self, request):
        queryset = analytics_repo.get_revenue_by_aircraft_type()
        df, raw_data = self.process_dataframe(queryset)
        
        if df is None:
            return Response({"message": "No data available"})

        
        stats = {
            "mean_revenue": df['total_revenue'].mean(),
            "median_revenue": df['total_revenue'].median(),
            "max_revenue": df['total_revenue'].max(),
            "min_revenue": df['total_revenue'].min(),
        }

       
        df['manufacturer'] = df['flight__aircraft__model'].apply(lambda x: x.split()[0] if x else 'Unknown')
        manufacturer_stats = df.groupby('manufacturer')['total_revenue'].sum().to_dict()

        return Response({
            "dataframe_data": raw_data,  
            "statistics": stats,         
            "grouped_by_manufacturer": manufacturer_stats 
        })


class PassengerAnalyticsView(BaseAnalyticsView):
    def get(self, request):
        queryset = analytics_repo.get_avg_ticket_price_by_nationality()
        df, raw_data = self.process_dataframe(queryset)

        if df is None:
            return Response({"message": "No data"})

        
        global_mean = df['avg_spend'].mean()
        high_spenders = df[df['avg_spend'] > global_mean]

        return Response({
            "data": raw_data,
            "global_mean_spend": global_mean,
            "high_spending_nationalities_count": len(high_spenders),
            "top_nationality": df.iloc[0].to_dict()
        })


class GeneralReportView(BaseAnalyticsView):
    def get(self, request):
     
        busy_airports = list(analytics_repo.get_flights_by_airport())
        frequent_flyers = list(analytics_repo.get_frequent_flyers())
        
       
        df_airports = pd.DataFrame(busy_airports)
        
        return Response({
            "busy_airports_top_3": busy_airports[:3],
            "frequent_flyers_count": len(frequent_flyers),
            "median_flights_per_airport": df_airports['total_flights'].median() if not df_airports.empty else 0
        })