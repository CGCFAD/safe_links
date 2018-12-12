import urllib
import pyperclip


class SafeLinksUrl:
    def __init__(self):
        self.name = 'ATP Safe Links Url'
        self.url = pyperclip.paste()


class DecodedUrl:
    def __init__(self):
        self.name = 'Original Url'
        url = pyperclip.paste()
        url = url.split('url=', 1)[-1]
        url = url.split('&data')[0]
        url = urllib.unquote(url).decode('utf8')
        self.url = url


def main():
    """
    Extracts original URL from ATP Safe Links URL.
    pip install -r requirements.txt

    Usage:  copy ATP Safe Links URL from email to clipboard (select URL, CTRL+C or select URL, CMD+C)
            python safe_links.py
            paste original URL as needed from clipboard (CTRL+V or CMD+V)
    """
    _safe_links = SafeLinksUrl()
    _decoded = DecodedUrl()
    print('\n' + _safe_links.name + ': ' + _safe_links.url)
    print('\n' + _decoded.name + ': ' + _decoded.url + '\n')
    pyperclip.copy(_decoded.url)


if __name__ == '__main__':
    main()
