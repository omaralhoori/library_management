import frappe

def get_context(context):
    params = frappe.form_dict
    whereStmt = ""
    if "book" in params:
        bookName = params["book"]
        whereStmt = "WHERE b.name='{}'".format(bookName)
    else:
        frappe.local.flags.redirect_location = '/library'
        raise frappe.Redirect
    context.books = frappe.db.sql("""
        SELECT b.title, b.image, b.description, b.language, b.pages, b.isbn_issn, b.stock,
        a.author_name as author, a.name as author_name, 
        p.publisher_name as publisher, p.name as publisher_name, b.release_date,
         c.category_name as category, c.name as category_name
        FROM `tabLibrary Book` as b
        INNER JOIN `tabLibrary Author` as a ON b.author=a.name
        LEFT JOIN `tabLibrary Publisher` as p ON b.publisher=p.name
        LEFT JOIN `tabLibrary Category` as c ON b.category=c.name
        {}
        LIMIT 1
    """.format(whereStmt),  as_dict=True)
    print(whereStmt)
    return context