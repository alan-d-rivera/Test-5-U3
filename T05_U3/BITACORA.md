# Bitácora


| Fecha | Predicción / decisión | Cambio | Prueba y evidencia | Commit |

| 05/11/2026 | Se predice que u(L) = 0.300 [mm] sera identico en las tres mallas de 2, 4 y 8 debidoi a la constacia de las cargas. | Refinamiento de la malla a 2, 4 y 8 elementos en la configuracion del modelo. | Ejecucion de "python src/ejecutar.py". Se obtuvo u(L) = 0.300000 mm, reaccion R0 = -40000 N y residuo numerico de equilibrio menor a 10^-11. | refinamiento de malla 2, 4 y 8 elementos |

| 05/11/2026 | Se predice una tasa de convergencia de orden cuadratico O(h^2) para el error absoluto en puntos medios al duplicar el numero de elementos. | Implementacion de la funcion analitica u_ref(x) y la funcion del error absoluto maximo en puntos medios dentro del archivo "src/analisis.py" | Evaluacion de errores absolutos en puntos medios: n=2 es 0.006250 mm , n=4 es 0.001563 mm  y n=8 es 0.000391 mm. | solucion analitica y calculo de error cuadratico |

| 05/11/2026 | Imponer la restriccion u(L) = 0 convertira la barra en un sistema hiperestatico, fijando el desplazamiento en x = L a 0 mm y generando una reaccion adicional RL. | Aplicacion de la restriccion u(L)=0 manteniendo constantes las cargas P y q. | Salida con u(L)=0.0000 mm, R0=-10000 N, RL=-30000 N. Verificacion de equilibrio R0+RL+P+qL=0. | test: evaluacion de restriccion adicional u(L)=0 |