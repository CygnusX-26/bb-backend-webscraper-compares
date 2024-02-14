import requests
from bs4 import BeautifulSoup
from duffel_api import Duffel

from src.google_flight_analysis.scrape import *
results = Scrape('AAA', 'ACN', '2024-03-03')
print(results.url)
ScrapeObjects(results)
print(results.data['Price ($)']) #see data

# toggle between DUFFEL_API_KEY/DUFFEL_API_TEST_KEY
# TODO: toggle after debug
duffel = Duffel(access_token = 'duffel_live_F2wL-aMXvC_KSgPwJo4rfJw9eK7GZ8ibxPGxphFV8Ce') # TEST FLIGHTS FOR YOU TO TRY


_to = 'BOS'
_from = 'ORD'
_date = '2024-03-04'

# r = requests.get(f'https://www.google.com/travel/flights?q=Flights%20to%20{_to}%20from%20{_from}%20on%20{_date}%20with%20one%20adult%20economy%20class%20oneway%20United_Airlines%20nonstop')

# soup = BeautifulSoup(r.text, 'html.parser')

# for li in soup.find_all('ul', class_='Rk10dc'):
#     for div in li.find_all('div', class_='gQ6yfe m7VU8c'):
#         for div2 in div.find_all('div', class_='yR1fYc'):
#             for div3 in div2.find_all('div', class_='mxvQLc ceis6c uj4xv uVdL1c A8qKrc'):
#                 print(div3.text)
#         break
#     break


# slice = [{
#         'origin': _from,
#         'destination': _to,
#         'departure_date': _date
#     }]

# offer_request = (
#         duffel.offer_requests.create()
#         .passengers([{'type': 'adult'}])
#         .slices(slice)
#         .cabin_class('economy')
#         .execute()
# )

# offers = duffel.offers.list(
#     offer_request.id, sort='total_amount', max_connections=0 # limit=max_flights_per_request '1' connections str before
# )

# for offer in offers:
#     if (offer.owner.name == 'United Airlines'):
#         print(offer.slices[0].segments[0].origin.iata_code, offer.slices[0].segments[0].departing_at, offer.owner.name)

