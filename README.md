# Insta light

### Instagram-style Flask application with frontend & backend
[insta-light.ga](http://insta-light.ga)

Features:
 - post list view
 - single post view
 - clickable images and buttons
 - filtering posts by tag, author, and entered text
 - jinja2 template engine
 - bookmarks

Details:
- running with Gunicorn
- loggers for api and frontend
- HTTP 404 Not Found, HTTP 500 Internal Server Error page templates
- correct display of hash tags in short post descriptions using re (html-tags exclusion mechanism)
- changeable style of the bookmark icon: transparent and vice versa, including mouse hover
- redirect to homepage after deleting the last bookmark from the bookmark page
- unit testing for api and dao levels with pytest
- deploying with GitHub Actions
- contenerizing with Docker

![Insta light](https://user-images.githubusercontent.com/106608272/208000166-77d9e37d-6fa9-42d8-877b-ead4d1300b67.gif)
