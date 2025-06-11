# Employee Management System

A full-stack web application built with Django (backend) and Vue.js (frontend) for managing employee information.

## Features

- **Employee Cards**: Display 4 employee cards per page with pagination
- **Employee Information**: Each card shows:
  - Employee name (bold)
  - Employee photo
  - Employee ID
  - Employee age
- **Edit Functionality**: Click the "Edit" button to open a popup with employee list
- **Employee Selection**: Select any employee from the popup to update the card
- **Bar Chart**: Visual representation of employee ages using Chart.js
- **Responsive Design**: Modern, beautiful UI with glassmorphism effects

## Project Structure

```
/
├── employee_backend/          # Django backend
│   ├── employee_backend/      # Main Django project
│   ├── employees/             # Employees app
│   └── media/                 # Employee photos storage
└── employee-frontend/         # Vue.js frontend
    ├── src/
    │   ├── components/        # Vue components
    │   └── assets/            # Static assets
    └── public/
        └── media/             # Frontend media files
```

## Backend (Django)

### Features

- Django REST Framework for API endpoints
- Employee model with name, ID, photo, and age
- CORS enabled for frontend communication
- Automatic image generation for sample employees
- Media file handling for employee photos

### API Endpoints

- `GET /api/employees/` - List all employees
- `GET /api/employees/{id}/` - Get specific employee
- `PUT /api/employees/{id}/` - Update employee
- `POST /api/employees/` - Create new employee
- `DELETE /api/employees/{id}/` - Delete employee
- `GET /api/employees/chart_data/` - Get data for bar chart

## Frontend (Vue.js)

### Components

- **App.vue**: Main application component
- **EmployeeList.vue**: Main container with pagination and chart
- **EmployeeCard.vue**: Individual employee card component
- **BarChart.vue**: Chart.js integration for age visualization

### Features

- Pagination (4 cards per page)
- Modal popup for employee selection
- Real-time chart updates
- Responsive grid layout
- Modern glassmorphism design

## Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn
- Git (optional, for cloning)

### Backend Setup

1. Navigate to the project directory:

   **Windows:**

   ```cmd
   cd C:\path\to\your\project\directory
   ```

   **macOS/Linux:**

   ```bash
   cd /path/to/your/project/directory
   ```

2. Create and activate virtual environment:

   **Windows:**

   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

   **macOS/Linux:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install Python dependencies:

   **All platforms:**

   ```bash
   pip install django djangorestframework django-cors-headers pillow
   ```

4. Navigate to backend directory and run migrations:

   **All platforms:**

   ```bash
   cd employee_backend
   python manage.py migrate
   ```

5. Create sample employees:

   **All platforms:**

   ```bash
   python manage.py create_sample_employees
   ```

6. Start Django development server:

   **All platforms:**

   ```bash
   python manage.py runserver
   ```

The backend will be available at: http://localhost:8000

### Frontend Setup

1. Navigate to frontend directory:

   **All platforms:**

   ```bash
   cd employee-frontend
   ```

2. Install Node.js dependencies:

   **All platforms:**

   ```bash
   npm install
   ```

3. Install additional packages:

   **All platforms:**

   ```bash
   npm install axios chart.js vue-chartjs
   ```

4. Start Vue development server:

   **All platforms:**

   ```bash
   npm run dev
   ```

The frontend will be available at: http://localhost:5173

## Quick Start (All Platforms)

For users who want to get started quickly:

1. **Clone or download the project**
2. **Backend:** Open terminal in project directory

   - Create virtual environment: `python -m venv venv` (Windows) or `python3 -m venv venv` (macOS/Linux)
   - Activate: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (macOS/Linux)
   - Install dependencies: `pip install django djangorestframework django-cors-headers pillow`
   - Navigate to backend: `cd employee_backend`
   - Run migrations: `python manage.py migrate`
   - Create sample data: `python manage.py create_sample_employees`
   - Start server: `python manage.py runserver`

3. **Frontend:** Open new terminal in project directory

   - Navigate to frontend: `cd employee-frontend`
   - Install dependencies: `npm install`
   - Install packages: `npm install axios chart.js vue-chartjs`
   - Start server: `npm run dev`

4. **Access the application:**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000

## Usage

1. **View Employees**: The main page displays 4 employee cards per page
2. **Navigate Pages**: Use "Previous" and "Next" buttons to navigate between pages
3. **Edit Employee**: Click the "Edit" button on any card to open the employee selection modal
4. **Select Employee**: Click on any employee in the modal to update the card
5. **View Chart**: Scroll down to see the bar chart showing employee age distribution

## Technologies Used

### Backend

- Django 5.2.2
- Django REST Framework
- django-cors-headers
- Pillow (for image processing)
- SQLite (database)

### Frontend

- Vue.js 3
- Chart.js
- Axios (HTTP client)
- Vite (build tool)

## File Storage

File paths are relative to the project root and work on all platforms:

- **Backend**: Employee photos are stored in `employee_backend/media/employee_photos/`
- **Frontend**: Placeholder images are stored in `employee-frontend/public/media/`

**Platform Notes:**

- Windows: Uses backslashes in actual file paths (e.g., `employee_backend\media\employee_photos\`)
- macOS/Linux: Uses forward slashes in actual file paths (e.g., `employee_backend/media/employee_photos/`)
- The application handles path differences automatically

## Platform Compatibility

This application is fully cross-platform compatible:

- **Windows 10/11**: Tested with Python 3.8+ and Node.js 16+
- **macOS**: Tested with Python 3.8+ and Node.js 16+
- **Linux (Ubuntu/Debian/CentOS)**: Compatible with Python 3.8+ and Node.js 16+

**Database:**

- Uses SQLite which is included with Python and works on all platforms
- No additional database setup required

**Dependencies:**

- All Python packages work across platforms
- All Node.js packages are platform-independent

## API Integration

The frontend communicates with the Django backend through REST API calls:

- Employee data fetching
- Chart data for visualization
- Real-time updates when employees are selected

## Responsive Design

The application features a modern, responsive design with:

- Glassmorphism effects
- Gradient backgrounds
- Smooth animations
- Mobile-friendly layout
- Accessible color scheme
