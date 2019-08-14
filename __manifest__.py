# -*- coding: utf-8 -*-
{
    'name': "send_mail_template_demo",

    'summary': """
        Demo module to show how you can send e-mail templates to people by clicking on a button""",

    'description': """
        Demo send e-mail templates 
    """,

    'author': "Nguyen xuan hieu",
    'website': "https://www.facebook.com/profile.php?id=100011399402018",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail', 'contacts'],

    # always loaded
    'data': [
        'views/mail_template.xml',
        'views/mail_to_manager.xml',

    ],
}
