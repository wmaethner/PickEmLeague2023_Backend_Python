# Introduction 
TODO: Give a short introduction of your project. Let this section explain the objectives or the motivation behind this project. 

## Project Structure


| Directory Path     | Description |
| ----------- | ----------- |
| ./migrations | Holds *alembic* configuration and other database migration related configuration       |
| ./migrations/versions   | Contains database migrations |
| .src/"project"/apis | Holds domain organized endpoints and business logic. For example in ../apis/auth.. there will be auth related endpoints and functionality such as registering, login, logout, etc. |
| .src/"project"/models | Holds application models such as User. Models will contain the database definitions (table name, columns, etc) which is used by alembic when generating migrations. They will also contain model specific functionality (instance and class methods).  |
| .src/"project"/schemas | Holds model schema definitions. These should match closely to the model definitions, but instead uses Marshmallow to define these schemas. Marshmallow and these schemas can then be used in the apis to easily define the expected format for input data and output data. |

# Getting Started
## Installation Process
1. Clone git repo
2. Create virtual environment
```console
python3 -m venv .venv
```
3. Activate virtual environment
```console
. .venv/bin/activate
```
4. Install dependencies
```console
pip install -r requirements.txt
```
5. Start postgres and create local database (match db name defined in config)
6. Run database migrations
```console
flask db upgrade
```

## Running locally
1. Run server (from project root)
```console
flask run
```
2. Swagger documentation at [http://127.0.0.1:5000/api/swagger](http://127.0.0.1:5000/api/swagger)



TODO: Guide users through getting your code up and running on their own system. In this section you can talk about:
1.	Installation process
2.	Software dependencies
3.	Latest releases
4.	API references

# Build and Test
TODO: Describe and show how to build your code and run the tests. 

## Creating Migrations
Run
```console
flask db migrate -m "Migration Message"
```

# Contribute
TODO: Explain how other users and developers can contribute to make your code better. 

If you want to learn more about creating good readme files then refer the following [guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops). You can also seek inspiration from the below readme files:
- [ASP.NET Core](https://github.com/aspnet/Home)
- [Visual Studio Code](https://github.com/Microsoft/vscode)
- [Chakra Core](https://github.com/Microsoft/ChakraCore)

# Helpful Tutorials and Articles
* Flask - [https://flask.palletsprojects.com/en/2.3.x/](https://flask.palletsprojects.com/en/2.3.x/)
* Flask Restx - [https://flask-restx.readthedocs.io/en/latest/index.html](https://flask-restx.readthedocs.io/en/latest/index.html)
* Flask Api with JWT Tutorial - [https://aaronluna.dev/series/flask-api-tutorial/part-1/](https://aaronluna.dev/series/flask-api-tutorial/part-1/)
* Adding enums to data models - [https://michaelcho.me/article/using-python-enums-in-sqlalchemy-models](https://michaelcho.me/article/using-python-enums-in-sqlalchemy-models)


# Things to add
- Unit tests
  - Look into fuzzy unit testing as well ([https://hypothesis.readthedocs.io/en/latest/](https://hypothesis.readthedocs.io/en/latest/))
- Autoformatting with [https://black.readthedocs.io/en/stable/](https://black.readthedocs.io/en/stable/)
- Documentation with [https://numpydoc.readthedocs.io/en/latest/format.html](https://numpydoc.readthedocs.io/en/latest/format.html)
- Simplified classes with attrs [https://www.attrs.org/en/stable/](https://www.attrs.org/en/stable/)
- Todo list associated with user
