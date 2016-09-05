#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), 'templates') #concatenates 2 file names.  The template directory is the directory current file is in and adding templetes to it
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

# hidden_html = """
# <input type="hidden" name="food" value="%s">
# """

# item_html = "<li>%s</li>"

# shopping_list_html = """
# <br>
# <br>
# <h2>Shopping List</h2>
# <ul>
# %s
# </ul>
# """

class Handler(webapp2.RequestHandler): #MainHandler class is defined here
    def write(self, *a, **kw): #method write lets print a string without typing self.response.out.write but with just self.write
        self.response.out.write(*a, **kw) #the default method is get which means when a form is submitted the perameter is added to the URL

    def render_str(self, template, **params): #takes file name and a bunch of extra parameters
        t = jinja_env.get_template(template) #use jinja parameter.  Call get_template and give it a filename file is loaded and stored in jinja template called t
        return t.render(params) #t.render passes in parameters that were passed into that function

    def render(self, template, **kw): #takes template and a bunch of extra parameters
        self.write(self.render_str(template, **kw)) #calls render_str and wraps it in self.write sends it back to the browser

class MainPage(Handler): #inherits from a class called MainHandler
    def get(self):
        items = self.request.get_all("food") #gets all of the get perameters or post perameters a list of all the food perameters
        self.render("shopping_list.html", items = items)


        # output = form_html
        # output_hidden = "" #holding place for hidden inputs

       
        # if items:
        #     output_items = ""
        #     for item in items:
        #         output_hidden += hidden_html % item # for each item in items add to the string hidden html subsituting the food name
        #         output_items += item_html % item

        #     output_shopping = shopping_list_html % output_items
        #     output += output_shopping

        # output = output % output_hidden


        # self.write(output) #if you want to make a basic form you can just return html directly from the Handler here.

class FizzBuzzHandler(Handler):
    def get(self):
        n = self.request.get('n', 0)
        n = n and int(n)
        self.render('fizzbuzz.html', n = n)

app = webapp2.WSGIApplication([
    ('/', MainPage),('/fizzbuzz', FizzBuzzHandler)], debug=True)
