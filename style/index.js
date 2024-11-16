const scrollImages = document.querySelector('.scroll-images');

// Lorsque l'animation arrive à la fin, déplacer l'élément pour créer un effet continu.
scrollImages.addEventListener('animationiteration', () => {
    // Déplace les images d'un coup pour simuler un retour fluide
    const firstImage = scrollImages.querySelector('img');
    scrollImages.appendChild(firstImage); // Déplace la première image à la fin
});
