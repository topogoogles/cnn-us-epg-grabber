import xbmc
import xbmcaddon
import time
from lib.epg_grabber import EPGGrabber

ADDON = xbmcaddon.Addon()
ADDON_NAME = ADDON.getAddonInfo("name")


def main():
    grabber = EPGGrabber()
    grabber.grab_epg()
    xbmc.log(f"{ADDON_NAME}: EPG grab completed", level=xbmc.LOGINFO)


def schedule_grab():
    interval = ADDON.getSettingInt("update_interval") * 3600  # Convert hours to seconds
    while True:
        main()
        time.sleep(interval)


if __name__ == "__main__":
    schedule_grab()
