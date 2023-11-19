# Presidio_Console-Based_Flight-Ticket-Booking-Application
This is a console based Flight Ticket Booking Application on the requirements given by Presidio for the Round 2 - Presidio Recruitment Drive (Made using Django)

## Requirements
## **Problem Statement #2**

## **Optional**: Database: MySQL or any other of your choice
**Types of Users**: User and Admin
## **User Use Cases**:
- **Login**: Users should be able to log in, and the application should check credentials
with the database or local storage (list or array).
- **Signup**: Implement a signup feature to add new users to the database or an array.
- **Search Flight**: Users should be able to search for flights using Flight name/ Date/Flight Number
- **Book Tickets**: Allow users to book tickets based on availability, assuming the default seat count is 60 for all flights.

## **Admin Use Cases**:
- **Login**: Admins should be able to log in.
- **Add Flights**: Admins should have the ability to add new flights to the system.
- **View Bookings**: Admins should be able to view bookings with the option to filter based on: Flight ID/Flight Name/ Date

## **The way I implemented the project**
I have used Django to implement this console based Flight Ticket Booking Application.

### **Prerequisites**

- Python (3.x recommended)
- Django

### **Implement this on your device**

- Install Python (3.x recommended) and Django
- Clone the repository or download the zip File
- Extract the Zip file
- Navigate to the project and open cmd prompt
- **Run migrations:**
  - `python manage.py migrate`
- **Create a superuser:**
  - `python manage.py createsuperuser`
  - Create your own Admin Credentials. This will be used as your admin login for the console based activities moreover also used in browser based admin console (Provided by Django).
- **Run the development server:**
  - `python manage.py runserver`
  - Open your browser and go to `<url displayed after running the above code>/admin/`. Log in with the superuser credentials to access the Django admin interface.
- **Run console based system:**
    - `python manage.py console_booking`

# Now the application is running in your device


# Features Implemented

## **Optional**: Database: MySQL or any other of your choice (Used sqlite3) Done✅

## **Types of Users**: User and Admin Done✅

## **User Use Cases**:
- **Login**: Users should be able to log in, and the application should check credentials
with the database or local storage (list or array). Done✅
- **Signup**: Implement a signup feature to add new users to the database or an array. Done✅
- **Search Flight**: Users should be able to search for flights using Flight name/ Date/Flight Number. Done✅
- **Book Tickets**: Allow users to book tickets based on availability, assuming the default seat count is 60 for all flights. Done✅

## **Admin Use Cases**:
- **Login**: Admins should be able to log in. Done✅
- **Add Flights**: Admins should have the ability to add new flights to the system. Done✅
- **View Bookings**: Admins should be able to view bookings with the option to filter based on: Flight ID/Flight Name/ Date. Done✅

# Output


