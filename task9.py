
# Campus Festival Registration and Financial Audit

# Participant records: (Participant_ID, Name, Fee_Paid)
participants = [
    ("P101", "Arun", 500),
    ("P102", "Bala", 500),
    ("P103", "Charan", 400),
    ("P101", "Arun", 500),  # Duplicate registration
    ("P104", "Deepak", 500),
    ("P105", "Esha", 0)     # Fee not paid
]

# Sponsorship records: (Sponsor_Name, Contribution)
sponsors = [
    ("ABC Company", 10000),
    ("XYZ Enterprises", 15000),
    ("Local Business", 5000)
]

# Expense records: (Expense_Category, Amount)
expenses = [
    ("Venue", 8000),
    ("Decoration", 3000),
    ("Food", 7000),
    ("Sound System", 4000),
    ("Certificates", 1000)
]

# 1. Detect duplicate participant IDs
seen_ids = set()
unique_participants = []
duplicates = []

for participant in participants:
    participant_id = participant[0]

    if participant_id in seen_ids:
        duplicates.append(participant)
    else:
        seen_ids.add(participant_id)
        unique_participants.append(participant)

# 2. Reconcile registration fees
total_collected = sum(p[2] for p in unique_participants)
registered_count = len(unique_participants)
unpaid_participants = [
    p for p in unique_participants if p[2] == 0
]

# 3. Calculate sponsorship contributions
total_sponsorship = sum(s[1] for s in sponsors)

# 4. Calculate total expenses
total_expenses = sum(e[1] for e in expenses)

# 5. Calculate final financial balance
total_income = total_collected + total_sponsorship
balance = total_income - total_expenses

# Display audit report
print("CAMPUS FESTIVAL FINANCIAL AUDIT")
print("-" * 40)

print("\nDuplicate Registrations:")
if duplicates:
    for p in duplicates:
        print(p[0], "-", p[1])
else:
    print("None")

print("\nUnique Participants:", registered_count)
print("Registration Fees Collected: Rs.", total_collected)

print("\nParticipants with Unpaid Fees:")
if unpaid_participants:
    for p in unpaid_participants:
        print(p[0], "-", p[1])
else:
    print("None")

print("\nTotal Sponsorship: Rs.", total_sponsorship)
print("\nExpense Details:")
for category, amount in expenses:
    print(category, ": Rs.", amount)

print("Total Expenses: Rs.", total_expenses)
print("Total Income: Rs.", total_income)
print("Final Financial Balance: Rs.", balance)

if balance > 0:
    print("Status: Festival has a surplus.")
elif balance < 0:
    print("Status: Festival has a deficit.")
else:
    print("Status: Festival budget is balanced.")
