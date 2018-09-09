import falcon
import re


def build_error(message):
    return {
        "message": message,
    }


class WifiResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.media = [{"a":"b"}, {"c": "d"}]

    def on_post(self, req, resp):
        info = req.media

        try:
            print(info.ssid)
            print(info.psk)
        except AttributeError as e:
            m = re.search("no attribute '(.*?)'", e.message)
            if m:
                resp.status = falcon.HTTP_400
                resp.media = build_error("{} is missing".format(m.group(1)))
            else:
                raise e


class RequireJSON(object):
    def process_request(self, req, resp):
        if not req.client_accepts_json:
            raise falcon.HTTPNotAcceptable(
                'This API only supports responses encoded as JSON.',
                href='https://json.org/example.html')

        if req.method in ('POST', 'PUT'):
            if 'application/json' not in req.content_type:
                raise falcon.HTTPUnsupportedMediaType(
                    'This API only supports requests encoded as JSON.',
                    href='https://json.org/example.html')


app = falcon.API(middleware=[
    RequireJSON()
])

wifi = WifiResource()
app.add_route('/wifi', wifi)
