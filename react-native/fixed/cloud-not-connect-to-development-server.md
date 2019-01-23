# Cloud not connect to development server.

## Fixed
### Getting current your IP address on your terminal
```bash
$ ifconfig
# find en0 node => 192.168.0.54
```
### Configure on your device
1. Shark your android device / command + M
2. Go to "Dev Settings" Menu > "Debug server host & port for device" Menu
3. Paste IP address and port to textbox
*** IP Address => 192.168.0.54 
*** Port => when do you run simulator that's tell you => 8081
4. Press OK button

## Reference
https://stackoverflow.com/questions/44446523/unable-to-load-script-from-assets-index-android-bundle-on-windows