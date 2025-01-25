// Animation pour les images au survol
const images = document.querySelectorAll('.photo-container img');
images.forEach(img => {
    img.addEventListener('mouseover', () => {
        img.style.transform = 'scale(1.1)';
    });

    img.addEventListener('mouseout', () => {
        img.style.transform = 'scale(1)';
    });
});
