# How to create a bootable installer for macOS

## Download

<https://support.apple.com/en-us/HT201475>

## Format USB

format via `Disk Utility`
`name` via if you want
`format` with `Mac OS Extend (Journaled)`
`Schema` with `GUID Partition Map`

## Make bootable installer

## Checking your volume

checking by `terminal` then typing `/Volumes/` and press tab keys then choose via up to you

## Create installer

open `terminal` then typing follow this

```bash
sudo /Applications/Install\ macOS\ Mojave.app/Contents/Resources/createinstallmedia --volume /Volumes/Mojave
# Mojave that name of Volume of my USB
Password:
Ready to start.
To continue we need to erase the volume at /Volumes/Mojave.
If you wish to continue type (Y) then press return: Y
Erasing disk: 0%... 10%... 20%... 30%... 100%
Copying to disk: 0%... 10%... 20%... 30%... 40%... 50%... 60%... 70%... 80%... 90%... 100%
Making disk bootable...
Copying boot files...
Install media now available at "/Volumes/Install macOS Mojave"
```

## Using

connect `USB installer` to any macOS
