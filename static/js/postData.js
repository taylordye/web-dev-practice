function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.getElementById('submit-btn').addEventListener('click', (e) => {
    e.preventDefault();

    const csrftoken = getCookie('csrftoken')

    fetch("", {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'X-CSRFToken': csrftoken
        },

        body: JSON.stringify({'post_data': 'Some data 🤠'}),
    })
    .then(res => {
        return res.json()
    })
    .then(data => {
        console.log(data);
    })
    .catch(issue => {
        console.log(issue);
    })
})
