# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Literature"),
			"icon": "fa fa-wrench",
			"items": [
				{
					"type": "doctype",
					"name": "Library Book",
					"label": _("Books"),
				},	
				{
					"type": "doctype",
					"name": "Library Category",
					"label": _("Categories"),
				},	
            ]
        },
		{
			"label": _("Transactions"),
			"icon": "fa fa-wrench",
			"items": [
				{
					"type": "doctype",
					"name": "Library Transaction",
					"label": _("Library Transaction"),
				},	
					
            ]
        },
		{
			"label": _("Members"),
			"icon": "fa fa-wrench",
			"items": [
				{
					"type": "doctype",
					"name": "Library Author",
					"label": _("Authors"),
				},	
				{
					"type": "doctype",
					"name": "Library Publisher",
					"label": _("Publishers"),
				},	
            ]
        },
	]
