document.getElementById('reviewForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var reviewText = document.getElementById('review').value;
    
    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
            'review': reviewText
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').textContent = 'Sentiment: ' + data.sentiment;
    });
});
