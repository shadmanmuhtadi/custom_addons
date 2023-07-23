from odoo import api, fields, models

class HospitalDoctor(models.Model):
    _name = 'doctor.details'
    _description = 'Doctor Details'

    name = fields.Char(string='Doctor Name')
    age = fields.Integer(string='Age')
    doctor_id = fields.Char(string='Doctor ID')
    gender = fields.Selection([
        ('male', 'Male'), 
        ('female', 'Female')], string="Gender")
    active = fields.Boolean(string="Active", default =True)
    patient_appoinment_ids = fields.Many2many('patient.details',string="Patient Appointment")

# class PreviousHistoryLine(models.Model):
#     _name = 'previous.history.line'
#     _description = 'Previous History Line'

#     previous_details = fields.Many2one('patient.details' , string= "Patient Name")
#     name = fields.Char(string = "Previous illness")
#     details = fields.Html(string="Details aoubt illness")