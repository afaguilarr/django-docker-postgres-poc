# DJANGO-DOCKER POC!

The idea of this project is to have a POC for a Django web app.
I guess this is only for the back-end.

To start the project for the first time execute `docker-compose build` and then `docker-compose up`.

To start the project just run `docker-compose up` inside this directory or `docker-compose up -d` to run the containers in the background.

To stop the containers just run `docker-compose stop` inside this directory.

To clear the containers, networks and volumes (clear the database) run `docker-compose down` inside this directory.

The web app is exposed in the port 8000, so you can hit it by using http://localhost:8000.

If a new dependency is added to the requirements.txt file, `docker-compose build` has to be run again before starting the containers.

### Commands

To run a console command inside the container just run it as: `sudo docker-compose run {{service}} {{command}}`.

e.g: `sudo docker-compose run web python manage.py startapp hello_world`

To connect to the postgres database use `sudo docker-compose run psql`.

To change the database, add/ change the models in `models.py` and execute the `sudo docker-compose run web python manage.py makemigrations hello_world` command, the next time you start the containers, the migration will be applied.

And that's it.

### Test

To test this API you can use the postman collection Django_Docker_POC.postman_collection.json