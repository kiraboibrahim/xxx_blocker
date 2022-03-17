import urllib
import re
import requests
import logging
import sys
from bs4 import BeautifulSoup as bs
from config import HOSTS_FILE, GOOGLE_SEARCH_QUERY, RESOLVE_TO

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
# File Handler - Log messages to a file
fh = logging.FileHandler("porn_blocker.log", mode="w", encoding="utf-8")
# Format log messages in form <datetime>: <levelname>: <log message>
formatter = logging.Formatter('%(asctime)s: %(levelname)s %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

headers = {
    "User-Agent": "Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0", 
}

comment = "# Add this to your original hosts file (/etc/hosts)\n# Feel free to add any hosts that are absent\n\n"

def download(url):
    try:
        return requests.get(url, headers=headers).text
    except Exception as e:
        logger.error(str(e))
        sys.exit(-1)

def get_host_name(href): 
    host =urllib.parse.urlparse(urllib.parse.parse_qs(urllib.parse.urlparse(urllib.parse.parse_qs(urllib.parse.urlparse(href).query)['q'][0]).query)['u'][0]).netloc
    return host
        
def get_porn_hosts():
    porn_hosts = []
    # Get 'all (not all)' websites that host adult content (pornography)
    soup = bs(download(GOOGLE_SEARCH_QUERY), "html.parser")
    links = soup.find_all(href=re.compile("^/url\?q=https://googleweblight\.com.*"))
    
    # Write to resolv.conf 
    with open(HOSTS_FILE, 'w') as f:
        f.write(comment)
        for link in links:
            porn_hosts.append(get_host_name(link['href']))
        # Remove duplicates
        porn_hosts = set(porn_hosts)
        for host in porn_hosts:
            f.write("%s\t%s\n" %(RESOLVE_TO, host))
        
get_porn_hosts()
