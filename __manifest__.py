{
    'name': 'Purchase Visibility',
    'version': '1.1',
    'category': 'Purchases',
    'summary': 'Restricción de visibilidad de órdenes y solicitudes de compra por usuario.',
    'description': 'Permite a los usuarios ver solo sus propias órdenes y solicitudes de compra o las de usuarios seleccionados.',
    'author': 'ALPHAQUEB CONSULTING SAS',
    'license': 'AGPL-3',
    'depends': ['base', 'purchase', 'purchase_requisition'],
    'data': [
    'security/purchase_visibility_security.xml',
    'security/ir.model.access.csv',
    'views/res_users_views.xml',
    ],

    'installable': True,
    'application': False,
}
