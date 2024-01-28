# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo import _
from .constant import BUREAU_TYPE
from .constant import TYPE_PERSON_SELECTION


class res_partner(models.Model):
    _inherit = 'res.partner'

    financed = fields.Boolean('Financed?')
    debt_bureau = fields.Float(
    )
    date_bureau = fields.Date('Bureau Date',
                              )
    date_due_bureau = fields.Date('Bureau Date Due',
                                  )
    type_bureau = fields.Selection(BUREAU_TYPE,
                                   string='Bureau Type',
                                   )
    type_person = fields.Selection(
        TYPE_PERSON_SELECTION, 'Type Person',
    )
    res_partner_bureau_ids = fields.One2many(
        'res.partner.bureau', 'res_partner_id',
    )
