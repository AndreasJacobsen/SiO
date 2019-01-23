# Project created as part of bachelor thesis at OsloMet 
## IMPORTANT
This project has NOT been updated in sevral years, a through security audit and update of Django version is required before you use this project.
The project contains previously hidden mailgun keys, these are now inactive. 

### Known security issues
Vulnerable versions: < 4.2b1
Patched version: 4.2b1
In PyYAML before 4.1, the yaml.load() API could execute arbitrary code. In other words, yaml.safe_load is not used.
---------

A maliciously crafted URL to a Django (1.10 before 1.10.7, 1.9 before 1.9.13, and 1.8 before 1.8.18) site using the django.views.static.serve() view could redirect to any other domain, aka an open redirect vulnerability.

In Django 1.10.x before 1.10.8 and 1.11.x before 1.11.5, HTML autoescaping was disabled in a portion of the template for the technical 500 debug page. Given the right circumstances, this allowed a cross-site scripting attack. This vulnerability shouldn't affect most production sites since you shouldn't run with "DEBUG = True" (which makes this page accessible) in your production settings.

Django 1.10 before 1.10.7, 1.9 before 1.9.13, and 1.8 before 1.8.18 relies on user input in some cases to redirect the user to an "on success" URL. The security check for these redirects (namely django.utils.http.is_safe_url()) considered some numeric URLs "safe" when they shouldn't be, aka an open redirect vulnerability. Also, if a developer relies on is_safe_url() to provide safe redirect targets and puts such a URL into a link, they could suffer from an XSS attack.

In Django 1.11.x before 1.11.18, 2.0.x before 2.0.10, and 2.1.x before 2.1.5, an Improper Neutralization of Special Elements in Output Used by a Downstream Component issue exists in django.views.defaults.page_not_found(), leading to content spoofing (in a 404 error page) if a user fails to recognize that a crafted URL has malicious content.

------------

Vulnerable versions: <= 2.19.1
Patched version: 2.20.0
The Requests package through 2.19.1 before 2018-09-14 for Python sends an HTTP Authorization header to an http URI upon receiving a same-hostname https-to-http redirect, which makes it easier for remote attackers to discover credentials by sniffing the networ

--------------
Vulnerable versions: < 1.2.1
Patched version: 1.2.1
webhooks/base.py in Anymail (aka django-anymail) before 1.2.1 is prone to a timing attack vulnerability on the WEBHOOK_AUTHORIZATION secret, which allows remote attackers to post arbitrary e-mail tracking events.

--------------
