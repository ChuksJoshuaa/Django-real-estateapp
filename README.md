Real Estate web app (Full Stack Frameworks with Django Project)

> > Fully reponsive Real Estate Application. From development to deployment.

<img src="https://res.cloudinary.com/chuksmbanaso/image/upload/v1638102793/media/Real_Estate/Screenshot_26_rw1nt0.png" title="Real Estate Django" alt="Chuks Real Estate Website">

<img src="https://res.cloudinary.com/chuksmbanaso/image/upload/v1638103160/media/Real_Estate/Screenshot_28_v8cf15.png" title="Real Estate Django" alt="Chuks Real Estate Website">

<img src="https://res.cloudinary.com/chuksmbanaso/image/upload/v1638102784/media/Real_Estate/Screenshot_27_rddd23.png" title="Map" alt="Chuks Real Estate Website">

## Built With

- [Python 3](https://www.python.org/) - Programming language that lets you work quickly and integrate systems more effectively..

- [Javascript](https://www.javascript.com) - It is a text-based programming language used both on the client-side and server-side that allows you to make web pages interactive..

- [Django](https://www.djangoproject.com/) - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design..

- [Cloudinary](https://cloudinary.com/) - Cloudinary provides a secure and comprehensive API for easily uploading media files from server-side code, directly from the browser or from a mobile application..

- [PostgreSQL](https://www.postgresql.org/) - Object-relational database management system (ORDBMS) with an emphasis on extensibility and standards..

- [Bootstrap](https://getbootstrap.com/) - Open source toolkit for developing with HTML, CSS, and JS..

- [folium](https://pypi.org/project/folium/) - folium builds on the data wrangling strengths of the Python ecosystem and the mapping strengths of the Leaflet.js library.. Manipulate your data in Python, then visualize it in a Leaflet map via folium..


## Tools, libraries and resources used:

- [Pillow](https://pillow.readthedocs.io/en/5.3.x/) - Pillow is the friendly PIL fork. PIL is the Python Imaging Library..

- [FontAwesome](https://fontawesome.com/) -  Font Awesome is designed to be used with inline elements (we like the <i> tag for brevity, but using a <span> is more semantically correct)..

- [PgAdmin](https://www.pgadmin.org/) - Open Source administration and development platform for PostgreSQL..

## Deployed With

- [Heroku](https://www.heroku.com/) - It is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud..

- [Gunicorn](https://gunicorn.org/) - Python WSGI HTTP Server for UNIX. It's a pre-fork worker model..

## Getting started

- Clone the repo and cd into the project directory.

- Ensure you have Python 3 and Postgres installed and create a virtual environment and activate it.

- Install dependencies: pip3 install -r requirements.txt.

## Deployment

- Make sure all the necessary python packages are installed.

- Also Make sure requirements.txt and Procfile exist pip3 freeze --local requirements.txt echo web: python app.py > Procfile..

- Create Heroku App, Select Postgres add-on, download Heroku CLI toolbelt, login to heroku (Heroku login), git init, connect git to heroku (heroku git remote -a ), git add ., git commit, git push heroku master.

- heroku run bash

- heroku run python manage.py migrate.

- heroku login
