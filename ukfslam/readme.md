## UKF-SLAM

Spuštění simulace modulem launch.py , např. pomocí terminálu otevřeného v adresáři ukfslam:
```
python3 launch.py
```

Situace je hořší než v případě EKF-SLAMu. Zobrazuje se téměř totožná chyba (tedy kontrola, zda-li je matice **P** pozitivně definitní, selže). V tomto případě však simulace neproběhne nikdy.  Chyba jako v předchozím výpisu znovu ukázána jen ve zkrácené verzi, tedy cesta k adresáři *ukfslam* a Python balíčkům zkrácena na ... ; dále je chybová hláška uvedena zhruba až od půlky - od posledního přepsaného modulu:
```console
user@localhost:/.../ukfslam$ python3 launch.py
Traceback (most recent call last):
  ...
  File "/.../ukfslam/unscented_update.py", line 87, in unscented_update
    PSD_check = np.linalg.cholesky(P)
  File "<__array_function__ internals>", line 200, in cholesky
  File "/.../python3.8/site-packages/numpy/linalg/linalg.py", line 756, in cholesky
    r = gufunc(a, signature=signature, extobj=extobj)
  File "/.../python3.8/site-packages/numpy/linalg/linalg.py", line 92, in _raise_linalgerror_nonposdef
    raise LinAlgError("Matrix is not positive definite")
  numpy.linalg.LinAlgError: Matrix is not positive definite
```

Snaha o nalezení chyby způsobující tento problém bohužel nedopadla úspěšně. Z časových důvodů nebylo možné zůstat na místě a nepostupovat dále, proto je tento problém alespoň takto zdokumentován. Řešení by možná poskytlo srovnání každého jednotlivého originálního *m* skriptu s odpovídajícím přepsaným modulem v Pythonu pro stejné vstupní hodnoty. Bohužel tento velmi rozsáhlý opravný krok se již nestihl vykonat. Možná, ale asi málo pravděpodobná varianta je, že se nějaká knihovní metoda v Pythonu chová trochu jinak než v MATLABu (např. výše uvedená *numpy.linalg.cholesky(P)* a její ekvivalent v MATLABu *chol(P) )* .

### AKTUALIZACE 22. 8.

**Již funguje**: chyba nalezena a odstraněna. Nastala skutečně výše zmíněná varianta, kdy metoda *numpy.linalg.cholesky(P)* počítá trochu jinak než její ekvivalent v MATLABu *chol(P)* a to sice, že MATLAB k výpočtu využívá diagonálu a horní trojúhelníkovou část matice **P**, kdežto *numpy.linalg.cholesky(P)* diagonálu a dolní trojúhelníkovou část. NumPy metoda neumožňuje přepnutí typu výpočtu, proto byl použit ekvivalent z modulu SciPy *scipy.linalg.cholesky()*. Ten má parametr, kterým typ výpočtu lze nastavit (počítá tedy stejným způsobem jako v MATLABu). Výše zmíněné je také uvedeno v příslušných dokumentacích:

https://www.mathworks.com/help/matlab/ref/chol.html

https://numpy.org/doc/stable/reference/generated/numpy.linalg.cholesky.html

https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.cholesky.html
