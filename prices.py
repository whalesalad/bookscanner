import pprint
import csv
import sys

import numpy
import isbndb

FIELD_ORDER = ['isbn', 'title', 'price', 'unknown']

def reject_outliers(data):
  return data[abs(data - numpy.mean(data)) < numpy.std(data)]

def get_book_info(isbn):
  """
  Returns the title and the average price of the book specified by the isbn.

  """
  book = isbndb.get_book(isbn)
  sellers = isbndb.get_sellers(isbn)

  prices = numpy.array([s[1] for s in sellers])
  purified = reject_outliers(prices)

  if len(purified):
    prices = purified

  avg_price = round(numpy.mean(prices), 2)

  return (book['title'], avg_price, )

def read_csv(path):
  with open(path) as f:
    return csv.DictReader(f.readlines())

def write_csv(path, books):
  with open(path, 'w') as w:
    writer = csv.DictWriter(w, fieldnames=FIELD_ORDER)
    writer.writeheader()

    for book in books:
      writer.writerow(book)

def update_csv(path, overwrite=False):
  """
  Update the CSV file at the specified path by iterating over
  each row and updating the title/price.

  """
  new_books = []

  for b in read_csv(path):
    book = b.copy()

    try:
      title, price = get_book_info(book['isbn'])
      book['title'] = title
      book['price'] = price
      book['unknown'] = False

    except:
      book['unknown'] = True

    new_books.append(book)

  write_csv(path, new_books)

  print "Finished updating %s book(s) successfully." % len(new_books)

if __name__ == "__main__":
  if len(sys.argv) <= 1:
    print "Specify the path to a CSV file to process."
    sys.exit(1)

  update_csv(sys.argv[1])
