Mobility App Framework
======================

This is a barebones framework that you can use to build your own web
application on top of the Cisco Mobility Services Engine (MSE) platform.


Requirements
------------

* Python v2.7.8 (https://www.python.org/download/releases/2.7.8)

* Pip (http://pip.readthedocs.org/en/latest/installing.html)


Installation
------------

1. Get this project:

   * via git: git clone https://github.com/relaxdiego/mobility.git

   * via a zip file: https://github.com/relaxdiego/mobility/releases

2. Run the following in your terminal:

   cd <foldername>

   pip install -r requirements.txt

3. Copy `config.yml.example` to `config.yml` in the same directory. Feel
   free to look inside the file and understand what the settings are.

Run the Sample App
------------------

1. Run the following in your terminal:

   python mobility/app/main.py

2. Point your browser to http://localhost:5000


Edit the Sample App
-------------------

* The main file is in mobility/app/main.py. Start there.

* Each function decorated with @app.route(...) is accessible
  via the browser. The value between the parentheses determines
  how it is accessed through the browser. For example, if the
  decorator is @app.route('/get_maps'), then you can access
  that method via http://localhost:5000/get_maps.

* Try creating a new route (e.g. /get_clients) and render a
  static template to begin with. Get comfortable with that and
  then move on to picking an API endpoint, getting data from
  that and then displaying it dynamically in your template.
  Use get_maps() and maps.html as your references.


