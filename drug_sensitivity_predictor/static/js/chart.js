const ctx = document.getElementById('ic50Chart').getContext('2d');
const chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Predicted IC50'],
        datasets: [{
            label: 'IC50 Value',
            data: [0],  // Replace with actual IC50 value dynamically
            backgroundColor: ['rgba(54, 162, 235, 0.6)'],
            borderColor: ['rgba(54, 162, 235, 1)'],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
