// Smooth scroll to features section
document.querySelector('.cta-btn').addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector('.features');
    target.scrollIntoView({ behavior: 'smooth' });
});
