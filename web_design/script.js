fetch()
  .then(response => response.json())
  .then(data => {
    const tablebody = document.querySelector('tbody');
    data.forEach(person => {
        const tableRow = document.createElement('tr');
        const nameCell = document.createElement('td');
        nameCell.textContent = person.name;
        tableRow.appendChild(nameCell);

        const jobtitleCell = document.createElement('td');
        jobtitleCell.textContent = person.jobtitle;
        tableRow.appendChild(jobtitleCell);

        const skillsCell = document.createElement('td');
        skillsCell.textContent = person.skills.join(', ');
        tableRow.appendChild(skillsCell);

        tablebody.appendChild(tableRow);

    });
    });

