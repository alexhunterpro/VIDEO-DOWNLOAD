# Alex Hunter Tools PRO (Python3) 

> **# Alex Hunter Tools PRO 🔥

> **# আপনার সব কাজের জন্য এক ঝাঁক Termux টুলস  

---

## 🌐 Social Media

[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/YourProfile)
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/YourGitHub)

---

## 🎥 Video Downloader
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/YourVideoLink)
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/YourProfile)
[![TikTok](https://img.shields.io/badge/TikTok-000000?style=for-the-badge&logo=tiktok&logoColor=white)](https://www.tiktok.com/@YourUsername)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/YourUsername)

---

## ⚡ Features
- Quick Downloader for YouTube & Facebook  
- Telegram Bot Manager  
- WiFi Security Tools  
- Termux Pro-Level Scripts  
---

## 🔷 Quick Git clone

```bash
# Clone the repository

git clone https://github.com/alexhunterpro/VIDEO-DOWNLOAD.git
cd VIDEO-DOWNLOAD
python3 videodownload.py

# Run in Termux (recommended)
python3 videodownload.py
```

---

## ✨ Features

* Clean, colorful terminal UI with banner and easy prompts
* Automatic Termux storage permission handling (`termux-setup-storage`)
* Detects & installs `yt-dlp` if missing (via pip)
* Save downloads to `/sdcard/DLP` by default (customizable)
* Video downloads (best/worst/custom format codes)
* Audio-only downloads (bestaudio)
* Lightweight, dependency-minimal, and mobile-first

---

## 🛠️ Requirements

* Termux on Android (recommended)
* Python 3.8+ (installed by repo script or `pkg install python`)
* `yt-dlp` (auto-installs if missing)
* Storage permission granted for Termux: `termux-setup-storage`

---

## 🚀 Installation (Termux)

1. Open Termux and update packages:

```bash
pkg update && pkg upgrade -y
pkg install python -y
pkg install git -y
```

2. Clone this repo and run:

```bash
git clone https://github.com/alexhunterpro/VIDEO-DOWNLOAD.git
cd VIDEO-DOWNLOAD
python3 videodownload.py

```

> When prompted, allow Termux storage permission so downloads save to `/sdcard/DLP`.

---

## 📥 Usage

* Run the script: `python3 videodownload.py`
* Enter a video or audio URL (YouTube, Vimeo, TikTok, many supported sites via yt-dlp).
* Choose `Video` or `Audio Only`.
* For Video: pick `h` (highest), `l` (lowest), or `c` (custom format code).
* Files are saved to `/sdcard/DLP` by default.

---

## 🧭 Configuration

```python
# default
download_dir = "/sdcard/DLP"
```

* To force an alternate output template, modify the `-o` argument when calling `yt-dlp` in the script.

---

## 🧩 Extending the tool

Suggested improvements:

* Add a configuration file (`config.json`) to persist user choices
* Add queueing and background downloads via `aria2c` + `yt-dlp --external-downloader`
* Add post-processing: subtitles, convert to mp3/m4a, or trim
* Add logging and retry logic for unstable networks

---

## 🤝 Contributing

Contributions are welcome. Please fork the repo, make changes on a branch, and open a pull request.

1. Fork
2. Create a feature branch: `git checkout -b feature/my-change`
3. Commit and push
4. Open a PR describing changes

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## 🙋 Contact Author 

- CYBER SENTINEL BANGLADESH 
- TEAM MEMBER ( ALEX HUNTER ) 🥱☠️
- Spammer & Hacking....!! 😌
- Gray Hacker....💥

- # Telegram : @alexhuntercsb

---

*Made with ❤️ — Alex Hunter Tools PRO*
