// Copyright (c) 2021, Omar Alhori and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Transaction', {
	refresh: function(frm) {
		frm.set_query("book", function() {
			return {
				query: "library_management.controllers.data_query.book_query"
			};
		});
	}
});
