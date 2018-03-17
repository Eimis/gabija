# gabija

![Preview](https://i.imgur.com/XV5Aewk.png "Preview")

A simple shopping list application

Requirements:

* pip `9.0.1`
* bower `1.8.0`

Setup:

* Clone this repo
* create a virtual environment `virtualenv virtualenv`
* run `source virtual/bin/activate` to activate your fresh virtual environment
* run `pip install -r requirements.txt` to install backend dependencies
* run `bower install` to install frontend dependencies
* run `cd gabija/ && ./manage.py migrate` to run migrations
* run `./manage.py collectstatic`
* `./manage.py runserver`
* Visit http://localhost:8000/#/ (don't forget the # character!)

Key points:

* The app starts in online mode initially, but works in offline mode as well
* Every action is synced with browser's localStorage
* Once one goes from offline to online mode, items (or actions that have been
  taken with the items) are synced to backend database
* In order to test this, you can add some items in online mode, switch to
  offline mode (even turn off Django's runserver command), change some of the
  items (mark as purchased, add new ones or remove existing ones), then get
  back to online mode again (don't forget to start Django's server with
  `./manage.py runserver` if you turned it offpreviously) and everyhing will
  be synced with database.

Some technical notes:

* Backend is implemented as a RESTful API with Django rest framework,
  serializers and etc.
* Frontend is implemented as a fully functional Angular-based Single page
  application with pluggable components approach (with such approach, every
  component has a `*.model.js`, `*.component.js`, `*.template.html`, `*.style.css`
  file), so that means that one can pull any component (in this case:
  `<shopping-list></shopping-list>` component) from anywhere and place it
  anywhere and everything should work automatically.
* To run API tests, run `./manage.py test`. Factoryboy is used for fixtures.
