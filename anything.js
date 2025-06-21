        document.addEventListener("DOMContentLoaded", function() {  
          var productCountByCategory = JSON.parse('{{ product_count_by_category|safe }}');
          var productCountByBrand = JSON.parse('{{ product_count_by_brand|safe }}');
    
          var ctxCategory = document.getElementById('productByCategoryChart').getContext('2d');
          var productByCategoryChart = new Chart(ctxCategory, {
            type: 'doughnut',
            data: {
              labels: Object.keys(productCountByCategory),
              datasets: [{
                data: Object.values(productCountByCategory),
                borderWidth: 1
              }]
            },
            options: {
              plugins: {
                legend: {
                  display: false
                },
              }
            }
          });
    
          var ctxBrand = document.getElementById('productByBrandChart').getContext('2d');
          var productByBrandChart = new Chart(ctxBrand, {
            type: 'doughnut',
            data: {
              labels: Object.keys(productCountByBrand),
              datasets: [{
                data: Object.values(productCountByBrand),
                borderWidth: 1
              }]
            },
            options: {
              plugins: {
                legend: {
                  display: false
                },
              }
            }
          });
        });