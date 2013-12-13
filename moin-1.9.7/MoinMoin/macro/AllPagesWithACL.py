# -*- coding: utf-8 -*-
"""
    MoinMoin - AllPagesWithACL Macro

    @copyright: 2007 Alexander "Loki" Agibalov
    @license: GNU GPL, see COPYING for details.

    changes:
        12.2007 - conversion to new syntax by Bolesław Kulbabiński
"""

import os
import re
from MoinMoin.Page import Page
from MoinMoin import wikiutil

def getAcl(request, pagename):
    pg = Page(request, pagename)
    pi = pg.get_pi()
    ret = pi["acl"].getString()
    if ret == '':
        ret = "not defined"
    return ret


def macro_AllPagesWithACL(macro, args):
    html = "<p><b>All pages:</b><br>"
    all = {}
    pages = macro.request.rootpage.getPageList()
#   pages = macro.request.rootpage.getPageList(filter = re.compile("^WikiSandBox").match)
    html += "Total: %s pages </p>" % str(len(pages))

    for pagename in pages:
        all[Page(macro.request, pagename).link_to(macro.request)] = getAcl(macro.request, pagename)

    html += "<table>"
    all1 = sorted(all.items())
    for pg, ac in all1:
        html += "<tr><td>%s</td>" % pg
        html += "<td>%s</td></tr>" % ac
    html += "</table>"

    return macro.formatter.rawHTML(html)


def execute(macro, args):
    try:
        return wikiutil.invoke_extension_function(
                   macro.request, macro_AllPagesWithACL, args, [macro])
    except ValueError, err:
        return macro.request.formatter.text(
                   "<<AllPagesWithACL: %s>>" % err.args[0])