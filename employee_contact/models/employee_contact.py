from odoo import models, fields

class EmployeeContact(models.Model):
    _name = 'employee.contact'
    _description = 'Employee Contact Information'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    email = fields.Char(string='Email')