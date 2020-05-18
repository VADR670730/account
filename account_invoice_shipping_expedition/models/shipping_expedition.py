# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from odoo import api, models, fields

class ShippingExpedition(models.Model):
    _inherit = 'shipping.expedition'

    account_invoice_line_id = fields.Many2one(
        comodel_name='account.invoice.line',
        string='Account Invoice Line Id'
    )
    invoice_date = fields.Date(
        string='Fecha factura'
    )
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Moneda',
    )
    cost = fields.Monetary(
        string='Coste'
    )