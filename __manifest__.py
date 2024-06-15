# -*- coding: utf-8 -*-
{
    'name': "tuyensinh",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/miki.province.csv',
        'data/miki.district.csv',
        'data/miki.ward.csv',
        'views/miki_province_views.xml',
        'views/miki_distriict_views.xml',
        'views/miki_ward_views.xml',
        'views/miki_student_views.xml',
        'views/portal/login_page.xml',
        'views/portal/information_page.xml',
        'views/miki_student_type_views.xml',
        'views/miki_department_views.xml',
        'views/miki_major_views.xml',
        'views/miki_subject_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ]
}

