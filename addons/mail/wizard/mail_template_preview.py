# -*- coding: utf-8 -*-
# Koda

from koda import api, fields, models
from koda.exceptions import UserError


class MailTemplatePreview(models.TransientModel):
    _name = 'mail.template.preview'
    _description = 'Email Template Preview'
    _MAIL_TEMPLATE_FIELDS = ['attachment_ids',
                             'body_html',
                             'subject',
                             'email_cc',
                             'email_from',
                             'email_to',
                             'partner_to',
                             'report_template_ids',
                             'reply_to',
                             'scheduled_date',
                            ]

    @api.model
    def _selection_target_model(self):
        return [(model.model, model.name) for model in self.env['ir.model'].sudo().search([])]

    @api.model
    def _selection_languages(self):
        return self.env['res.lang'].get_installed()


    mail_template_id = fields.Many2one('mail.template', string='Related Mail Template', required=True)
    model_id = fields.Many2one('ir.model', string='Targeted model', related="mail_template_id.model_id")
    resource_ref = fields.Reference(
        string='Record',
        compute='_compute_resource_ref',
        compute_sudo=False, readonly=False,
        selection='_selection_target_model',
        store=True
    )
    lang = fields.Selection(_selection_languages, string='Template Preview Language')
    no_record = fields.Boolean('No Record', compute='_compute_no_record')
    error_msg = fields.Char('Error Message', compute='_compute_mail_template_fields')
    # Fields same than the mail.template model, computed with resource_ref and lang
    subject = fields.Char('Subject', compute='_compute_mail_template_fields')
    email_from = fields.Char('From', compute='_compute_mail_template_fields', help="Sender address")
    email_to = fields.Char('To', compute='_compute_mail_template_fields',
                           help="Comma-separated recipient addresses")
    email_cc = fields.Char('Cc', compute='_compute_mail_template_fields', help="Carbon copy recipients")
    reply_to = fields.Char('Reply-To', compute='_compute_mail_template_fields', help="Preferred response address")
    scheduled_date = fields.Char('Scheduled Date', compute='_compute_mail_template_fields',
                                 help="The queue manager will send the email after the date")
    body_html = fields.Html('Body', compute='_compute_mail_template_fields', sanitize=False)
    attachment_ids = fields.Many2many('ir.attachment', 'Attachments', compute='_compute_mail_template_fields')
    # Extra fields info generated by _generate_template
    partner_ids = fields.Many2many('res.partner', string='Recipients', compute='_compute_mail_template_fields')

    @api.depends('model_id')
    def _compute_no_record(self):
        for preview, preview_sudo in zip(self, self.sudo()):
            model_id = preview_sudo.model_id
            preview.no_record = not model_id or not self.env[model_id.model].search_count([])

    @api.depends('lang', 'resource_ref')
    def _compute_mail_template_fields(self):
        """ Preview the mail template (body, subject, ...) depending of the language and
        the record reference, more precisely the record id for the defined model of the mail template.
        If no record id is selectable/set, the inline_template placeholders won't be replace in the display information. """
        error_msg = False
        mail_template = self.mail_template_id.with_context(lang=self.lang)
        if not self.resource_ref or not self.resource_ref.id:
            self._set_mail_attributes()
            self.error_msg = False
        else:
            try:
                mail_values = mail_template.with_context(template_preview_lang=self.lang)._generate_template(
                    [self.resource_ref.id],
                    self._MAIL_TEMPLATE_FIELDS
                )[self.resource_ref.id]
                self._set_mail_attributes(values=mail_values)
            except (ValueError, UserError) as user_error:
                self._set_mail_attributes()
                error_msg = user_error.args[0]
        self.error_msg = error_msg

    @api.depends('mail_template_id')
    def _compute_resource_ref(self):
        for preview in self:
            mail_template = preview.mail_template_id.sudo()
            model = mail_template.model
            res = self.env[model].search([], limit=1)
            preview.resource_ref = f'{model},{res.id}' if res else False

    def _set_mail_attributes(self, values=None):
        for field in self._MAIL_TEMPLATE_FIELDS:
            if field in ('partner_to', 'report_template_ids'):
                # partner_to is used to generate partner_ids, handled here below
                # report_template_ids generates attachments, no usage here
                continue
            field_value = values.get(field, False) if values else self.mail_template_id[field]
            self[field] = field_value
        self.partner_ids = values.get('partner_ids', False) if values else False
