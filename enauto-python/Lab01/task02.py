from netmiko import ConnectHandler

device_ip = '192.168.50.40'
device_username = 'cisco'
device_password = 'cisco123'
device_type = 'cisco_xe'

router = ConnectHandler(host=device_ip, username=device_username, password=device_password, device_type=device_type)

looback_int = ['interface loopback 11', 'ip address 2.1.1.1 255.255.255.0']
router.send_config_set(looback_int)


ip_interfaces = router.send_command('show ip int bri')
print(ip_interfaces)