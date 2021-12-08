import frappe
import math
BOOKS_IN_PAGE=20

def get_context(context):
    params = frappe.form_dict
    if "search_type" in params:
        searchType = params["search_type"]
        searchText = params["search"]
        whereStmt = "WHERE {} LIKE '%{}%'".format(searchType, searchText)
        context.books = frappe.db.sql("""
        SELECT b.name as book_name, b.title, b.image, b.description, a.author_name as author
        FROM `tabLibrary Book` as b
        JOIN `tabLibrary Author` as a ON b.author=a.name
        {}
    """.format(whereStmt),  as_dict=True)
    else:
        currentPage = 0
        if "page" in params:
            currentPage = int(params["page"]) - 1
        allBooks = frappe.db.sql("""SELECT COUNT(*) as allbooks FROM `tabLibrary Book`""", as_dict=True)
        context.pages = math.ceil(int(allBooks[0]["allbooks"]) / BOOKS_IN_PAGE)

        context.books = frappe.db.sql("""
            SELECT b.name as book_name, b.title, b.image, b.description, a.author_name as author
            FROM `tabLibrary Book` as b
            JOIN `tabLibrary Author` as a ON b.author=a.name
            LIMIT {},{}
        """.format(currentPage * BOOKS_IN_PAGE, BOOKS_IN_PAGE),  as_dict=True)
        context.categories = frappe.db.sql("""
            SELECT name, category_name FROM `tabLibrary Category`
        """, as_dict=True)
        context.currentPage = currentPage
    return context