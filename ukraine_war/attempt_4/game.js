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
    [UNIT_TYPES.INFANTRY]: { hp: 100, damage: 10, range: 3, symbol: '🪖', color: '#0288D1' },
    [UNIT_TYPES.SNIPER]: { hp: 80, damage: 20, range: 5, symbol: '🔫', color: '#01579B' },
    [UNIT_TYPES.HELICOPTER]: { hp: 150, damage: 30, range: 4, symbol: '🚁', color: '#C62828' }
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
        gameInfo.innerHTML = 'Defend the airport! Move units to the runway to destroy it or defeat all enemies.';
        requestAnimationFrame(this.gameLoop.bind(this));
    }

    spawnUnits() {
        // Ukrainian player units
        this.units.push(new Unit(15, 10, UNIT_TYPES.INFANTRY, 'ukrainian')); // Near bottom-right
        this.units.push(new Unit(14, 11, UNIT_TYPES.SNIPER, 'ukrainian')); // Sniper for runway
        // Russian enemies
        this.units.push(new Unit(5, 2, UNIT_TYPES.INFANTRY, 'russian')); // Near runway
        this.units.push(new Unit(6, 3, UNIT_TYPES.HELICOPTER, 'russian')); // Helicopter
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
                gameInfo.innerHTML += '<br>Decision: You focused on the runway, increasing damage!';
                UNIT_STATS[UNIT_TYPES.SNIPER].damage = 30; // Boost sniper damage
            } else {
                gameInfo.innerHTML += '<br>Decision: You defended the perimeter, strengthening units!';
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
            if (unit.type === UNIT_TYPES.SNIPER) {
                this.runwayHealth -= 10 * deltaTime; // Sniper damages runway
            } else {
                this.runwayHealth -= 5 * deltaTime; // Infantry damages less
            }
        });
        if (this.runwayHealth < 0) this.runwayHealth = 0;
    }

    checkWinConditions() {
        const enemiesAlive = this.units.filter(u => u.side === 'russian').length;
        if (this.runwayHealth <= 0 || enemiesAlive === 0) {
            gameInfo.innerHTML = `<p>Victory! You disrupted the runway or defeated the enemy!</p>`;
            this.gameOver = true;
        } else if (this.units.filter(u => u.side === 'ukrainian').length === 0 || this.gameTime >= GAME_DURATION) {
            gameInfo.innerHTML = `<p>Defeat! Your forces were overwhelmed.</p>`;
            this.gameOver = true;
        }
    }

    drawUI() {
        ctx.fillStyle = 'black';
        ctx.font = '16px Arial';
        ctx.fillText(`Time: ${Math.floor(this.gameTime)}s`, 10, 20);
        ctx.fillText(`Runway Health: ${Math.round(this.runwayHealth)}`, 10, 40);
        if (this.selectedUnit) {
            ctx.fillText(`Selected: ${this.selectedUnit.type} (HP: ${Math.round(this.selectedUnit.hp)})`, 10, 60);
        }
    }
}

// Map class
class Map {
    constructor() {
        this.tiles = [];
        for (let Y = 0; Y < MAP_HEIGHT; Y++) {
            this.tiles[Y] = [];
            for (let X = 0; X < MAP_WIDTH; X++) {
                this.tiles[Y][X] = { type: TILE_TYPES.GRASS, symbol: '🌿' };
            }
        }
        // Runway
        for (let X = 5; X <= 15; X++) this.tiles[5][X] = { type: TILE_TYPES.RUNWAY, symbol: '🛬' };
        // Building (tower)
        for (let X = 10; X <= 12; X++) for (let Y = 10; Y <= 12; Y++) this.tiles[Y][X] = { type: TILE_TYPES.BUILDING, symbol: '🏢' };
    }

    draw() {
        for (let Y = 0; Y < MAP_HEIGHT; Y++) {
            for (let X = 0; X < MAP_WIDTH; X++) {
                const tile = this.tiles[Y][X];
                const screenX = X * TILE_SIZE;
                const screenY = Y * TILE_SIZE;
                ctx.fillStyle = tile.type === TILE_TYPES.GRASS ? '#4CAF50' :
                               tile.type === TILE_TYPES.RUNWAY ? (game.runwayHealth > 0 ? '#9E9E9E' : '#424242') :
                               '#795548';
                ctx.fillRect(screenX, screenY, TILE_SIZE, TILE_SIZE);
                ctx.font = '24px Arial';
                ctx.fillStyle = 'black';
                ctx.fillText(tile.symbol, screenX + 4, screenY + 24);
            }
        }
    }
}

// Unit class
class Unit {
    constructor(X, Y, type, side) {
        this.X = X;
        this.Y = Y;
        this.type = type;
        this.side = side;
        this.hp = UNIT_STATS[type].hp;
        this.target = null;
        this.attackTimer = 0;
    }

    update(deltaTime) {
        if (this.target) {
            const distX = this.target.X - this.X;
            const distY = this.target.Y - this.Y;
            if (Math.abs(distX) <= UNIT_STATS[this.type].range && Math.abs(distY) <= UNIT_STATS[this.type].range) {
                this.attackTimer -= deltaTime;
                if (this.attackTimer <= 0) {
                    this.attackTimer = 1;
                    this.target.hp -= UNIT_STATS[this.type].damage;
                    if (this.target.hp <= 0) {
                        game.units = game.units.filter(u => u !== this.target);
                        this.target = null;
                    }
                }
            } else {
                // Move toward target
                if (Math.abs(distX) > Math.abs(distY)) {
                    this.X += Math.sign(distX);
                } else {
                    this.Y += Math.sign(distY);
                }
            }
        } else if (this.side === 'russian') {
            // Enemy AI: Move toward runway or nearest Ukrainian
            const ukrainians = game.units.filter(u => u.side === 'ukrainian');
            if (ukrainians.length > 0) {
                const closest = ukrainians.reduce((min, u) => {
                    const dist = Math.abs(u.X - this.X) + Math.abs(u.Y - this.Y);
                    return dist < min.dist ? { unit: u, dist } : min;
                }, { unit: null, dist: Infinity }).unit;
                this.target = closest;
            } else {
                this.target = { X: 10, Y: 5 }; // Head to runway
            }
        }
    }

    draw() {
        const screenX = this.X * TILE_SIZE;
        const screenY = this.Y * TILE_SIZE;
        ctx.fillStyle = game.selectedUnit === this ? 'yellow' : UNIT_STATS[this.type].color;
        ctx.fillRect(screenX, screenY, TILE_SIZE, TILE_SIZE);
        ctx.font = '24px Arial';
        ctx.fillStyle = 'white';
        ctx.fillText(UNIT_STATS[this.type].symbol, screenX + 4, screenY + 24);
        // Health bar
        ctx.fillStyle = 'red';
        ctx.fillRect(screenX, screenY - 8, TILE_SIZE, 4);
        ctx.fillStyle = 'green';
        ctx.fillRect(screenX, screenY - 8, (this.hp / UNIT_STATS[this.type].hp) * TILE_SIZE, 4);
    }

    moveTo(X, Y) {
        this.target = { X, Y };
    }

    attack(target) {
        if (Math.abs(target.X - this.X) <= UNIT_STATS[this.type].range && Math.abs(target.Y - this.Y) <= UNIT_STATS[this.type].range) {
            this.target = target;
            this.attackTimer = 1;
        } else {
            this.moveTo(target.X, target.Y);
        }
    }
}

// Event Listeners
const game = new Game();

document.getElementById('startButton').addEventListener('click', () => game.start());

canvas.addEventListener('click', (event) => {
    const rect = canvas.getBoundingClientRect();
    const X = Math.floor((event.clientX - rect.left) / TILE_SIZE);
    const Y = Math.floor((event.clientY - rect.top) / TILE_SIZE);
    const unit = game.units.find(u => u.X === X && u.Y === Y);
    if (unit && unit.side === 'ukrainian') {
        game.selectedUnit = unit;
    } else if (game.selectedUnit) {
        if (unit && unit.side === 'russian') {
            game.selectedUnit.attack(unit);
        } else {
            game.selectedUnit.moveTo(X, Y);
        }
    }
});
