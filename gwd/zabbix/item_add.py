from pyzabbix import ZabbixAPI

# Zabbix 服务器信息
ZABBIX_SERVER = 'http://your_zabbix_server/zabbix'
ZABBIX_USER = 'your_username'
ZABBIX_PASSWORD = 'your_password'

# 要添加监控项的主机名称列表
HOST_NAMES = [
    'Host1',
    'Host2',
    'Host3'
]

# 监控项配置
ITEM_CONFIG = {
    'name': 'Custom CPU Usage',  # 监控项名称
    'key_': 'system.cpu.util[,avg1]',  # 监控项键值
    'type': 0,  # 监控项类型，0 表示 Zabbix agent
    'value_type': 0,  # 数据类型，0 表示数值（浮点型）
    'interfaceid': None,  # 接口 ID，后续会根据主机获取
    'delay': 60  # 数据采集间隔（秒）
}


def add_items_to_hosts(zapi, host_names, item_config):
    for host_name in host_names:
        # 获取主机 ID
        hosts = zapi.host.get(filter={"host": host_name})
        if not hosts:
            print(f"未找到主机: {host_name}，跳过添加监控项。")
            continue
        host_id = hosts[0]['hostid']

        # 获取主机的第一个接口 ID
        interfaces = zapi.hostinterface.get(hostids=host_id)
        if not interfaces:
            print(f"主机 {host_name} 没有可用接口，跳过添加监控项。")
            continue
        item_config['interfaceid'] = interfaces[0]['interfaceid']

        # 检查监控项是否已经存在
        existing_items = zapi.item.get(filter={"hostid": host_id, "key_": item_config['key_']})
        if existing_items:
            print(f"主机 {host_name} 已经存在监控项 {item_config['key_']}，跳过添加。")
            continue

        try:
            # 添加监控项
            item = zapi.item.create(
                hostid=host_id,
                name=item_config['name'],
                key_=item_config['key_'],
                type=item_config['type'],
                value_type=item_config['value_type'],
                interfaceid=item_config['interfaceid'],
                delay=item_config['delay']
            )
            print(f"成功为主机 {host_name} 添加监控项，监控项 ID: {item['itemids'][0]}")
        except Exception as e:
            print(f"为主机 {host_name} 添加监控项时出错: {e}")


def main():
    # 连接到 Zabbix 服务器
    zapi = ZabbixAPI(ZABBIX_SERVER)
    zapi.login(ZABBIX_USER, ZABBIX_PASSWORD)
    print(f"成功连接到 Zabbix 服务器: {ZABBIX_SERVER}")

    # 批量添加监控项到主机
    add_items_to_hosts(zapi, HOST_NAMES, ITEM_CONFIG)

    # 断开与 Zabbix 服务器的连接
    zapi.user.logout()


if __name__ == "__main__":
    main()