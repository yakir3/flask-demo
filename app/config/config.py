import os

if os.getenv("FLASK_ENV") == "development":
    from .development import *
elif os.getenv("FLASK_ENV") == "production":
    from .production import *
else:
    raise KeyError