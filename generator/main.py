from generators import generate_random_clusters_starmap, generate_random_sphere_starmap


def generate_clusters():
    generate_random_clusters_starmap(14, 700, 40, 10, 25, 3)
    generate_random_clusters_starmap(14, 700, 45, 10, 25, 3)
    generate_random_clusters_starmap(14, 700, 50, 10, 25, 3)
    generate_random_clusters_starmap(14, 700, 55, 10, 25, 3)

    generate_random_clusters_starmap(7, 350, 25, 10, 25, 3)
    generate_random_clusters_starmap(7, 350, 30, 10, 25, 3)
    generate_random_clusters_starmap(7, 350, 35, 10, 25, 3)
    generate_random_clusters_starmap(7, 350, 40, 10, 25, 3)
    generate_random_clusters_starmap(7, 350, 45, 10, 25, 3)
    generate_random_clusters_starmap(7, 350, 50, 10, 25, 3)

    generate_random_clusters_starmap(7, 175, 15, 10, 25, 3)
    generate_random_clusters_starmap(7, 175, 20, 10, 25, 3)
    generate_random_clusters_starmap(7, 175, 25, 10, 25, 3)
    generate_random_clusters_starmap(7, 175, 30, 10, 25, 3)


def generate_spheres():
    generate_random_sphere_starmap(14, 700, 35, 25)
    generate_random_sphere_starmap(14, 700, 40, 25)
    generate_random_sphere_starmap(14, 700, 45, 25)
    generate_random_sphere_starmap(14, 700, 50, 25)

    generate_random_sphere_starmap(7, 350, 25, 25)
    generate_random_sphere_starmap(7, 350, 30, 25)
    generate_random_sphere_starmap(7, 350, 35, 25)
    generate_random_sphere_starmap(7, 350, 40, 25)
    generate_random_sphere_starmap(7, 350, 45, 25)

    generate_random_sphere_starmap(7, 250, 20, 25)
    generate_random_sphere_starmap(7, 250, 25, 25)
    generate_random_sphere_starmap(7, 250, 30, 25)

    generate_random_sphere_starmap(7, 150, 15, 25)
    generate_random_sphere_starmap(7, 150, 20, 25)
    generate_random_sphere_starmap(7, 150, 25, 25)


if __name__ == "__main__":
    generate_clusters()
    generate_spheres()
