import os
from app import create_app
my_settings_module = os.getenv("CONFIG_ENV")
app = create_app(my_settings_module)
