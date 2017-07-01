import ConfigParser
cfg=ConfigParser.ConfigParser()
print(cfg.read("settings.cfg"))
print(cfg)
demoString=cfg.get('english','greeting')
print(demoString)