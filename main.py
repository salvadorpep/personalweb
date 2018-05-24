#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Por defecto
import os
import jinja2
import webapp2

#Los que yo escojo
from models import Work


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class User():
    def __init__(self, name, lname, city, age, id):
        self.name = name
        self.lname = lname
        self.city = city
        self.age = age
        self.id = id

class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        # if params is None:
        #     params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        params = {}
        return self.render_template("index.html", params=params)


class WorksListHandler(BaseHandler):
    def get(self):
        params = {}
        return self.render_template("works_list.html", params=params)


class WorkDetailsHandler(BaseHandler):
    def get(self, work_id):
        work = Work.get_by_id(int(work_id))
        params = {"work": work}
        return self.render_template("work.html", params=params)


class WorkEditHandler(BaseHandler):
    def get(self, work_id):
        work = Work.get_by_id(int(work_id))
        params = {"work": work}
        return self.render_template("work_edit.html", params=params)

    def post(self, message_id):
        new_text = self.request.get("some_text")
            work = Work.get_by_id(int(work_id))
            work.work_text = new_text
            work.put()
        return self.redirect_to("wrk-list")


class AboutHandler(BaseHandler):
    def get(self):
        params = {}
        return self.render_template("about.html", params=params)


class ContactHandler(BaseHandler):
    def get(self):
        params = {}
        return self.render_template("contact.html", params=params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route("/works_list", WorksListHandler, name="wrk-list"),
    webapp2.Route('/work/<work_id:\d+>', WorkDetailsHandler),
    webapp2.Route('/work/<work_id:\d+>/edit', WorkEditHandler),
    webapp2.Route('/about', AboutHandler),
    webapp2.Route("/contact", ContactHandler),
], debug=True)
