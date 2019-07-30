# SiteConfig.py
# settings for hosting

# Profess Copyright (c) 2019 Joshua 'joshuas3' Stockin
# <https://github.com/JoshuaS3/profess/>.


# This file is part of Profess.

# Profess is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Profess is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Profess. If not, see <https://www.gnu.org/licenses/>.

from .types import *
from .View import *

class SiteConfig:
	Port = 80

	SSLEnabled = False
	SSLCertificate = ""
	SSLKey = ""

	NotFound = None
	BadRequest = None
	Error = None

	StaticServing = False
	StaticFolders = {}

	def __init__(self):
		self.NotFound = View("/404")
		self.NotFound.TemplateString = """<!doctype html>
<html>
	<head>
		<title>Error 404</title>
		<style>*{color:#333; font-family: Segoe UI, Helvetica Neue, sans-serif;}</style>
	</head>
	<body>
		<center>
			<h1>error 404</h1>
			<h2>resource not found</h2>
			<a href="/">return home</a>
		</center>
	</body>
</html>"""
		self.MethodNotAllowed = View("/405")
		self.MethodNotAllowed.TemplateString = """<!doctype html>
<html>
	<head>
		<title>Error 405</title>
		<style>*{color:#333; font-family: Segoe UI, Helvetica Neue, sans-serif;}</style>
	</head>
	<body>
		<center>
			<h1>error 405</h1>
			<h2>method not allowed</h2>
			<a href="/">return home</a>
		</center>
	</body>
</html>"""
		self.Error = View("/500")
		self.Error.TemplateString = """<!doctype html>
<html>
	<head>
		<title>Error 500</title>
		<style>*{color:#333; font-family: Segoe UI, Helvetica Neue, sans-serif;}</style>
	</head>
	<body>
		<center>
			<h1>error 500</h1>
			<h2>internal server failure</h2>
			<a href="/">return home</a>
		</center>
	</body>
</html>"""
