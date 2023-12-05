# -*- coding: utf-8 -*-
# Koda

import json

from koda import http
from koda.http import request
from koda.tools import misc


class ImportController(http.Controller):

    @http.route('/base_import/set_file', methods=['POST'])
    # pylint: disable=redefined-builtin
    def set_file(self, id):
        file = request.httprequest.files.getlist('ufile')[0]

        written = request.env['base_import.import'].browse(int(id)).write({
            'file': file.read(),
            'file_name': file.filename,
            'file_type': file.content_type,
        })

        return json.dumps({'result': written})
