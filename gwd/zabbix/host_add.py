from pyzabbix import ZabbixAPI

# Zabbix 服务器信息
ZABBIX_SERVER = 'http://your_zabbix_server/zabbix'
ZABBIX_USER = 'your_username'
ZABBIX_PASSWORD = 'your_password'

# 要导入的 IP 列表
IP_ADDRESSES = [
    '192.168.1.1',
    '192.168.1.2',
    '192.168.1.3'
]

# 监控项模板 ID（需要根据实际情况替换）
TEMPLATE_ID = '10001'

# 主机组 ID（需要根据实际情况替换）
HOSTGROUP_ID = '2'

def create_hosts(zapi, ip_addresses, template_id, hostgroup_id):
    for ip in ip_addresses:
        # 定义主机名称
        host_name = f'Host_{ip.replace(".", "_")}'

        # 检查主机是否已经存在
        existing_hosts = zapi.host.get(filter={"host": host_name})
        if existing_hosts:
            print(f'主机 {host_name} 已存在，跳过创建。')
            continue

        # 创建主机
        try:
            host = zapi.host.create(
                host=host_name,
                interfaces=[{
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": ip,
                    "dns": "",
                    "port": "10050"
                }],
                groups=[{
                    "groupid": hostgroup_id
                }],
                templates=[{
                    "templateid": template_id
                }]
            )
            print(f'成功创建主机 {host_name}，主机 ID: {host["hostids"][0]}')
        except Exception as e:
            print(f'创建主机 {host_name} 时出错: {e}')

def main():
    # 连接到 Zabbix 服务器
    zapi = ZabbixAPI(ZABBIX_SERVER)
    zapi.login(ZABBIX_USER, ZABBIX_PASSWORD)
    print(f'成功连接到 Zabbix 服务器: {ZABBIX_SERVER}')

    # 创建主机并关联模板
    create_hosts(zapi, IP_ADDRESSES, TEMPLATE_ID, HOSTGROUP_ID)

    # 断开与 Zabbix 服务器的连接
    zapi.user.logout()

if __name__ == "__main__":
    main()