# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class SaleSubscription(models.Model):
    _inherit = "sale.subscription"

    lead_id = fields.Many2one(
        string="# Lead",
        comodel_name="crm.lead",
        ondelete="restrict",
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )

    @api.multi
    def _prepare_criteria_allowed_lead_ids(self):
        self.ensure_one()
        criteria = [("id", "=", 0)]
        if self.partner_id:
            criteria = [
                ("partner_id", "=", self.partner_id.id),
            ]
        return criteria

    @api.multi
    def get_allowed_lead_ids(self):
        self.ensure_one()
        obj_crm_lead = self.env["crm.lead"]
        allowed_lead_ids = obj_crm_lead.search(
            self._prepare_criteria_allowed_lead_ids()
        )
        return allowed_lead_ids

    @api.multi
    @api.depends(
        "partner_id",
    )
    def _compute_allowed_lead_ids(self):
        for document in self:
            document.allowed_lead_ids = document.get_allowed_lead_ids()

    allowed_lead_ids = fields.Many2many(
        string="Allowed Leads",
        comodel_name="crm.lead",
        compute="_compute_allowed_lead_ids",
        store=False,
    )

    @api.onchange(
        "partner_id",
    )
    def onchange_lead_id(self):
        if self.partner_id:
            self.lead_id = False
