{
    'name': 'EMS Hospital',
    'author': 'Abhisha devi',
    'version': '17.0.1.0',    # Changed to match Odoo version format
    'summary': 'A module for hospital management',
    'description': 'A module for hospital management',  # Added description
    'category': 'Healthcare',
    'license': 'LGPL-3',      # Added license field
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient.xml'
    ],               # Added data field for views/security files
    'installable': True,
    'application': True,
    'sequence': 1,            # Added sequence for Apps list ordering
}