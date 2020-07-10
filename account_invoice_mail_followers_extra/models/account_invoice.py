# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
_logger = logging.getLogger(__name__)

from openerp import api, models, fields
from openerp.exceptions import Warning

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def action_invoice_open(self):    
        account_invoice_mail_followers_extra_ids = self.env['account_invoice_mail_followers_extra'].search([('partner_id', '=', int(self.partner_id.id))])    
        for account_invoice_mail_followers_extra_id in account_invoice_mail_followers_extra_ids:
            for partner_id_extra in account_invoice_mail_followers_extra_id.partner_ids_extra:
                mail_followers_ids = self.env['mail.followers'].search(
                    [
                        ('partner_id', '=', self.partner_id.id),
                        ('res_model', '=', 'account.invoice'),
                        ('res_id', '=', self.id)
                    ]
                )
                if len(mail_followers_ids)==0:
                    mail_followers_vals = {
                        'partner_id': partner_id_extra.id,
                        'res_model': 'account.invoice',
                        'res_id': self.id,
                        'subtype_ids': [(4, 1)]
                    }
                    mail_followers_obj = self.env['mail.followers'].sudo().create(mail_followers_vals)
        #return
        return super(AccountInvoice, self).action_invoice_open()                                                                                                                                         