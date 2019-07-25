# Model.py
# model component of the MVC model

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

from types import *

class Model:
	Name = None
	Config = None
	Queries = {}

	def __init__(self, name, config):
		types("str", name)
		types("ModelConfig", config)
		self.Name = name
		self.Config = config

	def AddQuery(self, queryName, query):
		types("str", queryName)
		types("str", query)
		self.Queries[queryName] = query

	def Query(self, queryName):
		types("str", queryName)