### PORN BLOCKER

#### Introduction

This porn blocker uses the hosts file located under the /etc (Linux Distributions) directory to block
access to websites that host adult content.

When a user visits the flagged porn hosts, user is redirected to localhost


**The adult content websites are obtained using google search techniques**

      intitle:"xxx videos"
      watch porn

The above google search query yields search results that have 'xxx videos' in their title
and the word 'watch' and 'porn' any where in the document.

**With the vast porn hosts out there, The results are not exhaustive and to combat that,
I have developed a chrome extension that scans the images on a website a user visits for nudity, if
found the webhost is flagged and the user is warned.**

#### Usage

* Run the main.py to generate a hosts file

      python3 main.py
      
* **Append** the contents of the generated 'hosts' file to the original hosts (/etc/hosts)
* Donot overwrite your original hosts file (It aint necessary)


#### Requirements
* Python 2 or Python 3