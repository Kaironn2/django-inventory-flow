document.addEventListener("DOMContentLoaded", function() {
    var dailySalesData = JSON.parse('{{ daily_sales_data|safe }}')
    console.log(dailySalesData)
    // var dailySalesQuantityData = JSON.parse('{{ daily_sales_quantity_data|safe }}');

    var ctxDailySales = document.getElementById('dailySalesChart').getContext('2d');
    var dailySalesChart = new Chart(ctxDailySales, {
    type: 'line',
    data: {
        labels: dailySalesData.dates,
        datasets: [{
        label: 'Valor em vendas',
        data: dailySalesData.values,
        fill: false,
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 2,
        tension: 0.5
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

    // var ctxDailySalesQuantity = document.getElementById('dailySalesQuantityChart').getContext('2d');
    // var dailySalesQuantityChart = new Chart(ctxDailySalesQuantity, {
    // type: 'bar',
    // data: {
    //     labels: dailySalesQuantityData.dates,
    //     datasets: [{
    //     label: 'Quantidade de Vendas',
    //     data: dailySalesQuantityData.values,
    //     backgroundColor: 'rgba(255, 99, 132, 0.6)',
    //     borderColor: 'rgba(255, 99, 132, 1)',
    //     borderWidth: 1
    //     }]
    // },
    // options: {
    //     scales: {
    //     y: {
    //         beginAtZero: true
    //     }
    //     }
    // }
    // });
});