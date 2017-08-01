
# -*- coding: utf-8 -*-

# Copyright 2017 Jakub Kukiełka

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from common import app, common_sources, subdomain_list
from flask import render_template
from flask_classy import FlaskView

import serve.subdomains.index
import serve.subdomains.blog

# class BlogView(FlaskView):
#     route_base = "/"
#     subdomain = "blog"

#     def __init__(self):
#         self.subdomain = "blog"
#         self.template = "blog.pug"

#         self.sources = {
#             "styles": [],
#             "scripts": []
#         }

#         self.meta = {
#             "title": "what lies within is void",
#             "curront_favicon": lookup_favicon(),
#             "default_tags": "test, thing, argarak, main",
#             "description": "spaghetti",
#             "is_article": False
#         }

#     def index(self):
#         return render_template(self.template, sources=self.sources, meta=self.meta)

# MainView.register(app)

#@app.route("/", subdomain="blog")
#def blog_home():
#    return render_template("blog.pug")

@app.route("/<page>", subdomain="blog")
def blog_page(page):
    return "You navigated to: {}".format(page)

#if __name__ == "__main__":
#    hello()
