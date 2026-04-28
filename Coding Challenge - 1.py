# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
# Store in variable: services
# Example: services = {"Web Development": 150, "Data Analysis": 175, ...}
# Include at least 5 different services
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cloud Consulting": 220,
    "Cybersecurity": 250,
    "IT Support": 95
}

# TODO 2: Create customer dictionaries
# Each customer should have: company_name, contact_person, email, phone
# Create at least 4 customer dictionaries
# Example: customer1 = {"company_name": "ABC Corp", "contact_person": "John Smith", ...}
customer1 = {
    "company_name": "NexaSoft Inc",
    "contact_person": "Sarah Johnson",
    "email": "sarah@nexasoft.com",
    "phone": "555-1001"
}

customer2 = {
    "company_name": "BlueWave Systems",
    "contact_person": "Michael Chen",
    "email": "michael@bluewave.com",
    "phone": "555-1002"
}

customer3 = {
    "company_name": "Vertex Dynamics",
    "contact_person": "Alicia Brown",
    "email": "alicia@vertex.com",
    "phone": "555-1003"
}

customer4 = {
    "company_name": "Summit Tech Group",
    "contact_person": "David Lee",
    "email": "david@summittech.com",
    "phone": "555-1004"
}

# TODO 3: Create a master customers dictionary
# Store in variable: customers
# Use customer IDs as keys and customer dictionaries as values
# Example: customers = {"C001": customer1, "C002": customer2, ...}
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
# Add your code here to display all customer information
for customer_id, info in customers.items():
    print(f"{customer_id}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
    print()

# TODO 5: Look up specific customers
# Use dictionary access to:
# - Get and display customer C002's information (store in c002_info)
# - Get and display customer C003's contact person (store in c003_contact)
# - Try to get customer C999 (doesn't exist) using .get() with a default message (store in c999_info)
c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print("\n\nCustomer Lookups:")
print("-" * 60)
# Add your code here
print("C002 Info:", c002_info)
print("C003 Contact Person:", c003_contact)
print("C999 Lookup:", c999_info)

# TODO 6: Update customer information
# - Change customer C001's phone number
# - Add a new field "industry" to customer C002
# - Display the updated customer information
customers["C001"]["phone"] = "555-9001"
customers["C002"]["industry"] = "Finance"

print("\n\nUpdating Customer Information:")
print("-" * 60)
# Add your code here
print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])

# TODO 7: Create project dictionaries for each customer
# Each project: {"name": "Project Name", "service": "Service Type", "hours": X, "budget": Y}
# Create a projects dictionary where customer IDs map to lists of projects
# Store in variable: projects
# Example: projects = {"C001": [project1, project2], "C002": [project3], ...}
project1 = {
    "name": "Website Redesign",
    "service": "Web Development",
    "hours": 120,
    "budget": 18000
}

project2 = {
    "name": "Security Audit",
    "service": "Cybersecurity",
    "hours": 60,
    "budget": 15000
}

project3 = {
    "name": "Sales Dashboard",
    "service": "Data Analysis",
    "hours": 90,
    "budget": 16000
}

project4 = {
    "name": "Cloud Migration",
    "service": "Cloud Consulting",
    "hours": 110,
    "budget": 25000
}

project5 = {
    "name": "Help Desk Setup",
    "service": "IT Support",
    "hours": 80,
    "budget": 7600
}

projects = {
    "C001": [project1, project2],
    "C002": [project3],
    "C003": [project4, project5],
    "C004": []
}

print("\n\nProject Information:")
print("-" * 60)
# Add your code here
for customer_id, project_list in projects.items():
    print(f"{customer_id}:")
    if project_list:
        for project in project_list:
            print(f"  {project}")
    else:
        print("  No projects assigned")
    print()

# TODO 8: Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost

print("\n\nProject Cost Calculations:")
print("-" * 60)
# Add your code here
for customer_id, project_list in projects.items():
    for project in project_list:
        rate = services[project["service"]]
        cost = rate * project["hours"]
        print(
            f"{customer_id} - {project['name']} | "
            f"Service: {project['service']} | "
            f"Hours: {project['hours']} | "
            f"Calculated Cost: ${cost:,.2f}"
        )

# TODO 9: Customer statistics using dictionary methods
# Display:
# - All customer IDs using .keys()
# - All customer companies using .values() and extracting company names
# - Count of total customers using len()

print("\n\nCustomer Statistics:")
print("-" * 60)
# Add your code here
customer_ids = list(customers.keys())
customer_companies = [customer["company_name"] for customer in customers.values()]
total_customers = len(customers)

print("Customer IDs:", customer_ids)
print("Customer Companies:", customer_companies)
print("Total Customers:", total_customers)

# TODO 10: Service usage analysis
# Create a dictionary that counts how many projects use each service
# Store in variable: service_counts
# Display the service usage counts
service_counts = {}

for project_list in projects.values():
    for project in project_list:
        service_name = project["service"]
        service_counts[service_name] = service_counts.get(service_name, 0) + 1

print("\n\nService Usage Analysis:")
print("-" * 60)
# Add your code here
for service, count in service_counts.items():
    print(f"{service}: {count}")

# TODO 11: Financial aggregations
# Calculate and display:
# - Total hours across all projects (store in total_hours)
# - Total budget across all projects (store in total_budget)
# - Average project budget (store in avg_budget)
# - Most expensive and least expensive projects (store in max_budget, min_budget)
all_projects = []
for project_list in projects.values():
    all_projects.extend(project_list)

total_hours = sum(project["hours"] for project in all_projects)
total_budget = sum(project["budget"] for project in all_projects)
avg_budget = total_budget / len(all_projects) if all_projects else 0
max_budget = max(project["budget"] for project in all_projects) if all_projects else 0
min_budget = min(project["budget"] for project in all_projects) if all_projects else 0

print("\n\nFinancial Summary:")
print("-" * 60)
# Add your code here
print("Total Hours:", total_hours)
print("Total Budget:", total_budget)
print("Average Project Budget:", avg_budget)
print("Highest Project Budget:", max_budget)
print("Lowest Project Budget:", min_budget)

# TODO 12: Customer summary report
# For each customer, show:
# - Customer details
# - Number of projects
# - Total hours
# - Total budget

print("\n\nCustomer Summary Report:")
print("-" * 60)
# Add your code here
for customer_id, info in customers.items():
    customer_projects = projects.get(customer_id, [])
    customer_total_hours = sum(project["hours"] for project in customer_projects)
    customer_total_budget = sum(project["budget"] for project in customer_projects)

    print(f"{customer_id} - {info['company_name']}")
    print(f"  Contact Person: {info['contact_person']}")
    print(f"  Email: {info['email']}")
    print(f"  Phone: {info['phone']}")
    print(f"  Number of Projects: {len(customer_projects)}")
    print(f"  Total Hours: {customer_total_hours}")
    print(f"  Total Budget: ${customer_total_budget:,.2f}")
    print()

# TODO 13: Create rate adjustments using dictionary comprehension
# Create a new dictionary with all service rates increased by 10%
# Store in variable: adjusted_rates
# Use dictionary comprehension: adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}
adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
# Add your code here
for service, rate in adjusted_rates.items():
    print(f"{service}: ${rate:,.2f}")

# TODO 14: Filter customers using dictionary comprehension
# Create a dictionary of only customers who have projects
# Store in variable: active_customers
# Hint: Use the projects dictionary to check which customers have projects
active_customers = {
    customer_id: info
    for customer_id, info in customers.items()
    if len(projects.get(customer_id, [])) > 0
}

print("\n\nActive Customers (with projects):")
print("-" * 60)
# Add your code here
for customer_id, info in active_customers.items():
    print(f"{customer_id}: {info['company_name']}")

# TODO 15: Create project summaries using dictionary comprehension
# Create a dictionary mapping customer IDs to their total project budgets
# Store in variable: customer_budgets
# Example result: {"C001": 25000, "C002": 15000, ...}
customer_budgets = {
    customer_id: sum(project["budget"] for project in project_list)
    for customer_id, project_list in projects.items()
}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
# Add your code here
for customer_id, budget in customer_budgets.items():
    print(f"{customer_id}: ${budget:,.2f}")

# TODO 16: Service pricing tiers using dictionary comprehension
# Create a dictionary categorizing services as "Premium" (>= 200), "Standard" (100-199), or "Basic" (< 100)
# Store in variable: service_tiers
# Use conditional expressions in the comprehension
service_tiers = {
    service: "Premium" if rate >= 200 else "Standard" if rate >= 100 else "Basic"
    for service, rate in services.items()
}

print("\n\nService Pricing Tiers:")
print("-" * 60)
# Add your code here
for service, tier in service_tiers.items():
    print(f"{service}: {tier}")

# TODO 17: Customer validation function
# Create a function validate_customer(customer_dict) that:
# - Checks if all required fields are present (company_name, contact_person, email, phone)
# - Returns True if valid, False otherwise
# - Use conditional logic to verify each field
# Test it on all customers and report results
def validate_customer(customer_dict):
    required_fields = ["company_name", "contact_person", "email", "phone"]
    for field in required_fields:
        if field not in customer_dict or customer_dict[field] == "":
            return False
    return True

print("\n\nCustomer Validation:")
print("-" * 60)
# Add your code here
for customer_id, info in customers.items():
    print(f"{customer_id}: {validate_customer(info)}")

# TODO 18: Project status tracking with loops and conditionals
# Add a "status" field to each project ("active", "completed", "pending")
# Use a loop to count projects by status
# Store counts in status_counts dictionary
# Display a summary of project statuses
status_sequence = {
    "C001": ["active", "completed"],
    "C002": ["pending"],
    "C003": ["active", "completed"],
    "C004": []
}

for customer_id, project_list in projects.items():
    for index, project in enumerate(project_list):
        project["status"] = status_sequence[customer_id][index]

status_counts = {}

for project_list in projects.values():
    for project in project_list:
        status = project["status"]
        status_counts[status] = status_counts.get(status, 0) + 1

print("\n\nProject Status Summary:")
print("-" * 60)
# Add your code here
for status, count in status_counts.items():
    print(f"{status}: {count}")

# TODO 19: Budget analysis function with aggregation
# Create a function analyze_customer_budgets(projects_dict) that:
# - Takes the projects dictionary as input
# - Uses loops to calculate total and average budget per customer
# - Returns a dictionary with customer IDs as keys and budget stats as values
# - Each value should be a dict with 'total', 'average', and 'count' keys
def analyze_customer_budgets(projects_dict):
    results = {}

    for customer_id, project_list in projects_dict.items():
        total = 0
        count = 0

        for project in project_list:
            total += project["budget"]
            count += 1

        average = total / count if count > 0 else 0

        results[customer_id] = {
            "total": total,
            "average": average,
            "count": count
        }

    return results

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
# Add your code here
budget_analysis = analyze_customer_budgets(projects)
for customer_id, stats in budget_analysis.items():
    print(f"{customer_id}: {stats}")

# TODO 20: Service recommendation system
# Create a function recommend_services(customer_id, customers, projects, services) that:
# - Analyzes the customer's past projects
# - Identifies services they haven't used yet
# - Returns a list of recommended services based on their budget range
# - Use loops, conditionals, and dictionary operations
def recommend_services(customer_id, customers, projects, services):
    if customer_id not in customers:
        return []

    customer_projects = projects.get(customer_id, [])
    used_services = set()
    total_budget_customer = 0

    for project in customer_projects:
        used_services.add(project["service"])
        total_budget_customer += project["budget"]

    avg_customer_budget = (
        total_budget_customer / len(customer_projects)
        if len(customer_projects) > 0 else 0
    )

    recommendations_list = []

    for service, rate in services.items():
        if service not in used_services:
            if avg_customer_budget >= 20000 and rate >= 150:
                recommendations_list.append(service)
            elif 10000 <= avg_customer_budget < 20000 and 100 <= rate <= 220:
                recommendations_list.append(service)
            elif avg_customer_budget < 10000 and rate < 200:
                recommendations_list.append(service)

    # If the customer has no projects yet, recommend all standard/basic services
    if len(customer_projects) == 0:
        recommendations_list = [
            service for service, rate in services.items() if rate <= 200
        ]

    return recommendations_list

recommendations = {}
for customer_id in customers.keys():
    recommendations[customer_id] = recommend_services(
        customer_id, customers, projects, services
    )

print("\n\nService Recommendations:")
print("-" * 60)
# Add your code here
for customer_id, recs in recommendations.items():
    print(f"{customer_id}: {recs}")