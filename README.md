# Get Book Prices

This project started when I realized I had a huge collection of books that I needed to sell and wanted to do it in an efficient manner.

### TODO

- Update this README and explain how it works.
- Explain the pain in the ass it is to use OpenCV to try and do fast barcode scanning to grab these ISBN's automagically.

### tl;dr

Given a CSV with these headers:

    isbn, title, price, unknown

And a [ISBNdb.com API Key](isbndb.com), update the CSV with titles and average pricing from the interwebs.

Here is an example of some of the books I have in my test list:

    isbn,title,price,unknown
    978-0-446-58200-1,Bo's Lasting Lessons,7.01,False
    978-0-553-41802-6,The Martian,13.03,False
    978-0-06-083865-2,A people's history of the United States,10.02,False
    0-452-01187-6,Atlas Shrugged,9.36,False
    0-595-40970-9,"Iron Fist, Lead Foot",15.0,False
    978-1-55017-041-2,Denison's Ice Road,14.16,False
