{
    'name': 'Mi Modulo',
    'version': '1.2.4',
    'summary': 'Modulo de practica',
    'description': 'Módulo para gestionar el control de pagos de un prestamo',
    'category': 'Sale',
    'website': 'https://www.gestionarpagos.com',
    'depends': ['base'],
    'data': [
        # Data
        'data/ir_sequence_data.xml',
        # Archivo de reglas de acceso
        'security/ir.model.access.csv',
        # Vistas
        'views/my_module_menus.xml',
        'views/cliente_views.xml',
        'views/prestamo_views.xml',
        'views/cobro_views.xml',
    ],
    'installable': True,
}
