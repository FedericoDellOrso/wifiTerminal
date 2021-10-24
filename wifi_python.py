import os

def set_wifi_ssid_psk(ssid, psk):
	os.system('sudo wpa_cli -i wlan0 remove_network 0')
	os.system('sudo wpa_cli -i wlan0 add_network')
	os.system('sudo wpa_cli -i wlan0 set_network 0 ssid ' + '\'"' + ssid + '"\'')
	os.system('sudo wpa_cli -i wlan0 set_network 0 psk ' + '\'"' + psk + '"\'')
	os.system('sudo wpa_cli -i wlan0 enable_network 0')
	os.system('sudo wpa_cli -i wlan0 save_config')

def main():
	set_wifi_ssid_psk('BELUGANET_5GEXT', 'D98B3840BF')

if __name__ == '__main__':
	main()
