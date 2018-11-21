#!/usr/bin/env python
import launchd_plist

plist = launchd_plist.Plist(Label="Label example")
print(plist)
plist["StartInterval"] = 1
print(plist.data)
