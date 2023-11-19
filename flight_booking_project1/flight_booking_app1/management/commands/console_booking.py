# flight_booking_app/management/commands/console_booking.py
from django.core.management.base import BaseCommand
from flight_booking_app1.models import User, Flight, Booking
from django.contrib.auth import authenticate

class Command(BaseCommand):
    help = 'Console-based flight booking system'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Console Booking System'))

        while True:
            self.stdout.write("\n1. Sign Up\n2. Log In\n3. Search Flight\n4. Book Ticket\n5. Admin Login\n6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.sign_up()
            elif choice == '2':
                self.log_in()
            elif choice == '3':
                self.search_flight()
            elif choice == '4':
                self.book_ticket()
            elif choice == '5':
                self.admin_login()
            elif choice == '6':
                break
            else:
                self.stdout.write(self.style.ERROR('Invalid choice. Try again.'))

    def sign_up(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        user, created = User.objects.get_or_create(username=username, defaults={'password': password})

        if created:
            self.stdout.write(self.style.SUCCESS(f'User {username} signed up successfully.'))
        else:
            self.stdout.write(self.style.ERROR(f'User {username} already exists. Try a different username.'))

    def log_in(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        try:
            user = User.objects.get(username=username, password=password)
            self.stdout.write(self.style.SUCCESS(f'User {username} logged in successfully.'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('Invalid username or password. Try again.'))

    def search_flight(self):
        search_param = input("Enter Flight Name, Date, or Flight ID: ")
        flights = Flight.objects.filter(flight_name__icontains=search_param)
        
        if flights:
            self.stdout.write(self.style.SUCCESS('Flights found:'))
            for flight in flights:
                self.stdout.write(f"Flight ID: {flight.flight_id}, Flight Name: {flight.flight_name}, Date: {flight.date}, Available Seats: {flight.seat_count - flight.booked_seats}")
        else:
            self.stdout.write(self.style.ERROR('No flights found.'))

    def book_ticket(self):
        username = input("Enter your username: ")
        flight_id = input("Enter Flight ID to book a ticket: ")

        try:
            user = User.objects.get(username=username)
            flight = Flight.objects.get(flight_id=flight_id)

            if flight.seat_count > flight.booked_seats:
                Booking.objects.create(user=user, flight=flight)
                flight.booked_seats += 1
                flight.save()
                self.stdout.write(self.style.SUCCESS(f'Ticket booked successfully for {username} on {flight.flight_name}.'))
            else:
                self.stdout.write(self.style.ERROR('Error: Flight not found or no available seats.'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR('User not found.'))
        except Flight.DoesNotExist:
            self.stdout.write(self.style.ERROR('Flight not found.'))

    def admin_login(self):
        admin_username = input("Enter admin username: ")
        admin_password = input("Enter admin password: ")

        admin_user = authenticate(username=admin_username, password=admin_password)

        if admin_user and admin_user.is_staff:
            self.stdout.write(self.style.SUCCESS(f'Admin {admin_username} logged in successfully.'))
            self.admin_menu()
        else:
            self.stdout.write(self.style.ERROR('Invalid admin credentials. Try again.'))

    def admin_menu(self):
        while True:
            self.stdout.write("\nAdmin Menu:\n1. Add Flight\n2. View Bookings\n3. Logout")
            admin_choice = input("Enter your choice: ")

            if admin_choice == '1':
                self.add_flight()
            elif admin_choice == '2':
                self.view_bookings()
            elif admin_choice == '3':
                break
            else:
                self.stdout.write(self.style.ERROR('Invalid choice. Try again.'))

    def add_flight(self):
        flight_id = input("Enter Flight ID: ")
        flight_name = input("Enter Flight Name: ")
        date = input("Enter Flight Date (YYYY-MM-DD): ")

        Flight.objects.create(flight_id=flight_id, flight_name=flight_name, date=date)
        self.stdout.write(self.style.SUCCESS(f'Flight {flight_name} added successfully.'))

    def view_bookings(self):
        bookings = Booking.objects.all()
        if bookings:
            self.stdout.write(self.style.SUCCESS('Bookings:'))
            for booking in bookings:
                self.stdout.write(f"User: {booking.user.username}, Flight: {booking.flight.flight_name}, Date: {booking.flight.date}, Booking Date: {booking.booking_date}")
        else:
            self.stdout.write(self.style.ERROR('No bookings found.'))