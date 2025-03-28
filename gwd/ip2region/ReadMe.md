一个离线IP地址定位库，微秒级别的查询效率，Star 16.5K+！
原创 有趣的开源集市 有趣的开源集市
 2024年08月23日 08:08 江苏
**点击上方蓝字 关注我**




在很多系统中都有一个获取访问用户的IP来源信息的功能。可别小瞧了此功能，此功能一方面是能够提升系统安全能力，防止暴露登录破解等，一方面能够为业务运营提供建议，持续提升业务运营效率。一般细分为以下几点：

1、安全防护层提升
访问控制: 根据IP地址的地理位置，限制特定地区的访问。例如，检测到某个地区的同类IP地址经常发起恶意请求，可以结合IP限制功能，暂时禁止这些IP地址的访问；

异常检测: 通过监测IP地址的地理位置与用户日常操作行为的是否一致性，识别异常行为。比如我们经常用的邮箱或者云账号，如果不在常用地登录都会收到异地登录提醒。


2、业务运营层提升

用户分析：根据用户的地理位置信息，提供个性化的内容推荐或者本地化服务，如新闻、商品推荐，本地商家活动推广等等；

市场分析：分析不同地区用户的访问模式和行为，以便更好地理解市场需求和用户偏好，比如优化不同区域的产品模式，对不同区域进行精准的广告投放等等；

运营决策：根据不同地区的经济水平和消费习惯，制定差异化的定价策略，利用地理位置信息优化物流配送路线，减少运输成本，提高配送效率等等。

所以，IP地址定位虽然在很多系统里面有可能是个小功能，但是能发挥的影响力可一点也不小。运用好IP来源信息能够在帮助企业实现安全的系统防护的同时，提供更精准业务决策的依据。而我们今天介绍的就是一个高性能的 IP 地址定位库-Ip2region




01 
— 
 Ip2region 介绍 

一个高性能的 IP 地址定位库，采用二分查找算法实现快速查询，能够达到毫秒级别。拥有详尽的 IP 数据库，覆盖全球范围内的 IP 地址，并支持持续更新以确保数据的准确性，并且支持 Java、PHP、Python、Go 等多种编程语言，使其能够轻松集成到不同的应用程序中。

图片

🏠  项目信息

#Github地址
https://github.com/lionsoul2014/ip2region
图片

🚀功能特性
极速查询响应: 提供了10微秒级别的查询效率，即使是基于文件的查询也能保持这种速度。

支持亿级数据量: 能够处理亿级别的IP数据段，适用于大规模数据。

自定义region信息: 默认的region信息格式为国家|区域|省份|城市|ISP，同时支持用户可以自定义这些信息，例如添加GPS信息、国际统一地域信息编码或邮编等。

数据去重和压缩: xdb格式生成程序会自动去重和压缩部分数据，生成的数据库大小随着数据详细度的增加而增大。

内存加速查询: 提供两种内存加速查询方式，包括vIndex索引缓存和将整个xdb文件加载到内存中。

数据生成和更新工具: 提供了xdb数据生成和更新的工具，支持多种编程语言实现，方便用户管理和更新IP数据。

多语言客户端实现: 提供了多种编程语言的查询客户端实现，如golang、php、java、lua、c、rust、python、nodejs、csharp和erlang等。

图片



02
—
 Ip2region 特殊说明 

ip2region 旨在于研究 IP 数据的存储和快速查询的设计和实现，并没有原始 IP 数据的支撑，也不提供商用版本。 项目的自带的 ./data/ip.merge.txt 原始数据已经很久没有更新，也不会再更新，对于数据精度和更新频率要求很高的使用场景建议更换高精度的IP地址数据。项目提供了详细的更换数据操作说明：

图片

03
—
 Ip2region 使用 

ip2region支持多种语言客户端查询，本文主要以python 查询客户端实现为例说明:

完全基于文件的查询
from xdbSearcher import XdbSearcher

def searchWithFile():
    # 1. 创建查询对象
    dbPath = "../../data/ip2region.xdb"
    searcher = XdbSearcher(dbfile=dbPath)
    
    # 2. 执行查询
    ip = "114.114.114.114"
    region_str = searcher.searchByIPStr(ip)
    print(region_str)
    
    # 3. 关闭searcher
    searcher.close()

缓存 VectorIndex 索引
可以提前从 xdb 文件中加载出来 VectorIndex 数据，然后全局缓存，每次创建 Searcher 对象的时候使用全局的 VectorIndex 缓存可以减少一次固定的 IO 操作，从而加速查询，减少 IO 压力。

from xdbSearcher import XdbSearcher

def searchWithVectorIndex():
     # 1. 预先加载整个 xdb
    dbPath = "../../data/ip2region.xdb"
    vi = XdbSearcher.loadVectorIndexFromFile(dbfile=dbPath)

    # 2. 使用上面的缓存创建查询对象, 同时也要加载 xdb 文件
    searcher = XdbSearcher(dbfile=dbPath, vectorIndex=vi)
    
    # 3. 执行查询
    ip = "1.2.3.4"
    region_str = searcher.search(ip)
    print(region_str)

    # 4. 关闭searcher
    searcher.close()

缓存整个 xdb 数据
也可以预先加载整个 ip2region.xdb 的数据到内存，然后基于这个数据创建查询对象来实现完全基于文件的查询，类似之前的 memory search。

from xdbSearcher import XdbSearcher

def searchWithContent():
    # 1. 预先加载整个 xdb
    dbPath = "../../data/ip2region.xdb";
    cb = XdbSearcher.loadContentFromFile(dbfile=dbPath)
    
    # 2. 仅需要使用上面的全文件缓存创建查询对象, 不需要传源 xdb 文件
    searcher = XdbSearcher(contentBuff=cb)
    
    # 3. 执行查询
    ip = "1.2.3.4"
    region_str = searcher.search(ip)
    print(region_str)

    # 4. 关闭searcher
    searcher.close()
查询测试

项目提供了查询测试脚本 search_test.py ，运行脚本，输入 ip 即可进行查询测试。也可以分别设置 cache-policy为 file/vectorIndex/content 来测试三种不同缓存实现的效率：

#查看使用帮助
python3 ./search_test.py
python3 search_test.py [command options]
options:
 --db string             ip2region binary xdb file path
 --cache-policy string   cache policy: file/vectorIndex/content
#测试IP地址
python3 ./search_test.py --db=../../data/ip2region.xdb --cache-policy=content
ip2region xdb searcher test program, cachePolicy: content
type 'quit' to exit
ip2region>> 1.2.3.4
region :美国|0|华盛顿|0|谷歌 , took 0.0689 ms
ip2region>> quit
searcher test program exited, thanks for trying
bench 测试
项目提供了bench_test.py 脚本来进行自动 bench 测试，一方面确保 xdb 文件没有错误，另一方面通过大量的查询测试平均查询性能：

#查看使用帮助
python3 ./bench_test.py
python bench_test.py [command options]
options:
 --db string             ip2region binary xdb file path
 --src string            source ip text file path
 --cache-policy string   cache policy: file/vectorIndex/content
通过默认的 data/ip2region.xdb 和 data/ip.merge.txt 来进行 bench 测试：
python3 ./bench_test.py --db=../../data/ip2region.xdb --src=../../data/ip.merge.txt --cache-policy=content
Bench finished, [cachePolicy: content, total: 3417955, took: 34.93 s, cost: 0.0094 ms/op]
可以通过设置 cache-policy 参数来分别测试 file/vectorIndex/content 三种不同的缓存实现的的性能。@Note：请注意 bench 使用的 src 文件需要是生成对应的 xdb 文件的相同的源文件
04
—
 最后 
综上所述，ip2region 是一个高效的 IP 地址定位库，它通过二分查找算法快速将 IP 地址转换为地理位置信息，支持多种编程语言，能够为系统的网络安全监控、内容个性化推荐、市场分析等多个场景提供帮助。如果正好你或者你的团队涉及到这方面的内容，不妨试试吧！
