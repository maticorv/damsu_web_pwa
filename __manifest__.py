# Copyright 2020 Lorenzo Battistini @ TAKOBI
# Copyright 2020 Tecnativa - Alexandre D. Díaz
# Copyright 2020 Tecnativa - João Marques
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    "name": "DAMSU - Progressive web application",
    "summary": "Make Odoo a PWA",
    'author': "Hexium Software Factory",
    'website': "https://hexium.com.ar",
    "version": "13.0.1.0.1",
    "development_status": "Beta",
    "category": "Website",
    "license": "LGPL-3",
    "application": True,
    "installable": True,
    "depends": ["web", "mail"],
    "data": ["templates/assets.xml", "views/res_config_settings_views.xml"],
    "images": ["static/description/pwa.png"],
}
