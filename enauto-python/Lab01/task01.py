from netmiko import ConnectHandler

device_ip = '192.168.50.40'
device_username = 'cisco'
device_password = 'cisco123'
device_type = 'cisco_xe'

router = ConnectHandler(host=device_ip, username=device_username, password=device_password, device_type=device_type)

router.disconnect()

print(router.is_alive())