const canvas = document.getElementById('tetris');
const context = canvas.getContext('2d');

const ROWS = 20;
const COLS = 10;
const BLOCK_SIZE = 30;

context.scale(BLOCK_SIZE, BLOCK_SIZE);

// Create the game grid
const createGrid = () =>
  Array.from({ length: ROWS }, () => Array(COLS).fill(0));

let grid = createGrid();
let score = 0;
const scoreElement = document.getElementById('score');

// Tetromino shapes
const tetrominoes = {
  I: [[1, 1, 1, 1]],
  O: [
    [1, 1],
    [1, 1],
  ],
  T: [
    [0, 1, 0],
    [1, 1, 1],
  ],
  S: [
    [0, 1, 1],
    [1, 1, 0],
  ],
  Z: [
    [1, 1, 0],
    [0, 1, 1],
  ],
  J: [
    [1, 0, 0],
    [1, 1, 1],
  ],
  L: [
    [0, 0, 1],
    [1, 1, 1],
  ],
};

// Randomly select a tetromino
const randomTetromino = () => {
  const keys = Object.keys(tetrominoes);
  const randomKey = keys[Math.floor(Math.random() * keys.length)];
  return tetrominoes[randomKey];
};

let piece = randomTetromino();
let position = { x: 3, y: 0 };

// Draw the grid and pieces
const draw = () => {
  context.fillStyle = '#000';
  context.fillRect(0, 0, canvas.width, canvas.height);

  grid.forEach((row, y) => {
    row.forEach((value, x) => {
      if (value) {
        context.fillStyle = 'cyan';
        context.fillRect(x, y, 1, 1);
      }
    });
  });

  piece.forEach((row, y) => {
    row.forEach((value, x) => {
      if (value) {
        context.fillStyle = 'yellow';
        context.fillRect(x + position.x, y + position.y, 1, 1);
      }
    });
  });
};

// Move the piece down
const drop = () => {
  position.y++;
  if (collide()) {
    position.y--;
    merge();
    clearLines();
    piece = randomTetromino();
    position = { x: 3, y: 0 };
    if (collide()) {
      alert('Game Over!');
      grid = createGrid();
      score = 0;
      scoreElement.textContent = score;
    }
  }
};

// Check for collisions
const collide = () => {
  for (let y = 0; y < piece.length; y++) {
    for (let x = 0; x < piece[y].length; x++) {
      if (
        piece[y][x] &&
        (grid[y + position.y] && grid[y + position.y][x + position.x]) !== 0
      ) {
        return true;
      }
    }
  }
  return false;
};

// Merge the piece into the grid
const merge = () => {
  piece.forEach((row, y) => {
    row.forEach((value, x) => {
      if (value) {
        grid[y + position.y][x + position.x] = value;
      }
    });
  });
};

// Clear completed lines and update score
const clearLines = () => {
  let linesCleared = 0;
  for (let y = grid.length - 1; y >= 0; y--) {
    if (grid[y].every((cell) => cell !== 0)) {
      grid.splice(y, 1);
      grid.unshift(Array(COLS).fill(0));
      linesCleared++;
    }
  }
  if (linesCleared > 0) {
    // Quadratic scoring: 1 line = 1 point, 2 lines = 4 points, 3 lines = 9 points, 4 lines = 16 points
    score += linesCleared * linesCleared;
    scoreElement.textContent = score;
  }
};

// Handle keyboard input
document.addEventListener('keydown', (event) => {
  if (event.key === 'ArrowLeft') {
    position.x--;
    if (collide()) {
      position.x++;
    }
  }
  if (event.key === 'ArrowRight') {
    position.x++;
    if (collide()) {
      position.x--;
    }
  }
  if (event.key === 'ArrowDown') {
    drop();
  }
  if (event.key === 'ArrowUp') {
    rotate();
  }
});

// Rotate the piece
const rotate = () => {
  const rotated = piece[0].map((_, i) =>
    piece.map((row) => row[i]).reverse()
  );
  const prevPiece = piece;
  piece = rotated;
  if (collide()) {
    piece = prevPiece;
  }
};

// Game speed control
const speedInput = document.getElementById('speed');
const speedValue = document.getElementById('speedValue');
let dropInterval = 500; // Default speed
let lastDropTime = 0;

speedInput.addEventListener('input', () => {
  dropInterval = parseInt(speedInput.value);
  speedValue.textContent = `${dropInterval} ms`;
});

// Game loop
const update = (time = 0) => {
  const deltaTime = time - lastDropTime;

  if (deltaTime > dropInterval) {
    drop();
    lastDropTime = time;
  }

  draw();
  requestAnimationFrame(update);
};

update();
