import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def berechne_seitenkante_theta(n, a, theta):
    theta_rad = math.radians(theta)
    R = a / (2 * math.sin(math.pi / n))
    s = R / math.sin(theta_rad)
    return s

def berechne_seitenkante_phi(n, a, phi):
    phi_rad = math.radians(phi)
    R = a / (2 * math.sin(math.pi / n))
    s = R / math.cos(phi_rad)
    return s

def berechne_hoehe_phi(n, a, phi):
    phi_rad = math.radians(phi)
    R = a / (2 * math.sin(math.pi / n))
    h = R * math.tan(phi_rad)
    return h

def berechne_hoehe_theta(n, a, theta):
    theta_rad = math.radians(theta)
    R = a / (2 * math.sin(math.pi / n))
    h = R * math.cos(theta_rad)
    return h

def zeichne_pyramide(n, a, h):
    # Berechne die Eckpunkte der Grundfläche
    winkel = 2 * math.pi / n
    grundflaeche = [
        (math.cos(i * winkel) * a / (2 * math.sin(math.pi / n)),
         math.sin(i * winkel) * a / (2 * math.sin(math.pi / n)), 0)
        for i in range(n)
    ]

    # Spitze der Pyramide
    spitze = (0, 0, h)

    # Erstelle die 3D-Darstellung
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Zeichne die Grundfläche
    grundflaeche_x = [p[0] for p in grundflaeche] + [grundflaeche[0][0]]
    grundflaeche_y = [p[1] for p in grundflaeche] + [grundflaeche[0][1]]
    grundflaeche_z = [p[2] for p in grundflaeche] + [grundflaeche[0][2]]
    ax.plot(grundflaeche_x, grundflaeche_y, grundflaeche_z, label='Grundfläche', color='blue')

    # Zeichne die Seitenflächen
    faces = []
    for punkt in grundflaeche:
        faces.append([punkt, spitze])

    # Füge die Seitenflächen hinzu
    for face in faces:
        poly = Poly3DCollection([face], facecolors='orange', edgecolors='r', alpha=0.5)
        ax.add_collection3d(poly)

    # Achsenbeschriftung
    ax.set_xlabel('X-Achse')
    ax.set_ylabel('Y-Achse')
    ax.set_zlabel('Z-Achse')
    ax.legend()
    plt.show()


def main():
    print("Willkommen zum Pyramiden-Seitenkanten-Rechner!")
    modus = input("Möchten Sie mit dem Neigungswinkel der Seitenkanten (Theta) oder dem Winkel der Seitenflächen (Phi) arbeiten? (Geben Sie 'theta' oder 'phi' ein): ").strip().lower()

    if modus not in ['theta', 'phi']:
        print("Ungültige Eingabe. Bitte starten Sie das Programm neu und geben Sie 'theta' oder 'phi' ein.")
        return

    n = int(input("Anzahl der Ecken des Grundflächen-Polygons (z. B. 3, 4, 5): "))
    a = float(input("Seitenlänge der Grundfläche: "))

    if modus == 'theta':
        theta = float(input("Neigungswinkel der Seitenkante (in Grad): "))
        h = berechne_hoehe_theta(n, a, theta)
    else:
        phi = float(input("Winkel der Seitenflächen zur Grundfläche (in Grad): "))
        h = berechne_hoehe_phi(n, a, phi)

    print(f"Die Höhe der Pyramide beträgt: {h:.2f} Einheiten.")
    zeichne_pyramide(n, a, h)

if __name__ == "__main__":
    main()
