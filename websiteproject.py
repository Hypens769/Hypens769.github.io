<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Game Website</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: #111;
            color: #eee;
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            height: 100vh;
        }
        header {
            background: #222;
            width: 100%;
            padding: 1rem;
            text-align: center;
            font-size: 2rem;
            font-weight: bold;
            color: #4CAF50;
        }
        #gameCanvas {
            background: #000;
            margin-top: 20px;
            border: 2px solid #4CAF50;
        }
    </style>
</head>
<body>

<header>
    🚗 My Car Game
</header>

<canvas id="gameCanvas" width="600" height="400"></canvas>

<script>
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');

    let carX = 270;
    let carY = 300;

    function drawCar() {
        ctx.fillStyle = 'lime';
        ctx.fillRect(carX, carY, 60, 30); // simple rectangle car
    }

    function clearCanvas() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }

    function updateGame() {
        clearCanvas();
        drawCar();
    }

    function moveCar(event) {
        const key = event.key;
        if (key === 'ArrowLeft' && carX > 0) {
            carX -= 10;
        } else if (key === 'ArrowRight' && carX < canvas.width - 60) {
            carX += 10;
        }
        updateGame();
    }

    document.addEventListener('keydown', moveCar);

    updateGame(); // initial draw
</script>

</body>
</html>