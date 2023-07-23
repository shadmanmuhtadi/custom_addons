{
    'name' : 'Hospital Managment System',
    'version' : '1.0',
    'summary': 'Hospital Managment System',
    'sequence': -100,
    'description': """Hospital Managment System""",
    'category': 'Productivity',
    'author': 'Shattam',
    'website': '',
    'depends' : ['mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu_view.xml',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/appointment_view.xml',
        'views/medicine_view.xml',
        'views/test.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}