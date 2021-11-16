# How to using samsung skin for android

## Download

1. Go to <https://developer.samsung.com/galaxy-emulator-skin>
2. Look for devices part and click `Galaxy Note`
3. Click `Download Skin` on Galaxy Note8


## Installation

### MacOS

1. Extract `Galaxy_Note8.zip`
2. Copy and paste `Galaxy_Note8` folder to `/Users/prawee/Library/Android/sdk/skins`
3. Create virtual devices and following detail
    - New Hardware Profile
        - Device Name: Note8
        - Device Type: Phone/Tablet
        - Screen 
            Screen size: 6.3 inch
            Resolution: 1440 x 2960 px
        - Memory
            Ram: 2048 MB
        - Input
            [check] Has Hardware Buttons(Back/Home/Menu)
            [check] Has Hardware Keyboard
        *** Default
        - Default Skin: Galaxy_Note8
        Then click `Finish` Button
    - Choose `Galaxy Note8` and `Next`
    - Download `R` (API Level 30) and click `Download` and click `Next`
    - Verify Configuration
        - AVD Name: Galaxy Note8 API 30 and click `Finished`

### CLI

```bash
adb devices -l
# List of devices attached
# emulator-5554          device product:sdk_gphone_arm64 model:sdk_gphone_arm64 device:emulator_arm64 transport_id:1
```