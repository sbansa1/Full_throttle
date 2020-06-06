### Assignment for programming test Currently doing in flask before learning Django

```text
- In the app folder you will find a factory pattern to instantiate the flask application
- Manage.py which is in the root of the application will have to code for initializing the database and create tables

- To run the project make sure you have docker installed on your machine. The below command will build the project on 
local docker instance. 
```

```commandline
docker-compose up --build

```

```text
Once the project is build then execute the following commands
```
```commandline
docker-compose exec test-service python manage.py create_db
docker-compose exec test-service python manage.py seed_db
```

```text
The above command will create a database inside the postgres container and will seed the database.
```

```text
Navigate to the path on your local ! [link](http://localhost:5003/doc)
which will open a swagger doc and you can then play with the api.
```

```text
Link to the Heroku

![Heroku-app](http://young-castle-99899.herokuapp.com/doc)

```
