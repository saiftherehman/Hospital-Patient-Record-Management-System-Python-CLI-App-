# **Hospital Patient Record Management System (Python CLI App)**

A clean and functional **Command Line Interface (CLI)** application for managing hospital patient records.  
This project demonstrates practical use of **Python**, **JSON storage**, **Enums**, **data tables**, and structured menu‑driven logic.

It allows hospital staff to **add**, **search**, **update**, **view**, and **delete** patient records — all stored locally in a JSON file.

---

## **Features**

- **Add Patient**  
  Create a new patient record with ID, name, age, diagnosis, room number, and admission status.

- **Search Patient**  
  Look up a patient using either their name or unique ID.

- **Update Status**  
  Change a patient’s admission status (Admitted / Discharged).

- **Update Room**  
  Assign a new room number to an existing patient.

- **Delete Patient**  
  Remove a patient record from the system.

- **Show All Patients**  
  Display all records in a clean table using `pandas` + `tabulate`.

- **Persistent Storage**  
  Records are saved in **patient.json**, automatically created and updated.

---

## **Project Structure**

```
hospital-record-system/
│
├── patient.json          # Auto-generated storage file
├── hospital_system.py    # Main CLI script
└── README.md             # Documentation
```

---

## **How It Works**

### **Data Storage**
All patient records are stored in a JSON file:

```json
[
  {
    "Unique Patient ID": "P001",
    "Name": "John",
    "Age": 45,
    "Disease / Diagnosis": "Flu",
    "Room No.": "A12",
    "Admission Status": "Admitted"
  }
]
```

### **Menu System**
The app uses an `Enum` to define menu selections:

```python
class selections(int, Enum):
    PATIENT_ADD = 1
    PATIENT_SEARCH = 2
    PATIENT_STATUS = 3
    PATIENT_ROOM = 4
    PATIENT_DELETE = 5
    PATIENTS_SHOW_ALL = 6
    EXIT = 7
```

Each option triggers a dedicated function.

---

## **Running the Application**

Make sure Python is installed, then run:

```bash
python hospital_system.py
```

You’ll see:

```
-----Hospital Patient Record Management System-----
1. Add New patient
2. Search patient (by ID or Name)
3. Update patient status
4. Update room number
5. Delete patient record
6. Show all patients
7. Exit
```

---

## **Example Usage**

### **Adding a Patient**
```
Patient ID: P001
Patient Name: Alex
Patient Age: 32
Patient Disease/Diagnosis: Fever
Patient Room No.: B10
Admission Status (Admitted/Discharged): Admitted
Patient Admitted!
```

### **Viewing All Patients**
```
+----------------------+--------+-----+----------------------+-----------+-------------------+
| Unique Patient ID    | Name   | Age | Disease / Diagnosis | Room No.  | Admission Status  |
+----------------------+--------+-----+----------------------+-----------+-------------------+
| P001                 | Alex   | 32  | Fever               | B10       | Admitted          |
+----------------------+--------+-----+----------------------+-----------+-------------------+
```

### **Searching**
```
Enter the patient Name or ID: Alex
Patient Found:
{'Unique Patient ID': 'P001', 'Name': 'Alex', 'Age': 32, ...}
```
