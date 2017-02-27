# Get Book Prices

This project started when I realized I had a huge collection of books that I needed to sell and wanted to do it in an efficient manner.

### tl;dr

Given a CSV with these headers and a bunch of ISBN numbers filled in:

    isbn, title, price, unknown

Update the CSV with a title and the average *used* price from the interwebs – via the [ISBNdb.com API](http://isbndb.com/api/v2/docs).

Here is an example of some of the books I have in my test list and the data that came back:

    isbn,title,price,unknown
    978-0-446-58200-1,Bo's Lasting Lessons,7.01,False
    978-0-553-41802-6,The Martian,13.03,False
    978-0-06-083865-2,A people's history of the United States,10.02,False
    0-452-01187-6,Atlas Shrugged,9.36,False
    0-595-40970-9,"Iron Fist, Lead Foot",15.0,False
    978-1-55017-041-2,Denison's Ice Road,14.16,False


### TODO

- Update this README and explain how it all works.
- A lot of the pricing is fucked, there is work to be done there.
- Explain the pain in the ass it is to use OpenCV to try and do fast barcode scanning to grab these ISBN's automagically.
- Would be fun to cleanup the ISBNdb micro-lib to instantiate a `Book` and ask for things like `book.prices`, `book.title`, etc... so that the code can be de-duped.
