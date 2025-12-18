fetch('http://shindie.id.vn/backend/server.py/api/hello')
    .then(res => res.json())
    .then(data => {
        document.getElementById('message').innerText = data.message;
    })
    .catch(() => {
        document.getElementById('message').innerText = 'Cannot reach backend';
    });
