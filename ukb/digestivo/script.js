fetch('data/tasks.csv')
  .then(response => response.text())
  .then(text => {
    const rows = text.trim().split('\n').slice(1);
    const tbody = document.querySelector('#task-table tbody');
    const now = new Date();

    rows.forEach(row => {
      const [task, created, due, done] = row.split(',');
      const dueDate = new Date(due);
      let deltaText = '';
      let deltaClass = '';   

      if (!isNaN(dueDate)) {
        const diffMs = dueDate - now;
        const days = Math.ceil(diffMs / (1000 * 60 * 60 * 24));
        deltaText = days > 0 ? `in ${days}d` : `${-days}d ago`;
        deltaClass = done === 'true' ? 'done' : (days < 0 ? 'overdue' : 'upcoming');
      } else {
        deltaText = 'TBD';
        deltaClass = 'upcoming';
      }

      const rowEl = document.createElement('tr');
      const status = done === 'true' ? '✔' : '';
      rowEl.innerHTML = `
        <td class="${done === 'true' ? 'done' : ''}">${status}</td>
        <td>${task}</td>
        <td>${created}</td>
        <td>${due}</td>
        <td class="${deltaClass}">${deltaText}</td>
      `;
      tbody.appendChild(rowEl);
    });
  });
