import frappe

def get_context(context):
    params = frappe.form_dict
    publisherName = ""
    if "publisher" in params:
        publisherName = params["publisher"]
    else:
        frappe.local.flags.redirect_location = '/library'
        raise frappe.Redirect
    context.books = frappe.db.sql("""
        SELECT b.name as book_name, b.title, b.image
        FROM `tabLibrary Book` as b
        WHERE publisher="{}"
    """.format(publisherName),  as_dict=True)
    context.publisher = frappe.db.sql("""
        SELECT publisher_name, bio, image, address, telephone, fax, web_address
        FROM `tabLibrary Publisher`
        WHERE name=%s
    """, publisherName, as_dict=True)
    return context