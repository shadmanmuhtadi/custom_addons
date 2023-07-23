from odoo import api, fields, models

class TestModel(models.Model):
    _name = 'test.model'
    _description = 'Test Model'

    test1_id = fields.Many2one('doctor.details',string='Test Field 1')
    test2_ids = fields.One2many('patient.details','test_field',string='Test Field 2')
    test3_ids = fields.Many2many('medicine.product',string='Test Field 3')
    test4 = fields.Char(string='Test Field 4')