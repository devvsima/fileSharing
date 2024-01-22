document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.getElementById('toggleTheme');
    const body = document.body;

    toggleButton.addEventListener('click', function () {
        body.classList.toggle('dark-theme');
    });
});
