Mini Cloud Drive

A web-based file storage system built using **Python Django**.  
Users can register, log in, upload, view, and preview files in a clean and professional interface.

**Features**

User Authentication: Register, log in, and log out securely.  
File Uploads: Upload PDFs, images, documents, and more.  
File Preview: View files directly before downloading.  
Sorting & Filtering: Filter files by extension and sort alphabetically or by date.  
*Modern UI: Simple, clean, and professional dashboard with custom CSS.  

Tech Stack Used

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite (default Django database)
- **Libraries:** Django built-in authentication

**File Architecture:** 

mini_drive_project/
│
├── mini_drive/ # Main project configuration files
│ ├── settings.py # Project settings and configuration
│ ├── urls.py # Root URL routing
│ └── wsgi.py # WSGI entry point
│
├── storage/ # Core application
│ ├── models.py # Defines the Document model
│ ├── views.py # Contains all backend logic
│ ├── urls.py # App-level URL patterns
│ ├── templates/ # HTML templates
│ │ ├── dashboard.html
│ │ ├── document_list.html
│ │ ├── upload_document.html
│ │ ├── login.html
│ │ └── register.html
│ └── static/ # CSS and static assets
│ └── css/
│ └── style.css
│
├── db.sqlite3 # Database file
├── manage.py # Django management script
├── requirements.txt 
├── Screenshots

**Problems Faced & Solutions**

During the development of this project, several challenges were encountered.  
One of the first issues was a "404 error for the login page". 
This happened because Django’s default authentication redirection conflicted with the custom routes.
The issue was resolved by creating dedicated `login` and `register` views and updating the URLs accordingly.
Another problem was the "no such table: storage_document” error. This occurred because the database tables were not created properly.
The solution involved running `python manage.py makemigrations` and `python manage.py migrate` to ensure all models were synced with the database.
There were also syntax errors in my html files, which were fixed by carefully checking the Django template logic and ensuring correct spacing and syntax.  
The CSS was not being applied properly was another issue. The fix was to correctly link static files using `{% load static %}` and the `{% static 'css/style.css' %}` tag in the HTML templates.  
Also, the file preview feature initially didn’t work. i took the help of AI to fix that issue.
After implementing the logout function, users were being redirected to non-existent pages that showed some django errors.
This was solved by updating the redirect URLs in the settings.py and proper navigation across pages.

**Learnings**

- Learned Django authentication, models, and templates.  
- Understood how URLs and migrations work.  
- Improved debugging skills.  

**Final Output**

Mini Cloud Drive with authentication, upload, preview, and filter features — styled with a modern UI and smooth navigation.


**Author:** Krrish Sachin Kathe (Roll No. 310, Class: SE IT-A1) (Worked on this project as a single person) 
**Project:** Mini Cloud Drive
