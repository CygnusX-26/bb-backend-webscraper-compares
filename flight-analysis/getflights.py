import requests
from bs4 import BeautifulSoup
from duffel_api import Duffel

from src.google_flight_analysis.scrape import *
# results = Scrape('AAA', 'ACN', '2024-03-03')
results = Scrape('ORD', 'SFO', '2024-03-03')

# print(results.url)
ScrapeObjects(results)
print(results.data.iloc[23]) #see data of the 23rd flight returned for example
print(results.data.keys()) # avaliable keys
def flight(data):

        flight = {}

        flight.info = {
            #'id': offer.id,
            'airline': data['Airline(s)'],
            'airline_code': offer.owner.iata_code,
            'airline_icon': f'https://assets.duffel.com/img/airlines/for-light-background/full-color-logo/{offer.owner.iata_code}.svg',
            'airline_full_logo': f'https://assets.duffel.com/img/airlines/for-light-background/full-color-lockup/{offer.owner.iata_code}.svg'
        }
        try:
            self.info['aircraft'] = segment.aircraft.name
        except AttributeError:
            self.info['aircraft'] = 'Plane'
        try:
            self.info['cabin_class_name'] = slice1.fare_brand_name
        except AttributeError:
            self.info['cabin_class_name'] = 'Likely: Economy'

        self.time = {
            'departing_at': data['Departure datetime'],
            'origin_time_zone': segment.destination.time_zone, # fix
            'arriving_at': data['Arrival datetime'],
            'destination_time_zone': segment.destination.time_zone,
            'duration': segment.duration
        }
        self.convert_duration()
        self.convert_timezone()

        self.location = {
            'origin_name': segment.origin.name,
            'origin_code': data['Origin'],
            'origin_city': airports_data[segment.origin.iata_code]['city'],
            'destination_name': segment.destination.name,
            'destination_code': data['Destination'],
            'destination_city': airports_data[segment.destination.iata_code]['city'],
        }
        self.cost = {
            'total_amount': float(data['Price ($)']),
            'total_currency': offer.total_currency,
            'total_emissions_kg': data['CO2 Emission (kg)']
        }
        self.baggage = {
            'carry_on': 0,
            'checked': 0,
            'max_add_checked': 0,
            'cost_add_checked': 0.0,
        }
        for baggage in passenger1.baggages:
            if baggage.type == 'carry_on':
                self.baggage['carry_on'] = int(baggage.quantity)
            elif baggage.type == 'checked':
                self.baggage['checked'] = int(baggage.quantity)
            
        # the outer flight is always the first one, connecting_flight is the second one
        self.connecting_flight = None


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

