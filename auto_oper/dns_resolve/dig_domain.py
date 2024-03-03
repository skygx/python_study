#/usr/bin/env python
# -*- coding:utf-8 -*-
'''
    @Project :   Pyproject
    @File    :   dig_domain.py
    @Contact :   guoxin_well@126.com
    @License :   (C)Copyright 2020-2021, xguo

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/21 下午 4:14   hello      1.0         None

'''

#!/usr/bin/env python

import dns.resolver, sys
import click


def get_domain_ip(domain):
    """Get the DNS record, if any, for the given domain."""
    dns_records = list()
    try:
        # get the dns resolutions for this domain
        dns_results = dns.resolver.resolve(domain)
        dns_records = [ip.address for ip in dns_results]
    except dns.resolver.NXDOMAIN as e:
        print("the domain does not exist so dns resolutions remain empty. domain:", domain)
    except dns.resolver.NoAnswer as e:
        print("the resolver is not answering so dns resolutions remain empty, domain:", domain)
    return dns_records


@click.command()
@click.option('-n','--domain', prompt='Please input an domain name',
              help='domain name.')
def dig_ip(domain):
    try:
        while True:
            for rdata in dns.resolver.resolve(domain, 'CNAME') :
                print (domain, "cname is", rdata)
                domain=rdata.target
                print("domain resolve ip address: ",get_domain_ip(domain))
    except Exception as e:
        print (e)
        return get_domain_ip(domain)

if __name__ == "__main__":
    print( "Recursive name lookup (simulates dig)...")
    print(dig_ip())
