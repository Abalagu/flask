based on flask tutorial project flaskr

## Notes

Instead of creating a Flask instance globally, create it inside an application factory function.  Configure the application inside such function.  
  
  
## Technical details
* `__name__` is the name of the current python module.
* `instance_relative_config=True` config relative to the instance folder, to hold data such as config secrets and database file that are not to be version controlled.
* `SECRET_KEY`, to keep data safe.  Should be overridden with a random value on deployment
 
 