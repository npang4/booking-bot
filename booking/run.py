from booking import Booking
import time


with Booking() as bot:
    bot.land_first_page()
    # bot.change_currency(currency='EUR')
    bot.select_place_to_go('New York')
    bot.select_dates(checkin_date="2022-12-30", checkout_date="2023-01-10")

time.sleep(20)