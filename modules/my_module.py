# Creating a company class
class Company:

    # Adding a constructor
    def __init__(self,name,location,email,contact):
        self.name = name
        self.location = location
        self.email = email
        self.contact = contact
        
        # Creating a new instince/object
company_one = Company('ELITE BUSINESS', 'WANDEGEYA', 'musiimentaagnes9@gmail.com', +256742443850)
print()


#Complete  and atleast create 2 functions for each:
# the author class  max. properties 5 (name,addres,contact, location, email, book cover---Resolution of the Pandemic)

class Author:
    def __init__(self,name,date_of_authorisation,contact,location,email):
        self.name = name
        self.date_of_authorisation = date_of_authorisation
        self.contact = contact
        self.location = location
        self.email = email


        #Adding a second function.
    def __str__(self):
        return f"{self.name}, {self.date_of_authorisation}, {self.contact}, {self.location}, {self.email
        }"

        # Creating an instince/object
author_details = Author('MUSIIMENTA', 27/2/20024, +256742443850, 'WANDEGEYA', 'musiimentaagnes9@gmail.com')
print(f"The details about the author of the book are as follows: {author_details}")






# Book class max. properties 5   (author, pages, title, sizes,)

class Book:
    def __init__(self,author,pages,title,book_cover,):
        self.author = author
        self.pages = pages
        self.title = title
        self.book_cover = book_cover

        # Adding a second function which must be on the sam line with the first function.
    def __str__(self):
         return f"{self.author}, {self.pages}, {self.title}, {self.book_cover}"
    

# Creating an object/instince    
book_details = Book('MUSIIMENTA', '500 PAGES', 'ELITE OPPORTUNITIES', 'JOB CONNECTIONS')

print(f"The book details are as follows {book_details}")