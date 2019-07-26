# View.py
# view component of the MVC model

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
from .Template import *

class View (Template):
	WebAddress = "/"
	AcceptedMethods = ["GET"]
	MimeType = "text/html"
	ControllerID = None

	def __init__(self, address="/", methods=["GET"], mime="text/html"):
		types(str, address)
		types(list, methods)
		types(str, mime)
		self.WebAddress = address
		for method in methods:
			types(str, method)
		self.AcceptedMethods = methods
		self.MimeType = mime
