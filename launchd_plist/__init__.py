#!/usr/bin/env python
import os
import plistlib
import public


"""
https://www.real-world-systems.com/docs/launchd.plist.5.html
"""

KEYS = [
    "Label",
    "Disabled",
    "UserName",
    "GroupName",
    "inetdCompatibility",
    "LimitLoadToHosts",
    "LimitLoadFromHosts",
    "LimitLoadToSessionType",
    "Program",
    "ProgramArguments",
    "EnableGlobbing",
    "EnableTransactions",
    "OnDemand",
    "KeepAlive",
    "RunAtLoad",
    "RootDirectory",
    "WorkingDirectory",
    "EnvironmentVariables",
    "Umask",
    "TimeOut",
    "ExitTimeOut",
    "ThrottleInterval",
    "InitGroups",
    "WatchPaths",
    "QueueDirectories",
    "StartOnMount",
    "StartInterval",
    "StartCalendarInterval",
    "StandardInPath",
    "StandardOutPath",
    "StandardErrorPath",
    "Debug",
    "WaitForDebugger",
    "SoftResourceLimits",
    "HardResourceLimits",
    "Nice",
    "ProcessType",
    "AbandonProcessGroup",
    "LowPriorityIO",
    "LaunchOnlyOnce",
    "MachServices",
    "Sockets"
]


def _mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def _mktouch(path):
    _mkdir(os.path.dirname(path))
    if not os.path.exists(path):
        open(path, "w").write("")


@public.add
class Plist:
    """launchd.plist generator"""
    __readme__ = ["data", "load", "create"]

    def __init__(self, **kwargs):
        self.update(kwargs)

    def update(self, *args, **kwargs):
        """Update the dictionary with the key/value pairs from other, overwriting existing keys"""
        inputdict = dict(*args, **kwargs)
        for k, v in inputdict.items():
            setattr(self, k, v)

    def get(self, key, default=None):
        """return the value for key if key is in the dictionary, else default"""
        return getattr(self, key, default)

    @property
    def data(self):
        """return dictionary with launchd plist keys only"""
        result = dict()
        for key in KEYS:
            if hasattr(self, key):
                value = getattr(self, key)
                if value is not None:
                    result[key] = value
        return result

    def load(self, path):
        """load data from .plist file"""
        data = plistlib.readPlist(path)
        self.update(data)
        return self

    def create(self, path):
        """create .plist file"""
        _mkdir(os.path.dirname(path))
        plistlib.writePlist(self.data, path)
        for key in ["StandardErrorPath", "StandardOutPath"]:
            path = getattr(self, key, None)
            if path:
                _mktouch(path)

    def __contains__(self, key):
        """return hasattr(self,key)"""
        return hasattr(self, key) and getattr(self, key, None) is not None

    def __getitem__(self, key):
        """return getattr(self,key)"""
        return getattr(self, key)

    def __setitem__(self, key, value):
        """setattr(self,key, value)"""
        return setattr(self, key, value)

    def __str__(self):
        return "<%s Label='%s'>" % (self.__class__.__name__, self.get("Label", "UNKNOWN"))

    def __repr__(self):
        return self.__str__()
