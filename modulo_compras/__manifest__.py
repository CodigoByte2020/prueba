{
    'name' : 'Modulo de compras',
    'version' : '3.3.5',
    'summary': 'Módulo para gestionar compras',
    'description': 'Módulo para realizar compras mas sencillas.',
    'category': 'Localization',
    'website': 'https://www.colossusperu.com',
    'depends' : ['purchase'],
    'data': [
        # Archivo de reglas de acceso
        'security/ir.model.access.csv',
        # Vistas
        'views/purchase_views.xml',
        'views/pedidohistorico_views.xml',
    ],
    'installable': True,
}