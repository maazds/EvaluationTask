from odoo import api, models, fields


class ProjectWorkflow(models.Model):
    _name = 'project.workflow'
    _description = 'Defining a workflow'

    name = fields.Char(string='Workflow Name')
    Workflow_name = fields.Many2one('workflow.in', 'Workflow', store=True)
    description = fields.Text(string='Description')
    project_id = fields.Many2one('project.project', string='Project',store=True)
    active = fields.Boolean(default=True)
    task_temp_ongoing = fields.One2many('project.task','workflow_id_ext', compute='compute_task_lists',string="Ongoing")
    task_temp_next = fields.One2many('project.task','workflow_id_ext', compute='compute_task_lists',string="Next")
    task_temp_upnext = fields.One2many('project.task','workflow_id_ext', compute='compute_task_lists',string="UP Next")
    @api.onchange('Workflow_name')
    def change_description(self):
        if self.Workflow_name:
            workflow = self.env['workflow.in'].browse(self.Workflow_name.ids)
            self.write({'description': workflow.description})

    @api.depends('Workflow_name')
    def compute_task_lists(self):

        for rec in self:
            if rec.Workflow_name:
                workflow_ids = self.env['project.task'].search(
                    [('workflow_id_ext', '=', rec.Workflow_name.id), ('state', '!=', 'done'),('state','!=','cancel')]).ids
                rec.task_temp_ongoing = [(6, 0, workflow_ids[-1])] if workflow_ids else [(5, 0, 0)]
                rec.task_temp_next = [(6, 0, workflow_ids[-2])] if len(workflow_ids) > 1 else [(5, 0, 0)]
                rec.task_temp_upnext = [(6, 0, workflow_ids[:-2])] if len(workflow_ids) > 2 else [(5, 0, 0)]