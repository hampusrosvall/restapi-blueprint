# Introduction 

This is my attempt of building a blueprint of a Flask RESTAPI application that sits behind a Nginx reverse proxy using the Flask-RESTful extension and Flask-SQLAlchemy. 

# Running the application 

Simply `cd ~/<dir_of_docker-compose.yaml_file>` and run `docker-compose up` in order to run the services defined in the `docker-compose.yml` file. The Nginx reverse proxy listens to port 80 and in order to verify the connection run: `curl localhost` in order to access the `Health` resource and response should be `{"message" : "Feeling good!"}`. 

# Credits 
The design of the RESTful API is credited to the following course on [Udemy](https://www.udemy.com/course/rest-api-flask-and-python/) and [this](https://www.youtube.com/watch?v=prlixoDIfrc) tutorial on YouTube in order to configure uWSGI. 

# TODO
- Extend the application with a PostgreSQL database 