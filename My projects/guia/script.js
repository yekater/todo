window.addEventListener('load', () => {
    
    // --- ЧАСТИЦЫ ТРЕНКАДИС ---
    const canvas = document.getElementById('trencadis-canvas');
    const ctx = canvas.getContext('2d');
    let particles = [];
    const mouse = { x: -1000, y: -1000 };

    const colors = ['#E63946', '#A8DADC', '#457B9D', '#FFB703', '#2A9D8F']; 

    function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        init();
    }

    class Triangle {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 15 + 10;
            this.color = colors[Math.floor(Math.random() * colors.length)];
            this.baseX = this.x;
            this.baseY = this.y;
            this.density = (Math.random() * 30) + 1;
        }

        draw() {
            ctx.fillStyle = this.color;
            ctx.globalAlpha = 0.8;
            ctx.beginPath();
            ctx.moveTo(this.x, this.y);
            ctx.lineTo(this.x + this.size, this.y + this.size * 0.3);
            ctx.lineTo(this.x + this.size * 0.4, this.y + this.size * 1.1);
            ctx.closePath();
            ctx.fill();
        }

        update() {
            let dx = mouse.x - this.x;
            let dy = mouse.y - this.y;
            let distance = Math.sqrt(dx * dx + dy * dy);
            let maxDistance = 150;

            if (distance < maxDistance) {
                let force = (maxDistance - distance) / maxDistance;
                let directionX = (dx / distance) * force * this.density;
                let directionY = (dy / distance) * force * this.density;
                this.x -= directionX;
                this.y -= directionY;
            } else {
                if (this.x !== this.baseX) {
                    this.x -= (this.x - this.baseX) * 0.05;
                }
                if (this.y !== this.baseY) {
                    this.y -= (this.y - this.baseY) * 0.05;
                }
            }
        }
    }

    function init() {
        particles = [];
        let numberOfParticles = (canvas.width * canvas.height) / 12000;
        for (let i = 0; i < numberOfParticles; i++) {
            particles.push(new Triangle());
        }
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles.forEach(p => {
            p.update();
            p.draw();
        });
        requestAnimationFrame(animate);
    }

    window.addEventListener('mousemove', (e) => {
        mouse.x = e.x;
        mouse.y = e.y;
    });

    resize();
    animate();
    window.addEventListener('resize', resize);


    // --- АНИМАЦИЯ ПОЯВЛЕНИЯ ТЕКСТА ---
    const tl = gsap.timeline({ defaults: { ease: "power4.out", duration: 1.5 } });
    
    tl.from(".title", { y: 80, opacity: 0, delay: 0.2 })
      .from(".subtitle", { y: 40, opacity: 0 }, "-=1")
      .from(".hero-info", { opacity: 0 }, "-=0.8")
      .from(".btn", { y: 20, opacity: 0 }, "-=1")
      .from(".navbar", { y: -40, opacity: 0 }, "-=1.2");


    // --- СКРОЛЛ-АНИМАЦИЯ КАРТИНОК ---
    gsap.registerPlugin(ScrollTrigger);

    const slides = gsap.utils.toArray(".slide");
    
    const scrollTl = gsap.timeline({
        scrollTrigger: {
            trigger: ".scroll-slider",
            start: "top top",
            end: "bottom bottom",
            scrub: 1
        }
    });

    slides.forEach((slide, i) => {
        if (i === 0) return; // Первый слайд уже на месте

        scrollTl.to(slide, {
            onStart: () => gsap.set(slide, { visibility: "visible" }),
            opacity: 1,
            y: "0%",
            startAt: { y: "100%", opacity: 0 },
            duration: 1,
            ease: "power2.inOut"
        });
    });
});