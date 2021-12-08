// Copyright (c) 2021, Omar Alhori and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Book', {
	refresh: function(frm) {
		frm.set_query("author", function() {
			return {
				query: "library_management.controllers.data_query.author_query"
			};
		});
		frm.set_query("publisher", function() {
			return {
				query: "library_management.controllers.data_query.publisher_query"
			};
		});
		frm.set_query("category", function() {
			return {
				query: "library_management.controllers.data_query.category_query"
			};
		});
	}
});
