based on flask tutorial project flaskr

## Notes

Instead of creating a Flask instance globally, create it inside an
application factory function. Configure the application inside such
function.


## Technical details

* `__name__` is the name of the current python module.
* `instance_relative_config=True` config relative to the instance
  folder, to hold data such as config secrets and database file that are
  not to be version controlled.
* `SECRET_KEY`, to keep data safe. Should be overridden with a random
  value on deployment

* `g`, unique for each request
* `current_app`, a placeholder instance object to be called upon when
  flask project instantiates a real one.

* calling order:

1. factory create app in `__init__.py`
2. enable `init_db` in `db.py` to flask cli

* Blueprint
  * to organize related views into groups

* db.execute()
  * use ? for query data values, rather than .format() and insert data directly.
  * using .format() is liable to SQL injection attack.
  * the `?` placeholder is only specific to sqlite3 python module

* validation
* error is reflected by model and controller interactions, not using javascript

* routing mechanism
  * user url_for to navigate to other routes based on param
  * by convention give a same name to both the view and the function
