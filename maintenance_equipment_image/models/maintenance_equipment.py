# Copyright 2021 Exo Software, Lda.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields,api


class MaintenanceEquipment(models.Model):
    _inherit = ["maintenance.equipment", "image.mixin"]
    _name = "maintenance.equipment"

    driver_name=fields.Many2one('hr.employee', string='Driver Name')
    father_name = fields.Char(string="Father Name")
    oiltype = fields.Selection([
        ('D', 'دیزل'),
        ('P', 'پطرول ')
    ],string="Oile Type")

class MaintenanceRequest(models.Model):
    _inherit = ['maintenance.request']

    quantity = fields.Float(string="quantity")
    owner = fields.Many2one('hr.employee')
    unite = fields.Selection([
        ('M', 'Meter '),
        ('CM', 'Centimeter '),
        ('MM', 'Millimeter '),
        ('KM', 'Kilometer '),
        ('FT', 'Foot '),
        ('In', 'Inch '),
        ('Kg', 'Kilogram '),
        ('g', 'Gram '),
        ('Mg', 'Milligram '),
        ('T', 'Ton')
        # Add more options as needed
    ], )
    eqdamno =fields.Float(string="Eqdam Number")
    seqn =fields.Float(string="Store Eqdam Number")


# this is the new table for distribution from or fcfive


class MaintenanceDistribution(models.Model):
    _name = "maintenance.distribution"
    _description = "This is just for storing Distribution Forms like FC5"
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Inherit from mail.thread and mail.activity.mixin

    distributionno=fields.Integer(string="Distribution No")
    distributiondate=fields.Date(string="Distribution Date",default=lambda self: fields.Date.today())
    distributionplace=fields.Char(string="Distribution Place")
    requestno=fields.Integer(string="Request No")
    requestdate=fields.Date(string="Request Date",default=lambda self: fields.Date.today())
    requestoffice=fields.Char(string="Request Office",default="مدیریت عمومی وسایط")
    quantity=fields.Float(string="Quantity")
    unite = fields.Selection([
        ('M', 'Meter '),
        ('CM', 'Centimeter '),
        ('MM', 'Millimeter '),
        ('KM','Kilometer '),
        ('FT','Foot '),
        ('In','Inch '),
        ('Kg','Kilogram '),
        ('g','Gram '),
        ('Mg','Milligram '),
        ('T','Ton')
        # Add more options as needed
    ], string="Unit",required=True)
    unitprice=fields.Float(string="Unite Price")
    totalprice = fields.Float(string="Total Price", compute="_compute_total_price")
    # responsible=fields.Char(string="Responsible")
    # this is for responsible section
    responsible = fields.Many2one('hr.employee')

    discription = fields.Text(string="Descriptions")

    @api.depends('quantity', 'unitprice')
    def _compute_total_price(self):
        for record in self:
            # print(self)
            record.totalprice = record.quantity * record.unitprice





