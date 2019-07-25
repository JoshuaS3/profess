# Site.py
# management of HTTP(S) requests and the MVC interface

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
from Model import *
from View import *
from Controller import *

class Site:
	__config = None

	def Start():
		pass

	def Stop():
		pass


	def AddController(controller):
		types(Controller, controller)

	def AddView(view):
		types(View, view)

	def AddModel(model):
		types(Model, model)


	def GetController(name):
		types("str", name)
		for controller in __controllers:
			if controller.Name == name:
				return controller

	def GetView(address):
		types("str", address)
		for view in __views:
			if view.WebAddress == address:
				return view

	def GetModel(name):
		types("str", name)
		for model in __models:
			if model.Name == name:
				return model


	__controllers = []
	__views = []
	__models = []
