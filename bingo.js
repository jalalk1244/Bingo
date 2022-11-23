
 const options = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        "answer":"Table 14 with the score: 1533",
        "name":"Jalaluddin Khalid"
     })
 };

fetch('https://customer-api.krea.se/coding-tests/api/squid-game', options)
.then(results => {
    if (results.ok) {
        console.log('SUCCESS')
    } else {
        console.log('FAILED')
    }
})
.then(data => console.log(data))
.catch(error => console.log('ERROR'));