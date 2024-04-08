
{
    'name': 'targetup Formation',
    'version': '1.0',
    'category': 'Product',
    'depends': ['base','product','hr_contract'],
    'author': 'omar ouhagua',
    'license': 'AGPL-3',
    'application': False,
    'data': [
        'views/product_view.xml',
        # 'views/product_template.xml',
     'views/contract_view.xml'

    ],
    'installable': True,
    'auto_install': False,
}