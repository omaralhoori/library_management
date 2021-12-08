import frappe

def get_context(context):
    params = frappe.form_dict
    authorName = ""
    if "author" in params:
        authorName = params["author"]
    else:
        frappe.local.flags.redirect_location = '/library'
        raise frappe.Redirect
    context.books = frappe.db.sql("""
        SELECT b.name as book_name, b.title, b.image
        FROM `tabLibrary Book` as b
        WHERE author="{}"
    """.format(authorName),  as_dict=True)
    context.author = frappe.db.sql("""
        SELECT author_name, bio, image
        FROM `tabLibrary Author`
        WHERE name=%s
    """, authorName, as_dict=True)
    return context