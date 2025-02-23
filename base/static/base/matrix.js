const canvas = document.getElementById('matrix-bg');
const ctx = canvas.getContext('2d');

// Set canvas size to window size
const resizeCanvas = () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
};
resizeCanvas();
window.addEventListener('resize', resizeCanvas);

// Matrix characters (using a mix of characters for variety)
const chars = '01ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const charArray = chars.split('');

// Column setup
const fontSize = 50;
const columns = canvas.width / fontSize;
const drops = Array(Math.floor(columns)).fill(1);

// Draw the Matrix rain
function draw() {
    // Semi-transparent black to create fade effect
    ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Green text
    ctx.fillStyle = '#0F0';
    ctx.font = fontSize + 'px monospace';

    // Loop over drops
    for (let i = 0; i < drops.length; i++) {
        // Random character
        const char = charArray[Math.floor(Math.random() * charArray.length)];
        
        // Calculate position
        const x = i * fontSize;
        const y = drops[i] * fontSize;

        // Add glow effect
        ctx.shadowColor = '#0F0';
        ctx.shadowBlur = 10;
        
        // Draw the character
        ctx.fillText(char, x, y);

        // Reset when off screen or randomly
        if (y > canvas.height && Math.random() > 0.975) {
            drops[i] = 0;
        }

        // Move drop down
        drops[i]++;
    }
}

// Animate
setInterval(draw, 33); // Around 30 FPS