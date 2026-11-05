# link-budget-intervals

## Français

Expliquer les marges radio avec hypothèses incertaines.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m link_budget_intervals examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Friis et conversion C/N0 vers Eb/N0 avec arithmétique d’intervalles monotones ; toutes les hypothèses de puissance, gains et bruit sont fournies.

### Limites

Espace libre, bornes indépendantes, pas de météo ni validation d’un modem ou liaison réelle. Les dépendances entre bornes peuvent rendre le résultat conservateur.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Explain radio margins under uncertain assumptions.

Synthetic data; no network access or secret required.

```sh
python -m link_budget_intervals examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Friis and C/N0 to Eb/N0 conversion using monotone interval arithmetic; all power, gain and noise assumptions are supplied.

### Limits

Free space, independent bounds, no weather or actual modem/link validation. Dependencies between bounds can make results conservative.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Explicar márgenes de radio con hipótesis inciertas.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m link_budget_intervals examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Friis y conversión C/N0 a Eb/N0 con aritmética de intervalos monótonos; se aportan potencia, ganancias y ruido.

### Límites

Espacio libre, cotas independientes, sin meteorología ni validación de módem o enlace real. Dependencias entre cotas pueden volver conservador el resultado.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.itu.int/rec/R-REC-P.525/en
