# Hospital Patient Record Management System

import json
from pathlib import Path
from enum import Enum
import pandas as pd
from tabulate import tabulate

class selections(int, Enum):
    PATIENT_ADD = 1
    PATIENT_SEARCH = 2
    PATIENT_STATUS = 3
    PATIENT_ROOM = 4
    PATIENT_DELETE = 5
    PATIENTS_SHOW_ALL = 6
    EXIT = 7

patient = []
if (patient_file := Path("patient.json")).is_file():
    patient = json.loads(patient_file.read_text())

# Add new patient
def new_patient(pid, name: str, age, dd, room, status: str):
    return {
        "Unique Patient ID": pid.capitalize(),
        "Name": name.capitalize(),
        "Age": age,
        "Disease / Diagnosis": dd.capitalize(),
        "Room No.": room.capitalize(),
        "Admission Status": status.capitalize()
    }

# Search patient (by ID or name)
def search_patient(info):
    for pat in patient:
        if info == pat["Name"] or info == pat["Unique Patient ID"]:
            print(f"Patient Found:\n{pat}")
            return
    print("Patient Not Found!")

# Update patient status
def status_patient(info):
    for pat in patient:
        if info == pat["Name"] or info == pat["Unique Patient ID"]:
            print(f"Current Status: {pat['Admission Status']}")
            status = input("Enter A (Admitted) or D (Discharged): ").upper()

            if status == "A" and pat["Admission Status"] == "Admitted":
                print("Already admitted.")
                return
            if status == "D" and pat["Admission Status"] == "Discharged":
                print("Already discharged.")
                return

            if status == "A":
                pat["Admission Status"] = "Admitted"
            elif status == "D":
                pat["Admission Status"] = "Discharged"
            else:
                print("Invalid input!")
                return

            print("Status Update Successful!")
            save()
            return
    print("Patient not found!")

# Update room number
def update_room(info):
    for pat in patient:
        if info == pat["Name"] or info == pat["Unique Patient ID"]:
            new_room = input("Enter the new room number: ").capitalize()
            if new_room == pat["Room No."]:
                print("Room not available. Try different room.")
            else:
                pat["Room No."] = new_room
                print(f"Room updated for {pat['Name']}")
                save()
            return
    print("Patient not found!")

# Delete patient record
def delete_patient(pid):
    global patient
    patient = [pat for pat in patient if pat["Unique Patient ID"] != pid]
    save()

def save():
    with open("patient.json", "w") as file:
        json.dump(patient, file, indent=4)

while True:
    print("-----Hospital Patient Record Management System-----")
    print(
        "1. Add New patient",
        "2. Search patient (by ID or Name)",
        "3. Update patient status",
        "4. Update room number",
        "5. Delete patient record",
        "6. Show all patients",
        "7. Exit",
        sep="\n",
    )

    choice = int(input("Enter the option: "))

    if choice == selections.PATIENT_ADD:
        patient_id = input("Patient ID: ").capitalize()
        patient_name = input("Patient Name: ").capitalize()
        patient_age = int(input("Patient Age: "))
        patient_dd = input("Patient Disease/Diagnosis: ").capitalize()
        patient_room = input("Patient Room No.: ").capitalize()
        patient_at = input("Admission Status (Admitted/Discharged): ").capitalize()

        patient.append(new_patient(patient_id, patient_name, patient_age, patient_dd, patient_room, patient_at))
        print("Patient Admitted!")
        save()

    elif choice == selections.PATIENT_SEARCH:
        given_info = input("Enter the patient Name or ID: ").capitalize()
        search_patient(given_info)
    
    elif choice == selections.PATIENT_STATUS:
        given_info = input("Enter patient Name or ID: ").capitalize()
        status_patient(given_info)

    elif choice == selections.PATIENT_ROOM:
        given_info = input("Enter patient Name or ID: ").capitalize()
        update_room(given_info)

    elif choice == selections.PATIENT_DELETE:
        given_id = input("Patient ID: ").capitalize()
        delete_patient(given_id)
        print("Patient record deleted (if existed)")

    elif choice == selections.PATIENTS_SHOW_ALL:
        if not patient:
            print("No patients found.")
        else:
            df = pd.DataFrame(patient)
            print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))

    elif choice == selections.EXIT:
        print("Program closed.")
        break
    else:
        print("Invalid input. Try again!")
