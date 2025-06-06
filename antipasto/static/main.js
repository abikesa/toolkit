function loadTasks() {
  fetch('/api/tasks')
    .then(res => res.json())
    .then(data => {
      const out = data.map(t => `<div class="card">
        <h3>${t.title}</h3>
        <p>Role: ${t.role}</p>
        <p>Layer: ${t.layer}</p>
        <p>Status: ${t.status}</p>
        <p>Due: ${t.deadline}</p>
      </div>`).join('');
      document.getElementById("output").innerHTML = out;
    });
}

function loadRoles() {
  fetch('/api/roles')
    .then(res => res.json())
    .then(data => {
      const out = data.map(r => `<div class="card">
        <h3>${r.name}</h3>
        <p>Responsibilities: ${r.responsibilities.join(', ')}</p>
      </div>`).join('');
      document.getElementById("output").innerHTML = out;
    });
}

function loadLayers() {
  fetch('/api/layers')
    .then(res => res.json())
    .then(data => {
      const out = data.map(l => `<div class="card">
        <h3>${l.name}</h3>
        <p>Scope: ${l.scope}</p>
        <p>Color: ${l.color}</p>
      </div>`).join('');
      document.getElementById("output").innerHTML = out;
    });
}

