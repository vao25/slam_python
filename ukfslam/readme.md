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
