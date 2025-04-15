// Constants
const TILE_SIZE = 32;
const MAP_WIDTH = 20;
const MAP_HEIGHT = 20;
const GAME_DURATION = 15 * 60; // 15 minutes in seconds

const UNIT_TYPES = {
    INFANTRY: 'infantry',
    SNIPER: 'sniper',
    HELICOPTER: 'helicopter'
};

const UNIT_STATS = {
    [UNIT_TYPES.INFANTRY]: { hp: 100, range: 5, damage: 10, attackSpeed: 1, speed: 1 },
    [UNIT_TYPES.SNIPER]: { hp: 80, range: 10, damage: 20, attackSpeed: 0.5, speed: 0.8 },
    [UNIT_TYPES.HELICOPTER]: { hp: 200, range: 8, damage: 40, attackSpeed: 0.5, speed: 2 }
};

const TILE_TYPES = {
    GRASS: 'grass',
    RUNWAY: 'runway',
    BUILDING: 'building',
    WOODS: 'woods',
    ROAD: 'road'
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
        this.selectedUnits = [];
        this.playerSide = null;
        this.gameTime = 0;
        this.gameOver = false;
        this.runwayHealth = 100;
        this.decisionMade = false;
        this.towerControlledBy = null;
        this.runwayControlledBy = null;
    }

    start() {
        if (!this.playerSide) {
            alert('Please select a side!');
            return;
        }
        this.spawnUnits();
        this.lastTime = performance.now();
        requestAnimationFrame(this.gameLoop.bind(this));
    }

    spawnUnits() {
        if (this.playerSide === 'russian') {
            // Russian VDV and helicopter
            this.units.push(new Unit(5, 5, UNIT_TYPES.INFANTRY, 'russian')); // VDV infantry
            this.units.push(new Unit(6, 6, UNIT_TYPES.HELICOPTER, 'russian')); // Ka-52
            this.units.push(new Unit(7, 5, UNIT_TYPES.SNIPER, 'russian')); // Sniper
            // Ukrainian defenders
            this.units.push(new Unit(15, 15, UNIT_TYPES.INFANTRY, 'ukrainian')); // National Guard
            this.units.push(new Unit(14, 14, UNIT_TYPES.SNIPER, 'ukrainian')); // MANPADS-like sniper
        } else {
            // Ukrainian defenders
            this.units.push(new Unit(15, 15, UNIT_TYPES.INFANTRY, 'ukrainian')); // National Guard
            this.units.push(new Unit(14, 14, UNIT_TYPES.SNIPER, 'ukrainian')); // MANPADS
            this.units.push(new Unit(13, 15, UNIT_TYPES.INFANTRY, 'ukrainian')); // Additional infantry
            // Russian attackers
            this.units.push(new Unit(5, 5, UNIT_TYPES.INFANTRY, 'russian')); // VDV
            this.units.push(new Unit(6, 6, UNIT_TYPES.HELICOPTER, 'russian')); // Ka-52
        }
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
        this.handleReinforcements();
        this.checkDecisionPoint();
        this.checkZoneControl();
        this.checkWinConditions();
    }

    render() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        this.map.draw();
        this.units.forEach(unit => unit.draw());
        this.drawUI();
    }

    handleReinforcements() {
        if (this.playerSide === 'russian' && Math.floor(this.gameTime) === 600 && !this.reinforcedRussian) {
            this.units.push(new Unit(0, 0, UNIT_TYPES.INFANTRY, 'russian')); // Tank-like infantry
            this.units.push(new Unit(1, 0, UNIT_TYPES.INFANTRY, 'russian')); // BMP-like
            this.reinforcedRussian = true;
            gameInfo.innerHTML += '<p>Russian reinforcements arrived from Belarus!</p>';
        }
        if (this.playerSide === 'ukrainian' && Math.floor(this.gameTime) === 480 && !this.reinforcedUkrainian) {
            this.units.push(new Unit(19, 19, UNIT_TYPES.SNIPER, 'ukrainian')); // Reserves
            this.units.push(new Unit(18, 19, UNIT_TYPES.INFANTRY, 'ukrainian')); // APC-like
            this.reinforcedUkrainian = true;
            gameInfo.innerHTML += '<p>Ukrainian reserves arrived to defend Hostomel!</p>';
        }
    }

    checkDecisionPoint() {
        if (Math.floor(this.gameTime) === 180 && !this.decisionMade) {
            const towerUnits = this.units.filter(u => u.side === 'russian' && u.x >= 10 && u.x <= 12 && u.y >= 10 && u.y <= 12).length;
            const runwayUnits = this.units.filter(u => u.side === 'russian' && u.x >= 5 && u.x <= 15 && u.y === 5).length;
            this.decisionMade = true;
            if (towerUnits > runwayUnits) {
                gameInfo.innerHTML += '<p>Decision: Russians focus on control tower. Ukrainian reserves arrive early.</p>';
                if (this.playerSide === 'ukrainian') this.gameTime = 420; // Fast-forward to 7 min
            } else {
                gameInfo.innerHTML += '<p>Decision: Russians focus on runway. Russian reinforcements arrive early.</p>';
                if (this.playerSide === 'russian') this.gameTime = 540; // Fast-forward to 9 min
            }
        }
    }

    checkZoneControl() {
        // Tower control
        const towerUnits = this.units.filter(u => u.x >= 10 && u.x <= 12 && u.y >= 10 && u.y <= 12);
        this.towerControlledBy = towerUnits.length > 0 ? (towerUnits.every(u => u.side === 'russian') ? 'russian' : (towerUnits.every(u => u.side === 'ukrainian') ? 'ukrainian' : 'contested')) : 'none';

        // Runway control
        const runwayUnits = this.units.filter(u => u.x >= 5 && u.x <= 15 && u.y === 5);
        this.runwayControlledBy = runwayUnits.length > 0 ? (runwayUnits.every(u => u.side === 'russian') ? 'russian' : (runwayUnits.every(u => u.side === 'ukrainian') ? 'ukrainian' : 'contested')) : 'none';

        // Runway damage by Ukrainian snipers (simulating MANPADS/mortars)
        if (this.playerSide === 'ukrainian') {
            runwayUnits.forEach(unit => {
                if (unit.side === 'ukrainian' && unit.type === UNIT_TYPES.SNIPER) {
                    this.runwayHealth -= 5 * deltaTime; // Gradual damage
                    if (this.runwayHealth < 0) this.runwayHealth = 0;
                }
            });
        }
    }

    checkWinConditions() {
        if (this.gameTime >= GAME_DURATION || this.runwayHealth <= 0) {
            let result = '';
            let score = 0;

            // Calculate score
            if (this.towerControlledBy === 'russian') score += 25;
            if (this.runwayControlledBy === 'russian') score += 25;
            if (this.runwayHealth > 0 && this.playerSide === 'russian') score += 10;
            if (this.runwayHealth <= 0 && this.playerSide === 'ukrainian') score += 35;
            const survivingUnits = this.units.filter(u => u.side === this.playerSide).length;
            score += survivingUnits * 5; // 5 points per surviving unit

            // Determine outcome
            if (this.playerSide === 'russian') {
                if (this.towerControlledBy === 'russian' && this.runwayControlledBy === 'russian' && this.runwayHealth > 0) {
                    result = `Russian Victory: Airport secured, runway intact. Score: ${score}/100`;
                } else if (this.runwayHealth <= 0) {
                    result = `Stalemate: Airport captured but runway destroyed. Score: ${score}/100`;
                } else {
                    result = `Ukrainian Victory: Russians failed to secure airport. Score: ${score}/100`;
                }
            } else {
                if (this.runwayHealth <= 0 || this.towerControlledBy !== 'russian' || this.runwayControlledBy !== 'russian') {
                    result = `Ukrainian Victory: Runway disrupted or airport defended. Score: ${score}/100`;
                } else {
                    result = `Russian Victory: Airport secured. Score: ${score}/100`;
                }
            }

            gameInfo.innerHTML = `<p>Game Over! ${result}</p><p>Historically, Ukrainians damaged the runway, delaying Russia's advance.</p>`;
            this.gameOver = true;
        }
    }

    drawUI() {
        ctx.fillStyle = 'black';
        ctx.font = '16px Arial';
        ctx.fillText(`Time: ${Math.floor(this.gameTime / 60)}:${Math.floor(this.gameTime % 60).toString().padStart(2, '0')}`, 10, 20);
        ctx.fillText(`Runway Health: ${Math.round(this.runwayHealth)}`, 10, 40);
        ctx.fillText(`Tower: ${this.towerControlledBy || 'none'}`, 10, 60);
        ctx.fillText(`Runway: ${this.runwayControlledBy || 'none'}`, 10, 80);
        if (this.selectedUnits.length > 0) {
            ctx.fillText(`Selected: ${this.selectedUnits[0].type} (Health: ${Math.round(this.selectedUnits[0].health)})`, 10, 100);
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
                this.tiles[y][x] = { type: TILE_TYPES.GRASS, walkable: true };
            }
        }
        // Runway
        for (let x = 5; x <= 15; x++) this.tiles[5][x] = { type: TILE_TYPES.RUNWAY, walkable: true };
        // Control tower
        for (let x = 10; x <= 12; x++) for (let y = 10; y <= 12; y++) this.tiles[y][x] = { type: TILE_TYPES.BUILDING, walkable: true };
        // Woods
        for (let x = 2; x <= 4; x++) for (let y = 2; y <= 4; y++) this.tiles[y][x] = { type: TILE_TYPES.WOODS, walkable: true };
        // Roads
        for (let x = 0; x < MAP_WIDTH; x++) this.tiles[0][x] = { type: TILE_TYPES.ROAD, walkable: true };
    }

    draw() {
        for (let y = 0; y < MAP_HEIGHT; y++) {
            for (let x = 0; x < MAP_WIDTH; x++) {
                const tile = this.tiles[y][x];
                const screenX = (x - y) * (TILE_SIZE / 2) + canvas.width / 2 - (MAP_WIDTH * TILE_SIZE) / 4;
                const screenY = (x + y) * (TILE_SIZE / 4) + canvas.height / 4;
                ctx.fillStyle = tile.type === TILE_TYPES.GRASS ? '#4CAF50' : 
                               tile.type === TILE_TYPES.RUNWAY ? (game.runwayHealth > 0 ? '#9E9E9E' : '#424242') :
                               tile.type === TILE_TYPES.BUILDING ? '#795548' :
                               tile.type === TILE_TYPES.WOODS ? '#388E3C' : '#B0BEC5';
                ctx.beginPath();
                ctx.moveTo(screenX, screenY + TILE_SIZE / 4);
                ctx.lineTo(screenX + TILE_SIZE / 2, screenY);
                ctx.lineTo(screenX + TILE_SIZE, screenY + TILE_SIZE / 4);
                ctx.lineTo(screenX + TILE_SIZE / 2, screenY + TILE_SIZE / 2);
                ctx.closePath();
                ctx.fill();
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
        this.health = UNIT_STATS[type].hp;
        this.path = [];
        this.speed = UNIT_STATS[type].speed;
        this.currentTarget = null;
        this.attackTarget = null;
        this.attackTimer = 0;
    }

    update(deltaTime) {
        if (this.currentTarget) {
            const dx = this.currentTarget.x - this.x;
            const dy = this.currentTarget.y - this.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
            const step = this.speed * deltaTime;
            if (distance < step) {
                this.x = this.currentTarget.x;
                this.y = this.currentTarget.y;
                this.currentTarget = this.path.length > 0 ? this.path.shift() : null;
            } else {
                this.x += (dx / distance) * step;
                this.y += (dy / distance) * step;
            }
        } else {
            const enemies = game.units.filter(u => u.side !== this.side);
            let closest = enemies.reduce((min, u) => {
                const dist = Math.hypot(u.x - this.x, u.y - this.y);
                return dist < min.dist && dist <= UNIT_STATS[this.type].range ? { unit: u, dist } : min;
            }, { unit: null, dist: Infinity });
            if (closest.unit) this.attack(closest.unit);
        }
        if (this.attackTarget) {
            this.attackTimer -= deltaTime;
            if (this.attackTimer <= 0) {
                this.attackTimer = 1 / UNIT_STATS[this.type].attackSpeed;
                this.attackTarget.health -= UNIT_STATS[this.type].damage;
                if (this.attackTarget.health <= 0) {
                    game.units = game.units.filter(u => u !== this.attackTarget);
                    this.attackTarget = null;
                }
            }
        }
    }

    draw() {
        const screenX = (this.x - this.y) * (TILE_SIZE / 2) + canvas.width / 2 - (MAP_WIDTH * TILE_SIZE) / 4;
        const screenY = (this.x + this.y) * (TILE_SIZE / 4) + canvas.height / 4;
        ctx.save();
        ctx.translate(screenX + TILE_SIZE / 4, screenY + TILE_SIZE / 8);
        
        if (this.type === UNIT_TYPES.INFANTRY) {
            ctx.fillStyle = this.side === 'russian' ? '#D32F2F' : '#0288D1'; // Red for Russian, Blue for Ukrainian
            ctx.beginPath();
            ctx.arc(0, 0, TILE_SIZE / 4, 0, Math.PI * 2); // Circle for infantry
            ctx.fill();
            ctx.fillStyle = '#FFFFFF';
            ctx.fillRect(-2, -2, 4, 4); // Small square as "rifle"
        } else if (this.type === UNIT_TYPES.SNIPER) {
            ctx.fillStyle = this.side === 'russian' ? '#B71C1C' : '#01579B';
            ctx.beginPath();
            ctx.moveTo(0, -TILE_SIZE / 4);
            ctx.lineTo(-TILE_SIZE / 4, TILE_SIZE / 4);
            ctx.lineTo(TILE_SIZE / 4, TILE_SIZE / 4);
            ctx.closePath(); // Triangle for sniper
            ctx.fill();
            ctx.fillStyle = '#000000';
            ctx.fillRect(0, -TILE_SIZE / 8, 2, TILE_SIZE / 4); // "Scope"
        } else if (this.type === UNIT_TYPES.HELICOPTER) {
            ctx.fillStyle = this.side === 'russian' ? '#C62828' : '#0277BD';
            ctx.fillRect(-TILE_SIZE / 4, -TILE_SIZE / 8, TILE_SIZE / 2, TILE_SIZE / 4); // Rectangle for helicopter
            ctx.fillStyle = '#B0BEC5';
            ctx.beginPath();
            ctx.arc(0, 0, TILE_SIZE / 8, 0, Math.PI * 2); // Rotor
            ctx.fill();
        }

        // Health bar
        ctx.fillStyle = 'red';
        ctx.fillRect(-TILE_SIZE / 4, -TILE_SIZE / 2, TILE_SIZE / 2, 4);
        ctx.fillStyle = 'green';
        ctx.fillRect(-TILE_SIZE / 4, -TILE_SIZE / 2, (this.health / UNIT_STATS[this.type].hp) * (TILE_SIZE / 2), 4);

        ctx.restore();
    }

    moveTo(targetX, targetY) {
        const start = { x: Math.floor(this.x), y: Math.floor(this.y) };
        const goal = { x: targetX, y: targetY };
        this.path = aStar(start, goal, game.map) || [];
        if (this.path.length > 0) this.currentTarget = this.path.shift();
    }

    attack(target) {
        this.attackTarget = target;
        this.attackTimer = 1 / UNIT_STATS[this.type].attackSpeed;
    }
}

// A* Pathfinding
function aStar(start, goal, map) {
    const openSet = [`${start.x},${start.y}`];
    const cameFrom = {};
    const gScore = { [`${start.x},${start.y}`]: 0 };
    const fScore = { [`${start.x},${start.y}`]: heuristic(start, goal) };

    while (openSet.length > 0) {
        const currentKey = openSet.sort((a, b) => fScore[a] - fScore[b])[0];
        openSet.shift();
        const [cx, cy] = currentKey.split(',').map(Number);
        const current = { x: cx, y: cy };
        if (current.x === goal.x && current.y === goal.x) return reconstructPath(cameFrom, current);
        const neighbors = getNeighbors(current, map);
        for (let neighbor of neighbors) {
            const neighborKey = `${neighbor.x},${neighbor.y}`;
            const tentativeGScore = gScore[currentKey] + 1;
            if (!(neighborKey in gScore) || tentativeGScore < gScore[neighborKey]) {
                cameFrom[neighborKey] = currentKey;
                gScore[neighborKey] = tentativeGScore;
                fScore[neighborKey] = tentativeGScore + heuristic(neighbor, goal);
                if (!openSet.includes(neighborKey)) openSet.push(neighborKey);
            }
        }
    }
    return null;
}

function heuristic(a, b) {
    return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
}

function getNeighbors(pos, map) {
    const neighbors = [];
    const directions = [{ x: 1, y: 0 }, { x: -1, y: 0 }, { x: 0, y: 1 }, { x: 0, y: -1 }];
    for (let dir of directions) {
        const nx = pos.x + dir.x;
        const ny = pos.y + dir.y;
        if (nx >= 0 && nx < MAP_WIDTH && ny >= 0 && ny < MAP_HEIGHT && map.tiles[ny][nx].walkable) {
            neighbors.push({ x: nx, y: ny });
        }
    }
    return neighbors;
}

function reconstructPath(cameFrom, current) {
    const path = [current];
    let currentKey = `${current.x},${current.y}`;
    while (cameFrom[currentKey]) {
        const [px, py] = cameFrom[currentKey].split(',').map(Number);
        current = { x: px, y: py };
        path.unshift(current);
        currentKey = `${current.x},${current.y}`;
    }
    return path;
}

// Screen to Grid conversion
function screenToGrid(screenX, screenY) {
    const offsetX = screenX - (canvas.width / 2 - (MAP_WIDTH * TILE_SIZE) / 4);
    const offsetY = screenY - canvas.height / 4;
    const a = TILE_SIZE / 2;
    const b = TILE_SIZE / 4;
    const gridX = Math.round((offsetX / a + offsetY / b) / 2);
    const gridY = Math.round((offsetY / b - offsetX / a) / 2);
    return { x: gridX, y: gridY };
}

// Event Listeners
const game = new Game();

document.getElementById('startButton').addEventListener('click', () => game.start());
document.getElementById('selectRussian').addEventListener('click', () => game.playerSide = 'russian');
document.getElementById('selectUkrainian').addEventListener('click', () => game.playerSide = 'ukrainian');

canvas.addEventListener('click', (event) => {
    const rect = canvas.getBoundingClientRect();
    const screenX = event.clientX - rect.left;
    const screenY = event.clientY - rect.top;
    const gridPos = screenToGrid(screenX, screenY);
    const unit = game.units.find(u => Math.floor(u.x) === gridPos.x && Math.floor(u.y) === gridPos.y && u.side === game.playerSide);
    if (unit) game.selectedUnits = [unit];
    else game.selectedUnits = [];
});

canvas.addEventListener('contextmenu', (event) => {
    event.preventDefault();
    const rect = canvas.getBoundingClientRect();
    const screenX = event.clientX - rect.left;
    const screenY = event.clientY - rect.top;
    const gridPos = screenToGrid(screenX, screenY);
    const enemy = game.units.find(u => Math.floor(u.x) === gridPos.x && Math.floor(u.y) === gridPos.y && u.side !== game.playerSide);
    if (enemy) game.selectedUnits.forEach(unit => unit.attack(enemy));
    else game.selectedUnits.forEach(unit => unit.moveTo(gridPos.x, gridPos.y));
});
