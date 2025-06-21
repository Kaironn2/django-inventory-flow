document.addEventListener('DOMContentLoaded', function() {
    const ctxDailySales = document.getElementById('dailySalesChart').getContext('2d')
    const dailySalesChart = new Chart(ctxDailySales, {
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
                    beginAtZero: true,
                    ticks: {
                        color: '#FFF'
                    }
                },
                x: {
                    ticks: {
                        color: '#FFF',
                        callback: function(value, index, ticks) {
                            const raw = this.getLabelForValue(value);
                            const date = new Date(raw);
                            return date.toLocaleDateString('pt-BR')
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    labels: {
                        color: '#FFF'
                    }
                },
                title: {
                    color: '#FFF'
                }
            }
        }
    });

    const ctxDailySalesQuantity = document.getElementById('dailySalesQuantityChart').getContext('2d')
    const dailySalesQuantityChart = new Chart(ctxDailySalesQuantity, {
        type: 'bar',
        data: {
            labels: dailySalesQuantityData.dates,
            datasets: [{
                label: 'Quantidade de Vendas',
                data: dailySalesQuantityData.values,
                backgroundColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        color: '#FFF'
                    }
                },
                x: {
                    ticks: {
                        color: '#FFF',
                        callback: function(value, index, ticks) {
                            const raw = this.getLabelForValue(value);
                            const date = new Date(raw);
                            return date.toLocaleDateString('pt-BR')
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    labels: {
                        color: '#FFF'
                    },
                },
                title: {
                    color: '#FFF'
                }
            }
        }
    });

    const ctxCategory = document.getElementById('productByCategoryChart').getContext('2d')
    const productByCategoryChart = new Chart(ctxCategory, {
        type: 'doughnut',
        data: {
            labels: Object.keys(productByCategoryData),
            datasets: [{
                data: Object.values(productByCategoryData),
                borderWidth: 1
            }]
        },
        options: {
            plugins: {
                legend: {
                    display: false,
                    labels: {
                        color: '#FFF'
                    }
                },
                title: {
                    color: '#FFF'
                }
            }
        }
    });

    const ctxBrand = document.getElementById('productByBrandChart').getContext('2d')
    const productByBrandChart = new Chart(ctxBrand, {
        type: 'doughnut',
        data: {
            labels: Object.keys(productByBrandData),
            datasets: [{
                labels: Object.keys(productByBrandData),
                borderWidth: 1
            }]
        },
        options: {
            plugins: {
                legend: {
                    display: false,
                    labels: {
                        color: '#FFF'
                    }
                },
                title: {
                    color: '#FFF'
                }
            }
        }
    })

})
