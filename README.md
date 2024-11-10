# CNN-US-EPG-Grabber

## Project Objective

The **_CNN-US-EPG-Grabber_** is a Kodi add-on designed to fetch and generate Electronic Program Guide (EPG) data for the IPTV channel version of the widely popular American news channel  and media network company **CNN** in its United States edition. This add-on scrapes the channel website to create a `XMLTV` file, which can be used with Kodi's _PVR IPTV Simple Client_ to accurately display metadata and other related information for the current TV guide.

## Features

- Scrapes **CNN** schedule from the official website
- Generates a XMLTV-format EPG file
- Integrates seamlessly with Kodi's PVR IPTV Simple Client add-on
- It features a fully customizable update interval for continuous updating

## Limitations

- The add-on relies purely on the CNN's website structure. _CAUTION:_ Changes to the website may require updates to the scraping logic.
- EPG data is limited to what's available on CNN's public schedule page, which typically covers **_only the current day_**
- The add-on does not provide video content; it only generates EPG data.
- Accuracy of the EPG data depends on the timeliness and correctness of CNN's published schedule.

## Installation

1. Download the latest release zip file from the GitHub repository.
2. In Kodi, go to Add-ons > Install from zip file.
3. Select the downloaded zip file to install the add-on.

## Configuration

### Creating the Custom Channels XML File

Create a file named `cnn_us.channels.xml` in Kodi's userdata  folder (in Windows normally under  `C:\Users\<YourUsername>\AppData\Roaming\Kodi\userdata`
) with the following content:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<channels>
    <channel id="CNNUSA.us">
        <display-name lang="en">CNN US</display-name>
    </channel>
</channels>
```

This file defines the channel information for CNN US, which is used by the EPG grabber.

### Creating M3U Playlist

Create a file named `cnn_us.m3u` in Kodi's `userdata` folder with the following content:

```m3u
#EXTM3U
#EXTINF:-1 tvg-id="CNNUSA.us" tvg-name="CNN US" tvg-country="US" tvg-language="English" tvg-logo="https://cdn.cnn.com/cnn/.e/img/3.0/global/misc/cnn-logo.png" group-title="News",CNN US
https://turnerlive.warnermediacdn.com/hls/live/586495/cnngo/cnn_slate/VIDEO_0_3564000.m3u8
```

This M3U playlist provides the stream information for CNN US. Note that the stream URL may need to be updated if it changes.

## Usage

1. Install and configure the PVR IPTV Simple Client add-on in Kodi.
2. Set the EPG source in PVR IPTV Simple Client to:
   `special://userdata/addon_data/script.epggrabber.cnn/guide.xml`
3. Set the M3U playlist source to:
   `special://userdata/cnn_us.m3u`
4. Run the CNN-US-EPG-Grabber add-on to generate the initial EPG data.
5. Configure the update interval in the add-on settings if desired.

## Contributing

Contributions to improve the **_CNN-US-EPG-Grabber_** are welcome. Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
