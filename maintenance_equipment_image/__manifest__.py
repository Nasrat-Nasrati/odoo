# Copyright 2021 Exo Software
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Maintenance Equipment MCIT",
    "summary": """this is for management of cars in MCIT""",
    "category": "Maintenance",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "Nasrat Nasrati," "Odoo Developer at MCIT",
    "maintainers": ["epg mcit team"],
    "website": "https://github.com/OCA/maintenance",
    "depends": ["maintenance","hr"],
    "data": [
        "security/maintenance_file.xml",
        "security/ir.model.access.csv",
        "views/maintenance_equipment_views.xml",
        "reports/report.xml",
        "reports/report_form.xml",

    ],
    "installable": True,
    "application": False,
}
