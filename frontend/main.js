fetch('http://localhost:5000/api/hello')
    .then(res => res.json())
    .then(data => {
        document.getElementById('message').innerText = data.message;
    })
    .catch(() => {
        document.getElementById('message').innerText = 'Cannot reach backend';
    });
