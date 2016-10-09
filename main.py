#!/usr/bin/env python

# Main class that handles root requests - '/'
# It manages user authentication and sessions
# by extending jinja and webapp2. 
# Key entities


# [START imports]
import os
import urllib
import json

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from hierarchy import tree, node
from collections import OrderedDict

import jinja2
import webapp2

# jinja environment setup
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# classification hierarchy structure
path = os.path.join(os.path.split(__file__)[0], 'statics/lcco.json')
LCC_TREE = tree(path)

STATS = []
with open('statics/stats.json', 'rb') as stat_file:
    STATS = dict(json.load(stat_file))

# loading cumm_Stats
with open('statics/cumm_stats.json', 'rb') as cumm_file:
    CSTATS = dict(json.load(cumm_file))

# master frequency dictionary
fdict = OrderedDict()
with open('statics/master_frequency.json', 'rb') as freq_file:
    fdict =  json.load(freq_file)

# [END imports]

# [START tree]
class Tree(webapp2.RequestHandler):

    def get(self):

        req_node = self.request.get('request')
        current_node = LCC_TREE.getNode(req_node)

        resp = {'description' : current_node.getDesc(), 'LCCN' : current_node.getLCCN()}
        children = current_node.getChildren()
        child_list = []

        if children:
            for child in children:
                child_list.append( {'LCCN' : child.getLCCN(), 'description' : child.getDesc()} )

        resp['children'] = child_list

        if current_node:
            self.response.write(json.dumps(resp))

        else:
            self.response.write('No such LCC #')
# [END tree]


# [START stats]

class Stats(webapp2.RequestHandler):

    # this class handles stat
    # requests for each node
    def get(self):

        if STATS:
            self.response.write(json.dumps(STATS))

        else:
            self.response.error(404)

# [END stats]


# [START Cstats]

class CStats(webapp2.RequestHandler):

    # this class handles stat
    # requests for each node
    def get(self):

        if CSTATS:
            self.response.write(json.dumps(CSTATS))

        else:
            self.response.error(404)

# [END Cstats]

class Frequency(webapp2.RequestHandler):

    # this class serves the 
    # word frequency document

    def get(self):

        req = self.request.get('node')

        try:
            self.response.write(fdict[req])

        except Exception, e:
            print e
            self.response.write(0)

# [START entities]

class Dataset(ndb.Model):
    user     = ndb.StringProperty()
    blob_key = ndb.BlobKeyProperty()



# [START dataset_upload_handler]
class DatasetUploadHandler(webapp2.RequestHandler):

    def get(self):

        user = users.get_current_user()
        if user:
            upload_url = blobstore.create_upload_url('/dataset_upload')

            template_values = {
                'upload_url': upload_url
            }

            # building response from template
            template = JINJA_ENVIRONMENT.get_template('webapp/dataset_upload.html')
            self.response.write(template.render(template_values))

        else:
            self.response.write('Please login to upload files')


# [END dataset_upload_handler]

# [START dataset_upload]

# this class handles uploads of dataset files
# and stores it in the blob store.
# These files are processed to extract words
class DatasetUpload(blobstore_handlers.BlobstoreUploadHandler):

    def post(self):

        try:

            dataset = self.get_uploads()[0]
            user_dataset = Dataset(
                user=users.get_current_user().user_id(),
                blob_key=dataset.key())
            user_dataset.put()

            self.redirect('/')

        except Exception, e:
            print e
            self.error(500)            


# [END dataset_upload]

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
    ('/lcco', Tree ),
    ('/upload',DatasetUploadHandler),
    ('/dataset_upload', DatasetUpload),
    ('/stats', Stats),
    ('/cumm_stats', CStats),
    ('/frequency', Frequency),
    ('/', MainPage),
], debug=True)
# [END app]
