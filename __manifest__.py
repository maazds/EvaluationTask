# -*- coding: utf-8 -*-
{
    'name': "workflow_evaluation",
    'summary': """Task""",
    'description': """workflow evaluation task""",
    'author': "Maaz Aslam",
    'website': "https://www.yourcompany.com",
    'category': 'Evaluation',
    'version': '0.1',
    'depends': ['base', 'project'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/project_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
