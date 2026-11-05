"""Complete las dos funciones antes de ejecutar el estudio."""
import numpy as np


def desplazamiento_referencia(x, L, E, A, P, q):
    """u(0)=0, EA*u'(L)=P, q uniforme. Devuelva un array en mm."""
    EA = E * A
    x_arr = np.asarray(x, dtype=float)
    return ((P + q * L) * x_arr - 0.5 * q * (x_arr ** 2)) / EA


def error_puntos_medios(resultado, L, E, A, P, q):
    """Devuelva el maximo error absoluto de u_h frente a u_ref en puntos medios.
    No basta comparar los nodos: interpole u_h linealmente en cada elemento.
    """
    # Extraer nodos y desplazamientos del diccionario u objeto resultado
    if isinstance(resultado, dict):
        nodos = resultado.get('nodos', resultado.get('x'))
        u_h = resultado.get('u', resultado.get('desplazamientos'))
    else:
        nodos = getattr(resultado, 'nodos', getattr(resultado, 'x'))
        u_h = getattr(resultado, 'u', getattr(resultado, 'desplazamientos'))

    nodos = np.asarray(nodos, dtype=float)
    u_h = np.asarray(u_h, dtype=float)

    # 1. Coordenadas de los puntos medios de cada elemento
    x_medios = (nodos[:-1] + nodos[1:]) / 2.0

    # 2. Interpolación lineal de MEF en el punto medio de cada elemento
    u_h_medios = (u_h[:-1] + u_h[1:]) / 2.0

    # 3. Solución de referencia exacta calculada en los puntos medios
    u_ref_medios = desplazamiento_referencia(x_medios, L, E, A, P, q)

    # 4. Error absoluto máximo entre nodos en mm
    return float(np.max(np.abs(u_h_medios - u_ref_medios)))
