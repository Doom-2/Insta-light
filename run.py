from flask import Flask, render_template
from logs import logger_main

# Importing a blueprints
from main.views import main_blueprint
from posts.views import post_blueprint
from api.views import api_blueprint

# Create a flask instance
app = Flask(__name__, static_folder='static')
# In order to use Cyrillic characters
app.config['JSON_AS_ASCII'] = False

# Registering a blueprints
app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def page_not_found(error):
    logger_main.error('404 Page not found')
    return render_template('404-page_not_found.html')


@app.errorhandler(500)
def internal_server_error(error):
    logger_main.error('500 Internal server error')
    return render_template('500-internal-error.html')


# Starting the server only if the file is running and not imported
if __name__ == "__main__":
    app.run(host="localhost", port=4000)
