#!/usr/bin/env python

def html_tag(tag):
    def wrap_text(text):
        return f"<{tag}>{text}</{tag}>"

    return wrap_text

h1_tag = html_tag("h1")
h2_tag = html_tag("h2")
print(h1_tag("TITLE"))
print(h2_tag("subtitle"))
