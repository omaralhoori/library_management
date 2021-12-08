frappe.listview_settings['Library Transaction'] = {
    hide_name_column: true, 
    add_fields: ["type"],
    get_indicator: function(doc) {
		if(doc.type == 'Return') {
			return [__("Return"), "green", "enabled,=,1"];
		} else {
			return [__("Lending"), "orange", "enabled,=,0"];
		}
	}
}