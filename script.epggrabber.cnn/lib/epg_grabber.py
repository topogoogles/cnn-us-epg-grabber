import requests
from bs4 import BeautifulSoup
import datetime
import xml.etree.ElementTree as ET
import xbmc
import xbmcaddon

ADDON = xbmcaddon.Addon()
ADDON_NAME = ADDON.getAddonInfo("name")


class EPGGrabber:
    def __init__(self):
        self.url = "https://www.cnn.com/tv/schedule/cnn"
        self.output_file = xbmc.translatePath(
            "special://userdata/addon_data/script.epggrabber.cnn/guide.xml"
        )

    def grab_epg(self):
        # Log the start of EPG grab
        xbmc.log(f"{ADDON_NAME}: Starting EPG grab for CNN US", level=xbmc.LOGINFO)

        schedule = self.scrape_cnn_schedule()
        xmltv = self.create_xmltv(schedule)
        xmltv.write(self.output_file, encoding="utf-8", xml_declaration=True)

        # Log the completion of EPG grab
        xbmc.log(
            f"{ADDON_NAME}: EPG data saved to {self.output_file}", level=xbmc.LOGINFO
        )

    def scrape_cnn_schedule(self):
        # Fetch and parse the CNN schedule page
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, "html.parser")

        schedule = []
        date = datetime.date.today()
        schedule_container = soup.find("div", class_="schedule-grid")

        if schedule_container:
            for show in schedule_container.find_all("div", class_="schedule-row"):
                time = show.find("span", class_="time").text.strip()
                title = show.find("span", class_="title").text.strip()

                hour, minute = map(int, time.split(":"))
                start_time = datetime.datetime.combine(
                    date, datetime.time(hour, minute)
                )

                schedule.append({"start": start_time, "title": title})

        return schedule

    def create_xmltv(self, schedule):
        # Create XMLTV structure
        tv = ET.Element("tv")
        channel = ET.SubElement(tv, "channel", id="CNNUSA.us")
        ET.SubElement(channel, "display-name").text = "CNN US"

        for program in schedule:
            prog = ET.SubElement(
                tv,
                "programme",
                start=program["start"].strftime("%Y%m%d%H%M%S"),
                channel="CNNUSA.us",
            )
            ET.SubElement(prog, "title").text = program["title"]

        return ET.ElementTree(tv)
