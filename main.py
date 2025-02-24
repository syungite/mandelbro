import py5

def setup():
    py5.size(800, 800)  
    py5.background(0)
    py5.no_stroke()

    for k in range(800):  
        for m in range(800):
            a = k / 200.0 - 2.0
            b = m / 200.0 - 2.0
            x = 0.0
            y = 0.0

            for n in range(500):
                px, py = x, y
                x = px * px - py * py + a
                y = 2.0 * px * py + b

                if x * x + y * y > 4:
                    py5.fill(255)
                    py5.rect(int(k), int(m), 1, 1)
                    break
    py5.save_frame("mandelbrot.png")

if __name__ == '__main__':
    py5.run_sketch()



