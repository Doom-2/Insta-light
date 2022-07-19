from flask import Flask

# Importing a blueprints
from main.views import main_blueprint
from posts.views import post_blueprint


# Create a flask instance
app = Flask(__name__)

# Registering a blueprints
app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)

# Starting the server only if the file is running and not imported
if __name__ == "__main__":
    app.run()
