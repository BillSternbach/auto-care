# Auto Care Project Roadmap

This document outlines the planned next steps, priorities, and phases for the Auto Care project.

---

## Phase 1 - Core Functionality

### 1. Finish CRUD Operations
- Implement **Update/Delete (UD)** for vehicles and maintenance records
- Ensure database operations are robust and handle edge cases

### 2. Add Service (Maintenance) CLI
- CLI commands to:
  - Add new maintenance/service records
  - List upcoming/past services
  - Update or delete service entries

### 3. Implement Basic Validation / Error Handling
- Validate user inputs:
  - Mileage cannot be negative
  - Dates must be valid and logical
  - Required fields must be present
- Gracefully handle invalid CRUD operations

---

## Phase 2 - Testing & Reliability

### 4. Add Unit & Integration Tests
- Test CRUD operations for vehicles and maintenance records
- Test CLI commands for correct behavior
- Test validation logic (e.g., invalid inputs raise errors)

### 5. Refine Vehicle Logic
- Define rules for maintenance intervals:
  - Mileage-based
  - Time-based
- Alerts or recommendations (optional CLI printouts or logs)
- Validate logical inconsistencies (e.g., service date in the future)

___

## Phase 3 - Documentation & Project Health

### 6. SDLC & Support Documents
- **Requirements doc:** Functional & non-functional requirements
- **Test plan:** Summary of test coverage
- **Deployment/maintenance guide:** How to set up environment, run CLI, add vehicles, update DB

### 7. Optional Enhancements
- CLI improvements: colored outputs, formatted tables
- Notifications or reminders (print statements or logs)
- Input santitization and advanced error handling
- Future: GUI or web interface

---

## Priority Summary
1. Finish UD for CRUD
2. Build CLI for adding/viewing services
3. Add validation/error handling
4. Add tests
5. Refine vehicle maintenance logic
6. Link documentation + add SDLC docs
7. Optional enhancements
