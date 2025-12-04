# 🛡️ CyberSafe Quiz

**Διαδραστική Εφαρμογή Αξιολόγησης Κυβερνοασφάλειας & Ψηφιακού Γραμματισμού**

Μια web-based εφαρμογή που αξιολογεί τις γνώσεις κυβερνοασφάλειας χρηστών σε τρεις κατηγορίες (Παιδιά, Ενήλικες, Επαγγελματίες) και παρέχει εξατομικευμένες προτάσεις βελτίωσης.

---

## 📋 Περιεχόμενα

- [Χαρακτηριστικά](#χαρακτηριστικά)
- [Τεχνολογίες](#τεχνολογίες)
- [Απαιτήσεις](#απαιτήσεις)
- [Εγκατάσταση](#εγκατάσταση)
- [Εκκίνηση](#εκκίνηση)
- [Δομή Έργου](#δομή-έργου)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)
- [Συχνές Ερωτήσεις](#συχνές-ερωτήσεις)

---

## ✨ Χαρακτηριστικά

### 🎯 Τρεις Κατηγορίες Χρηστών

**1. Παιδιά (8-12 ετών)** - 45 ερωτήσεις
- Κωδικοί (Passwords)
- Phishing
- Social Media
- Ιδιωτικότητα (Privacy)
- Διαδικτυακή Συμπεριφορά
- Ασφαλής Περιήγηση
- Influencers

**2. Ενήλικες** - 30 ερωτήσεις
- Κωδικοί & Αυθεντικοποίηση
- Phishing
- Social Media
- Ιδιωτικότητα
- Online Shopping
- Ασφάλεια Συσκευών

**3. Επαγγελματίες IT** - 35 ερωτήσεις
- Προηγμένη Αυθεντικοποίηση (MFA, Zero Trust)
- Social Engineering
- Ασφάλεια Δικτύου
- Incident Response
- Compliance (GDPR, ISO 27001)
- Προστασία Δεδομένων

### 📊 Αναλυτικά Αποτελέσματα

- **Συνολικό σκορ** σε ποσοστό (%)
- **Επίπεδο επίδοσης** (Beginner, Intermediate, Advanced, Expert)
- **Γραφήματα**:
  - Bar Chart - Επίδοση ανά θεματική
  - Radar Chart - Συνολική ανάλυση
- **Εξατομικευμένες προτάσεις** βελτίωσης ανά θεματική και κατηγορία

### 🎨 User Experience

- Modern, responsive UI με animated gradient background
- Real-time feedback μετά από κάθε απάντηση
- Progress bar για παρακολούθηση προόδου
- Glassmorphism design effects
- Κινούμενα εικονίδια (floating cybersecurity icons)

---

## 🛠️ Τεχνολογίες

### Frontend
- **React.js 18** - UI Framework
- **Tailwind CSS** - Styling
- **Recharts** - Data Visualization
- **Lucide React** - Icons

### Backend
- **Python 3.8+** - Server Language
- **Flask** - Web Framework
- **Flask-CORS** - Cross-Origin Resource Sharing
- **SQLAlchemy** - ORM

### Database
- **MySQL 8** - Relational Database

---

## 💻 Απαιτήσεις

### Software
- Node.js (v14 ή νεότερη)
- Python (v3.8 ή νεότερη)
- MySQL (v8 ή νεότερη)

### Hardware
- 4GB RAM (ελάχιστο)
- 500MB ελεύθερος χώρος δίσκου

### Operating System
- Windows 10/11
- macOS 10.15+
- Linux (Ubuntu 20.04+)

---

## 📦 Εγκατάσταση

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/cyber-quiz-app.git
cd cyber-quiz-app
```

### 2. Εγκατάσταση MySQL Database

#### Δημιουργία Database
```sql
CREATE DATABASE cyber_quiz_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE cyber_quiz_db;
```

#### Εκτέλεση Schema
```bash
mysql -u root -p cyber_quiz_db < database/schema.sql
```

### 3. Backend Setup

```bash
cd backend

# Δημιουργία virtual environment
python -m venv venv

# Ενεργοποίηση (Windows)
venv\Scripts\activate

# Ενεργοποίηση (Mac/Linux)
source venv/bin/activate

# Εγκατάσταση dependencies
pip install -r requirements.txt

# Ρύθμιση database connection
# Επεξεργαστείτε το app.py και βάλτε τον κωδικό MySQL
```

#### Εισαγωγή Ερωτήσεων
```bash
python insert_all_questions.py
```

**Αναμενόμενο output:**
```
✅ Επιτυχής εισαγωγή 110 ερωτήσεων!
   - Παιδιά: 45
   - Ενήλικες: 30
   - Επαγγελματίες: 35
```

### 4. Frontend Setup

```bash
cd ../frontend

# Εγκατάσταση dependencies
npm install
```

---

## 🚀 Εκκίνηση

### Start Backend (Terminal 1)

```bash
cd backend
venv\Scripts\activate  # Windows
# ή
source venv/bin/activate  # Mac/Linux

python app.py
```

**Εκτελείται στο:** http://localhost:5000

### Start Frontend (Terminal 2)

```bash
cd frontend
npm start
```

**Εκτελείται στο:** http://localhost:3000

**Η εφαρμογή θα ανοίξει αυτόματα στο browser!** 🎉

---

## 📁 Δομή Έργου

```
cyber-quiz-app/
│
├── backend/
│   ├── app.py                      # Flask main application
│   ├── models.py                   # SQLAlchemy models
│   ├── insert_all_questions.py    # Script εισαγωγής ερωτήσεων
│   ├── requirements.txt            # Python dependencies
│   └── venv/                       # Virtual environment
│
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   └── DemographicsForm.js
│   │   ├── App.js                  # Main React component
│   │   ├── AnimatedBackground.js   # Background animations
│   │   ├── AnimatedBackground.css
│   │   └── index.css
│   ├── package.json
│   └── tailwind.config.js
│
├── database/
│   └── schema.sql                  # Database schema
│
└── README.md
```

---

## 🔌 API Endpoints

### Base URL
```
http://localhost:5000/api
```

### Endpoints

#### 1. Get Themes by Category
```http
GET /themes/<category>
```

**Parameters:**
- `category`: `child`, `adult`, or `professional`

**Response:**
```json
[
  {
    "id": 1,
    "theme_name": "passwords",
    "display_name": "Κωδικοί Πρόσβασης",
    "description": "Ασφαλείς κωδικοί..."
  }
]
```

#### 2. Get Questions by Category
```http
GET /questions/<category>
```

**Response:**
```json
[
  {
    "id": 1,
    "question_text": "Τι είναι Two Factor Authentication;",
    "options": {
      "a": "Έλεγχος δύο email",
      "b": "Έλεγχος με κωδικό + άλλο στοιχείο",
      "c": "Δεν ξέρω"
    },
    "correct_answer": "b",
    "explanation": "Το 2FA προσθέτει επιπλέον ασφάλεια...",
    "theme": "passwords_auth"
  }
]
```

#### 3. Get Questions by Theme
```http
GET /questions/<category>/<theme>
```

#### 4. Submit Quiz Results
```http
POST /results
```

**Request Body:**
```json
{
  "session_id": "session-123456",
  "category": "adult",
  "answers": [...],
  "demographics": {...}
}
```

#### 5. Get Results
```http
GET /results/<session_id>
```

---


---

## ❓ Συχνές Ερωτήσεις

### Q: Πώς αλλάζω τον κωδικό της βάσης;
**A:** Επεξεργαστείτε το `backend/app.py` στη γραμμή 9:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:YOUR_PASSWORD@localhost/cyber_quiz_db'
```

### Q: Πώς προσθέτω νέες ερωτήσεις;
**A:** 
1. Ανοίξτε το `backend/insert_all_questions.py`
2. Προσθέστε ερωτήσεις στην αντίστοιχη λίστα (`child_questions`, `adult_questions`, `professional_questions`)
3. Εκτελέστε: `python insert_all_questions.py`

### Q: Το backend δεν εκκινεί - "Port 5000 already in use"
**A:** Αλλάξτε την πόρτα στο `app.py`:
```python
app.run(debug=True, port=5001)
```
Και στο `frontend/src/App.js`:
```javascript
const response = await fetch('http://localhost:5001/api/...');
```

### Q: Πώς κάνω deploy σε production;
**A:**
- Frontend: Deploy στο Netlify, Vercel ή GitHub Pages
- Backend: Deploy στο Heroku, AWS EC2 ή DigitalOcean
- Database: Χρησιμοποιήστε managed MySQL (AWS RDS, Google Cloud SQL)

---

## 🔐 Ασφάλεια

### Σημειώσεις Ασφάλειας:
- Μην κάνετε commit το `app.py` με πραγματικούς κωδικούς
- Χρησιμοποιήστε environment variables για sensitive data
- Ενεργοποιήστε HTTPS σε production
- Εφαρμόστε rate limiting στο API

### Προτεινόμενο για Production:
```python
# backend/.env
DATABASE_URL=mysql+pymysql://user:password@host/db
SECRET_KEY=your-secret-key-here
FLASK_ENV=production
```

---

## 📈 Μελλοντικές Βελτιώσεις

- [ ] Multi-language support (EN, GR)
- [ ] Admin panel για διαχείριση ερωτήσεων
- [ ] Export αποτελεσμάτων σε PDF
- [ ] Leaderboard functionality
- [ ] Email reports
- [ ] Social sharing
- [ ] Progressive Web App (PWA)
- [ ] Mobile apps (React Native)

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork το repository
2. Δημιουργήστε ένα feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit τις αλλαγές (`git commit -m 'Add AmazingFeature'`)
4. Push στο branch (`git push origin feature/AmazingFeature`)
5. Ανοίξτε ένα Pull Request

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.


---

## 🙏 Acknowledgments

- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://react.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Recharts](https://recharts.org/)
- [Lucide Icons](https://lucide.dev/)

---

## 📊 Statistics

- **Total Questions:** 110
  - Παιδιά: 45
  - Ενήλικες: 30
  - Επαγγελματίες: 35
- **Themes:** 19 unique themes
- **Languages:** Greek (Ελληνικά)
- **Database Tables:** 6
- **API Endpoints:** 5



*Τελευταία ενημέρωση: Οκτώβριος 2025*