import math

def berechne_seitenkante_theta(n, a, theta):
    """
    Berechnet die Seitenkante mit dem Neigungswinkel der Seitenkanten.
    
    Parameter:
    n (int): Anzahl der Ecken des Grundflächen-Polygons.
    a (float): Seitenlänge der Grundfläche.
    theta (float): Neigungswinkel der Seitenkante (in Grad).
    
    Rückgabe:
    float: Länge der Seitenkante.
    """
    theta_rad = math.radians(theta)
    R = a / (2 * math.sin(math.pi / n))
    s = R / math.sin(theta_rad)
    return s

def berechne_seitenkante_phi(n, a, phi):
    """
    Berechnet die Seitenkante mit dem Winkel der Seitenflächen zur Grundfläche.
    
    Parameter:
    n (int): Anzahl der Ecken des Grundflächen-Polygons.
    a (float): Seitenlänge der Grundfläche.
    phi (float): Winkel der Seitenflächen zur Grundfläche (in Grad).
    
    Rückgabe:
    float: Länge der Seitenkante.
    """
    phi_rad = math.radians(phi)
    R = a / (2 * math.sin(math.pi / n))
    s = R / math.cos(phi_rad)
    return s

def main():
    print("Willkommen zum Pyramiden-Seitenkanten-Rechner!")
    print("Sie können wählen, ob Sie mit dem Neigungswinkel der Seitenkanten oder dem Winkel der Seitenflächen arbeiten möchten.")
    
    # Auswahl des Modus
    modus = input("Möchten Sie mit dem Neigungswinkel der Seitenkanten (Theta) oder dem Winkel der Seitenflächen (Phi) arbeiten? (Geben Sie 'theta' oder 'phi' ein): ").strip().lower()

    if modus not in ['theta', 'phi']:
        print("Ungültige Eingabe. Bitte starten Sie das Programm neu und geben Sie 'theta' oder 'phi' ein.")
        return

    # Gemeinsame Eingaben
    n = int(input("Anzahl der Ecken des Grundflächen-Polygons (z. B. 3, 4, 5): "))
    a = float(input("Seitenlänge der Grundfläche: "))

    if modus == 'theta':
        theta = float(input("Neigungswinkel der Seitenkante (in Grad): "))
        seitenkante = berechne_seitenkante_theta(n, a, theta)
    else:
        phi = float(input("Winkel der Seitenflächen zur Grundfläche (in Grad): "))
        seitenkante = berechne_seitenkante_phi(n, a, phi)

    print(f"\nDie Länge der Seitenkante beträgt: {seitenkante:.2f} Einheiten.")

if __name__ == "__main__":
    main()
