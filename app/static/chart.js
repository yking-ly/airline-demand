window.renderChart = function (data) {
    const ctx = document.getElementById('priceChart').getContext('2d');

    const chartData = {
        labels: data.map((d, i) => `Offer ${i + 1}`),
        datasets: [{
            label: 'Price ($)',
            data: data.map(d => d.price),
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgb(54, 162, 235)',
            borderWidth: 2,
            fill: true,
            tension: 0.3
        }]
    };

    new Chart(ctx, {
        type: 'line',
        data: chartData,
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: false
                }
            }
        }
    });
};
