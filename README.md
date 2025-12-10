# Internet & Web Basics Workshop

A comprehensive workshop repository for the **Setif Developers Group (SDG)** that teaches the fundamentals of how the Internet and the Web work, covering frontend development, backend development, and full-stack integration.

## 📚 Workshop Overview

This workshop is designed to provide hands-on experience with web development fundamentals, from basic HTML/CSS/JavaScript to building full-stack applications with modern frameworks and APIs.

### Learning Objectives

- Understand how the Internet and the Web actually work
- Learn frontend development with HTML, CSS, and JavaScript
- Build interactive web applications with React and Vite
- Create backend APIs using FastAPI (Python)
- Integrate frontend and backend to build full-stack applications
- Work with databases (SQLite) for data persistence
- Handle CORS and HTTP communication

---

## 📁 Project Structure

```
Internet_web_basic/
├── frontend/              # Frontend development modules
│   ├── hello/            # Basic HTML/CSS/JS introduction
│   └── simple-app/       # React + Vite application
├── backend/              # Backend development with FastAPI
│   └── main.py          # Simple FastAPI server
└── full-stack/          # Full-stack integration examples
    ├── client/          # Frontend client (vanilla JS)
    └── second_version/  # Backend with database integration
```

---

## 🚀 Getting Started

### Prerequisites

- **Node.js** (v16 or higher) - for frontend development
- **Python** (v3.8 or higher) - for backend development
- **npm** or **yarn** - package manager
- **pip** - Python package manager
- A modern web browser (Chrome, Firefox, Edge, etc.)
- A code editor (VS Code recommended)

---

## 📖 Workshop Modules

### 1️⃣ Frontend Basics (`frontend/hello/`)

A simple introduction to web development fundamentals.

**What you'll learn:**
- HTML structure
- CSS styling
- Basic JavaScript

**Files:**
- `index.html` - Main HTML page
- `style.css` - Styling
- `main.js` - JavaScript logic

**How to run:**
```bash
cd frontend/hello
# Open index.html in your browser or use a local server:
python -m http.server 8000
# Visit: http://localhost:8000
```

---

### 2️⃣ React Application (`frontend/simple-app/`)

A modern React application built with Vite, featuring Hot Module Replacement (HMR) and ESLint.

**What you'll learn:**
- React components and hooks
- Vite build tool
- Modern JavaScript (ES6+)
- Component-based architecture

**Tech Stack:**
- React 18
- Vite
- ESLint with React plugins

**How to run:**
```bash
cd frontend/simple-app

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production (optional)
npm run build
```

The app will be available at `http://localhost:5173`

---

### 3️⃣ Backend API (`backend/`)

A FastAPI backend server with RESTful endpoints.

**What you'll learn:**
- RESTful API design
- FastAPI framework
- Pydantic models for data validation
- HTTP methods (GET, POST)

**Features:**
- `GET /` - Hello world endpoint
- `GET /random` - Returns a random integer
- `POST /comment` - Accepts user comments with validation

**How to run:**
```bash
cd backend

# Create virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn pydantic

# Run the server
uvicorn main:app --reload

# API will be available at: http://localhost:8000
# Interactive docs at: http://localhost:8000/docs
```

---

### 4️⃣ Full-Stack Application (`full-stack/`)

A complete full-stack application with frontend-backend integration.

#### Client (`full-stack/client/`)

**What you'll learn:**
- Form handling
- Fetch API for HTTP requests
- Client-server communication

**Features:**
- Workshop feedback form
- Rating system (1-10)
- Multiple input types (text, number, select)
- Form validation

**How to run:**
```bash
cd full-stack/client
# Open index.html in your browser or use:
python -m http.server 8001
# Visit: http://localhost:8001
```

#### Server (`full-stack/second_version/`)

**What you'll learn:**
- Database integration (SQLite)
- CORS configuration
- Data persistence
- SQL operations

**Features:**
- SQLite database for storing feedback
- CORS middleware for cross-origin requests
- `POST /submit_feedback/` - Stores user feedback

**How to run:**
```bash
cd full-stack/second_version

# Install dependencies
pip install fastapi uvicorn pydantic

# Run the server
uvicorn main:app --reload --port 8000

# API will be available at: http://localhost:8000
```

**Running the complete full-stack app:**
1. Start the backend server (port 8000)
2. Open the client in your browser (port 8001)
3. Submit feedback through the form
4. Data will be stored in `feedback.db`

---

## 🛠️ Technologies Used

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling
- **JavaScript (ES6+)** - Logic and interactivity
- **React** - UI library
- **Vite** - Build tool and dev server

### Backend
- **Python** - Programming language
- **FastAPI** - Modern web framework
- **Pydantic** - Data validation
- **SQLite** - Database
- **Uvicorn** - ASGI server

---

## 📝 Workshop Flow

1. **Start with Frontend Basics** (`frontend/hello/`)
   - Understand HTML, CSS, and JavaScript fundamentals
   
2. **Build a React App** (`frontend/simple-app/`)
   - Learn modern frontend development with React and Vite
   
3. **Create a Backend API** (`backend/`)
   - Build RESTful APIs with FastAPI
   
4. **Integrate Full-Stack** (`full-stack/`)
   - Connect frontend and backend
   - Work with databases
   - Handle real-world scenarios (CORS, validation, etc.)

---

## 🎯 Next Steps

After completing this workshop, you can:
- Build more complex React applications
- Explore advanced FastAPI features (authentication, file uploads, WebSockets)
- Learn about deployment (Docker, cloud platforms)
- Dive deeper into databases (PostgreSQL, MongoDB)
- Explore other frontend frameworks (Vue.js, Angular)
- Learn about state management (Redux, Zustand)

---

## 🤝 Contributing

This is a workshop repository for educational purposes. If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

---

## 📧 Contact

**Setif Developers Group (SDG)**

For questions or feedback about this workshop, please reach out to the SDG community.

---

## 📄 License

This project is open source and available for educational purposes.

---

**Happy Learning! 🚀**