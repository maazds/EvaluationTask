from odoo import api,fields,models

class Workflowin(models.Model):
    _name = 'workflow.in'
    _description = 'workflow name'
    _rec_name = 'Workflow_name'

    Workflow_name = fields.Char(string='Workflow Name')
    description = fields.Text(string='Description')
    active = fields.Boolean(default=True)
