from __future__ import unicode_literals
import frappe

from frappe.desk.reportview import get_filters_cond, get_match_cond
from frappe.utils import unique


@frappe.whitelist()
def author_query(doctype, txt, searchfield, start, page_len, filters):
	conditions = []
	fields = get_fields("Library Author", ["name", "author_name"])

	return frappe.db.sql("""select {fields} from `tabLibrary Author`
		WHERE ({key} like %(txt)s
				or author_name like %(txt)s)
			{fcond} {mcond}
        order by
			if(locate(%(_txt)s, name), locate(%(_txt)s, name), 99999),
			if(locate(%(_txt)s, author_name), locate(%(_txt)s, author_name), 99999),
			idx desc,
			name, author_name
		limit %(start)s, %(page_len)s""".format(**{
			'fields': ", ".join(fields),
			'key': searchfield,
			'fcond': get_filters_cond(doctype, filters, conditions),
			'mcond': get_match_cond(doctype)
		}), {
			'txt': "%%%s%%" % txt,
			'_txt': txt.replace("%", ""),
			'start': start,
			'page_len': page_len
		})

@frappe.whitelist()
def publisher_query(doctype, txt, searchfield, start, page_len, filters):
	conditions = []
	fields = get_fields("Library Publisher", ["name", "publisher_name"])

	return frappe.db.sql("""select {fields} from `tabLibrary Publisher`
		WHERE ({key} like %(txt)s
				or publisher_name like %(txt)s)
			{fcond} {mcond}
        order by
			if(locate(%(_txt)s, name), locate(%(_txt)s, name), 99999),
			if(locate(%(_txt)s, publisher_name), locate(%(_txt)s, publisher_name), 99999),
			idx desc,
			name, publisher_name
		
		limit %(start)s, %(page_len)s""".format(**{
			'fields': ", ".join(fields),
			'key': searchfield,
			'fcond': get_filters_cond(doctype, filters, conditions),
			'mcond': get_match_cond(doctype)
		}), {
			'txt': "%%%s%%" % txt,
			'_txt': txt.replace("%", ""),
			'start': start,
			'page_len': page_len
		})

@frappe.whitelist()
def category_query(doctype, txt, searchfield, start, page_len, filters):
	conditions = []
	fields = get_fields("Library Category", ["name", "category_name"])

	return frappe.db.sql("""select {fields} from `tabLibrary Category`
		WHERE ({key} like %(txt)s
				or category_name like %(txt)s)
			{fcond} {mcond}
		order by
			if(locate(%(_txt)s, name), locate(%(_txt)s, name), 99999),
			if(locate(%(_txt)s, category_name), locate(%(_txt)s, category_name), 99999),
			idx desc,
			name, category_name
		limit %(start)s, %(page_len)s""".format(**{
			'fields': ", ".join(fields),
			'key': searchfield,
			'fcond': get_filters_cond(doctype, filters, conditions),
			'mcond': get_match_cond(doctype)
		}), {
			'txt': "%%%s%%" % txt,
			'_txt': txt.replace("%", ""),
			'start': start,
			'page_len': page_len
		})

@frappe.whitelist()
def book_query(doctype, txt, searchfield, start, page_len, filters):
	conditions = []
	fields = get_fields("Library Book", ["name", "title"])

	return frappe.db.sql("""select {fields} from `tabLibrary Book`
		WHERE ({key} like %(txt)s
				or title like %(txt)s)
			{fcond} {mcond}
		order by
			if(locate(%(_txt)s, name), locate(%(_txt)s, name), 99999),
			if(locate(%(_txt)s, title), locate(%(_txt)s, title), 99999),
			idx desc,
			name, title
		limit %(start)s, %(page_len)s""".format(**{
			'fields': ", ".join(fields),
			'key': searchfield,
			'fcond': get_filters_cond(doctype, filters, conditions),
			'mcond': get_match_cond(doctype)
		}), {
			'txt': "%%%s%%" % txt,
			'_txt': txt.replace("%", ""),
			'start': start,
			'page_len': page_len
		})

def get_fields(doctype, fields=None):
	if fields is None:
		fields = []
	meta = frappe.get_meta(doctype)
	fields.extend(meta.get_search_fields())

	if meta.title_field and not meta.title_field.strip() in fields:
		fields.insert(1, meta.title_field.strip())

	return unique(fields)