import sys
import requests

try:
  ISBNDB_ACCESS_KEY = os.environ['ISBNDB_ACCESS_KEY']
except:
  print '[isbndb] ISBNDB_ACCESS_KEY must be defined.'
  sys.exit(1)

BASE_URL = "http://isbndb.com/api/v2/json/%s" % ISBNDB_ACCESS_KEY

def purify_isbn(isbn):
  return isbn.replace('-', '')


def get_book(isbn):
  isbn = purify_isbn(isbn)
  req = requests.get(BASE_URL + "/book/%s" % isbn)
  return req.json()['data'][0]


def clean_seller(result):
  # Skip sellers that are not 'murrican
  if result.get('currency_code') != 'USD':
    return None

  # Skip new books
  if int(result.get('is_new')) == 1:
    return None

  return [result.get('store_id'), float(result.get('price'))]


def get_sellers(isbn):
  isbn = purify_isbn(isbn)
  req = requests.get(BASE_URL + "/prices/%s" % isbn)

  response = req.json()

  sellers = []

  for price_result in response.get('data'):
    sellers.append(clean_seller(price_result))

  return filter(None, sellers)
