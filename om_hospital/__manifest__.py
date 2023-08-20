{
    'name' : 'Hospital Managment System',
    'version' : '1.0',
    'summary': 'Hospital Managment System',
    'sequence': -100,
    'description': """Hospital Managment System""",
    'category': 'Productivity',
    'author': 'Shattam',
    'website': '',
    'depends' : ['base','mail','web','sale','purchase'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu_view.xml',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/appointment_view.xml',
        'views/medicine_view.xml',
        'views/puchase_view.xml',
        'reports/report.xml',
        'reports/sale_report_inherit.xml',  
        'reports/patient_card.xml',  
        'reports/appointment_card.xml',  
        
],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'om_hospital/static/src/css/custom.css',
            # 'om_hospital/static/src/js/remove_menu.js',
        ],

        # 'web.assets_frontend': [
        # ],

        'web.assets_qweb': [
            'om_hospital/static/src/xml/base.xml',
        ],

    },
    'auto_install': False,
    'license': 'LGPL-3',
}