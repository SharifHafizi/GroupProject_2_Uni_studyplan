# ============================
#  DEL 2 – Studieplan-system
# ============================

class Emne:
    def __init__(self, kode, navn, semester, studiepoeng):
        self._kode = kode.upper()
        self.navn = navn
        self.semester = semester.upper()  # "H" for høst, "V" for vår
        self.studiepoeng = int(studiepoeng)

    @property
    def kode(self):
        """Gjør emnekoden skrivebeskyttet"""
        return self._kode

    def __str__(self):
        semnavn = "Høst" if self.semester == "H" else "Vår"
        return f"{self.kode} - {self.navn} ({semnavn}) - {self.studiepoeng} sp"


class Studieplan:
    def __init__(self, plan_id, tittel):
        self.plan_id = plan_id
        self.tittel = tittel
        self.semestre = [[] for _ in range(6)]  # 6 tomme semestre

    def legg_til_emne(self, emne, semnr):
        if semnr < 1 or semnr > 6:
            print("Semester må være mellom 1 og 6.")
            return
        # sjekk at semesteret stemmer
        if (emne.semester == "H" and semnr not in [1, 3, 5]) or \
           (emne.semester == "V" and semnr not in [2, 4, 6]):
            print(f"{emne.kode} kan bare legges i et {emne.semester}-semester.")
            return
        # sjekk om plass
        total = sum(e.studiepoeng for e in self.semestre[semnr-1])
        if total + emne.studiepoeng > 30:
            print("Ikke plass i semesteret (maks 30 sp).")
            return
        if emne in self.semestre[semnr-1]:
            print("Emnet finnes allerede i dette semesteret.")
            return
        self.semestre[semnr-1].append(emne)
        print(f"{emne.kode} lagt til i semester {semnr} i {self.tittel}.")

    def fjern_emne(self, kode):
        for sem in self.semestre:
            for e in sem:
                if e.kode == kode:
                    sem.remove(e)
                    print(f"{kode} fjernet fra {self.tittel}.")
                    return
        print(f"{kode} finnes ikke i {self.tittel}.")

    def skriv_ut(self):
        print(f"\nStudieplan: {self.tittel} ({self.plan_id})")
        for i, sem in enumerate(self.semestre, start=1):
            sem_type = "Høst" if i in [1,3,5] else "Vår"
            total = sum(e.studiepoeng for e in sem)
            print(f"\nSemester {i} ({sem_type}):")
            if sem:
                for e in sem:
                    print("  ", e)
            else:
                print("  Ingen emner.")
            print(f"  Totalt: {total} sp")
        print("-" * 40)

    def er_gyldig(self):
        gyldig = True
        for i, sem in enumerate(self.semestre, start=1):
            total = sum(e.studiepoeng for e in sem)
            if total != 30:
                print(f"Semester {i} har {total} sp: Ikke gyldig (bør ha 30).")
                gyldig = False
        if gyldig:
            print("Studieplanen er gyldig!")


# ==========================================
# Globale lister
# ==========================================
alle_emner = []
alle_studieplaner = []


# ==========================================
# Funksjoner
# ==========================================

def lag_nytt_emne():
    kode = input("Emnekode:F.eks(INFO100) ").strip().upper()
    if any(e.kode == kode for e in alle_emner):
        print("Emnet finnes allerede!")
        return
    navn = input("Navn på emnet:F.eks(info in programming) ").title()

    semester = input("Semester (H/V): ").strip().upper()
    if semester not in ["H", "V"]:
        print("Ugyldig semester! Bruk H for høst eller V for vår.")
        return
    try:
        poeng = int(input("Studiepoeng: "))
    except ValueError:
        print("Ugyldig antall studiepoeng!")
        return

    alle_emner.append(Emne(kode, navn, semester, poeng))
    print(f"Emnet {kode} ble opprettet!")


def skriv_ut_alle_emner():
    if not alle_emner:
        print("Ingen emner registrert.")
        return
    print("\nAlle registrerte emner:")
    for e in alle_emner:
        print(" ", e)


def lag_ny_studieplan():
    plan_id = input("Studieplan-ID: ").strip()
    tittel = input("Tittel: ").title()
    alle_studieplaner.append(Studieplan(plan_id, tittel))
    print(f"Ny studieplan '{tittel}' opprettet!")


def velg_studieplan():
    if not alle_studieplaner:
        print("Ingen studieplaner finnes.")
        return None
    print("\nTilgjengelige studieplaner:")
    for i, sp in enumerate(alle_studieplaner, start=1):
        print(f"{i}. {sp.tittel} ({sp.plan_id})")
    try:
        valg = int(input("Velg studieplan: ")) - 1
        return alle_studieplaner[valg]
    except (ValueError, IndexError):
        print("Ugyldig valg.")
        return None


def legg_til_emne_i_plan():
    plan = velg_studieplan()
    if not plan:
        return
    if not alle_emner:
        print("Ingen emner registrert.")
        return
    kode = input("Emnekode: ").strip().upper()
    emne = next((e for e in alle_emner if e.kode == kode), None)
    if not emne:
        print("Fant ikke emnet.")
        return
    try:
        semnr = int(input("Semester (1–6): "))
    except ValueError:
        print("Ugyldig semester.")
        return
    plan.legg_til_emne(emne, semnr)


def fjern_emne_fra_plan():
    plan = velg_studieplan()
    if not plan:
        return
    kode = input("Emnekode som skal fjernes: ").strip().upper()
    plan.fjern_emne(kode)


def skriv_ut_studieplan():
    plan = velg_studieplan()
    if plan:
        plan.skriv_ut()


def sjekk_studieplan_gyldighet():
    plan = velg_studieplan()
    if plan:
        plan.er_gyldig()


def finn_studieplaner_med_emne():
    kode = input("Emnekode: ").strip().upper()
    funnet = False
    for sp in alle_studieplaner:
        for sem in sp.semestre:
            if any(e.kode == kode for e in sem):
                print(f"- {sp.tittel} ({sp.plan_id})")
                funnet = True
                break
    if not funnet:
        print("Ingen studieplaner bruker dette emnet.")


def lagre_til_fil():
    with open("DATA120_Host_25_opgavep/Oppgave10_GP/data.txt", "w", encoding="utf-8") as f:
        f.write("[EMNER]\n")
        for e in alle_emner:
            f.write(f"{e.kode};{e.navn};{e.semester};{e.studiepoeng}\n")
        f.write("[STUDIEPLANER]\n")
        for sp in alle_studieplaner:
            f.write(f"{sp.plan_id};{sp.tittel}\n")
            for sem in sp.semestre:
                f.write(";".join(e.kode for e in sem) + "\n")
    print("Data lagret til data.txt!")


def les_fra_fil():
    global alle_emner, alle_studieplaner
    try:
        with open("DATA120_Host_25_opgavep/Oppgave10_GP/data.txt", "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        alle_emner.clear()
        alle_studieplaner.clear()

        i = 1
        # Les emner
        while i < len(lines) and lines[i] != "[STUDIEPLANER]":
            if lines[i]:
                kode, navn, sem, sp = lines[i].split(";")
                alle_emner.append(Emne(kode, navn, sem, sp))
            i += 1
        i += 1  # hopp over [STUDIEPLANER]
        # Les studieplaner
        while i < len(lines):
            if not lines[i]:
                i += 1
                continue
            plan_id, tittel = lines[i].split(";")
            sp = Studieplan(plan_id, tittel)
            for j in range(6):
                i += 1
                if i >= len(lines):
                    break
                sem_line = lines[i].strip()
                if sem_line:
                    koder = sem_line.split(";")
                    for k in koder:
                        emne = next((e for e in alle_emner if e.kode == k), None)
                        if emne:
                            sp.semestre[j].append(emne)
            alle_studieplaner.append(sp)
            i += 1
        print("Data lest fra data.txt!")
    except FileNotFoundError:
        print("Filen finnes ikke!")


# ==========================================
# Hovedmeny
# ==========================================

def hovedmeny():
    while True:
        print("\n--- MENY ---")
        print("1. Lag et nytt emne")
        print("2. Legg til et emne i en studieplan")
        print("3. Fjern et emne fra en studieplan")
        print("4. Skriv ut ei liste over alle registrerte emner")
        print("5. Lag en ny tom studieplan")
        print("6. Skriv ut en studieplan")
        print("7. Sjekk om en studieplan er gyldig")
        print("8. Finn hvilke studieplaner som bruker et oppgitt emne")
        print("9. Lagre til fil")
        print("10. Les fra fil")
        print("11. Avslutt")
        valg = input("Velg et tall (1–11): ")

        if valg == "1":
            lag_nytt_emne()
        elif valg == "2":
            legg_til_emne_i_plan()
        elif valg == "3":
            fjern_emne_fra_plan()
        elif valg == "4":
            skriv_ut_alle_emner()
        elif valg == "5":
            lag_ny_studieplan()
        elif valg == "6":
            skriv_ut_studieplan()
        elif valg == "7":
            sjekk_studieplan_gyldighet()
        elif valg == "8":
            finn_studieplaner_med_emne()
        elif valg == "9":
            lagre_til_fil()
        elif valg == "10":
            les_fra_fil()
        elif valg == "11":
            print("Avslutter programmet.")
            break
        else:
            print("Ugyldig valg.")


# ==========================================
# Start programmet
# ==========================================
if __name__ == "__main__":
    hovedmeny()
