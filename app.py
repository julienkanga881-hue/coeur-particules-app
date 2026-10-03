import streamlit as st

st.set_page_config(page_title="Cœur Particules Lumineuses", page_icon="💙", layout="centered")

st.title("💙 Animation de Cœur en Particules")
st.caption("Une magnifique animation interactive inspirée du code web !")

# Code HTML/JS intégré dans Streamlit via un composant HTML
heart_html = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cœur Particules</title>
    <style>
        body {
            margin: 0;
            background-color: #050505;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        canvas {
            display: block;
        }
    </style>
</head>
<body>
    <canvas id="heartCanvas"></canvas>

    <script>
        const canvas = document.getElementById('heartCanvas');
        const ctx = canvas.getContext('2d');

        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        const particles = [];
        const numParticles = 300;

        // Fonction mathématique pour tracer la forme d'un cœur
        function getHeartPoint(t) {
            let x = 16 * Math.pow(Math.sin(t), 3);
            let y = -(13 * Math.cos(t) - 5 * Math.cos(2*t) - 2 * Math.cos(3*t) - Math.cos(4*t));
            return { x: x * 15, y: y * 15 };
        }

        class Particle {
            constructor() {
                this.init();
            }
            init() {
                let t = Math.random() * Math.PI * 2;
                let p = getHeartPoint(t);
                this.x = canvas.width / 2 + p.x + (Math.random() - 0.5) * 20;
                this.y = canvas.height / 2 + p.y + (Math.random() - 0.5) * 20;
                this.size = Math.random() * 2 + 1;
                this.speedX = (Math.random() - 0.5) * 1.5;
                this.speedY = (Math.random() - 0.5) * 1.5;
                this.color = Math.random() > 0.5 ? '#00f2fe' : '#4facfe';
                this.alpha = Math.random();
            }
            update() {
                this.x += this.speedX;
                this.y += this.speedY;
                this.alpha -= 0.005;
                if (this.alpha <= 0) {
                    this.init();
                }
            }
            draw() {
                ctx.save();
                ctx.globalAlpha = Math.max(this.alpha, 0);
                ctx.fillStyle = this.color;
                ctx.shadowBlur = 10;
                ctx.shadowColor = '#00f2fe';
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fill();
                ctx.restore();
            }
        }

        for (let i = 0; i < numParticles; i++) {
            particles.push(new Particle());
        }

        function animate() {
            ctx.fillStyle = 'rgba(5, 5, 5, 0.2)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            particles.forEach(particle => {
                particle.update();
                particle.draw();
            });

            requestAnimationFrame(animate);
        }

        animate();

        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        });
    </script>
</body>
</html>
"""

# Affichage du composant dans l'application Streamlit
st.components.v1.html(heart_html, height=600, scrolling=False)
