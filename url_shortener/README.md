

# 🌐 URL Shortener & Analytics Dashboard

Welcome to your modern, privacy-friendly URL shortener! This project lets you create, share, and track short links with ease—no sign-up, no hassle, just instant results.

---

## 🚀 Features

- Shorten any link (with optional custom code)
- Password-protect your links (PIN)
- Set expiration dates and schedule activation
- QR code generation for every short link
- Click analytics and beautiful charts
- Global stats dashboard for all links
- No authentication required—public and easy
- Works on LAN, mobile, and public (ngrok) access
- Malicious URL protection

---

## 🛠️ Quick Start

1. Clone this repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up MongoDB (local or cloud)
4. Copy `.env.example` to `.env` and set your secrets
5. Run the app:
   ```bash
   python app.py
   ```
6. Open [http://localhost:5000](http://localhost:5000) in your browser

---

## 📊 Stats & Analytics

- Visit `/stats` for a global dashboard of all links and clicks
- Each short link has its own `/stats/&lt;short_code&gt;` page
- See click history, activity charts, and more

---

## 🌍 Public & Mobile Access

- Run with `host=0.0.0.0` for LAN/mobile
- Use [ngrok](https://ngrok.com/) for public URLs:
  ```bash
  ngrok http 5000
  ```

---

## 🧑‍💻 Tech Stack

- Python Flask (backend)
- MongoDB (database)
- Tailwind CSS (UI)
- Plotly & Pandas (analytics)

---

## 📝 Customization & Deployment

- Edit `gunicorn.conf.py` for production
- Deploy anywhere Python & MongoDB are supported

---

## ❤️ Contributing

Pull requests and ideas are welcome! This project is for everyone—no login, no tracking, just useful links.

---

## 📄 License

MIT License. Use it, remix it, share it!
