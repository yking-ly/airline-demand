# ✈️ Airline Booking Demand Analyzer

A sleek web application that fetches real-time flight offers using the **Amadeus API**, analyzes route demand, stores search data, and visualizes market trends. Built with **FastAPI**, **SQLite**, **TailwindCSS**, and deployed on **Render**.

---

## 🚀 Features

- 🔍 Search flight offers by source, destination, and date  
- ✨ Autocomplete airport suggestions while typing  
- 📊 Real-time aggregation of popular flight routes  
- 💰 Price trend analysis via charts  
- 🧠 Hover-based UX enhancements (duration, stops, airline info)  
- 🛫 Displays airline name and logo  
- 🌐 Powered by [Amadeus Travel APIs](https://developers.amadeus.com/)  
- ☁️ Fully deployed on **Render**

---

## 🛠️ Tech Stack

| Category   | Tools / Libraries                    |
|------------|--------------------------------------|
| Backend    | FastAPI, SQLAlchemy, Uvicorn         |
| Frontend   | Jinja2, TailwindCSS, Chart.js        |
| APIs       | Amadeus Flight Offers Search API     |
| Database   | SQLite3 (via SQLAlchemy)             |
| Hosting    | Render Cloud                         |
| Secrets    | dotenv (.env)                        |

---

## 🧑‍💻 Local Development Setup

### 🔧 Prerequisites

- Python 3.9+
- [Amadeus API Credentials](https://developers.amadeus.com/)
- Virtual environment (recommended)

### 📦 Install Dependencies

```bash
git clone https://github.com/YOUR_USERNAME/airline-demand-app.git
cd airline-demand-app
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 🔐 Environment Variables

Create a .env file in the root:
```bash
AMADEUS_API_KEY=your_amadeus_key
AMADEUS_API_SECRET=your_amadeus_secret
```

### 🚀 Start the Server

```bash
uvicorn app.main:app --reload
```
Then visit: http://localhost:8000

### 📄 License
This project is licensed under the MIT License.
