# AI-Powered Calendar Assistant

## Project Overview
The AI-Powered Calendar Assistant is an intelligent personal assistant that monitors your Google Calendar and sends WhatsApp alerts to keep you informed of your schedule. Designed to automate your daily planning, it minimizes manual work and enhances your productivity.

## Key Features
- **Instant WhatsApp Alerts**: Get notified in real-time for upcoming events.
- **Zero Manual Work**: Automate your calendars to reduce workloads.
- **Intelligent Context Understanding**: The assistant understands the context of your events for smarter alerts.
- **Multi-App Integration**: Seamlessly integrates with various applications for enhanced functionality.
- **Fast & Secure Design**: Built with performance and security in mind.

## What This Workflow Does
The AI-Powered Calendar Assistant operates in a 4-step process:
1. **Detects New Events**: Listens for new events added to your Google Calendar.
2. **AI Analysis via Groq**: Analyzes the event using AI to determine relevance and context.
3. **Smart Actions**: Executes actions such as setting email reminders, creating tasks, or performing searches based on the event details.
4. **WhatsApp Alerts**: Sends automated alerts to your WhatsApp account whenever there’s an update.

## Workflow Architecture
The workflow consists of 5 phases:
1. **Trigger**: The initiation of the calendar monitoring process.
2. **AI Decision**: The AI evaluates the new event to determine the appropriate actions.
3. **Action**: Engaging with additional applications for task execution.
4. **Notification**: Sending alerts through WhatsApp.
5. **Logging**: Keeping a record of actions taken for troubleshooting and auditing purposes.

## Example WhatsApp Notifications
- "Reminder: Team meeting scheduled for 3 PM today."
- "Upcoming event: Doctor's appointment tomorrow at 10 AM!"

## Step-by-Step Execution Flow
1. A new event is added to Google Calendar.
2. The assistant detects the new event and triggers the workflow.
3. The AI analyzes the event details.
4. Based on the analysis, it performs necessary actions and sends notifications.

## Setup Requirements
### Prerequisites
- A Google Calendar account.
- A WhatsApp account for receiving notifications.
- Docker installed on your machine for deployment.

### Credentials to Configure
- Google Calendar API credentials.
- WhatsApp API credentials for sending messages.

## Docker Installation Steps
1. Install Docker from the [official website](https://www.docker.com/get-started).
2. Clone this repository:
   ```bash
   git clone https://github.com/Abdullah17521/AI-Assitant-.git
   cd AI-Assitant-
   ```
3. Build the Docker image:
   ```bash
   docker build -t ai-calendar-assistant .
   ```
4. Run the container:
   ```bash
   docker run -d -p 8080:8080 ai-calendar-assistant
   ```

## Troubleshooting Guide
### Common Issues and Solutions
- **Issue**: Events not detected.
  - **Solution**: Check Google Calendar API permissions.
- **Issue**: WhatsApp notifications not sent.
  - **Solution**: Verify WhatsApp API credentials.

## Learning Outcomes
- Understanding AI integration with calendar applications and messaging services.
- Implementing event-driven workflows for automation.

## Technical Deep-Dive
The workflow consists of over 30 nodes. These nodes include:
- **Event Detection Node**: Listens for new calendar events.
- **AI Processing Nodes**: Analyze event details.
- **Action Nodes**: Execute commands like sending emails and creating tasks.
- **Notification Node**: Send WhatsApp messages for alerts.
- **Logging Node**: Track the status of events and actions.
- **Interconnections**: Nodes communicate using REST APIs and Webhooks to allow seamless data flow and processing across the system.

---