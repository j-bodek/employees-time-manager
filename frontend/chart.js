let charts = document.querySelectorAll('.myChart')
charts.forEach(chart => {
    let ctx = chart.getContext('2d');

    let delayed;
    let myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['E01', 'E02', 'E03', 'E04', 'E05', 'E06', 'E07', 'E08', 'E09', 'E10'],
            datasets: [{
                    label: '# of Votes1',
                    data: [12, 19, 3, 5, 2, 3, 12, 53, 64, 12],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.6)',
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                    ],
                    borderWidth: 1
                },
                {
                    label: '# of Votes2',
                    data: [10, 17, 2, 1, 5, 1, 21, 42, 12, 7],
                    backgroundColor: [
                        'rgba(75, 192, 192, 0.6)',
                    ],
                    borderColor: [
                        'rgba(54, 162, 235, 1)',
                    ],
                    borderWidth: 1
                },
            ]
        },
        options: {
            animation: {
                onComplete: () => {
                    delayed = true;
                },
                delay: (context) => {
                    let delay = 0;
                    if (context.type === 'data' && context.mode === 'default' && !delayed) {
                        delay = context.dataIndex * 300 + context.datasetIndex * 100;
                    }
                    return delay;
                },
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Poniedziałek'
                },
            },
            responsive: true,
            scales: {
                x: {
                    stacked: true,
                },
                y: {
                    stacked: true
                }
            }
        }
    });
})