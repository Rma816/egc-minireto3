# Diario TDD

## Ciclo 1

### Red
- Prueba añadida: `test_one_feature_is_tiny`.
- Técnica de diseño de pruebas empleada: caso mínimo representativo.
- Motivo de elegir este caso: una característica es el menor modelo válido y
	establece la primera categoría.
- Fallo observado: `classify_model_size()` lanzaba `NotImplementedError`.

### Green
- Código mínimo escrito: `return "tiny"`.
- Resultado de las pruebas: el caso de una característica pasó.

### Refactor
- Mejora realizada, o motivo por el que no era necesaria: No fue necesaria; la
	implementación mínima no tenía duplicación ni estructura que simplificar.

## Ciclo 2

### Red
- Prueba añadida: `test_zero_features_is_invalid`, que exige un `ValueError`
	para cero características.
- Técnica de diseño de pruebas empleada: caso inválido representativo.
- Motivo de elegir este caso: un número menor que uno no representa un modelo
	válido y debe rechazarse antes de clasificarlo.
- Fallo observado: la implementación devolvía `tiny` en lugar de lanzar una
	excepción.

### Green
- Código mínimo escrito: validación `feature_count < 1` seguida de la
	clasificación existente de `tiny`.
- Resultado de las pruebas: pasan el caso de una característica y el caso
	inválido.

### Refactor
- Mejora realizada, o motivo por el que no era necesaria: No fue necesaria;
	la validación quedó expresada de forma directa.

## Ciclo 3

### Red
- Pruebas añadidas: los límites 5/6, 15/16 y 30/31.
- Técnica de diseño de pruebas empleada: pruebas de valores frontera.
- Motivo de elegir estos casos: cada pareja comprueba el último valor de una
	categoría y el primero de la siguiente.
- Fallo observado: los valores posteriores a 5 seguían devolviendo `tiny`.

### Green
- Código mínimo escrito: condiciones ordenadas para `tiny`, `small`,
	`medium` y `large`.
- Resultado de las pruebas: toda la batería pasa.

### Refactor
- Mejora realizada, o motivo por el que no era necesaria: No fue necesaria;
	las condiciones son pequeñas, ordenadas y legibles.

## Ciclo 4

### Red
- Prueba modificada: los casos de frontera se agruparon en una prueba
	parametrizada con `pytest.mark.parametrize`.
- Técnica de diseño de pruebas empleada: parametrización de una misma
	estructura de aserción.
- Motivo de elegir este caso: reduce repetición sin perder ninguno de los
	límites relevantes.
- Fallo observado: no se esperaba un nuevo fallo; fue un refactor de pruebas
	después de comprobar el comportamiento.

### Green
- Código mínimo escrito: no se modificó la implementación.
- Resultado de las pruebas: toda la batería sigue pasando.

### Refactor
- Mejora realizada, o motivo por el que no era necesaria: se eliminaron las
	pruebas individuales redundantes y se conservaron separadas las pruebas de
	clasificación inválida.
