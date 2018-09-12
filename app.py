import falcon
import re

from wifi_list import scan_wifi_aps
from wpa import add_config, remove_existing_config
from connectivity import is_connected_to_internet


def build_message(message):
    return {
        "message": message,
    }


class WifiResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.media = scan_wifi_aps()

    def on_post(self, req, resp):
        info = req.media

        try:
            add_config(info["ssid"], info["psk"])
        except AttributeError as e:
            m = re.search("no attribute '(.*?)'", e.message)
            if m:
                resp.status = falcon.HTTP_400
                resp.media = build_message("{} is missing".format(m.group(1)))
            else:
                raise e

    def on_delete(self, req, resp):
        remove_existing_config()

        resp.status = falcon.HTTP_200
        resp.media = build_message("Removed wifi config")


class ConnectivityResource(object):
    def on_get(self, req, resp, dest):
        if dest == "internet":
            resp.status = falcon.HTTP_200
            resp.media = build_message(is_connected_to_internet())
        else:
            resp.status = falcon.HTTP_400
            resp.media = build_message("Malformed request")


class RequireJSON(object):
    def process_request(self, req, resp):
        if not req.client_accepts_json:
            raise falcon.HTTPNotAcceptable(
                "This API only supports responses encoded as JSON.",
                href="https://json.org/example.html")

        if req.method in ("POST", "PUT"):
            if "application/json" not in req.content_type:
                raise falcon.HTTPUnsupportedMediaType(
                    "This API only supports requests encoded as JSON.",
                    href="https://json.org/example.html")


app = falcon.API(middleware=[
    RequireJSON()
])

app.add_route("/wifi", WifiResource())
app.add_route("/connectivity/{dest}", ConnectivityResource())
