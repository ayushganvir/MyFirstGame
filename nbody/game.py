def game(universe, game_clock):
    delta_t = game_clock.tick() / 1000.0
    for star in universe.stars:
        star.display()

    for p0 in universe.particles:
        gx, gy = (0, 0)
        for p in universe.particles:
            if p == p0:
                continue

            delta_gx, delta_gy = p.gravity_between(p0)
            if p0.name == 'Sun' and p.distance_from(p0) < 20:
                universe.particles.remove(p)

            gy += delta_gy
            gx -= delta_gx

        p0.moving(delta_t, gx, gy)
        p0.display()
