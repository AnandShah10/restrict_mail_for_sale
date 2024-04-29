from odoo import models, fields, api, _
from odoo.exceptions import UserError
from markupsafe import Markup
import re


class MailThread(models.AbstractModel):
    _inherit = 'sale.order'

    # @api.model
    # def message_post(self, **kwargs):
    #     partner_ids = kwargs.get('partner_ids')
    #     print('partner_ids--------', partner_ids)
    #     print('partner_ids--------', self, self.message_partner_ids)
    #     subtype_xmlid = kwargs.get('subtype_xmlid')
    #     if self.message_partner_ids and subtype_xmlid == 'mail.mt_comment' and not partner_ids:
    #         print('enter here........')
    #         partner_restricted = self.env['res.partner'].search([
    #             ('id', 'in', self.message_partner_ids.ids),
    #             ('restrict_mail', '=', True)
    #         ])
    #         print('partner_restricted-----', partner_restricted)
    #         # if partner_restricted:
    #         #     raise UserError("Email not sent to restricted partners")
    #     if partner_ids and subtype_xmlid == 'mail.mt_comment':
    #         partner_restricted = self.env['res.partner'].search(
    #             [('id', 'in', partner_ids), ('restrict_mail', '=', True)])
    #         if partner_restricted:
    #             raise UserError('Email not sent to restricted partners')
    #     return super(MailThread, self).message_post(**kwargs)

    def action_confirm(self):
        super(MailThread, self).action_confirm()
        partner_id = []
        for partner in self.partner_id:
            if partner.restrict_mail:
                partner_id.append(partner.id)
            self.message_unsubscribe(partner_id)

    # To restrict Follower
    def _notify_get_recipients(self, message, msg_vals, **kwargs):
        print(message, 'mmmmmmmmmmmm')
        print(message.partner_ids, 'reciver.............')
        print(message.body, 'body........................')
        recipients = list(message.partner_ids.ids)  # Recipients Of The Message
        print(msg_vals, 'MMMMMMMMMMMMMMMMMMM')
        print(kwargs, 'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
        data = super()._notify_get_recipients(message, msg_vals, **kwargs)
        print(data, 'ddddddddddddddddddddddddddd')
        restrict = []
        filtered_recipients = []
        if msg_vals['subtype_id'] == 1:  # For Message send
            for i in data:
                # Restricted Partners
                partner_restricted = self.env['res.partner'].search(
                    [('id', '=', i['id']), ('restrict_mail', '=', True)])
                print(partner_restricted, 'restrict.................')
                if partner_restricted:
                    print("helllo")
                    print(type(msg_vals['body']))
                    print(msg_vals['body'], 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                    # To remove name of resctricted partner
                    anchor_pattern = r'<a[^>]*>@' + str(partner_restricted.name) + r'</a>'
                    new_message_body = re.sub(anchor_pattern, '', str(message.body))
                    # new_message_body = str(message.body).replace(f'@{partner_restricted.name}', '')
                    # new_body = str(msg_vals['body']).replace(f'@{partner_restricted.name}', '')
                    new_body = re.sub(anchor_pattern, '', str(msg_vals))
                    msg_vals['body'] = Markup(new_body)
                    message.body = new_message_body  # New Message Body
                    print(message.body, 'bodyyyyyyyyyyyyyyyyyyyyyyyyyy')
                    print(msg_vals['body'], 'yyyyyyyyyyyyyyyyyyyyyyyyyy')
                    restrict.append(partner_restricted.id)

                else:
                    print('hi')
                    pass
                print(i, 'data11111111111111111111111111111')

        filtered_list = [item for item in data if item['id'] not in restrict]
        if recipients:
            for i in recipients:
                if i not in restrict:
                    filtered_recipients.append(i)
        # To only have non restricted partner as recipients
        message.partner_ids = [(5, 0, 0)]
        message.partner_ids = [(6, 0, filtered_recipients)]
        print(filtered_list, 'filter,,,,,,,,,,,,,,,,,,,,,')
        print(filtered_recipients, 'fillllllllll')
        print(message.partner_ids, 'pppppppppppppppppart')
        return filtered_list  # Non restricted


class ResPartner(models.Model):
    _inherit = 'res.partner'

    restrict_mail = fields.Boolean(default=False)
