"""
dashboard - Our Opal Application
"""
from opal.core import application

class Application(application.OpalApplication):
    javascripts   = [
        'js/dashboard/routes.js',
        'js/opal/controllers/discharge.js',
        # Uncomment this if you want to implement custom dynamic flows.
        # 'js/dashboard/flow.js',
    ]
    styles = [
        "css/dashboard.css",
    ]
