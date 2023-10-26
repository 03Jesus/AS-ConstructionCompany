
# FastAPI backend server for construction company
## About this project:
A construction company uses separate systems for equipment, inventory, scheduling, payroll and accounting accumulated over decades. Data is siloed, limiting operational insight. Adding new analytics is difficult and time-consuming. Changing any system requires complex coordination. Disconnected systems make it nearly impossible to optimize decisions throughout the construction lifecycle. For example, equipment and material allocation is not optimal because work schedules lack real-time visibility. This leads to delays, unplanned downtime and bloated inventories. The company needs to share unified data across all facets of construction operations to increase productivity. The solution would identify microservices aligned with construction capabilities, such as scheduling and equipment management. These microservices would expose relevant operations data through APIs managed by a gateway. This data is transmitted to an analytics platform in the cloud for optimization using AI. This approach gradually decomposes isolated systems into specific, decoupled services that provide unified access to data. There are some specifics:

▪ Develop microservices for scheduling, teams, project management.

▪ Expose relevant operational data through APIs controlled by a gateway.

▪ Transfer API data to a cloud analytics platform.

▪ Apply analytics and AI to optimize scheduling and equipment usage.

## The MVP
Our MVP for this project is create a CRUD microservices for: Employees, payrolls, gadgets (tools), equipment, schedules, clients, and of course, projects. These will be connected to a database where the server will be able to make the respective calls.

# How tu run

## 1. Create a Python virtual environment

### On Windows:
`python -m venv **virtual_enviornment_name**`
### On Linux / Mac OS
`python3 -m virtualenv **virtual_enviornment_name**`

## 2. Activate the virtual environment
### On Windows
`**virtual_enviornment_name**\Scripts\activate`
### On Linux / Mac OS
`source  **virtual_enviornment_name**/bin/activate`

## 3. Install the dependencies
### On Windows
`pip install -r requirements.txt`
### On Linux / Mac OS
`pip3 intall -r requirements.txt`

## 4. Run the FastAPI Server
`uvicorn main:app --reload`
  
  

# Environment Variables

You must have an `.env` file at the same level of the `main.py` file. With the next variables:
`DATABASE_URL=**URL_OF_THE_DATABASE**`