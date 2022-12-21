// create canvas element and append it to document body
var canvas = document.getElementById("drawing-canvas")

// some hotfixes... ( ≖_≖)
document.body.style.margin = 0;

// get canvas 2D context and set him correct size
var ctx = canvas.getContext('2d');

// last known position
var pos = { x: 0, y: 0 };

document.addEventListener('mousemove', draw);
document.addEventListener('mousedown', setPosition);
document.addEventListener('mouseenter', setPosition);
document.getElementById('reset-btn').onclick = function() {
  ctx.clearRect(0, 0, 252, 252);
}

// new position from mouse event
function setPosition(e) {
  pos.x = e.clientX;
  pos.y = e.clientY;
}


function draw(e) {
  // mouse left button must be pressed
  if (e.buttons !== 1) return;

  ctx.beginPath(); // begin

  ctx.lineWidth = 10;
  ctx.lineCap = 'round';
  ctx.strokeStyle = 'black';

  ctx.moveTo(pos.x, pos.y); // from
  setPosition(e);
  ctx.lineTo(pos.x, pos.y); // to

  ctx.stroke(); // draw it!
}
