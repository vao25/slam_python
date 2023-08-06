## EKF-SLAM

Spuštění simulace modulem launch.py , např. pomocí terminálu otevřeného v adresáři ekfslam_v1:
```
python3 launch.py
```

I přes veškerou snahu nefunguje výsledná realizace bohužel ideálně. Občas se objeví následující chybová hláška. Aby nebylo zbytečně zabíráno místo,
je cesta k adresáři *ekfslam_v1* a Python balíčkům zkrácena na ... ; dále je chybová hláška uvedena zhruba až od půlky - od posledního přepsaného modulu:

```console
user@localhost:/.../ekfslam_v1$ python3 launch.py
Traceback (most recent call last):
  ...
  File "/.../ekfslam_v1/KF_joseph_update.py", line 23, in KF_joseph_update
    PSD_check= np.linalg.cholesky(P)
  File "<__array_function__ internals>", line 200, in cholesky
  File "/.../python3.8/site-packages/numpy/linalg/linalg.py", line 756, in cholesky
    r = gufunc(a, signature=signature, extobj=extobj)
  File "/.../python3.8/site-packages/numpy/linalg/linalg.py", line 92, in_raise_linalgerror_nonposdef
    raise LinAlgError("Matrix is not positive definite")
  numpy.linalg.LinAlgError: Matrix is not positive definite
```

Dočasným řešením je simulaci spustit znovu, protože tato chyba nenastává v každém případě.
