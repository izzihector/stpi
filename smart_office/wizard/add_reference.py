from odoo import fields, models, api
from datetime import datetime

class AddReference(models.TransientModel):
    _name = 'add.reference.file'
    _description = 'Add Reference'


    cooespondence_ids = fields.Many2many('muk_dms.file', string='Correspondence')
    description = fields.Text()
    folder_id = fields.Many2one('folder.master', string="Select File")


    def confirm_button(self):
        if self:
            letter_id = []
            current_employee = self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1)
            for file in self.cooespondence_ids:
                letter_id.append(file.id)
                self.folder_id.folder_ids = [(6, 0, letter_id)]
                self.env['file.tracker.report'].create({
                    'name': str(file.name),
                    'type': 'Correspondence',
                    'assigned_by': str(current_employee.user_id.name),
                    'assigned_by_dept': str(current_employee.department_id.name),
                    'assigned_by_jobpos': str(current_employee.job_id.name),
                    'assigned_by_branch': str(current_employee.branch_id.name),
                    'assigned_date': datetime.now().date(),
                    'action_taken': 'assigned_to_file',
                    'remarks': self.description,
                    'details': "Correspondence attached to file {}".format(self.folder_id.folder_name)
                })
            form_view = self.env.ref('smart_office.foldermaster_form_view')
            tree_view = self.env.ref('smart_office.foldermaster_tree_view1')
            value = {
                'domain': str([('id', '=', self.folder_id.id)]),
                'view_type': 'form',
                'view_mode': 'tree, form',
                'res_model': 'folder.master',
                'view_id': False,
                'views': [(form_view and form_view.id or False, 'form'),
                          (tree_view and tree_view.id or False, 'tree')],
                'type': 'ir.actions.act_window',
                'res_id': self.folder_id.id,
                'target': 'current',
                'nodestroy': True
            }
            return value