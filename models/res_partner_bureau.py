# -*- coding: utf-8 -*-
from odoo import fields, models, api


class res_partner_bureau(models.Model):
    _name = 'res.partner.bureau'

    res_partner_id = fields.Many2one(
        'res.partner', 'Partner',
    )
    comment = fields.Char('Comment',
                          size=1024,
                          )
    date = fields.Date('Payment Date',
                       )
    amount = fields.Float('Amount',
                          )