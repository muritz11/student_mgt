# tis will serves as a pointer to Flask, informing it about the existence of our application and to run the application

# we import the app module from the app file, what we r basically doing is importing the app object in the init file.
from app import app


if __name__ == "__main__":
    app.run()
    app.run(debug=True)
