#!/usr/bin/env python

# Main class that handles root requests - '/'
# It manages user authentication and sessions
# by extending jinja and webapp2. 
# Key entities


# [START imports]
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

# jinja environment setup
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]

# [START main_page]
class MainPage(webapp2.RequestHandler):

    def get(self):

        # checking for currently signed in user
        # prompting signin if user not signed in.

        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'user': user,
            'url': url,
            'url_linktext': url_linktext,
        }

        # building response from template
        template = JINJA_ENVIRONMENT.get_template('webapp/index.html')
        self.response.write(template.render(template_values))
# [END main_page]


# [START app]

# debug flag should be set to 
# to false when deploying.

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
# [END app]
