# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe

def execute():

	# frappe.db.set_value("DocField", {"parent": "Awfis Lead Detail", "fieldname": "requirement_date"}, "read_only", 1)
	# frappe.db.set_value("DocField", {"parent": "Awfis Lead Detail", "fieldname": "type"}, "read_only", 1)
	# frappe.db.set_value("DocField", {"parent": "Awfis Lead Detail", "fieldname": "city"}, "read_only", 1)
	# frappe.db.set_value("DocField", {"parent": "Awfis Lead Detail", "fieldname": "center"}, "read_only", 1)
	# frappe.db.set_value("DocField", {"parent": "Awfis Lead Detail", "fieldname": "lead_channel"}, "read_only", 1)
	# frappe.db.set_value("DocField", {"parent": "Awfis Lead Detail", "fieldname": "lead_source"}, "read_only", 1)
	# frappe.db.set_value("DocField", {"parent": "Awfis Lead Detail", "fieldname": "lead_sub_source"}, "read_only", 1)
	# frappe.db.set_value("DocField", {"parent": "Awfis Lead Detail", "fieldname": "lead_campaign"}, "read_only", 1)
	# frappe.db.set_value("DocField", {"parent": "Awfis Lead Detail", "fieldname": "lead_channel_partner"}, "read_only", 1)
	# frappe.db.set_value("DocField", {"parent": "Awfis Lead Detail", "fieldname": "space_type"}, "read_only", 1)
	# frappe.db.set_value("DocField", {"parent": "Awfis Lead Detail", "fieldname": "capacity"}, "read_only", 1)
	# frappe.db.set_value("DocField", {"parent": "Awfis Lead Detail", "fieldname": "qty"}, "read_only", 1)
	# frappe.db.set_value("DocField", {"parent": "Awfis Lead Detail", "fieldname": "tenure"}, "read_only", 1)
	# frappe.db.set_value("DocField", {"parent": "Awfis Lead Detail", "fieldname": "tenure_qty"}, "read_only", 1)
	
	
	# frappe.db.commit()

	# frappe.db.sql('update tabDocField set search_index=0 where fieldtype="Small Text"')
	# frappe.db.sql('update tabDocField set in_list_view=0 where fieldtype="Image"')

	# for dt in frappe.db.sql_list("""select name from `tabDocType` where issingle=0"""):
	# 	desc = dict((d["Field"], d) for d in frappe.db.sql("desc `tab{}`".format(dt), as_dict=True))
	# 	alter_table = []

	# 	if desc["name"]["Type"] != "varchar(255)":
	# 		alter_table.append("change `name` `name` varchar(255) not null")

	# 	for fieldname in ("modified_by", "owner", "parent", "parentfield", "parenttype"):
	# 		if desc[fieldname]["Type"] != "varchar(255)":
	# 			alter_table.append("change `{fieldname}` `{fieldname}` varchar(255)".format(fieldname=fieldname))

	# 	if alter_table:
	# 		alter_table_query = "alter table `tab{doctype}` {alter_table}".format(doctype=dt, alter_table=",\n".join(alter_table))
	# 		# print alter_table_query
	# 		frappe.db.sql_ddl(alter_table_query)

