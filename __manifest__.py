# -*- coding: utf-8 -*-
#############################################################################
#
#    Mapleshub Solutions.
#
#    Copyright (C) 2024-TODAY Mapleshub Solutions(<https://www.mapleshub.com>)
#    Author: Mapleshub Solutions(<https://www.mapleshub.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'Mapleshub Odoo Database Query',
    'summary': "Direct Database query to view and export in excel",
    'summary': """
                Database query from odoo backend, it only allow select query to preview and export in excel
    """,
    'description': """
                Database query from odoo backend, it only allow select query to preview and export in excel
    """,
    'author': "Mapleshub Solutions",
    'maintainer': 'Mapleshub Solutions',
    'company': 'Mapleshub Solutions',
    'website': "https://www.mapleshub.com",
    'support': 'service@mapleshub.com',
    'category': 'Tools',
    'version': '18.0.0.0.1',
    'sequence': 1,
    'license': 'AGPL-3',
    'depends': ['base'],
    'images': ["static/description/banner.gif"],
    'data': [
        'security/ir.model.access.csv',
        'wizards/field_data_export_wizard.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'mh_odoo_database_query/static/src/css/*',
        ],
    },
}
