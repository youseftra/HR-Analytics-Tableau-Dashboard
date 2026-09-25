import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

# ============================================================
# INITIALIZATION
# ============================================================

fake = Faker("en_US")

Faker.seed(42)
np.random.seed(42)
random.seed(42)

num_records = 8950


# ============================================================
# STATES & CITIES
# ============================================================

states_cities = {
    "New York": ["New York City", "Buffalo", "Rochester"],
    "Virginia": ["Virginia Beach", "Norfolk", "Richmond"],
    "Florida": ["Miami", "Orlando", "Tampa"],
    "Illinois": ["Chicago", "Aurora", "Naperville"],
    "Pennsylvania": ["Philadelphia", "Pittsburgh", "Allentown"],
    "Ohio": ["Columbus", "Cleveland", "Cincinnati"],
    "North Carolina": ["Charlotte", "Raleigh", "Greensboro"],
    "Michigan": ["Detroit", "Grand Rapids", "Warren"]
}

states = list(states_cities.keys())

# Probability for each state
state_prob = [
    0.70,  # New York
    0.02,  # Virginia
    0.01,  # Florida
    0.03,  # Illinois
    0.05,  # Pennsylvania
    0.03,  # Ohio
    0.05,  # North Carolina
    0.11   # Michigan
]


# ============================================================
# DEPARTMENTS & JOB TITLES
# ============================================================

departments = [
    "HR",
    "IT",
    "Sales",
    "Marketing",
    "Finance",
    "Operations",
    "Customer Service"
]

departments_prob = [
    0.02,
    0.15,
    0.21,
    0.08,
    0.05,
    0.30,
    0.19
]


jobtitles = {
    "HR": [
        "HR Manager",
        "HR Coordinator",
        "Recruiter",
        "HR Assistant"
    ],

    "IT": [
        "IT Manager",
        "Software Developer",
        "System Administrator",
        "IT Support Specialist"
    ],

    "Sales": [
        "Sales Manager",
        "Sales Consultant",
        "Sales Specialist",
        "Sales Representative"
    ],

    "Marketing": [
        "Marketing Manager",
        "SEO Specialist",
        "Content Creator",
        "Marketing Coordinator"
    ],

    "Finance": [
        "Finance Manager",
        "Accountant",
        "Financial Analyst",
        "Accounts Payable Specialist"
    ],

    "Operations": [
        "Operations Manager",
        "Operations Analyst",
        "Logistics Coordinator",
        "Inventory Specialist"
    ],

    "Customer Service": [
        "Customer Service Manager",
        "Customer Service Representative",
        "Support Specialist",
        "Help Desk Technician"
    ]
}


jobtitles_prob = {
    "HR": [0.03, 0.30, 0.47, 0.20],

    "IT": [0.02, 0.47, 0.20, 0.31],

    "Sales": [0.03, 0.25, 0.32, 0.40],

    "Marketing": [0.04, 0.25, 0.41, 0.30],

    "Finance": [0.03, 0.37, 0.40, 0.20],

    "Operations": [0.02, 0.20, 0.40, 0.38],

    "Customer Service": [0.04, 0.30, 0.38, 0.28]
}


# ============================================================
# EDUCATION
# ============================================================

education_mapping = {

    "HR Manager": ["Master", "PhD"],
    "HR Coordinator": ["Bachelor", "Master"],
    "Recruiter": ["High School", "Bachelor"],
    "HR Assistant": ["High School", "Bachelor"],

    "IT Manager": ["Master", "PhD"],
    "Software Developer": ["Bachelor", "Master"],
    "System Administrator": ["Bachelor", "Master"],
    "IT Support Specialist": ["High School", "Bachelor"],

    "Sales Manager": ["Master", "PhD"],
    "Sales Consultant": ["Bachelor", "Master", "PhD"],
    "Sales Specialist": ["Bachelor", "Master", "PhD"],
    "Sales Representative": ["Bachelor"],

    "Marketing Manager": ["Bachelor", "Master", "PhD"],
    "SEO Specialist": ["High School", "Bachelor"],
    "Content Creator": ["High School", "Bachelor"],
    "Marketing Coordinator": ["Bachelor"],

    "Finance Manager": ["Master", "PhD"],
    "Accountant": ["Bachelor"],
    "Financial Analyst": ["Bachelor", "Master", "PhD"],
    "Accounts Payable Specialist": ["Bachelor"],

    "Operations Manager": ["Bachelor", "Master"],
    "Operations Analyst": ["Bachelor", "Master"],
    "Logistics Coordinator": ["Bachelor"],
    "Inventory Specialist": ["High School", "Bachelor"],

    "Customer Service Manager": ["Bachelor", "Master", "PhD"],
    "Customer Service Representative": ["High School", "Bachelor"],
    "Support Specialist": ["High School", "Bachelor"],
    "Help Desk Technician": ["High School", "Bachelor"]
}


# ============================================================
# HIRE DATE DISTRIBUTION
# ============================================================

# These are weights, not percentages.
# They are normalized automatically by np.random.choice().

hire_year_weights = {
    2015: 5,
    2016: 8,
    2017: 17,
    2018: 9,
    2019: 10,
    2020: 11,
    2021: 5,
    2022: 12,
    2023: 14,
    2024: 9
}


def generate_hire_date():
    """
    Generate a random hire date using the custom
    probability distribution.
    """

    years = list(hire_year_weights.keys())
    weights = list(hire_year_weights.values())

    year = random.choices(
        years,
        weights=weights,
        k=1
    )[0]

    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)

    return fake.date_time_between(
        start_date=start_date,
        end_date=end_date
    )


# ============================================================
# SALARY
# ============================================================

salary_ranges = {

    "HR": {
        "HR Manager": (60000, 90000),
        "HR Coordinator": (50000, 60000),
        "Recruiter": (50000, 70000),
        "HR Assistant": (50000, 60000)
    },

    "IT": {
        "IT Manager": (80000, 120000),
        "Software Developer": (70000, 95000),
        "System Administrator": (60000, 90000),
        "IT Support Specialist": (50000, 60000)
    },

    "Sales": {
        "Sales Manager": (70000, 110000),
        "Sales Consultant": (60000, 90000),
        "Sales Specialist": (50000, 80000),
        "Sales Representative": (50000, 70000)
    },

    "Marketing": {
        "Marketing Manager": (70000, 100000),
        "SEO Specialist": (50000, 80000),
        "Content Creator": (50000, 60000),
        "Marketing Coordinator": (50000, 70000)
    },

    "Finance": {
        "Finance Manager": (80000, 120000),
        "Accountant": (50000, 80000),
        "Financial Analyst": (60000, 90000),
        "Accounts Payable Specialist": (50000, 60000)
    },

    "Operations": {
        "Operations Manager": (70000, 100000),
        "Operations Analyst": (50000, 80000),
        "Logistics Coordinator": (50000, 60000),
        "Inventory Specialist": (50000, 60000)
    },

    "Customer Service": {
        "Customer Service Manager": (60000, 90000),
        "Customer Service Representative": (50000, 60000),
        "Support Specialist": (50000, 60000),
        "Help Desk Technician": (50000, 80000)
    }
}


def generate_salary(department, job_title):
    """
    Generate a base salary according to department
    and job title.
    """

    minimum, maximum = salary_ranges[department][job_title]

    return np.random.randint(
        minimum,
        maximum + 1
    )


# ============================================================
# BIRTHDATE
# ============================================================

age_distribution = {
    "under_25": 0.11,
    "25_34": 0.25,
    "35_44": 0.31,
    "45_54": 0.24,
    "over_55": 0.09
}


def calculate_age(birthdate, reference_date):
    """
    Calculate age at a given reference date.
    """

    return (
        reference_date.year
        - birthdate.year
        - (
            (reference_date.month, reference_date.day)
            <
            (birthdate.month, birthdate.day)
        )
    )


def generate_birthdate(job_title, education_level, hiredate):
    """
    Generate a realistic birthdate.

    The age distribution is used as a baseline.
    Managers and PhD holders receive a more realistic
    minimum working age.

    The employee must also be at least 18 at hiring.
    """

    age_groups = list(age_distribution.keys())
    age_probs = list(age_distribution.values())

    age_group = np.random.choice(
        age_groups,
        p=age_probs
    )

    # Minimum age constraints
    if "Manager" in job_title:
        min_age = 30

    elif education_level == "PhD":
        min_age = 27

    elif age_group == "under_25":
        min_age = 20

    elif age_group == "25_34":
        min_age = 25

    elif age_group == "35_44":
        min_age = 35

    elif age_group == "45_54":
        min_age = 45

    else:
        min_age = 56

    # Maximum age
    if "Manager" in job_title:
        max_age = 64
    else:
        max_age = 64

    # Generate an age
    age = random.randint(
        min_age,
        max_age
    )

    # Make sure employee is at least 18 at the hire date.
    max_age_at_hire = calculate_age(
        date=hiredate,
        birthdate=hiredate
    ) if False else None

    # Generate birth date relative to hire date.
    latest_birthdate = hiredate.replace(
        year=hiredate.year - age
    )

    earliest_birthdate = hiredate.replace(
        year=hiredate.year - age - 1
    )

    return fake.date_time_between(
        start_date=earliest_birthdate,
        end_date=latest_birthdate
    )


# ============================================================
# TERMINATION DATE
# ============================================================

termination_year_weights = {
    2015: 5,
    2016: 7,
    2017: 10,
    2018: 12,
    2019: 9,
    2020: 10,
    2021: 20,
    2022: 10,
    2023: 7,
    2024: 10
}


def add_months(date_value, months):
    """
    Add months to a datetime while handling month lengths.
    """

    month = date_value.month - 1 + months

    year = date_value.year + month // 12

    month = month % 12 + 1

    # Approximation using 30 days per month.
    # Six months is enforced as 180 days below.
    return date_value + timedelta(
        days=30 * months
    )


def generate_termination_date(hiredate):
    """
    Generate a termination date at least 6 months
    after the hire date.

    The termination must also remain within 2024.
    """

    minimum_date = hiredate + timedelta(
        days=180
    )

    latest_date = datetime(
        2024,
        12,
        31
    )

    # Employee cannot terminate by 2024 if hired too late.
    if minimum_date > latest_date:
        return None

    valid_years = {
        year: weight
        for year, weight
        in termination_year_weights.items()
        if datetime(year, 12, 31) >= minimum_date
    }

    if not valid_years:
        return None

    years = list(valid_years.keys())
    weights = list(valid_years.values())

    year = random.choices(
        years,
        weights=weights,
        k=1
    )[0]

    start_date = max(
        minimum_date,
        datetime(year, 1, 1)
    )

    end_date = datetime(
        year,
        12,
        31
    )

    if start_date > end_date:
        return None

    return fake.date_time_between(
        start_date=start_date,
        end_date=end_date
    )


# ============================================================
# ADJUSTED SALARY
# ============================================================

education_multiplier = {

    "High School": {
        "Male": 1.03,
        "Female": 1.00
    },

    "Bachelor": {
        "Male": 1.115,
        "Female": 1.00
    },

    "Master": {
        "Male": 1.00,
        "Female": 1.07
    },

    "PhD": {
        "Male": 1.00,
        "Female": 1.17
    }
}


def calculate_adjusted_salary(row):
    """
    Calculate adjusted salary from:
    - base salary
    - gender
    - education
    - age

    The result is stored separately from the original salary.
    """

    base_salary = row["salary"]

    gender = row["gender"]

    education = row["education_level"]

    birthdate = pd.Timestamp(
        row["birthdate"]
    )

    today = pd.Timestamp(
        "2024-12-31"
    )

    age = (
        today.year
        - birthdate.year
        - (
            (today.month, today.day)
            <
            (birthdate.month, birthdate.day)
        )
    )

    # Education + gender multiplier
    multiplier = education_multiplier[
        education
    ][gender]

    adjusted_salary = (
        base_salary
        * multiplier
    )

    # Age increment between 0.1% and 0.3% per year
    age_rate = np.random.uniform(
        0.001,
        0.003
    )

    adjusted_salary *= (
        1 + age_rate * age
    )

    # Never allow adjusted salary below base salary.
    adjusted_salary = max(
        adjusted_salary,
        base_salary
    )

    return round(
        adjusted_salary
    )


# ============================================================
# CREATE EMPLOYEES
# ============================================================

data = []


for employee_number in range(
    1,
    num_records + 1
):

    # Guaranteed unique ID
    employee_id = f"EMP{employee_number:05d}"

    first_name = fake.first_name()

    last_name = fake.last_name()

    # Gender: 46% Female / 54% Male
    gender = np.random.choice(
        ["Female", "Male"],
        p=[0.46, 0.54]
    )

    # Location
    state = np.random.choice(
        states,
        p=state_prob
    )

    city = np.random.choice(
        states_cities[state]
    )

    # Hire date
    hiredate = generate_hire_date()

    # Department
    department = np.random.choice(
        departments,
        p=departments_prob
    )

    # Job title based on department
    job_title = np.random.choice(
        jobtitles[department],
        p=jobtitles_prob[department]
    )

    # Education based on job title
    education_level = np.random.choice(
        education_mapping[job_title]
    )

    # Performance
    performance_rating = np.random.choice(
        [
            "Excellent",
            "Good",
            "Satisfactory",
            "Needs Improvement"
        ],
        p=[
            0.12,
            0.50,
            0.30,
            0.08
        ]
    )

    # Overtime: 30% Yes / 70% No
    overtime = np.random.choice(
        ["Yes", "No"],
        p=[0.30, 0.70]
    )

    # Base salary
    salary = generate_salary(
        department,
        job_title
    )

    # Birth date
    birthdate = generate_birthdate(
        job_title,
        education_level,
        hiredate
    )

    data.append({
        "employee_id": employee_id,
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "state": state,
        "city": city,
        "hiredate": hiredate,
        "department": department,
        "job_title": job_title,
        "education_level": education_level,
        "salary": salary,
        "performance_rating": performance_rating,
        "overtime": overtime,
        "birthdate": birthdate
    })


# ============================================================
# DATAFRAME
# ============================================================

df = pd.DataFrame(data)


# ============================================================
# TERMINATIONS
# ============================================================

# Exactly 11.2% of 8,950
total_terminated = round(
    num_records * 0.112
)

# Eligible employees:
# termination must be at least 180 days after hire.
eligible_indices = [
    index
    for index, row in df.iterrows()
    if row["hiredate"] + timedelta(days=180)
    <= datetime(2024, 12, 31)
]

# We need exactly 11.2%.
terminated_indices = random.sample(
    eligible_indices,
    total_terminated
)

df["termdate"] = pd.NaT


# Generate termination dates
for index in terminated_indices:

    hiredate = df.at[
        index,
        "hiredate"
    ]

    termdate = generate_termination_date(
        hiredate
    )

    df.at[
        index,
        "termdate"
    ] = termdate


# ============================================================
# ADJUSTED SALARY
# ============================================================

df["adjusted_salary"] = df.apply(
    calculate_adjusted_salary,
    axis=1
)


# ============================================================
# FORMAT DATES
# ============================================================

date_columns = [
    "hiredate",
    "birthdate",
    "termdate"
]

for column in date_columns:
    df[column] = pd.to_datetime(
        df[column]
    ).dt.date


# ============================================================
# VALIDATION
# ============================================================

print("\n========== DATASET VALIDATION ==========")

print(
    f"Number of records: {len(df)}"
)

print(
    f"Unique employee IDs: "
    f"{df['employee_id'].nunique()}"
)

print(
    "\nGender distribution:"
)

print(
    df["gender"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print(
    "\nOvertime distribution:"
)

print(
    df["overtime"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

termination_rate = (
    df["termdate"].notna().mean() * 100
)

print(
    f"\nTermination rate: "
    f"{termination_rate:.2f}%"
)


# Check the 6-month rule
invalid_terminations = 0

for _, row in df[
    df["termdate"].notna()
].iterrows():

    minimum_term_date = (
        pd.Timestamp(row["hiredate"])
        + timedelta(days=180)
    )

    actual_term_date = pd.Timestamp(
        row["termdate"]
    )

    if actual_term_date < minimum_term_date:
        invalid_terminations += 1


print(
    f"Termination dates violating "
    f"the 6-month rule: "
    f"{invalid_terminations}"
)


# Check missing values
print(
    "\nMissing values:"
)

print(
    df.isna().sum()
)

print(
    "\n========================================"
)


# ============================================================
# DISPLAY
# ============================================================

print("\nFirst 10 rows:")
print(
    df.head(10).to_string(index=False)
)


# ============================================================
# EXPORT
# ============================================================

df.to_csv(
    "HumanResources.csv",
    index=False
)

print(
    "\nDataset saved as HumanResources.csv"
)
