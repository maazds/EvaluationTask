# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WorkflowEval(models.Model):
    _inherit = 'project.task'
    _description = 'Project Task'

    project_task_id = fields.Many2one('project.task', 'Next Task',store=True)
    project_task_milestone_ext = fields.Selection([('new', 'New'), ('progress', 'Progress'), ('done', 'Done')],
                                                  'Milestone', default='new')
    workflow_id = fields.Many2one('project.workflow', string="Workflow",required=True)
    workflow_id_ext = fields.Many2one('workflow.in', string="Select Workflow",required=True,store=True)
    state = fields.Selection([
        ('new', 'New'),
        ('ongoing', 'On Going'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], default='new', string='State')
    def mark_done(self):
       self.write({'state':'done'})
        # x = self.env['project.task'].search([])
        # for rec in x:
        #     return ({rec.stage_id.name : 'Done'})
    def mark_cancel(self):
        self.write({'state':'cancel'})

    def mark_ongoing(self):
        # print(self.env.user)
        self.write({'state': 'ongoing'})


