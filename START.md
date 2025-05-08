# Project Startup Guide

Follow these steps to preview and run your project (backend and frontend):

---

## 1. Activate the Virtual Environment
**From your project root:**
```powershell
.venv\Scripts\Activate.ps1
```
**Path:** `./` (project root)

---

## 2. Start the Backend Server
**From your project root:**
```powershell
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```
**Path:** `./` (project root)

---

## 3. Start the Frontend Dev Server
**Open a new terminal.**

**Navigate to the frontend directory:**
```powershell
cd frontend
```
**Path:** `./frontend`

**If you haven't already installed dependencies:**
```powershell
npm install
```

**Then start the dev server:**
```powershell
npm run dev
```

---

## 4. Open Your Browser
Go to: [http://localhost:5173](http://localhost:5173)

**Tip:**
- Always activate the virtual environment before running backend commands or installing Python packages.
- Leave both backend and frontend servers running in their own terminals while you preview the app. 