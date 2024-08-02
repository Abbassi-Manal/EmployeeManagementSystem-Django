# Employee Management System 💻

The Employee Management System is a web application developed using the Django framework. It is designed to manage employee information, including personal and employment details and salary information. This project aims to provide an intuitive and efficient interface to store, retrieve, and update employee data. 🌐

## Key Features 🔑

- **Employee Registration**: Users can add new employees to the system, including their personal details, employment details, and salary information. 📝
- **Employee Listing**: Users can view a comprehensive list of all employees in the system, including their details. 📋
- **Employee Search**: Users can search for specific employees based on various criteria, such as name, employee ID, or department. 🔍
- **Employee Update**: Users can update the details of existing employees, such as their contact information or job title. 🖋️
- **Employee Deletion**: Users can remove employees from the system if necessary. 🗑️
- **Database Management**: The system uses a MySQL database to store employee data, which can be exported and imported. 💾

## Installation Guide 🛠️

Follow these steps to run the Employee Management System:

1. **Install Dependencies**:
   - Run the following command in your terminal or command prompt to install the required dependencies:
     ```
     pip install -r requirements.txt
     ```

2. **Set Up the Database**:
   - Open the `employee_management.sql` file in the `Data` folder.
   - Create a new MySQL database and import the `employee_management.sql` file to set up the necessary tables and data. 🗃️

3. **Launch the Application**:
   - Run the command `python manage.py runserver` to start the Employee Management System. 🚀

4. **Access the Application**:
   - Enter the following URL in your web browser: `http://127.0.0.1:8000/` 🌐

5. **Access the Database**:
   - To view the contents of the database, open the `employee_management.sql` file in the `Data` folder. 👀

## Usage 🤖

1. **Employee Registration**: Click the "Add Employee" button to open the employee registration form and enter the necessary information. 📋
2. **Employee Listing**: The main window displays a list of all employees in the system. You can sort the list by clicking on the column headers. 📊
3. **Employee Search**: Use the search bar at the top of the window to search for employees based on different criteria. 🔍
4. **Employee Update**: Select an employee from the list and click the "Update Employee" button to modify their details. ✏️
5. **Employee Deletion**: Select an employee from the list and click the "Delete Employee" button to remove them from the system. 🗑️

Enjoy using the Employee Management System! 😊
