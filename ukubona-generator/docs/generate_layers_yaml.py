import random
from datetime import datetime, timedelta
import yaml

# Seed for consistency
random.seed(42)

# Define roles, scopes, names, and templates
roles = ["Engineer", "Data Scientist", "Analyst", "Designer", "QA Lead", "Legal Counsel",
         "Executive", "Compliance Officer", "Educator", "Community", "People Ops", "Researcher"]
scopes = ["Tactical", "Operational", "Informational", "Strategic", "Existential"]
names = ["Priya Patel", "Isaac Huang", "Fatima Khaled", "Jayden Brooks", "Sofia Martins",
         "Tomás Ngugi", "Dr. Lena Moreno", "Raul Tanaka", "Helena Dube", "Eli Schwartz",
         "Hugo Müller", "Liyana Shaikh", "Santiago Lee", "Mei-Lin Cho", "Tara Okonkwo",
         "Diego Moretti", "Ava Johnson", "Ben Nakamura", "Noah Kim", "Miriam Zafar",
         "Layla Nasser", "Markus Feldman", "Nia Roberts", "Arjun Desai", "Zoë Tremblay"]
task_templates = [
    "Update {} module", "Draft proposal for {}", "Run QA tests on {}",
    "Review {} documentation", "Refactor {} system", "Plan {} initiative",
    "Conduct {} audit", "Design {} workflow", "Deploy {} patch", "Simulate {} model"
]
layers_info = {
    "synaptic": "#8e44ad",
    "axonal": "#2980b9",
    "symbolic": "#16a085",
    "existential": "#c0392b",
    "regulatory": "#f39c12",
    "commons": "#2ecc71"
}

def random_task():
    today = datetime.today()
    delta = random.randint(-5, 30)
    deadline = today + timedelta(days=delta)
    if delta < 0:
        status = "overdue"
        remaining = f"{abs(delta)} days ago"
    elif delta == 0:
        status = "due today"
        remaining = "today"
    else:
        status = "pending"
        remaining = f"{delta} days"

    scope = random.choice(scopes)
    role = random.choice(roles)
    owner = random.choice(names)
    title = random.choice(task_templates).format(scope.lower())
    description = f"{title} for {role.lower()} in {scope.lower()} scope."

    return {
        "title": title,
        "description": description,
        "deadline": deadline.strftime("%Y-%m-%d"),
        "status": status,
        "remaining": remaining,
        "owner": owner,
        "role": role,
        "scope": scope
    }

# Build the full YAML data
data = {"layers": {}}
for layer, color in layers_info.items():
    tasks = [random_task() for _ in range(random.randint(2, 5))]
    tasks.sort(key=lambda x: x["deadline"])
    data["layers"][layer] = {
        "name": layer.capitalize(),
        "color": color,
        "tasks": tasks
    }

# Write to file
with open("layers.yml", "w") as f:
    yaml.dump(data, f, sort_keys=False)

print("✅ Generated: layers.yml")

