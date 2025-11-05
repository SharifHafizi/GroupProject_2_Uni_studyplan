DAT120 øving 10: Gruppeprosjekt del 2
Læringsmål
Dere skal lære å jobbe med en litt større programmeringsoppgave i grupper. Dere skal lære
grunnleggende bruk av Git og Github. Dere skal lære hvordan å videreutvikle et program som
dere jobbet med for en liten stund siden. Merk at oppgavene her vil være på et litt mer
overordnet nivå enn tidligere.
Overordnet oppgavebeskrivelse
Emne- og studieplanrevisjon er en prosess som skjer hver høst. Studieprogramlederne og de
som underviser emnene ser på de ulike emnene og studieprogrammene våre og ser om det er
noe som skal endres, både i studieprogrammene og i de enkelte emnene. Mange av emnene
brukes på flere studieprogrammer, og en endring i ett emne kan derfor påvirke mange
studieprogrammer. Dette gjelder særlig om et emne flyttes fra høst til vår eller motsatt.
Dette prosjektet går ut på å lage et forenklet system for å lagre og redigere studieplaner. I del 2
skal dere utvide systemet fra del 1 ved å bruke klasser og objekter samt håndtere flere ulike
studieprogrammer.
Oppgaver
I del 2 av prosjektet skal dere utvide programmet på følgende vis:
a) Klasse for emner: I stedet for å lagre emnedata i flere lister skal dere lage en klasse for
et emne og lagre emnene i ei enkelt liste. Emneklassen skal i tillegg til emnekode,
semester og studiepoeng inneholde et navn på emnet. Hvis dere ønsker kan dere også
legge til flere ting slik som eksamensform og emnebeskrivelse. Skriv om kode fra del 1
slik at den behandler emne-objekter i stedet for flere lister. Tenk over hvilke av
funksjonene dere lagde i del 1 som bør være metoder i emneklassen og hvilke som
fortsatt skal være vanlige funksjoner.
Merk at semester i Emne-klassen skal være «H» for høst og «V» for vår. Samme emne kan
fint gå i 1. semester i ett studieprogram og i 3. semester i et annet studieprogram, men
kan ikke gå i 1. semester (et høstsemester) i ett studieprogram og 2. semester (et
vårsemester) i et annet studieprogram.
b) Flere studieplaner: Lag en klasse for en studieplan. En studieplan skal ha en id, en tittel
og lister med emner for hvert semester tilsvarende studieplanen fra del 1. Tenk over
hvilke av funksjonene dere lagde i del 1 som bør være metoder i studieplan-klassen og
hvilke som fortsatt skal være vanlige funksjoner.
c) Lag nye og oppdaterte menyvalg: Se den nye menyen oppgitt under, med beskrivelse av
menyvalgene. Merk at alle emnelister fra del 1 skal bruke Emne-objekter i stedet for de
tidligere løsningene for å lagre referanser til emner eller data om emner. Merk at alle
menyvalg som i del 1 handlet om det ene studieprogrammet nå skal la brukeren velge
studieprogram og skal bruke objekter av studieplan-klassen.
d) Frivillig: Gjør emnekode til en egenskap i emne-klassen som bare kan leses og ikke
redigeres etter at emnet er opprettet.
Menyvalg for del 2:
Her er menyvalgene for det endelige systemet.
1. Lag et nytt emne
2. Legg til et emne i en studieplan
3. Fjern et emne fra en studieplan
4. Skriv ut ei liste over alle registrerte emner
5. Lag en ny tom studieplan
6. Skriv ut en studieplan med hvilke emner som er i hvert semester
7. Sjekk om en studieplan er gyldig eller ikke
8. Finn hvilke studieplaner som bruker et oppgitt emne
9. Lagre emnene og studieplanene til fil
10. Les inn emnene og studieplanene fra fil
11. Avslutt
12. Frivillig: Slett et emne fra lista over emner
13. Frivillig: Legg til et anbefalt valgemne i en studieplan
14. Frivillig: Fjern et anbefalt valgemne fra en studieplan
15. Frivillig: Legg til et annet valgemne i en studieplan
16. Frivillig: Fjern et annet valgemne fra en studieplan
17. Frivillig: Rediger et emne
18. Frivillig: Legg til en studieretning til en studieplan
19. Frivillig: Fjern en studieretning fra en studieplan
20. Frivillig: Slett en studieplan fra lista over studieplaner
21. Frivillig: Flytt et emne til et annet semester i en studieplan
22. Frivillig: Endre tittel til en studieplan
Beskrivelse av hvert valg
1. Lag et nytt emne: Emnene skal lagres som objekter av klassen Emne i ei liste med slike
objekter. Ellers som del 1
2. Legg til et emne i en studieplan: Brukeren skal få velge hvilken studieplan emnet skal
legges til, ellers som del 1. Et emne kan legges til flere studieplaner.
3. Fjern et emne fra en studieplan: Som frivillig menyvalg 10 fra del 1 bortsett fra at
brukeren skal velge hvilket studieprogram emnet skal fjernes fra.
4. Skriv ut ei liste over alle registrerte emner: Som del 1 bortsett fra bruk av Emne-klasse
5. Lag en ny tom studieplan: En studieplan skal minimum ha en id, en tittel, og lister med
emner for hvert semester tilsvarende studieplanen fra del 1. Emnelistene skal starte
tomme.
6. Skriv ut en studieplan med hvilke emner som er i hvert semester: Brukeren skal oppgi
hvilken studieplan som skal skrives ut, ellers som del 1.
7. Sjekk om en studieplan er gyldig eller ikke: Brukeren skal oppgi hvilken studieplan
som skal sjekkes, ellers som del 1.
8. Finn hvilke studieplaner som bruker et oppgitt emne: Brukeren skal oppgi emnekode
til et emne og så skal systemet skrive ut tittel på alle studieplaner som bruker dette
emnet.
9. Lagre emnene og studieplanene til fil
10. Les inn emnene og studieplanene fra fil
11. Avslutt
12. Frivillig: Slett et emne fra lista over emner
13. Frivillig: Legg til et anbefalt valgemne i en studieplan: En studieplan skal ha et antall
studiepoeng reservert til valgemner og ei liste med anbefalte valgemner. De anbefalte
valgemnene må ha samme semester som studiepoengene reservert til valgemner. For
typiske ingeniørprogrammer er studiepoengene reservert til valgemner i 5. semester, og
de anbefalte valgemnene må da være høst-emner.
14. Frivillig: Fjern et anbefalt valgemne fra en studieplan
15. Frivillig: Legg til et annet valgemne i en studieplan: Studieplanene skal ha separate
lister for anbefalte valgemner og andre valgemner. Andre valgemner må også være i riktig
semester, se punkt 13.
16. Frivillig: Fjern et annet valgemne fra en studieplan
17. Frivillig: Rediger et emne: Brukeren skal få anledning til å redigere minimum emnenavn
og semester til et emne. Hvis brukeren skifter semester skal emnet fjernes fra alle
studieprogram som bruker emnet og systemet skal skrive ut hvilke studieprogrammer
dette er og at alle disse studieprogrammene må oppdateres.
18. Frivillig: Legg til en studieretning til en studieplan: En studieplan med ulike
studieretninger har en gruppe emner som er felles for alle studieretningene og en gruppe
emner som er ulike for hver studieretning. Sjekk for eksempel studieplanen for bachelor i
elektroteknologi med to studieretninger. Det enkleste er kanskje å definere noen
semestre som felles og noen semestre som ulike.
19. Frivillig: Fjern en studieretning fra en studieplan
20. Frivillig: Slett en studieplan fra lista over studieplaner
21. Frivillig: Flytt et emne til et annet semester i en studieplan: Semesteret som emnet
flyttes til må fortsatt vær et gyldig semester for emnet. For eksempel et høstemne kan
flyttes til 1., 3. og 5. semester, men ikke til 2., 4. eller 6. semester.
22. Frivillig: Endre tittel til en studieplan
Godkjenning
Denne øvingen skal gjøres i grupper på inntil 4 studenter. Dere skal i utgangspunktet bruke de
samme gruppene som for øving 7. Øvingen skal godkjennes ved å demonstrere det gruppa har
lagd på samme vis som for de tidligere øvingene. I tillegg skal dere vise studentassistenten
Github repo-et deres. Denne øvingen og øving 7 skal godkjennes bare en gang for hver gruppe,
dere kan demonstrere en gang og så får alle i gruppa godkjent. Så mange medlemmer av gruppa
som mulig skal være med når øvingen godkjennes, men hvis et medlem av gruppa ikke kan av en
eller annen grunn trenger dere ikke å være helt fulltallige.
