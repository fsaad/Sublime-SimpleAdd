# Copyright (c) 2020 Feras A. Saad <fsaad@mit.edu>
# Released under the MIT License; refer to LICENSE.txt.

import sublime
import sublime_plugin

def to_float(z):
    try:
        return float(z)
    except ValueError:
        return 0

def simple_add_str(substr):
    x = substr.replace(',', ' ').replace('\n', ' ')
    y = x.split(' ')
    return [to_float(z) for z in y]

class simple_add(sublime_plugin.TextCommand):

    def run(self, edit):
        regions = list(self.view.sel())
        terms_list = [self.view.substr(region) for region in regions]
        terms_str = ' '.join(terms_list)
        x = simple_add_str(terms_str)
        s = sum(x)
        sublime.status_message('sum = %1.2f' % (s,))
