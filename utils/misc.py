#
#   Utility functions
#
import sys
import socket
import urllib.parse as urlparse


def check_domain(target_url):
    """Get the target url from the user, clean and return it"""

    domain = urlparse.urlparse(target_url).hostname

    try:
        if socket.gethostbyname(domain):
            pass
    except Exception:
        print("[!] Domain doesn't resolve. Check URL")
        sys.exit(1)


def prepare_target(target_url):
    """Examine target url compliance adding default handle (http://) and look for a final /"""

    if not target_url.startswith("http://") and not target_url.startswith(
        "https://"
    ):
        target_url = f"http://{target_url}"
    if not target_url.endswith("/") and "***" not in target_url:
        target_url += "/"
    check_domain(target_url)
    return target_url


def prepare_proxies(proxies):
    """It takes a list of proxies and returns a dictionary"""

    if proxies:
        proxies_dict = {}
        for proxy_item in proxies:
            if proxy_item.startswith("http://"):
                proxies_dict["http"] = proxy_item
            elif proxy_item.startswith("https://"):
                proxies_dict["https"] = proxy_item
        return proxies_dict
    return {}


def make_cookie_jar(cookies):
    d = {}
    c = cookies.split(",")
    if c[0] == "":
        return d
    for entry in c:
        key, value = entry.split(":")
        d[key] = value
    return d
