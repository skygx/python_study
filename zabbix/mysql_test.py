#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   mysql_test.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/3/1 下午 4:48   hello      1.0         None

'''
import pymysql
import time
import xlsxwriter

zbx_host = '192.168.226.20'
zbx_port = 3308
zbx_username = 'zabbix'
zbx_password = 'zabbix'
zbx_dbname = 'zabbix'

# 需要查询的服务器所在组名
groupname = 'Linux servers'
date = time.strftime("%Y%m%d", time.localtime())
fname = 'Zabbix_Report_weekly_%s.xlsx' % date

keys = [
    [u'CPU平均空闲值', 'trends', 'system.cpu.util[,idle]', 'avg', '%.2f', 1, ''],
    [u'CPU最小空闲值', 'trends', 'system.cpu.util[,idle]', 'min', '%.2f', 1, ''],
    [u'CPU5分钟负载', 'trends', 'system.cpu.load[all,avg5]', 'avg', '%.2f', 1, ''],
    [u'物理内存大小(单位G)', 'trends_uint', 'vm.memory.size[total]', 'avg', '', 1073741824, 'G'],
    [u'物理内存已用(单位G)', 'trends_uint', 'vm.memory.size[available]', 'avg', '', 1073741824, 'G'],
    [u'物理内存可用率(%)', 'trends', 'vm.memory.utilization', 'avg', '%.2f', 1, '%'],
    [u'swap总大小(单位G)', 'trends_uint', 'system.swap.size[,total]', 'avg', '', 1073741824, 'G'],
    [u'swap平均剩余(单位G)', 'trends_uint', 'system.swap.size[,free]', 'avg', '', 1073741824, 'G'],
    [u'根分区总大小(单位G)', 'trends_uint', 'vfs.fs.size[/,total]', 'avg', '', 1073741824, 'G'],
    [u'根分区剩余(单位G)', 'trends_uint', 'vfs.fs.size[/,free]', 'avg', '', 1073741824, 'G'],
    [u'根分区已使用(单位G)', 'trends_uint', 'vfs.fs.size[/,used]', 'avg', '', 1073741824, 'G'],
    [u'网卡进口流量(单位Kbps)', 'trends_uint', 'net.if.in["ens33"]', 'avg', '', 1024, 'Kbps'],
    [u'网卡出口流量(单位Kbps)', 'trends_uint', 'net.if.out["ens33"]', 'avg', '', 1024, 'Kbps'],
]

Title = [
    u'CPU5分钟负载',
    u'CPU平均空闲值',
    u'CPU最小空闲值',
    u'swap平均剩余(单位G)',
    u'swap总大小(单位G)',
    u'根分区剩余(单位G)',
    u'根分区总大小(单位G)',
    u'物理内存已用(单位G)',
    u'物理内存大小(单位G)',
    u'物理内存可用率(%)',
    u'网卡出口流量(单位Kbps)',
    u'网卡进口流量(单位Kbps)',
    u'硬盘使用率(单位%)',
    u'Swap剩余率(单位%)',
    u'内存使用率(单位%)',
    u'根分区已使用(单位G)'
]
Title_dict = {
    u'CPU5分钟负载': 1,
    u'CPU平均空闲值': 2,
    u'CPU最小空闲值': 3,
    u'swap平均剩余(单位G)': 4,
    u'swap总大小(单位G)': 5,
    u'根分区剩余(单位G)': 6,
    u'根分区总大小(单位G)': 7,
    u'物理内存已用(单位G)': 8,
    u'物理内存大小(单位G)': 9,
    u'物理内存可用率(%)': 10,
    u'网卡出口流量(单位Kbps)': 11,
    u'网卡进口流量(单位Kbps)': 12,
    u'硬盘使用率(单位%)': 13,
    u'Swap剩余率(单位%)': 14,
    u'内存使用率(单位%)': 15,
    u'根分区已使用(单位G)':16
}
disk_full = Title[6]
disk_free = Title[5]
disk_used = Title[15]
swap_full = Title[4]
swap_free = Title[3]
# swap_pfree = Title[16]

mem_full = Title[8]
mem_used = Title[7]
mem_pused = Title[9]

keys_disk = Title[12]
keys_swap = Title[13]
keys_mem = Title[14]
keys_cpu = Title[0]

class Test:
    def __init__(self):
        self.conn = pymysql.connect(host=zbx_host, port=zbx_port, user=zbx_username, passwd=zbx_password, db=zbx_dbname,
                                    charset="utf8")
        self.cursor = self.conn.cursor()


    def getgroupid(self):
        sql = "select groupid from hstgrp where name='%s'" % groupname
        self.cursor.execute(sql)
        # groupid = self.cursor.fetchone()['groupid']
        groupid = self.cursor.fetchone()[0]
        # print 'groupid is %s' % groupid
        return groupid

    def gethostid(self):
        # sql = '''select hostid from hosts_groups where groupid=(select groupid from groups where name='%s') ''' %groupname
        groupid = self.getgroupid()
        # print groupid
        sql = "select hostid from hosts_groups where groupid='%s'" % groupid
        self.cursor.execute(sql)
        hostid_list = self.cursor.fetchall()
        # print 'hostid_list:',hostid_list
        return hostid_list

    def gethostlist(self):
        host_list = {}
        hostid_list = self.gethostid()
        # print hostid_list
        for item in hostid_list:
            # print item
            # hostid = item['hostid']
            hostid = item[0]
            # print(hostid)
            sql = "select host from hosts where status=0 and flags=0 and hostid = %s" % hostid
            self.cursor.execute(sql)
            host_ip = self.cursor.fetchone()
            # print(host_ip)
            # print host_ip['host']
            # ！！！判断如果主机被zabbix改成disable的状态时，hosts表格里面host变为空后，字典空键赋值报错《TypeError: 'NoneType' object has no attribute '__getitem__'》
            if host_ip is None:
                continue
            host_list[host_ip[0]] = {'hostid': hostid}
        # print host_list
        return host_list

    def getitemid(self):
        hostid_list = self.gethostlist()
        # print hostid_list.items()
        keys_dict = {}
        for hostitem in hostid_list.items():
            hostip = hostitem[0]
            hostid = hostitem[1]['hostid']
            # print hostitem
            host_info = []
            for item in keys:
                keys_list = []
                keys_list.append({'title': item[0]})
                keys_list.append({'table': item[1]})
                keys_list.append({'itemname': item[2]})
                keys_list.append({'value': item[3]})
                keys_list.append({'form': item[4]})
                keys_list.append({'ratio': item[5]})
                keys_list.append({'unit': item[6]})
                itemname = item[2]
                sql = "select itemid from items where hostid='%s' and key_='%s'" % (hostid, itemname)
                self.cursor.execute(sql)
                itemid = self.cursor.fetchone()
                # print(itemid)
                if itemid is None:
                    continue
                keys_list.append(itemid)
                # keys_dict['itemid'] = itemid['itemid']
                # print hostip,keys_dict
                host_info.append(tuple(keys_list))
                # print host_info
            keys_dict[hostip] = host_info
        # print(keys_dict)
        return keys_dict

    def getvalue(self):
        # 时间区间为7天内
        stoptime = time.time() - 7 * 3600
        startime = time.time()
        host_info_list = self.getitemid()
        # print host_info_list
        host_dict = {}
        for ip in host_info_list:
            host_info = host_info_list[ip]
            length = len(host_info)
            # print(ip,length)
            host_item = {}
            for i in range(length):
                # print(host_info[i])
                value = host_info[i][3]['value']
                ratio = host_info[i][5]['ratio']
                table = host_info[i][1]['table']
                itemid = host_info[i][7][0]
                # itemname = host_info[i][2]['itemname']
                unit = host_info[i][6]['unit']
                title = host_info[i][0]['title']
                sql = "select avg(value_%s)/%s result from %s where itemid=%s and clock<=%d and clock>=%d" % (
                    value, ratio, table, itemid, startime, stoptime)
                self.cursor.execute(sql)
                result = self.cursor.fetchone()[0]
                # print(result)
                if result is None:
                    continue
                else:
                    host_item[title] = '%.2f%s' % (result, unit)

            # 硬盘剩余率


            # print(host_item)


            if disk_full in host_item and disk_used in host_item:
                # print "Disk_percent:%.2f%%" %(float(host_item[disk_free].strip("GKbps"))/float(host_item[disk_full].strip("GKbps"))*100)
                host_item[keys_disk] = "%.2f" % (
                        float(host_item[disk_used].strip("GKbps")) / float(host_item[disk_full].strip("GKbps")) * 100)
                host_item[disk_free] = "%.2f" % (float(host_item.get(disk_full).strip("GKbps")) - float(
                    host_item.get(disk_used).strip("GKbps")))


            # Swap剩余率
            if swap_full in host_item and swap_free in host_item :
                # print "Swap_percent:%.2f%%" %(float(host_item[swap_full].strip("GKbps"))/float(host_item[swap_full].strip("GKbps"))*100)
                host_item[keys_swap] = "%.2f" % (
                        float(host_item[swap_full].strip("GKbps")) / float(host_item[swap_full].strip("GKbps")) * 100)
                # pass
            # 内存使用率
            if mem_used in host_item and mem_full in host_item:
                # print "Mem_percent:%.2f%%" %(float(host_item[mem_used].strip("GKbps")) / float(host_item[mem_full].strip("GKbps")) * 100)
                host_item[keys_mem] = "%.2f" % (
                        float(host_item[mem_used].strip("GKbps")) / float(host_item[mem_full].strip("GKbps")) * 100)
            # print(host_item.get(disk_free))

            host_dict[ip] = host_item

        return host_dict

    def dispalyvalue(self):
        value = self.getvalue()
        for ip in value:
            print
            "\n\rip:%s\n\r获取服务器信息:" % (ip)
            for key in value[ip]:
                print
                "%s:%s" % (key, value[ip][key])

    def __del__(self):
        # 关闭数据库连接
        self.cursor.close()
        self.conn.close()

    def createreport(self):
        host_info = self.getvalue()
        # 创建一个excel表格
        workbook = xlsxwriter.Workbook(fname)
        # 设置第一行标题格式
        format_title = workbook.add_format()
        format_title.set_border(1)  # 边框
        format_title.set_bg_color('#1ac6c0')  # 背景颜色
        format_title.set_align('center')  # 左右居中
        format_title.set_bold()  # 字体加粗
        format_title.set_valign('vcenter')  # 上下居中
        format_title.set_font_size(12)
        # 设置返回值的格式
        format_value = workbook.add_format()
        format_value.set_border(1)
        format_value.set_align('center')
        format_value.set_valign('vcenter')
        format_value.set_font_size(12)
        # 创建一个名为Report的工作表
        worksheet1 = workbook.add_worksheet("总览表格")
        # 设置列宽
        worksheet1.set_column('A:D', 15)
        worksheet1.set_column('E:J', 23)
        worksheet1.set_column('K:R', 25)
        # 设置行高
        worksheet1.set_default_row(25)
        # 冻结首行首列
        worksheet1.freeze_panes(1, 1)
        # 将标题写入第一行
        i = 1
        for title in Title:
            worksheet1.write(0, i, title.encode('utf-8').decode('utf-8'), format_title)
            i += 1
        # 写入第一列、第一行
        worksheet1.write(0, 0, "主机".encode('utf-8').decode('utf-8'), format_title)
        # 根据每个ip写入相应的数值
        j = 1
        for ip in host_info:
            keys_ip = sorted(host_info[ip])  # 取出每个ip的键值，并把键值进行排序
            host_value = host_info[ip]  # 取出没有排序的键值
            if len(host_value) != 0:  # 如果出现｛'10.1.12.1':{}｝这种情况的时候，需要跳过，不将其写入表格中
                worksheet1.write(j, 0, ip, format_value)
            else:
                continue
            # k = 1
            for item in keys_ip:
                # worksheet1.write(j,k,host_value[item],format_value)
                worksheet1.write(j, Title_dict[item], host_value[item], format_value)
                # k += 1
            j += 1
        ##########################性能报表#############################
        worksheet2 = workbook.add_worksheet("性能报表")
        # 设置列宽
        worksheet2.set_column('A:E', 25)
        # 设置行高
        worksheet2.set_default_row(25)
        # 冻结首行首列
        worksheet2.freeze_panes(1, 1)
        # 写入第一列、第一行
        worksheet2.write(0, 0, "主机".encode('utf-8').decode('utf-8'), format_title)

        worksheet2.write(0, 1, keys_cpu, format_title)
        worksheet2.write(0, 2, keys_mem, format_title)
        worksheet2.write(0, 3, keys_swap, format_title)
        worksheet2.write(0, 4, keys_disk, format_title)
        j = 1
        for ip in host_info:
            keys_ip = sorted(host_info[ip])  # 取出每个ip的键值，并把键值进行排序
            host_value = host_info[ip]  # 取出没有排序的键值
            # Title[12]=硬盘剩余率(单位%)
            if len(
                    host_value) != 0 and keys_disk in host_value and keys_swap in host_value and keys_mem in host_value and keys_cpu in host_value:  # 如果出现｛'10.1.12.1':{}｝这种情况的时候，需要跳过，不将其写入表格中
                worksheet2.write(j, 0, ip, format_value)
                worksheet2.write(j, 1, host_value[keys_cpu], format_value)
                worksheet2.write(j, 2, host_value[keys_mem], format_value)
                worksheet2.write(j, 3, host_value[keys_swap], format_value)
                worksheet2.write(j, 4, host_value[keys_disk], format_value)
            # keys_mem in host_value: # or keys_swap in host_value
            else:
                continue
            j += 1
        ###############制作内存大于90%的服务器表格########################
        worksheet3 = workbook.add_worksheet("内存大于90%")
        # 设置列宽
        worksheet3.set_column('A:B', 25)
        # 设置行高
        worksheet3.set_default_row(25)
        # 冻结首行首列
        worksheet3.freeze_panes(1, 1)
        # 写入第一列、第一行
        worksheet3.write(0, 0, "主机".encode('utf-8').decode('utf-8'), format_title)
        worksheet3.write(0, 1, keys_mem, format_title)
        j = 1
        for ip in host_info:
            keys_ip = sorted(host_info[ip])  # 取出每个ip的键值，并把键值进行排序
            host_value = host_info[ip]  # 取出没有排序的键值
            if len(host_value) != 0 and keys_mem in host_value and float(
                    host_value[keys_mem]) > 90.0:  # 如果出现｛'10.1.12.1':{}｝这种情况的时候，需要跳过，不将其写入表格中
                # print type(float(host_value[keys_mem]))
                # if float(host_value[keys_mem]) < 20.0:
                worksheet3.write(j, 0, ip, format_value)
                worksheet3.write(j, 1, host_value[keys_mem], format_value)
            else:
                continue
            j += 1
        #######################制作硬盘空间小于20%的服务器表格#########################
        # 制作硬盘空间小于20%的服务器表格
        worksheet4 = workbook.add_worksheet("磁盘空间低于20%")
        # 设置列宽
        worksheet4.set_column('A:B', 25)
        # 设置行高
        worksheet4.set_default_row(25)
        # 冻结首行首列
        worksheet4.freeze_panes(1, 1)
        # 写入第一列、第一行
        worksheet4.write(0, 0, "主机".encode('utf-8').decode('utf-8'), format_title)
        worksheet4.write(0, 1, keys_disk, format_title)
        j = 1
        for ip in host_info:
            keys_ip = sorted(host_info[ip])  # 取出每个ip的键值，并把键值进行排序
            host_value = host_info[ip]  # 取出没有排序的键值)
            if len(host_value) != 0 and keys_disk in host_value and float(
                    host_value[keys_disk]) < 20.0:  # 如果出现｛'10.1.12.1':{}｝这种情况的时候，需要跳过，不将其写入表格中
                # print type(float(host_value[keys_disk]))
                # if float(host_value[keys_disk]) < 20.0:
                worksheet4.write(j, 0, ip, format_value)
                worksheet4.write(j, 1, host_value[keys_disk], format_value)
            else:
                continue
            j += 1

            #######################制作CPU负载大于8的服务器表格#########################
            # 制作CPU负载大于8的服务器表格
            worksheet5 = workbook.add_worksheet("CPU负载大于8")
            # 设置列宽
            worksheet5.set_column('A:B', 25)
            # 设置行高
            worksheet5.set_default_row(25)
            # 冻结首行首列
            worksheet5.freeze_panes(1, 1)
            # 写入第一列、第一行
            worksheet5.write(0, 0, "主机".encode('utf-8').decode('utf-8'), format_title)
            worksheet5.write(0, 1, keys_cpu, format_title)
            j = 1
            for ip in host_info:
                keys_ip = sorted(host_info[ip])  # 取出每个ip的键值，并把键值进行排序
                host_value = host_info[ip]  # 取出没有排序的键值
                if len(host_value) != 0 and keys_cpu in host_value and float(
                        host_value[keys_cpu]) > 8:  # 如果出现｛'10.1.12.1':{}｝这种情况的时候，需要跳过，不将其写入表格中
                    # print type(float(host_value[keys_cpu]))
                    # if float(host_value[keys_cpu]) < 20.0:
                    worksheet5.write(j, 0, ip, format_value)
                    worksheet5.write(j, 1, host_value[keys_cpu], format_value)
                else:
                    continue
                j += 1
        workbook.close()




if __name__ == '__main__':
    t=Test()
    a=t.getgroupid()
    b=t.gethostid()
    c=t.gethostlist()
    d=t.getitemid()
    e=t.getvalue()
    # f=t.dispalyvalue()
    g=t.createreport()
    # print(a)
    # print(b)
    # print(e)
