# -*- coding:utf-8 -*-
import json
from django.http import HttpResponse
from ansible_api import AnsibleAPI

def ansible_runner(request):
  ip = request.POST.get('ip', '')
  username = request.POST.get('username', '')
  password = request.POST.get('password', '')
  command = request.POST.get('command', '')
  port = request.POST.get('port', '')

  resource = [
  {'hostname': ip, 'ip':ip, 'username': username, 'password':password, 'port':port},
  ]

  api = AnsibleAPI(resource)
  # 开始模拟以ad-hoc方式运行ansible命令
  api.run(
    [ip,],          # 指出本次运行涉及的主机，在resource中定义
    'command',      # 本次运行使用的模块
    command,        # 模块的参数
        )
  # 获取结果，是一个字典格式，如果是print可以用json模块美化一下
  return HttpResponse(json.dumps(api.get_result(),indent=4))

# curl -d "ip=172.16.3.195&username=root&password=@381af846c3eb6ec&command=hostname&port=77" "http://172.16.5.14//ansible_api/"
