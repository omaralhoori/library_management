# -*- coding: utf-8 -*-
# Copyright (c) 2021, Omar Alhori and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class LibraryTransaction(Document):
	# def before_insert(self):
	
	def validate(self):
		old_doc = self.get_doc_before_save()
		if not old_doc:
			make_transaction(self)
		else:
			if old_doc.type != self.type:
				make_transaction(self)


def make_transaction(transaction):
	if transaction.type == 'Lending':
		lend_book(transaction)
	elif transaction.type == 'Return':
		return_book(transaction)

def lend_book(transaction):
	stock = frappe.db.get_value("Library Book", transaction.book, ["stock"])
	if stock and stock > 0:
		frappe.db.set_value("Library Book", transaction.book, {"stock": stock - 1})
	else:
		frappe.throw(_("The book is not available"))

def return_book(transaction):
	stock = frappe.db.get_value("Library Book", transaction.book, ["stock"])
	print(stock)
	if stock is not None:
		frappe.db.set_value("Library Book", transaction.book, {"stock": stock + 1})
	else:
		frappe.throw(_("The book is not available"))