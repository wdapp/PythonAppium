import os,sys
BIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BIR)
# yaml配置文件的路径
# yamlpath = "%s\conf\driver_config.yaml"%BIR  #方式一
yamlpath = os.path.join(BIR,'conf','driver_config.yaml') #方式二
# 日志文件
log_path = BIR+"\log\log.log"
screen_path = os.path.join(BIR,'screenshots')

