# ZEST TIGER V3.0 🐯
**Elite Multi-Platform Penetration Testing Tool**

## 📝 وصف الأداة / Description
أداة **ZEST TIGER** هي محرك متطور لاختبار الاختراق، مصمم بلغة بايثون للعمل بمرونة عالية على أنظمة **Linux** وتطبيق **Termux**.

---

## 🚀 تعليمات التثبيت / Installation Guide

### 💻 أولاً: خانة التثبيت على Kali Linux (Desktop/Laptop)
```bash
sudo apt update && sudo apt install git python3 -y
git clone [https://github.com/slomalsharqi/Zest_Tiger.git](https://github.com/slomalsharqi/Zest_Tiger.git)
cd Zest_Tiger
pip3 install -r requirements.txt
python3 zest.py


📱 ثانياً: خانة التثبيت على تطبيق Termux (Android)
pkg update && pkg upgrade -y
pkg install git python -y
git clone [https://github.com/slomalsharqi/Zest_Tiger.git](https://github.com/slomalsharqi/Zest_Tiger.git)
cd Zest_Tiger
pip install colorama requests
python zest.py
