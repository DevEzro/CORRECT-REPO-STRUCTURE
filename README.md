# CORRECT-REPO-STRUCTURE
Un repositorio que simula la estructura correcta de un repositorio, desde el init hasta el release, pasando por el desarrollo, las pruebas y las mejoras

## RAMAS
- Cada rama se encarga de una fase en concreto del desarrollo:
  - ### main
    Es la rama principal donde se encuentra el c´doigo estable y listo para producción
  - ### dev
    Es la rama de desarrollo donde se integran las nuevas características del proyecto
  - ### test
    Se validan las funcionalidades para comprobar su correcto funcionamiento antes de integrarlas en `main` o `dev`
  - ### feature
    Rama temporal para desarrollar una funcionalidad nueva, basándose en `dev` y que se fusiona con ella antes de ser eliminada.
  - ### release
    Sirve para preparar una nueva versión del software antes de lanzarse. Se realizan pruebas finales y pequeñas mejoras
  - ### hotfix
    Se corrigen errores críticos en producción y se crea a partir de `main`. Al solucionarse se vuelve a fusiona tanto en `dev` como en  `main`