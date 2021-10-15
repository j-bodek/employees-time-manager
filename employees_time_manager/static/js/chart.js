let show_charts_btn = document.querySelector('#show_charts')

let display_charts = function (chart) {
    let ctx = chart.getContext('2d');

    day = chart.getAttribute("name");
    day_data = received_data[day]
    // subtract coresponding value in day_work from starting_day_work to get number of available minutes
    available_employees_time = Object.values(day_data['starting_day_work']).map((e, index) => e - Object.values(day_data['day_work'])[index])

    let delayed;
    let myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(day_data['day_work']),
            datasets: [{
                    label: 'Dostępny Czas',
                    data: available_employees_time,
                    backgroundColor: [
                        'rgba(237, 106, 94, 0.6)',
                    ],
                    borderColor: [
                        'rgba(237, 106, 94, 1)',
                    ],
                    borderWidth: 1
                },
                {
                    label: 'Potrzebny Czas',
                    data: Object.values(day_data['starting_day_work']),
                    backgroundColor: [
                        'rgba(23, 195, 178, 0.6)',
                    ],
                    borderColor: [
                        'rgba(23, 195, 178, 1)',
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
                    text: day
                },
            },
            responsive: true,
            scales: {
                // x: {
                //     stacked: true,
                // },
                // y: {
                //     stacked: true
                // }
            }
        }
    });
}


show_charts_btn.addEventListener('click', (e) => {
    checked_days = document.querySelectorAll('input[class=day]:checked');
    // display none all active charts
    active_charts = document.querySelectorAll('.myChart')
    active_charts.forEach(chart => {
        chart.style.display = 'none'
    })

    checked_days.forEach(day => {
        let chart = document.getElementById('myChart' + day.getAttribute("name"));
        chart.style.display = 'block'
        display_charts(chart)
    });
})