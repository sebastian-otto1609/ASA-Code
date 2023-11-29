rule1 = "access-list outside_access_in line 2 extended permit tcp host 10.1.1.10 host 192.168.10.10 eq https"
rule2 = "access-list outside_access_in line 4 extended permit tcp 10.1.1.0 255.255.255.128 host 192.168.10.10 eq https"
rule3 = "access-list outside_access_in line 6 extended permit tcp 10.1.1.0 255.255.255.128 192.168.10.0 255.255.255.192 eq https"
rule4 = [
    "access-list outside_access_in line 8 extended permit tcp object-group DM_INLINE_NETWORK_1 host 192.168.10.10 eq https",
    "access-list outside_access_in line 8 extended permit tcp host 10.1.1.11 host 192.168.10.10 eq https",
    "access-list outside_access_in line 8 extended permit tcp host 10.1.1.12 host 192.168.10.10 eq https"
    ]