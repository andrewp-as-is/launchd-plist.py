#!/usr/bin/env python
import os
import launchd_plist


class MyPlist(launchd_plist.Plist):
    Label = "MyPlist"
    StartInterval = 1
    Custom_key = "works for Capitalized keys!"

    @property
    def StandardErrorPath(self):
        return os.path.expanduser("~/Logs/LaunchAgents/%s/err.log" % self.Label)


path = "/tmp/launchd.plist"
MyPlist().create(path)
print(open(path).read())
