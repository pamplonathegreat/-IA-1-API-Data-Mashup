Documentation

Project Description
-The project is a locally hosted Django application that searches book by Title
-It combines book metadata (e.g. title, description, and date released) and cover images into a single result
-It presents a computed field which is involved in the number of charaters in the book title

APIs Used
For book name
-OpenLibrary.org. (2025). Search API | Open Library. Openlibrary.org. https://openlibrary.org/dev/docs/api/search

For book cover
-OpenLibrary.org. (2024). Open Library Covers API | Open Library. Openlibrary.org. https://openlibrary.org/dev/docs/api/covers

‌How to set-up locally
***Important note: Django and Python must be configured and in set-up with the IDE used already

1. Clone the Repository and Project
2. Install Dependencies
    pip install django requests
3. Run Django migrations
    python manage.py migrate
4. Start Server
    python manage.py runserver


How the Data Join Works
-The books API which contains the book details returns the Cover ID, therefore matching and returning the book detail with the book cover 

Known Limitations
-It shows first 5 search results only
-No advance filtering
-It has data inconsistencies such as there are books without a book cover saved in the API

AI Usage Note
-Fixing Syntax and Error explanation
**    return check_method()
  File "C:\Users\pampl\Desktop\MSYS 22\msys22\Lib\site-packages\django\urls\resolvers.py", line 517, in check
    messages.extend(check_resolver(pattern))
                    ~~~~~~~~~~~~~~^^^^^^^^^
RecursionError: maximum recursion depth exceeded

**C:\Users\pampl\AppData\Local\Programs\Python\Python313\python.exe: can't open file 'C:\\Users\\pampl\\Desktop\\MSYS 22\\manage.py': [Errno 2] No such file or directory