# Koda

from koda.addons.mrp.tests.common import TestMrpCommon


class TestMrpWorkorderCommon(TestMrpCommon):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        grp_workorder = cls.env.ref('mrp.group_mrp_routings')
        cls.env.user.write({'groups_id': [(4, grp_workorder.id)]})
