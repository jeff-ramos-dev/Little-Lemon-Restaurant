# Little Lemon Restaurant

*Make sure to change database settings to match your local MYSQL database*

## Endpoints to test

| Name | Endpoint |
|---|---|
| Home | http://127.0.0.1:8000/ |
| About | http://127.0.0.1:8000/about/ |
| Menu | http://127.0.0.1:8000/menu/ |
| Book | http://127.0.0.1:8000/book/ |
| Bookings | http://127.0.0.1:8000/bookings/?date={date}
| Reservations | http://127.0.0.1:8000/reservations/ |
| Menu API view | http://127.0.0.1:8000/api/menu/ |
| Menu Item API view | http://127.0.0.1:8000/menu/{menuItemId}/ |
| Bookings API view | http://127.0.0.1:8000/api/bookings/tables/ |
| Booking API view | http://127.0.0.1:8000/api/bookings/tables/{bookingId}/ |
| Users | http://127.0.0.1:8000/auth/users/ |
| User Token Creation | http://127.0.0.1:8000/auth/token/login/ |
| Admin portal | http://127.0.0.1:8000/admin/ |





Grading Criteria:
1. ***Is the app added to the installed apps list in the settings file?***
    - Check in littlelemon/settings.py under INSTALLED_APPS.

2. ***Is the database configuration updated inside the settings file?***
    - Check in littlelemon/settings.py under DATABASES.

3. ***Were migrations performed?***
    - Run the command:
    `python manage.py makemigrations`
    - Verify that "No changes detected" is returned.

4. ***Are there three fields in the booking form: First name, Reservation date and Reservation slot?***
    - Check in restaurant/models.py.

5. ***Does a date selector open up when you click on the reservation date field on the booking form?***
    - Navigate to 127.0.0.1:8000/book/ and click calendar icon in the Reservation Date input.

6. ***Are all the bookings available as JSON data on the reservations page?***
    - Navigate to 127.0.0.1:8000/reservations/ and click on the "View JSON" button.

7. ***Is duplicate booking prohibited on a specific date if the time is already booked?***
    - Navigate to 127.0.0.1:8000/book/ and fill in all the fields.
    - Hit Reserve.
    - Choose the same date as the booking you just made.
    - Try to select the same time as the booking you just made.

8. ***Does changing the date refresh the booking data?***
    - Navigate to 127.0.0.1:8000/book/ and change the Reservation Date.
    - Check on the right to see if bookings change

9. ***Is a duplicate booking on a specific date and time unavailable if the slot is already booked?***
    - Navigate to 127.0.0.1:8000/book/ and fill in all the fields.
    - Hit Reserve.
    - Choose the same date as the booking you just made.
    - Try to select the same time as the booking you just made.

10. ***Can you display bookings for a specific date using the API?***
    - Navigate to 127.0.0.1:8000/bookings/?date=<YYYY-MM-DD> to see bookings on a given date

11. ***If there is no booking, does a No Booking message show for that date?***
    - Navigate to 127.0.0.1:8000/book/ and choose a date that has no bookings
    - Check on the right to see if "No bookings" is displayed

12. ***Was fetch API used to retrieve data from the API?***
    - Check in restaurant/templates/book.html under the script tag inside of the getBookings() function

13. ***Is the current date automatically selected when you open the booking form?***
    - Navigate to 127.0.0.1:8000/book/ and check that the Reservation Date field is already filled with today's date.