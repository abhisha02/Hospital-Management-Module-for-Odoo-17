from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name ="hospital.patient"
    _description="patient Records"

    name =fields.Char(string='Name',required=True)
    age=fields.Integer(string="age")
    is_child=fields.Boolean(string="is child")
    notes=fields.Text(string="notes")
    gender=fields.Selection([('male','Male'),('female','Female')],string="gender")