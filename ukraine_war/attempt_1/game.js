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
    [UNIT_TYPES.INFANTRY]: { range: 5, damage: 10, attackSpeed: 1, speed: 1 },
    [UNIT_TYPES.SNIPER]: { range: 10, damage: 20, attackSpeed: 0.5, speed: 0.8 },
    [UNIT_TYPES.HELICOPTER]: { range: 8, damage: 40, attackSpeed: 0.5, speed: 2 }
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
            this.units.push(new Unit(5, 5, UNIT_TYPES.INFANTRY, 'russian'));
            this.units.push(new Unit(6, 6, UNIT_TYPES.HELICOPTER, 'russian'));
            this.units.push(new Unit(15, 15, UNIT_TYPES.INFANTRY, 'ukrainian'));
        } else {
            this.units.push(new Unit(15, 15, UNIT_TYPES.INFANTRY, 'ukrainian'));
            this.units.push(new Unit(14, 14, UNIT_TYPES.SNIPER, 'ukrainian'));
            this.units.push(new Unit(5, 5, UNIT_TYPES.INFANTRY, 'russian'));
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
            this.units.push(new Unit(0, 0, UNIT_TYPES.INFANTRY, 'russian'));
            this.reinforcedRussian = true;
        }
        if (this.playerSide === 'ukrainian' && Math.floor(this.gameTime) === 480 && !this.reinforcedUkrainian) {
            this.units.push(new Unit(19, 19, UNIT_TYPES.SNIPER, 'ukrainian'));
            this.reinforcedUkrainian = true;
        }
    }

    checkDecisionPoint() {
        if (Math.floor(this.gameTime) === 180 && !this.decisionMade) {
            const towerUnits = this.units.filter(u => u.side === 'russian' && u.x >= 10 && u.x <= 12 && u.y >= 10 && u.y <= 12).length;
            const runwayUnits = this.units.filter(u => u.side === 'russian' && u.x >= 5 && u.x <= 15 && u.y === 5).length;
            this.decisionMade = true;
            if (towerUnits > runwayUnits) {
                gameInfo.innerHTML += '<p>Decision: Russians focus on control tower. Ukrainian reserves arrive early.</p>';
                if (this.playerSide === 'ukrainian') this.gameTime = 420; // Fast-forward to 7 minutes
            } else {
                gameInfo.innerHTML += '<p>Decision: Russians focus on runway. Russian reinforcements arrive early.</p>';
                if (this.playerSide === 'russian') this.gameTime = 540; // Fast-forward to 9 minutes
            }
        }
    }

    checkWinConditions() {
        if (this.gameTime >= GAME_DURATION) {
            const towerControl = this.units.filter(u => u.x >= 10 && u.x <= 12 && u.y >= 10 && u.y <= 12);
            const runwayControl = this.units.filter(u => u.x >= 5 && u.x <= 15 && u.y === 5);
            const towerSide = towerControl.every(u => u.side === 'russian') ? 'russian' : (towerControl.every(u => u.side === 'ukrainian') ? 'ukrainian' : 'contested');
            const runwaySide = runwayControl.every(u => u.side === 'russian') ? 'russian' : (runwayControl.every(u => u.side === 'ukrainian') ? 'ukrainian' : 'contested');
            let result = '';
            if (towerSide === 'russian' && runwaySide === 'russian' && this.runwayHealth > 0) {
                result = 'Russian Victory: Both zones controlled, runway intact.';
            } else if (this.runwayHealth <= 0 || towerSide !== 'russian' || runwaySide !== 'russian') {
                result = 'Ukrainian Victory: Russians failed to secure both zones or runway destroyed.';
            } else {
                result = 'Stalemate: Russians control zones but runway is destroyed.';
            }
            gameInfo.innerHTML = `<p>Game Over! ${result}</p>`;
            this.gameOver = true;
        }
    }

    drawUI() {
        ctx.fillStyle = 'black';
        ctx.font = '16px Arial';
        ctx.fillText(`Time: ${Math.floor(this.gameTime / 60)}:${Math.floor(this.gameTime % 60).toString().padStart(2, '0')}`, 10, 20);
        ctx.fillText(`Runway Health: ${this.runwayHealth}`, 10, 40);
        if (this.selectedUnits.length > 0) {
            ctx.fillText(`Selected: ${this.selectedUnits[0].type} (Health: ${this.selectedUnits[0].health})`, 10, 60);
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
        // Hardcode runway (horizontal strip)
        for (let x = 5; x <= 15; x++) this.tiles[5][x] = { type: TILE_TYPES.RUNWAY, walkable: true };
        // Hardcode control tower
        for (let x = 10; x <= 12; x++) for (let y = 10; y <= 12; y++) this.tiles[y][x] = { type: TILE_TYPES.BUILDING, walkable: true };
    }

    draw() {
        for (let y = 0; y < MAP_HEIGHT; y++) {
            for (let x = 0; x < MAP_WIDTH; x++) {
                const tile = this.tiles[y][x];
                const screenX = (x - y) * (TILE_SIZE / 2) + canvas.width / 2 - (MAP_WIDTH * TILE_SIZE) / 4;
                const screenY = (x + y) * (TILE_SIZE / 4) + canvas.height / 4;
                ctx.fillStyle = tile.type === TILE_TYPES.GRASS ? 'green' : tile.type === TILE_TYPES.RUNWAY ? 'gray' : 'brown';
                ctx.fillRect(screenX, screenY, TILE_SIZE, TILE_SIZE);
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
        this.health = 100;
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
        ctx.fillStyle = this.side === 'russian' ? 'red' : 'blue';
        ctx.fillRect(screenX, screenY, TILE_SIZE / 2, TILE_SIZE / 2);
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
        if (current.x === goal.x && current.y === goal.y) return reconstructPath(cameFrom, current);
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
