<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/launchd-plist.svg?maxAge=3600)](https://pypi.org/project/launchd-plist/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/launchd-plist.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/launchd-plist.py/actions)

### Installation
```bash
$ [sudo] pip install launchd-plist
```

#### Features
+   Capitalized attrs and properties identified as launchd.plist keys (custom keys also supported)

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

#### Related
+   [`launchd-env` - launchd.plist environment variables](https://pypi.org/project/launchd-env/)
+   [`launchd-exec` - execute script via launchd](https://pypi.org/project/launchd-exec/)
+   [`launchd-generator` - launchd.plist generator](https://pypi.org/project/launchd-generator/)
+   [`launchd-logs` - launchd.plist logs](https://pypi.org/project/launchd-logs/)
+   [`launchctl.py` - `launchctl` python interface](https://pypi.org/project/launchd-plist/)
+   [`launchd-plist.py` - launchd.plist class](https://pypi.org/project/launchd-plist/)

#### Links
+   [launchd.plist](https://www.real-world-systems.com/docs/launchd.plist.5.html)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
