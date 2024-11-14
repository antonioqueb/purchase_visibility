{
    'name': 'Purchase Visibility',
    'version': '1.0',
    'category': 'Purchases',
    'summary': 'Restricción de visibilidad de órdenes y solicitudes de compra por usuario.',
    'description': 'Permite a los usuarios ver solo sus propias órdenes y solicitudes de compra.',
    'author': 'ALPHAQUEB CONSULTING SAS',
    'depends': ['purchase', 'purchase_requisition'],
    'data': [
        'security/purchase_visibility_security.xml',  
        'security/ir.model.access.csv',              
    ],
    'installable': True,
    'application': False,
}
