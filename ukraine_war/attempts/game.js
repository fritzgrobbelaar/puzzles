// Constants
const TILE_SIZE = 32;
const MAP_WIDTH = 20;
const MAP_HEIGHT = 15;
const GAME_DURATION = 5 * 60; // 5 minutes

const UNIT_TYPES = {
    INFANTRY: 'infantry',
    SNIPER: 'sniper',
    HELICOPTER: 'helicopter'
};

const UNIT_STATS = {
    [UNIT_TYPES.INFANTRY]: { hp: 100, damage: 10, range: 3, speed: 2, color: '#0288D1' },
    [UNIT_TYPES.SNIPER]: { hp: 80, damage: 15, helicopterDamage: 30, range: 5, speed: 1.5, color: '#01579B' },
    [UNIT_TYPES.HELICOPTER]: { hp: 150, damage: 20, range: 4, speed: 3, color: '#C62828' }
};

const TILE_TYPES = {
    GRASS: 'grass',
    RUNWAY: 'runway',
    BUILDING: 'building'
};

// Canvas setup
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const gameInfo = document.getElementById('gameInfo');

// Game class
class Game {
    constructor() {
        this.map = new Map();
        this.units = [];
        this.selectedUnit = null;
        this.gameTime = 0;
        this.gameOver = false;
        this.runwayHealth = 100;
        this.decisionMade = false;
    }

    start() {
        this.units = [];
        this.selectedUnit = null;
        this.gameTime = 0;
        this.gameOver = false;
        this.runwayHealth = 100;
        this.decisionMade = false;
        this.spawnUnits();
        this.lastTime = performance.now();
        gameInfo.innerHTML = 'Defend the airport! Move units to the runway to destroy it or defeat all enemies. Sniper excels vs. helicopter!';
        requestAnimationFrame(this.gameLoop.bind(this));
    }

    spawnUnits() {
        // Ukrainian player units
        this.units.push(new Unit(15, 10, UNIT_TYPES.INFANTRY, 'ukrainian'));
        this.units.push(new Unit(14, 11, UNIT_TYPES.SNIPER, 'ukrainian'));
        this.units.push(new Unit(16, 9, UNIT_TYPES.INFANTRY, 'ukrainian'));
        this.units.push(new Unit(13, 12, UNIT_TYPES.INFANTRY, 'ukrainian'));
        // Russian enemies
        this.units.push(new Unit(5, 2, UNIT_TYPES.INFANTRY, 'russian'));
        this.units.push(new Unit(7, 2, UNIT_TYPES.INFANTRY, 'russian'));
        this.units.push(new Unit(6, 3, UNIT_TYPES.HELICOPTER, 'russian'));
    }

    gameLoop(time) {
        if (this.gameOver) return;
        const deltaTime = (time - this.lastTime) / 1000;
        this.lastTime = time;
        this.update(deltaTime);
        this.render();
        requestAnimationFrame(this.gameLoop.bind(this));
    }

    update(deltaTime) {
        this.gameTime += deltaTime;
        this.units.forEach(unit => unit.update(deltaTime));
        this.checkRunwayDamage();
        this.checkWinConditions();
        if (!this.decisionMade && this.gameTime >= 60) {
            this.decisionMade = true;
            const runwayUnits = this.units.filter(u => u.side === 'ukrainian' && u.y === 5 && u.x >= 5 && u.x <= 15).length;
            if (runwayUnits > 0) {
                gameInfo.innerHTML += '<br>Decision: Focused on runway, snipers deal more damage!';
                UNIT_STATS[UNIT_TYPES.SNIPER].damage = 25;
                UNIT_STATS[UNIT_TYPES.SNIPER].helicopterDamage = 50;
            } else {
                gameInfo.innerHTML += '<br>Decision: Defended perimeter, units are tougher!';
                this.units.filter(u => u.side === 'ukrainian').forEach(u => u.hp += 50);
            }
        }
    }

    render() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        this.map.draw();
        this.units.forEach(unit => unit.draw());
        this.drawUI();
    }

    checkRunwayDamage() {
        const runwayUnits = this.units.filter(u => u.side === 'ukrainian' && u.y === 5 && u.x >= 5 && u.x <= 15);
        runwayUnits.forEach(unit => {
            const damage = unit.type === UNIT_TYPES.SNIPER ? 5 : 2;
            this.runwayHealth -= damage * deltaTime;
        });
        if (this.runwayHealth < 0) this.runwayHealth = 0;
    }

    checkWinConditions() {
        const enemiesAlive = this.units.filter(u => u.side === 'russian').length;
        const ukrainiansAlive = this.units.filter(u => u.side === 'ukrainian').length;
        if (this.runwayHealth <= 0 || enemiesAlive === 0) {
            gameInfo.innerHTML = `<p style="color: green; font-weight: bold;">Victory! You disrupted the runway or defeated the enemy!</p>`;
            this.gameOver = true;
        } else if (ukrainiansAlive === 0) {
            gameInfo.innerHTML = `<p style="color: red; font-weight: bold;">Defeat! Your forces were overwhelmed.</p>`;
            this.gameOver = true;
        } else if (this.gameTime >= GAME_DURATION) {
            gameInfo.innerHTML = `<p style="color: red; font-weight: bold;">Defeat! Time ran out.</p>`;
            this.gameOver = true;
        }
    }

    drawUI() {
        // Semi-transparent panel
        ctx.fillStyle = 'rgba(0, 0, 0, 0.5)';
        ctx.fillRect(10, 10, 200, 80);
        ctx.fillStyle = 'white';
        ctx.font = 'bold 16px Arial';
        ctx.fillText(`Time: ${Math.floor(this.gameTime)}s`, 20, 30);
        ctx.fillText(`Runway Health: ${Math.round(this.runwayHealth)}`, 20, 50);
        if (this.selectedUnit) {
            ctx.fillText(`Selected: ${this.selectedUnit.type} (HP: ${Math.round(this.selectedUnit.hp)})`, 20, 70);
        }
    }
}

// Map class
class Map {
    constructor() {
        this.tiles = [];
        for (let y = 0; y < MAP_HEIGHT; y++) {
            this.tiles[y] = [];
            for (let x = 0; x < MAP_WIDTH; x++) {
                this.tiles[y][x] = { type: TILE_TYPES.GRASS };
            }
        }
        for (let x = 5; x <= 15; x++) this.tiles[5][x] = { type: TILE_TYPES.RUNWAY };
        for (let x = 10; x <= 12; x++) for (let y = 10; y <= 12; y++) this.tiles[y][x] = { type: TILE_TYPES.BUILDING };
    }

    draw() {
        for (let y = 0; y < MAP_HEIGHT; y++) {
            for (let x = 0; x < MAP_WIDTH; x++) {
                const tile = this.tiles[y][x];
                const screenX = x * TILE_SIZE;
                const screenY = y * TILE_SIZE;
                if (tile.type === TILE_TYPES.GRASS) {
                    ctx.fillStyle = '#4CAF50';
                    ctx.fillRect(screenX, screenY, TILE_SIZE, TILE_SIZE);
                    // Grass texture
                    ctx.fillStyle = 'rgba(0, 100, 0, 0.2)';
                    for (let i = 0; i < 3; i++) {
                        ctx.fillRect(screenX + Math.random() * TILE_SIZE, screenY + Math.random() * TILE_SIZE, 2, 2);
                    }
                } else if (tile.type === TILE_TYPES.RUNWAY) {
                    const healthRatio = game.runwayHealth / 100;
                    ctx.fillStyle = `rgb(${150 + 50 * healthRatio}, ${150 + 50 * healthRatio}, ${150 + 50 * healthRatio})`;
                    ctx.fillRect(screenX, screenY, TILE_SIZE, TILE_SIZE);
                    // Cracks
                    if (healthRatio < 0.8) {
                        ctx.strokeStyle = 'black';
                        ctx.beginPath();
                        ctx.moveTo(screenX + 5, screenY + 5);
                        ctx.lineTo(screenX + 15, screenY + 15);
                        ctx.stroke();
                    }
                } else {
                    ctx.fillStyle = '#795548';
                    ctx.fillRect(screenX, screenY, TILE_SIZE, TILE_SIZE);
                    // Building texture
                    ctx.fillStyle = 'rgba(255, 255, 255, 0.1)';
                    ctx.fillRect(screenX + 5, screenY + 5, 10, 10);
                }
            }
        }
    }
}

// Unit class
class Unit {
    constructor(x, y, type, side) {
        this.x = x;
        this.y = y;
        this.type = type;
        this.side = side;
        this.hp = UNIT_STATS[type].hp;
        this.targetX = null;
        this.targetY = null;
        this.attackTarget = null;
        this.attackTimer = 0;
        this.animTime = 0;
    }

    update(deltaTime) {
        this.animTime += deltaTime;
        if (this.attackTarget && this.attackTarget.hp > 0) {
            const distX = Math.abs(this.attackTarget.x - this.x);
            const distY = Math.abs(this.attackTarget.y - this.y);
            if (distX <= UNIT_STATS[this.type].range && distY <= UNIT_STATS[this.type].range) {
                this.targetX = null;
                this.targetY = null;
                this.attackTimer -= deltaTime;
                if (this.attackTimer <= 0) {
                    this.attackTimer = 1;
                    const damage = this.type === UNIT_TYPES.SNIPER && this.attackTarget.type === UNIT_TYPES.HELICOPTER ?
                                   UNIT_STATS[this.type].helicopterDamage : UNIT_STATS[this.type].damage;
                    this.attackTarget.hp -= damage;
                    if (this.attackTarget.hp <= 0) {
                        if (this.attackTarget.type === UNIT_TYPES.HELICOPTER) {
                            // Explosion effect
                            this.attackTarget.animTime = 0.5; // Trigger fade
                        }
                        game.units = game.units.filter(u => u !== this.attackTarget);
                        this.attackTarget = null;
                    }
                }
            } else {
                this.targetX = this.attackTarget.x;
                this.targetY = this.attackTarget.y;
            }
        }

        if (this.targetX !== null && this.targetY !== null) {
            const dx = this.targetX - this.x;
            const dy = this.targetY - this.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
            const step = UNIT_STATS[this.type].speed * deltaTime;
            if (distance <= step) {
                this.x = this.targetX;
                this.y = this.targetY;
                this.targetX = null;
                this.targetY = null;
            } else {
                this.x += (dx / distance) * step;
                this.y += (dy / distance) * step;
            }
        }

        if (this.side === 'russian' && !this.attackTarget && !this.targetX) {
            const ukrainians = game.units.filter(u => u.side === 'ukrainian');
            if (ukrainians.length > 0) {
                const closest = ukrainians.reduce((min, u) => {
                    const dist = Math.abs(u.x - this.x) + Math.abs(u.y - this.y);
                    return dist < min.dist ? { unit: u, dist } : min;
                }, { unit: null, dist: Infinity }).unit;
                this.attackTarget = closest;
            } else {
                this.targetX = 10;
                this.targetY = 5;
            }
        }
    }

    draw() {
        const screenX = Math.round(this.x * TILE_SIZE);
        const screenY = Math.round(this.y * TILE_SIZE);
        ctx.save();
        ctx.translate(screenX + TILE_SIZE / 2, screenY + TILE_SIZE / 2);

        // Selection glow
        if (game.selectedUnit === this) {
            ctx.fillStyle = `rgba(255, 255, 0, ${0.5 + 0.3 * Math.sin(this.animTime * 2)})`;
            ctx.beginPath();
            ctx.arc(0, 0, TILE_SIZE / 1.5, 0, Math.PI * 2);
            ctx.fill();
        }

        // Unit drawing
        ctx.fillStyle = UNIT_STATS[this.type].color;
        if (this.type === UNIT_TYPES.INFANTRY) {
            // Humanoid shape
            ctx.beginPath();
            ctx.arc(0, -TILE_SIZE / 4, 6, 0, Math.PI * 2); // Head
            ctx.fill();
            ctx.fillRect(-4, -TILE_SIZE / 4, 8, 12); // Body
            ctx.fillRect(6, -TILE_SIZE / 4, 8, 2); // Rifle
            // Idle sway
            ctx.translate(0, Math.sin(this.animTime * 3) * 2);
        } else if (this.type === UNIT_TYPES.SNIPER) {
            // Crouched with rifle
            ctx.beginPath();
            ctx.arc(0, -TILE_SIZE / 3, 5, 0, Math.PI * 2); // Head
            ctx.fill();
            ctx.fillRect(-4, -TILE_SIZE / 4, 8, 8); // Body
            ctx.fillRect(0, -TILE_SIZE / 3, 12, 2); // Long rifle
        } else if (this.type === UNIT_TYPES.HELICOPTER) {
            // Helicopter with rotor
            const scale = this.animTime > 0.5 ? 0 : 1 - this.animTime / 0.5; // Explosion fade
            ctx.scale(scale, scale);
            ctx.fillRect(-TILE_SIZE / 3, -TILE_SIZE / 6, TILE_SIZE * 2 / 3, TILE_SIZE / 3); // Body
            ctx.fillStyle = 'gray';
            ctx.beginPath();
            const rotorScale = 1 + 0.1 * Math.sin(this.animTime * 10); // Spin effect
            ctx.ellipse(0, -TILE_SIZE / 6, 12 * rotorScale, 4, 0, 0, Math.PI * 2); // Rotor
            ctx.fill();
            ctx.fillStyle = this.hp <= 0 ? 'red' : UNIT_STATS[this.type].color;
            if (this.hp <= 0) {
                ctx.globalAlpha = 1 - this.animTime / 0.5;
                ctx.beginPath();
                ctx.arc(0, 0, TILE_SIZE / 2, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        // Attack flash
        if (this.attackTimer > 0.8) {
            ctx.fillStyle = 'red';
            ctx.beginPath();
            ctx.arc(0, 0, 4, 0, Math.PI * 2);
            ctx.fill();
            ctx.scale(1.1, 1.1); // Recoil effect
        }

        // Health bar
        ctx.fillStyle = 'red';
        ctx.fillRect(-TILE_SIZE / 2, -TILE_SIZE, TILE_SIZE, 4);
        ctx.fillStyle = 'green';
        ctx.fillRect(-TILE_SIZE / 2, -TILE_SIZE, (this.hp / UNIT_STATS[this.type].hp) * TILE_SIZE, 4);

        ctx.restore();
    }

    moveTo(x, y) {
        if (x >= 0 && x < MAP_WIDTH && y >= 0 && y < MAP_HEIGHT) {
            this.targetX = x;
            this.targetY = y;
            this.attackTarget = null;
        }
    }

    attack(target) {
        this.attackTarget = target;
        this.attackTimer = 1;
    }
}

// Event Listeners
const game = new Game();

document.getElementById('startButton').addEventListener('click', () => game.start());

canvas.addEventListener('click', (event) => {
    const rect = canvas.getBoundingClientRect();
    const x = Math.floor((event.clientX - rect.left) / TILE_SIZE);
    const y = Math.floor((event.clientY - rect.top) / TILE_SIZE);
    const unit = game.units.find(u => Math.floor(u.x) === x && Math.floor(u.y) === y);
    if (unit && unit.side === 'ukrainian') {
        game.selectedUnit = unit;
    } else if (game.selectedUnit) {
        if (unit && unit.side === 'russian') {
            game.selectedUnit.attack(unit);
        } else {
            game.selectedUnit.moveTo(x, y);
        }
    }
});
