// Vortex Bounce - Full Version
const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
const scoreElement = document.getElementById("score");

// Game State
const ball = { 
    x: 400, 
    y: 400, 
    vx: Math.random() * 6 - 3,  // Random initial velocity
    vy: Math.random() * 6 - 3,
    radius: 20 
};
let squareAngle = 0;
let score = 0;
let isGameOver = false;

// Colors
const COLORS = {
    background: "#0a0a1e",
    square: "#64c8ff",
    ball: "#ffd700",
    text: "#ffffff"
};

// Input Handling
let keys = {};
document.addEventListener("keydown", (e) => keys[e.key] = true);
document.addEventListener("keyup", (e) => keys[e.key] = false);

// Game Loop
function update(deltaTime) {
    if (isGameOver) return;

    // Rotate square based on arrow keys
    if (keys["ArrowLeft"]) squareAngle -= deltaTime * 120; // 120° per second
    if (keys["ArrowRight"]) squareAngle += deltaTime * 120;

    // Move ball
    ball.x += ball.vx;
    ball.y += ball.vy;

    // Boundary collisions (rotated square)
    const buffer = ball.radius + 5;
    const distance = Math.sqrt(
        Math.pow(ball.x - 400, 2) + 
        Math.pow(ball.y - 400, 2)
    );

    if (distance > 200 - buffer) {
        // Bounce effect
        const angle = Math.atan2(ball.y - 400, ball.x - 400);
        ball.vx = Math.cos(angle) * -5;
        ball.vy = Math.sin(angle) * -5;
        score += 10;
        scoreElement.textContent = `Score: ${score}`;
    }

    // Game over if ball escapes
    if (ball.x < -100 || ball.x > 900 || ball.y < -100 || ball.y > 900) {
        isGameOver = true;
        alert(`Game Over! Final Score: ${score}\nRefresh to play again.`);
    }
}

function draw() {
    // Clear screen
    ctx.fillStyle = COLORS.background;
    ctx.fillRect(0, 0, 800, 800);

    // Draw rotating square
    ctx.strokeStyle = COLORS.square;
    ctx.lineWidth = 3;
    ctx.save();
    ctx.translate(400, 400);
    ctx.rotate((squareAngle * Math.PI) / 180);
    ctx.strokeRect(-200, -200, 400, 400);
    ctx.restore();

    // Draw ball
    ctx.fillStyle = COLORS.ball;
    ctx.beginPath();
    ctx.arc(ball.x, ball.y, ball.radius, 0, Math.PI * 2);
    ctx.fill();
}

// Frame rate independence
let lastTime = 0;
function loop(timestamp) {
    const deltaTime = (timestamp - lastTime) / 1000;
    lastTime = timestamp;
    update(deltaTime);
    draw();
    requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
