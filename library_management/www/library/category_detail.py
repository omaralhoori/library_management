import frappe

def get_context(context):
    params = frappe.form_dict
    categoryName = ""
    if "category" in params:
        categoryName = params["category"]
    else:
        frappe.local.flags.redirect_location = '/library'
        raise frappe.Redirect
    context.books = frappe.db.sql("""
        SELECT b.name as book_name, b.title, b.image
        FROM `tabLibrary Book` as b
        WHERE category="{}"
    """.format(categoryName),  as_dict=True)
    context.category = frappe.db.sql("""
        SELECT category_name, description
        FROM `tabLibrary Category`
        WHERE name=%s
    """, categoryName, as_dict=True)
    return context