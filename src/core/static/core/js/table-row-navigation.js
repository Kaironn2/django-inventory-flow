function activateTableRowNavigation() {
    const rows = document.querySelectorAll('tr[data-href]');

    rows.forEach(row => {
        row.addEventListener('click', () => {
            const url = row.getAttribute('data-href');
            window.location.href = url;
        });
    });
}

document.addEventListener('DOMContentLoaded', activateTableRowNavigation);

document.body.addEventListener('htmx:afterSwap', (e) => {
    activateTableRowNavigation();
    lucide.createIcons();
});
