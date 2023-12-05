# # -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from koda.exceptions import UserError
from koda.tests import tagged, HttpCase
from koda.tools import file_open

@tagged('post_install', '-at_install')
class TestHrRecruitmentSign(HttpCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        with file_open('sign/static/demo/sample_contract.pdf', "rb") as f:
            pdf_content = f.read()

        cls.attachment = cls.env['ir.attachment'].create({
            'type': 'binary',
            'raw': pdf_content,
            'name': 'test_applicant_contract.pdf',
        })

        cls.applicant = cls.env['hr.applicant'].create({
            'name': 'Caped Baldy',
        })
        cls.template = cls.env['sign.template'].create({
            'name': 'recruitment test template',
            'attachment_id': cls.attachment.id,
        })
        cls.env['sign.item'].create([
            {
                'type_id': cls.env.ref('sign.sign_item_type_text').id,
                'required': True,
                'responsible_id': cls.env.ref('sign.sign_item_role_customer').id,
                'page': 1,
                'posX': 0.273,
                'posY': 0.158,
                'template_id': cls.template.id,
                'width': 0.150,
                'height': 0.015,
            }
        ])

    def test_send_applicant_sign_request(self):
        with self.assertRaises(UserError):
            # can't unlink the campaign as it's used by a job as it's referral campaign
            # unlinking the campaign would break sent referral links
            self.applicant._send_applicant_sign_request()

        self.applicant.write({
            'partner_name': 'Saitama',
            'email_from': 'caped.baldy@heroassociation.net',
        })
        self.applicant.partner_id = self.env['res.partner'].create({
            'is_company': False,
            'name': self.applicant.partner_name,
            'email': self.applicant.email_from,
        })
        wizard = self.env['hr.recruitment.sign.document.wizard'].create({
            'applicant_id': self.applicant.id,
            'partner_id': self.applicant.partner_id.id,
            'partner_name': self.applicant.partner_name,
            'sign_template_ids': self.template,
            'applicant_role_id': self.env.ref('sign.sign_item_role_customer').id,
            'subject': 'Signature Request Test',
            'message': 'test',
        })
        wizard.validate_signature()

        # create the employee
        self.start_tour("/web", 'applicant_sign_request_tour', login='admin', timeout=300)

        self.assertEqual(self.applicant.sign_request_count, 1)
        self.assertEqual(self.applicant.emp_id.sign_request_count, 1)
