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
    try:
        interval = ADDON.getSettingNumber("update_interval")
        xbmc.log(
            f"{ADDON_NAME}: Retrieved update_interval: {interval}", level=xbmc.LOGINFO
        )

        if interval is None or interval == 0:
            interval = 24  # Default to 24 hours if setting is not found or invalid
            xbmc.log(
                f"{ADDON_NAME}: Using default interval of 24 hours", level=xbmc.LOGINFO
            )

        interval_seconds = interval * 3600  # Convert hours to seconds
        xbmc.log(
            f"{ADDON_NAME}: Scheduling grab every {interval} hours ({interval_seconds} seconds)",
            level=xbmc.LOGINFO,
        )

        while True:
            main()
            xbmc.log(
                f"{ADDON_NAME}: Sleeping for {interval_seconds} seconds",
                level=xbmc.LOGINFO,
            )
            time.sleep(interval_seconds)
    except Exception as e:
        xbmc.log(f"{ADDON_NAME}: Error in schedule_grab: {str(e)}", level=xbmc.LOGERROR)


if __name__ == "__main__":
    schedule_grab()
