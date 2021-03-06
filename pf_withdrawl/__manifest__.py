# -*- coding: utf-8 -*-
{
	'name': 'Pf Withdrawal',
	'version': '12.0.0.0.1',
	'summary': 'PF Withdrawal',
	'category': 'Tools',
	'author': 'Dexciss Technologies Pvt Ltd(@ RGupta and Sangita)',
	'maintainer': 'dexciss Techno Solutions',
	'company': 'dexciss Techno Solutions',
	'website': 'https://www.dexciss.com',
	'depends': ['base','hr','ohrms_loan','hr_branch_company','hr_payroll'],
	'data': [
		'security/ir.model.access.csv',
		'security/pf_withdrawal_security.xml',
        'views/pf_withdrawal.xml',
        'wizard/report_wizard.xml',
        'views/report.xml',
        'views/salary_rule.xml',
        'views/pf_type_view.xml',
	],
	'images': [],
	'license': 'AGPL-3',
	'installable': True,
	'application': False,
	'auto_install': False,
}