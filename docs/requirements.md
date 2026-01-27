# Auto Care - MVP Reqirements (PRD-Lite)

## Problem
Vehicle owners track service records between reciepts, notes, and memory, making it difficult to have a complete service record.

## Audience
A vehicle owner who wants a simple method to record and review service history in one place.

## Goals
- Users can add and view their vehicles and records
- Users can add vehicle maintenance records
- Data persists between runs

## Non-Goals
- Web interface
- User accounts or authentication
- Service reminders or notifications
- Cloud sunchronization

## Success Criteria
- User can add a vehicle in the CLI
- User can add service records linked to a vehicle
- User can view service history by vehicle
- Data is stored locally and persists across sessions
- All CLI commands are intuitive to use

## Future Considerations (Out of Scope for MVP)
- VIN-Based lookup to allow authorized parties (dealers and insurers) to view maintenance history
- Web interface built on top of existing application
- Impliment access control and encryption to allow multiple users or cloud synchronization
