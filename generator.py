CONFIG = {
    "copyright": "2022 天依网络 保留所有权利",
    "link_href": "/",
    "link_desc": "返回首页"
}
CSS = ["awsl.min.css", "style.css"]
ERRORS = [
    {"code": 301, "img": 301, "title": "HTTP 301 信息: 页面跳转", "msg": "您这边请。<br>所请求资源 URI 已被永久更改。您将被跳转到另一个页面。"},
    {"code": 302, "img": 302, "title": "HTTP 302 信息: 页面跳转", "msg": "您这边请。<br>所请求资源 URI 已被暂时更改。您将被跳转到另一个页面。"},
    {"code": 400, "img": 400, "title": "HTTP 400 错误: 请求格式不正确", "msg": "你要干什么？不可以干坏事哦！<br>请求的格式不正确，服务器无法处理您的请求。"},
    {"code": 401, "img": 401, "title": "HTTP 401 错误: 需要身份验证", "msg": "天依需要验证你的身份！<br>您需要验证身份才能访问该页面。"},
    {"code": 403, "img": 403, "title": "HTTP 403 错误: 没有访问权限", "msg": "不可以涩涩！<br>您没有访问该页面所需的权限。"},
    {"code": 404, "img": 404, "title": "HTTP 404 错误: 找不您请求的页面", "msg": "欸嘿？<br>您访问的页面不存在，它可能被移动到其他地方、被删除或是被天依吃掉了。"},
    {"code": 405, "img": 405, "title": "HTTP 405 错误: 不允许使用该请求方法", "msg": "不可以涩涩！<br>目标资源不支持该 HTTP 方法。或许只有阿绫可以？"},
    {"code": 418, "img": 500, "title": "HTTP 418 错误: 只有红茶可以吗？", "msg": "这是根据 RFC 2324 定义的 HTCPCP 错误，当请求一个茶壶冲泡咖啡的时候会返回此错误。天依暂时不想喝咖啡，想和天依一切喝茶吗？"},
    {"code": 451, "img": 500, "title": "HTTP 451 错误: 欢迎来到美丽新世界！", "msg": "欢迎来到美丽新世界！此站点被管理员暂停访问。希望我们终将在没有黑暗的地方相遇，在自由的阳光下各抒己见。"},
    {"code": 500, "img": 500, "title": "HTTP 500 错误: 服务器错误", "msg": "服务器发生了一个错误。可能是因为服务器被天依啃了。"},
]

import os
import base64

def get_err_img(code: int):
    filename = f"images/{code}.png" if code != 500 else "images/500.gif"
    mimetype = "image/png" if code != 500 else "image/gif"
    with open(filename, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return f"data:{mimetype};base64,{data}"

template = open("template.html", "r", encoding="utf-8").read()
template = template.strip().replace("\r", "").replace("\n", "")

CONFIG["css"] = ""
for css_file in CSS:
    CONFIG["css"] += "<style>" + open(f"css/{css_file}", "r", encoding="utf-8").read() + "</style>"

for error in ERRORS:
    format_strings = CONFIG.copy()
    format_strings["err_title"] = error["title"]
    format_strings["err_desc"] = error["msg"]
    format_strings["err_img"] = get_err_img(error["img"])
    print(f"Generating HTML: {error['code']} - {error['title']}")
    os.makedirs("dist", exist_ok=True)
    with open(f"dist/{error['code']}.html", "w+", encoding="utf-8") as f:
        f.write(template.format(**format_strings))
