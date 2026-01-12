from django.db import models


class Airport(models.Model):
    airport_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    iata_code = models.CharField(max_length=3, unique=True)

    class Meta:
        db_table = 'Airport'

    def __str__(self):
        return f"{self.name} ({self.iata_code})"


class Aircraft(models.Model):
    aircraft_id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50, null=True, blank=True)
    capacity = models.PositiveIntegerField()
    registration_no = models.CharField(max_length=20, unique=True, null=True, blank=True)

    class Meta:
        db_table = 'Aircrafts'

    def __str__(self):
        return self.model


class Flight(models.Model):
    flight_id = models.AutoField(primary_key=True)
    flight_number = models.CharField(max_length=10)
    departure_time = models.DateTimeField(null=True, blank=True)
    arrival_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=30, null=True, blank=True)

    aircraft = models.ForeignKey(
        Aircraft,
        on_delete=models.PROTECT,
        db_column='aircraft_id'
    )

    airport = models.ForeignKey(
        Airport,
        on_delete=models.PROTECT,
        db_column='airport_id'
    )

    class Meta:
        db_table = 'Flights'

    def __str__(self):
        return self.flight_number


class Passenger(models.Model):
    passenger_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    passport_number = models.CharField(max_length=20, unique=True)
    nationality = models.CharField(max_length=50)
    birth_date = models.DateField()

    class Meta:
        db_table = 'Passengers'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    booking_date = models.DateTimeField()
    seat_number = models.CharField(max_length=10)
    travel_class = models.CharField(max_length=20, db_column='class')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    flight = models.ForeignKey(
        Flight,
        on_delete=models.CASCADE,
        db_column='flight_id'
    )

    passenger = models.ForeignKey(
        Passenger,
        on_delete=models.CASCADE,
        db_column='passenger_id'
    )

    class Meta:
        db_table = 'Bookings'


class Crew(models.Model):
    crew_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    license_number = models.CharField(max_length=50, null=True, blank=True)
    nationality = models.CharField(max_length=50)

    class Meta:
        db_table = 'Crew'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class FlightCrew(models.Model):
    flight = models.ForeignKey(
        Flight,
        on_delete=models.CASCADE,
        db_column='flight_id'
    )

    crew = models.ForeignKey(
        Crew,
        on_delete=models.CASCADE,
        db_column='crew_id'
    )

    assigned_role = models.CharField(max_length=50)

    class Meta:
        db_table = 'Flight_Crew'
        unique_together = ('flight', 'crew')


class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    ticket_number = models.CharField(max_length=50)
    issue_date = models.DateTimeField()
    payment_status = models.CharField(max_length=30)

    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE,
        db_column='booking_id'
    )

    class Meta:
        db_table = 'Tickets'
