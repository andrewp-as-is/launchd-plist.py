<!--
https://pypi.org/project/readme-generator/
-->

[![](https://img.shields.io/badge/OS-MacOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/pyversions/launchd-plist.svg?longCache=True)](https://pypi.org/project/launchd-plist/)
[![](https://img.shields.io/pypi/v/launchd-plist.svg?maxAge=3600)](https://pypi.org/project/launchd-plist/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/launchd-plist.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/launchd-plist.py/)

#### Installation
```bash
$ [sudo] pip install launchd-plist
```

#### Features
+   Capitalized attrs and properties identified as launchd.plist keys (custom keys also supported)

#### Classes
class|`__doc__`
-|-
`launchd_plist.Plist` |launchd.plist class

#### Functions
function|`__doc__`
-|-
`launchd_plist.read(path)` |return a dictionary with a plist file data
`launchd_plist.update(path, **kwargs)` |update a plist file
`launchd_plist.write(path, data)` |write a dictionary to a plist file

#### Examples
```python
>>> class MyPlist(launchd_plist.Plist):
    Label = "MyPlist"
    StartInterval = 1
    Custom_key = "works"

    @property
    def StandardErrorPath(self):
        return os.path.expanduser("~/Logs/LaunchAgents/%s/err.log" % self.Label)

>>> MyPlist().create('launchd.plist')
```

`launchd.plist`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Custom_key</key>
    <string>works for Capitalized keys!</string>
    <key>Label</key>
    <string>MyPlist</string>
    <key>StandardErrorPath</key>
    <string>/Users/russianidiot/Logs/LaunchAgents/MyPlist/err.log</string>
    <key>StartInterval</key>
    <integer>1</integer>
</dict>
</plist>
```

#### Related projects
+   [`launchd-env` - launchd.plist environment variables](https://pypi.org/project/launchd-env/)
+   [`launchd-exec` - execute script via launchd](https://pypi.org/project/launchd-exec/)
+   [`launchd-generator` - launchd.plist generator](https://pypi.org/project/launchd-generator/)
+   [`launchd-logs` - launchd.plist logs](https://pypi.org/project/launchd-logs/)
+   [`launchctl.py` - `launchctl` python interface](https://pypi.org/project/launchd-plist/)
+   [`launchd-plist.py` - launchd.plist class](https://pypi.org/project/launchd-plist/)

#### Links
+   [launchd.plist](https://www.real-world-systems.com/docs/launchd.plist.5.html)

<p align="center">
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>