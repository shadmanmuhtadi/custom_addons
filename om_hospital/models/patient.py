from datetime import date
from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = 'patient.details'
    _inherit= ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Details'

    name = fields.Char(string='Patient Name', tracking= True)
    contact_number = fields.Char(string="Contact Number" , tracking= True)
    email = fields.Char(string="Email", tracking= True)
    date_of_birth = fields.Date(string="Date of Birth", tracking= True)
    age = fields.Integer(string='Age', compute = '_compute_age', tracking= True)
    ref = fields.Char(string='Patient ID', tracking= True)
    test_field = fields.Many2one('test.model',string = "Test Field")
    test_html = fields.Html(string = 'Test HTML')
    gender = fields.Selection([
        ('male', 'Male'), 
        ('female', 'Female')], string="Gender", default = 'male')
    active = fields.Boolean(string="Active", default =True, tracking= True)
    # previous_illness_ids = fields.One2many('previous.history.line','previous_details',string= "Previous Illness Record")
    
    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0