from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name = 'appointment.details'
    _inherit= ['mail.thread', 'mail.activity.mixin']
    _description = 'Appointment Details'
    _rec_name = 'patient_id'
    #this is a comment

    patient_id = fields.Many2one('patient.details', string="Patient ID")
    gender = fields.Selection([
    ('male', 'Male'), 
    ('female', 'Female')], string="Gender", related = 'patient_id.gender')
    age = fields.Integer(string='Age', related= "patient_id.age")
    appointment_time= fields.Datetime(string="Appointment Time")
    booking_time= fields.Date(string= "Booking Time")
    ref = fields.Char(string='Reference')
    prescription = fields.Html(string = "Prescription")
    prescription_line_ids = fields.One2many('appointment.prescription.line','appointment_id', string='Prescription Line')
    doctor_id=fields.Many2one('res.users',string="Doctor")
    sutotal = fields.Float(compute = '_subtotal', string="Sub Total",readonly = True)
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")
    state = fields.Selection([
        ('draft', 'Draft'), 
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancel')], string="In which State", default= "draft", required=True)

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_in_consultation(self):
        for rec in self:
            rec.state = 'in_consultation'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    # def action_test(self):
    #     print("Button Clicked!!!!!!!!!!!!")
    #     return {
    #             'effect': {
    #                 'fadeout': 'slow',
    #                 'message': 'Click Here For the effect',
    #                 'type': 'rainbow_man',
    #             }
    #         }
    

class AppointmentPrescriptionLine(models.Model):
    _name = 'appointment.prescription.line'
    _description = 'Appointment Prescription Line'

    name_id=fields.Many2one('medicine.product',string='Medicine')
    qty= fields.Integer(string='Quantity')
    price= fields.Float(related='name_id.unit_price',string='Price')
    appointment_id=fields.Many2one('appointment.details',string="Appointment")


class MedicineProduct(models.Model):
    _name = 'medicine.product'
    _description = 'Medicine Product'
    _rec_name = 'name'

    name=fields.Char(string='Medicine', Tracking= True)
    strength=fields.Char(string='Strength')
    manufacture=fields.Char(string='Manufactured By')
    indications= fields.Char(string="Indication")
    dosage=fields.Html(string="Dosage")
    unit_price= fields.Float(string='Price')
    add_image = fields.Image(string="Add Image")

