# API 文档 - 词典

## 1. /api/dicts
- 类型：GET
- 参数：
	- `uid`：整数，用户id
	- `pwhash`：字符串，密码哈希
- 返回1：`{'success': False}`
	- 400：用户名或密码哈希为空
	- 401：用户名或密码错误
	- 500：系统错误
- 返回2：`{'success': True, 'dicts': dicts}`（200）

## 2. /api/dict
- 类型：POST
- 参数：
	- `uid`：整数，用户id
	- `pwhash`：字符串，密码哈希
	- `dictname`：字符串，词典名称
- 返回1：`{'success': False, 'message': 'Missing required fields'}`（400）
- 返回2：`{'success': False}`
	- 401：用户名或密码错误
	- 500：系统错误
- 返回3：`{'success': True, 'dict_id': dict_id, 'message': 'Dictionary created'}`（200）
