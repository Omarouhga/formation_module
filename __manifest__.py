
{
    'name': 'targetup Formation',
    'version': '1.0',
    'category': 'Product',
    'depends': ['base','product','crm','hr_contract'],
    'license': 'AGPL-3',
    'application': False,
    'data': [
        'views/product_view.xml',
    'views/product_template.xml',
    # 'data/sequence.xml',
    #'views/contract_view.xml',
    #'views/indicatif_pays_view.xml',
    'views/lead_view_inhereted.xml'

    ],
    'installable': True,
    'auto_install': False,
}