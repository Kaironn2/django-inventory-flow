function openModal() {
    document.getElementById('modal').classList.remove('hidden');
}

function closeModal() {
    document.getElementById('modal').classList.add('hidden');
    document.getElementById('modal-content').innerHTML = '';
}

document.getElementById('modal').addEventListener('click', function (event) {
    if (event.target.id === 'modal') {
        closeModal();
    }
});

document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') {
        closeModal();
    }
});

document.body.addEventListener('htmx:afterRequest', function (e) {
    const targetId = e.detail.target.id;
    if (targetId === "category-table") {
        closeModal();
    }
});
