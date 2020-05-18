# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from openerp import api, models, fields
from openerp.exceptions import Warning

class AccountAssetAsset(models.Model):
    _inherit = 'account.asset.asset'
    
    depreciated_value = fields.Float(
        compute='_depreciated_value',
        string='Depreciacion acumulada',
        store=False
    )
    
    @api.one        
    def _depreciated_value(self):
        self.depreciated_value = 0
        if len(self.depreciation_line_ids)>0:
            for depreciation_line_id in self.depreciation_line_ids:
                if depreciation_line_id.move_id.id>0:
                    if depreciation_line_id.move_id.state=='posted':
                        self.depreciated_value += depreciation_line_id.amount
              
    @api.multi
    def set_to_close(self):
        for item in self:
            if item.state!='close':                
                if len(item.depreciation_line_ids)>0:
                    for depreciation_line_id in item.depreciation_line_ids:
                        if item.state!='close':
                            depreciation_line_id.post_lines_and_close_asset()                
            
        return super(AccountAssetAsset, self).set_to_close()                    