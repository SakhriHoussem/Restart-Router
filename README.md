# Restart Router
## Restart Router TP-link TD-W8968 programmatically

### Installation :

 - install [Python 3.6](https://www.python.org/downloads/release/python-360/)

 - install [Selenium](http://selenium-python.readthedocs.io/) python library with :
 
```shell
pip install selenium
```
### Download Driver:

Download browser driver to control it with python

 - [Chrome Driver](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver)
 - [FireFox Driver](https://github.com/mozilla/geckodriver/releases)
 - [Safari Driver](https://www.seleniumhq.org/download/)
 - [Opera Driver](https://github.com/operasoftware/operachromiumdriver/releases)
 - [Edge Driver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
 - [Internet Explorer Driver](https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver)

### executer : 

```python
Restart(link='http://192.168.1.1/',
  username="admin",
  password="admin",
  driver='chrome', # name in lowercase 
  driver_path='chromedriver.exe'
 )
```
