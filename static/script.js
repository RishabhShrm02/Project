document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('uploadForm');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(form);

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                resultDiv.textContent = `Upload successful: ${data.message}`;
            } else {
                resultDiv.textContent = `Error: ${data.error}`;
            }
        })
        .catch(error => {
            resultDiv.textContent = `Error: ${error.message}`;
        });
    });
});
