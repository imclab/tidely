#!/usr/bin/env python

import os
import sys
import web

curdir = os.path.dirname(__file__)
if curdir not in sys.path: sys.path.append(curdir)

import xtide

class graph:
    def GET(self):
        i = web.input()

        start_time = None
        if "site" not in i: return "No site specified."
        if "time" in i: start_time = float(i.time)

        web.header('Content-Type', 'image/png')
        g = xtide.xtide_graph(i.site, start_time = start_time)
        return g
