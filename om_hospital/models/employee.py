from odoo import api, fields, models

class employee(models.Model):
    _name = 'doctor.employee'
    _inherit = 'purchase.order'