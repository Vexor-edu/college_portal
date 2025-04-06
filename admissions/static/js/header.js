window.addEventListener('scroll', function () {
    const header = document.querySelector('.site-header');
    header.classList.toggle('sticky', window.scrollY > 0);
});
