# Copyright (c) 2019, Officexlr Business Solutions Pvt Ltd. and Contributors
# License: MIT. See license.txt

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Metabase",
			"color": "grey",
			"icon": "octicon octicon-dashboard",
			"type": "page",
			"link": "metabase-dashboard",
			"label": _("Dashboard")
		}
	]
