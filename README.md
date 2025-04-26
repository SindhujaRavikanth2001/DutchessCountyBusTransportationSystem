# 🚌 Dutchess County Bus Transportation System (DCBTS)

A database-driven web application designed to revolutionize public transport for Dutchess County commuters, tourists, and administrators.

## ✨ Project Overview

- **Goal**: Enhance the Dutchess County Public Transportation (DCPT) system through a digital, user-friendly, and admin-friendly application.
- **Scope**: Streamlined trip planning, reservation management, user authentication, admin controls, and optimized data management.
- **Team**: The Four-Ce (Sindhuja Ravikanth, Shanmukha Chowdary Nalla, Gaurav Bapurao Sherla, Katipally Chanakya Vardhan Reddy)

## 🌐 Features

- User login, signup, password reset, and profile management.
- Admin portal for managing users, buses, routes, and tickets.
- View bus schedules, route stops, ticket types, and make reservations.
- Notifications for holidays and route changes.
- Secure database integration with proper foreign key handling.
- Optimized data insertion and bulk loading via CSV imports.

## 📅 Technologies Used

- **Backend**: MySQL Database
- **Frontend**: HTML, CSS, JS (Graphical User Interface)
- **Database Modeling**: ERDPlus for ER diagrams, MySQL Workbench for EER diagrams

## 📖 Database Design

- **Entities**: User, Admin, Bus, Reservation, TicketType, Payment, BusRoute, BusStop, Schedule, Department, Employee, Notification, Holidays
- **Relationships**: Detailed foreign key relationships ensuring referential integrity.
- **EER Features**: Generalization, specialization, aggregation, weak/strong entities, multi-valued and composite attributes.

## 📊 Project Structure

```
DCBTS-Project/
├── Database Schema
│   ├── Create Statements
│   ├── Insert Statements
│   ├── Optimization Techniques
├── GUI Design
│   ├── User Interface (User/Commuter)
│   └── Admin Interface
├── Entity Relationship Models
│   ├── ER Model
│   └── Enhanced EER Model
├── Documentation
│   ├── Project Report (Phase 8)
│   └── User Guide
└── GitHub Repository
```

## 🔗 GitHub Repository

[https://github.com/SindhujaRavikanth2001/DBMS_Project](https://github.com/SindhujaRavikanth2001/DBMS_Project)

## 🏢 Key Modules

- **Login Module**
- **Reservation Management**
- **Ticket Purchasing & Payment Tracking**
- **Holiday Notification Alerts**
- **Admin User Management Panel**

## ⚡ Highlights

- Real-time bus route search between source and destination.
- Fare estimation based on user profile (e.g., student, adult).
- Favorites feature to bookmark frequent routes.
- Foreign key handling and bulk data loading optimized for performance.
- Data security and backup strategies incorporated.

## 🔢 Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/SindhujaRavikanth2001/DBMS_Project.git
```

2. **Set up MySQL Database**
- Create the database using provided `CREATE TABLE` scripts.
- Insert sample data using provided `INSERT` and `LOAD DATA` scripts.

3. **Run the Application**
- Launch the GUI for user/admin access (HTML/JS/CSS files provided in templates).

## 📈 Performance Enhancements

- Disabled foreign key checks temporarily during data loading.
- Used bulk inserts instead of multiple single-row inserts.
- Indexed critical columns to speed up joins and lookups.

## 🔗 References

- Dutchess County Public Transportation official data
- NYC Transit, Moovit app comparisons

## 🎓 Team Contributions

- **Sindhuja Ravikanth**: Team Lead, Backend, DB Design
- **Shanmukha Chowdary Nalla**: Application Logic, Data Engineering
- **Gaurav Bapurao Sherla**: Documentation, Testing
- **Katipally Chanakya Vardhan Reddy**: Frontend Development, Optimization

## 🔒 License

This project is licensed under the MIT License.
