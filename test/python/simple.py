#!/usr/bin/env python3

import sys
sys.path.append('src')

import python as profess

config = profess.SiteConfig()
config.Port = 8080
config.StaticServing = True
config.StaticFolders["/projects_files"] = "test/python/projects_files"

site = profess.Site(config)

styleTemplate = profess.Template()
styleTemplate.TemplateFile = "test/python/base.css"
site.AddTemplate("STYLE", styleTemplate)

index = profess.View("/")
index.TemplateFile = "test/python/index.html"
site.AddView(index)

style = profess.View("/style")
style.TemplateFile = "test/python/style.html"
site.AddView(style)

projects = profess.View("/projects")
projects.TemplateFile = "test/python/projects.html"
site.AddView(projects)

blog = profess.View("/blog")
blog.TemplateFile = "test/python/blog.html"
blog.Methods = ["GET", "POST"]
site.AddView(blog)


site.Start()
