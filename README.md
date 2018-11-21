[![](https://img.shields.io/pypi/pyversions/launchd-plist.svg?longCache=True)](https://pypi.org/pypi/launchd-plist/)
[![](https://img.shields.io/pypi/v/launchd-plist.svg?maxAge=3600)](https://pypi.org/pypi/launchd-plist/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/launchd-plist.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/launchd-plist.py/)

#### Install
```bash
$ [sudo] pip install launchd-plist
```

#### Features
+   based on [launchd.plist keys](https://www.real-world-systems.com/docs/launchd.plist.5.html)

#### Classes

###### `launchd_plist.Plist`

launchd plist class

method|description
-|-
`create(path)`|create .plist file
`load(path)`|load data from .plist file

@property|description
-|-
`data`|return dictionary with launchd plist keys only

#### Examples
```python
>>> class MyPlist(launchd_plist.Plist):
    Label = "MyPlist"
    StartInterval = 1

    @property
    def StandardErrorPath(self):
        return "path/to/logs/%s/err.log" % self.Label

>>> MyPlist().create('path/to/launchagent.plist')
```

[launchd.plist keys](https://www.real-world-systems.com/docs/launchd.plist.5.html)
```python
>>> launchd_plist.KEYS
['Label', ..., 'Sockets']
```

#### Links
+   [launchd.plist(5) Mac OS](https://www.real-world-systems.com/docs/launchd.plist.5.html)

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>