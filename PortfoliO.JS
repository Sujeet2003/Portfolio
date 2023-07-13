// Menu-Icon Toggle

let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('nav');

menuIcon.onclick = () =>{
    menuIcon.classList.toggle('bx-x');
    navbar.classList.toggle('active');
};

// Nav active section

let activePage = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('nav a');

window.onscroll = () => {
    activePage.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop - 200;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if(top >= offset && top < offset+height){
            navLinks.forEach(links =>{
                links.classList.remove('active');
                document.querySelector('nav a[href*=' + id + ']').classList.add('active');
            });
        };
    });
    menuIcon.classList.toggle('bx-x');
    navbar.classList.remove('active');
};

/* Animation of contents */
ScrollReveal({ 
    reset: true,
    distance: '80px',
    duration: 1000,
    delay: 100
});
ScrollReveal().reveal('.heading, .home-content, .about-content',{ origin: 'top' });
ScrollReveal().reveal('.home-content h1',{ origin: 'left' });
ScrollReveal().reveal('.home-content p',{ origin: 'right' });
// ScrollReveal().reveal('.home-img, .about-img,  .skills-content, .academics, .portfolio-container, form', { origin: 'bottom' });



// Typed JS
const typed = new Typed('.designation',{
    strings: ['Web developer', 'Web Designer', 'Frontend Developer'],
    typeSpeed: 100,
    backSpeed: 100,
    backDelay: 1000,
    loop: true
});
