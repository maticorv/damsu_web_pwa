/* Copyright 2020 Tecnativa - Alexandre D. Díaz
 * License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl). */

odoo.define("damsu_web_pwa.webclient", function(require) {
    "use strict";

    var WebClient = require("web.WebClient");
    var PWAManager = require("damsu_web_pwa.PWAManager");

    WebClient.include({
        /**
         * @override
         */
        show_application: function() {
            this.pwa_manager = new PWAManager(this);
            return this._super.apply(this, arguments);
        },
    });
});
