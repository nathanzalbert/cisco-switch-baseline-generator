#!/usr/bin/env python3

"""
Cisco Catalyst 9000 Baseline Generator
Prints a Cisco Catalyst 9000 baseline configuration.
"""

# ========= EDIT THESE VALUES ========= #

hostname = "SW-ACCESS-01"

domain_name = "company.local"

username = "admin"
password = "Cisco123!"
enable_secret = "Cisco123!"

management_vlan = 10
management_ip = "192.168.10.10"
subnet_mask = "255.255.255.0"
default_gateway = "192.168.10.1"

primary_dns = "8.8.8.8"
secondary_dns = "1.1.1.1"

ntp_server = "192.168.10.50"
syslog_server = "192.168.10.100"

snmp_community = "PUBLIC"

access_vlan = 20
allowed_vlans = "10,20,30,999"

# ========= CONFIGURATION TEMPLATE ========= #

config = f"""
!
!=========================================================
! Cisco Catalyst 9000 Baseline Configuration
!=========================================================
!

hostname {hostname}

!
! Basic Configuration
!
no ip domain-lookup
ip domain-name {domain_name}
service password-encryption

!
! AAA
!
aaa new-model
aaa authentication login default local
aaa authorization exec default local

!
! Local User
!
username {username} privilege 15 secret {password}
enable secret {enable_secret}

!
! SSH
!
crypto key generate rsa modulus 2048
ip ssh version 2
ip ssh authentication-retries 3
ip ssh time-out 60

!
! Management VLAN
!
vlan {management_vlan}
 name MANAGEMENT

interface Vlan{management_vlan}
 description Management Interface
 ip address {management_ip} {subnet_mask}
 no shutdown

ip default-gateway {default_gateway}

!
! DNS
!
ip name-server {primary_dns}
ip name-server {secondary_dns}

!
! NTP
!
ntp server {ntp_server}

!
! Syslog
!
logging host {syslog_server}
logging buffered 16384

!
! SNMP
!
snmp-server community {snmp_community} RO

!
! Spanning Tree
!
spanning-tree mode rapid-pvst
spanning-tree extend system-id

!
! LLDP
!
lldp run

!
! User Ports
!
interface range GigabitEthernet1/0/1-24
 description USER PORTS
 switchport mode access
 switchport access vlan {access_vlan}
 spanning-tree portfast
 spanning-tree bpduguard enable
 storm-control broadcast level 1.00
 storm-control multicast level 1.00
 no shutdown

!
! Unused Ports
!
interface range GigabitEthernet1/0/25-48
 description UNUSED PORTS
 switchport mode access
 switchport access vlan 999
 shutdown

!
! Uplink
!
interface TenGigabitEthernet1/1/1
 description UPLINK
 switchport mode trunk
 switchport trunk native vlan 999
 switchport trunk allowed vlan {allowed_vlans}
 no shutdown

!
! Console
!
line console 0
 logging synchronous
 exec-timeout 10 0
 login local

!
! VTY
!
line vty 0 15
 login local
 transport input ssh
 exec-timeout 10 0

!
! Banner
!
banner motd ^

********************************************
* Authorized Access Only                   *
* Activity Is Monitored and Recorded       *
********************************************

^

end
"""

print(config)