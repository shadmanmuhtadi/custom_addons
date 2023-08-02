from odoo import api, models, _

class PatientCardReport(models.AbstractModel):
    _name = 'report.om_hospital.report_patient'
    _description = 'Patient card Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['patient.details'].browse(docids[0])
        appointments = self.env['appointment.details'].search([('patient_id', '=', docids[0])])
        appointment_list = []
        return {
            'doc_model': 'patient.details',
            'docs': docs,
            'appointment_list': appointment_list,
        }