const canvas = document.getElementById('tetris');
const context = canvas.getContext('2d');

const ROWS = 20;
const COLS = 10;
const BLOCK_SIZE = 30;

// Set canvas dimensions
canvas.width = COLS * BLOCK_SIZE;
canvas.height = ROWS * BLOCK_SIZE;

// Scale the context
context.scale(BLOCK_SIZE, BLOCK_SIZE);

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

// Log the piece and position
console.log('Piece:', piece);
console.log('Position:', position);

// Draw the grid and pieces
const draw = () => {
  // Clear the canvas
  context.fillStyle = '#000';
  context.fillRect(0, 0, canvas.width, canvas.height);

  // Draw the current piece (yellow)
  piece.forEach((row, y) => {
    row.forEach((value, x) => {
      if (value) {
        context.fillStyle = 'yellow';
        context.fillRect(x + position.x, y + position.y, 1, 1);
        context.strokeStyle = '#000';
        context.strokeRect(x + position.x, y + position.y, 1, 1);
      }
    });
  });

  // Draw a test block at (0, 0)
  context.fillStyle = 'red';
  context.fillRect(0, 0, 1, 1);

  // Manually draw the Tetromino piece at a fixed position (green)
  piece.forEach((row, y) => {
    row.forEach((value, x) => {
      if (value) {
        context.fillStyle = 'green';
        context.fillRect(x + 3, y, 1, 1); // Draw a green block at (x + 3, y)
      }
    });
  });
};

// Move the piece down
const drop = () => {
  position.y++;
  if (position.y + piece.length > ROWS) {
    position.y--;
    piece = randomTetromino();
    position = { x: 3, y: 0 };
    console.log('New Piece:', piece);
    console.log('New Position:', position);
  }
};

// Game loop
const update = () => {
  drop();
  draw();
  requestAnimationFrame(update);
};

// Initial draw
draw();
update();
