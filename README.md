# idp-project : ADOPT A PUPPY

## System & Architecture

### Technologies & TOOLS

* **Docker**
* **Python-Flask**
* **Python-Flask-Migrate**
* **Prometheus**
* **Apache HTTP Web Server**
* **Vanilla JavaScript**
* **HTML**
* **GIT**

### Services

#### **1. The client is an Apache Web Server implemented with Vanilla JS & HTML**
		The user opens the browser and can access a website for adopting dogs. He/she can see there 
	a list of all the puppies in the shelter, where they can find information regarding the dogs
	(their description, age, name and if they are available to adopt at the moment or not).
		If an user is ready to adopt a puppy, he/she can fill up a form for adoption.
#### **2. The server is implemented with Python-Flask**
		The server takes care of the CRUD principles implemented for the db models. Moreover, it 
	represents the logic of storing the information regarding puppies, owners and their matches.
#### **3. The persistent database is implemented in SQLAlchemy with Python-Flask-Migrate**
		The Flask-Migrate extension uses SQLAlchemy package that allows applications to manage a database 
	using high-level entities such as classes, objects and methods instead of tables and SQL. 
	This extension is a Flask wrapper for Alembic, a database migration framework for SQLAlchemy.
#### **4. The dbadmin is implemented in Python3**
		The db admin is able to manage the database, for example to add more puppies to be put up for adoption.
#### **5. The monitoring service is using Prometheus**
		Prometheus is an open-source toolkit of monitoring that collects metrics using the implemented HTTP endpoints.


