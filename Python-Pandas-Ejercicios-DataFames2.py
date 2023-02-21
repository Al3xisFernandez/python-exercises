from __init__ import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
def hechos():
    pass#,inplace=True
    print(f'''
    ● Crear un objeto de la clase `DataFrame`.
    ● Especificar nombres de índices arbitrarios a un objeto `DataFrame`.
    ● Crear un `DataFrame` a partir de listas varias.
    ● Crear un `DataFrame` a partir de Pandas Series.
    ● Crear un `DataFrame` a partir de una matriz (lista de listas) Python.
    ● Crear un `DataFrame` a partir de un diccionario Python.
    ● Crear un `DataFrame` a partir de una lista de  diccionarios Python.
    ● Crear un `DataFrame` a partir de arreglos *NumPy* y genera columnas e índices.
    ● Crear un arreglos *NumPy* a partir de un `DataFrame`.
    ● Obtener los ejes (atributos de filas y columnas) de un `DataFrame`.
    ● Obtener los nombres de las filas y las columnas de un `DataFrame`.
    ● Obtener un reporte con la información básica de un objeto `DataFrame`.
    ● Obtener estadísticas básicas en un objeto `DataFrame` con la función `describe`.
    ● Renombrar una columna de un `DataFrame` con la función `rename`.
    ● Seleccionar filas de un `DataFrame` a partir su composición.
    ● Usando las funciones `.iloc()` y `.loc()` 
    ● Escriba un programa Pandas para invertir el orden usando notación de slicing:
                                                        de las columnas de un `DataFrame` dado.
                                                        de las filas de un `DataFrame` dado.
                                                        de las filas reseteando el index de un `DataFrame` dado.
    ● Seleccionar columnas de un objeto `DataFrame` usando notación de slicing.
    ● Seleccionar filas de 2 en dos y resetea el index de un objeto `DataFrame` usando notación de slicing.
    ● Seleccionar todas las columnas de un `DataFrame`, excepto una en particular usando `loc`.
    ● Seleccionar los primeros, ultimos y resto `n` registros (filas) de un objeto `DataFrame` usando `iloc`.
    ● Remover las últimas `n` filas (registros) de un objeto `DataFrame` usando `iloc`.
    ● Obtener la posición numérica de una columna a partir de su nombre con `get_loc`.
    ● Seleccionar filas de un `DataFrame` a partir su posición con `take`.
    ● Seleccionar columnas de un `DataFrame` y colocalo como index con `set_index('X')`.
    ● Obtener los elementos entre el array seleccionando y un range, una serie y un df utiliza la función `isin`.
    ● Seleccionar los registros donde las columnas de un `DataFrame` tengan los mismos valores.
    ● Seleccionar los registros donde las columnas de un `DataFrame` tengan valores entre 2 y 4 utiliza la función `between`.
            limites no incluidos
            limmites incluidos
    ● Obtener un `DataFrame` tengan fechas en un periodo de dias ajustable por 5 columnas en cada registro diario.
    ● Combinar varios objetos  `Series` en un `DataFrame` con la función `concat` () 
    ● Combinar dos objetos `DataFrame` con la función `concat` () 
    ● Obtener los ejes (atributos de filas y columnas) de un `DataFrame` luego de indexar con ['a', 'b', 'c', 'd', 'e'] .
    ● Confirmar si hay o no Nan en el `DataFrame`.
    ● Contar los elementos que son nulos (NaN) en el `DataFrame` usando la función `.isnull()` o `.isna()`que son alias.
    ● Reemplazar los NaN (nulo) con un valor específico usando las funciones `.fillna()` por 0 y por la media `.meam()`.
    ● Eliminar filas o registros con la función `DataFrame`.drop`.
    ● Eliminar registros que no cumplan con una condición sobre una columna específica.
    ● Calcular el promedio, la mediana, el maximo, el minimo y el producto 
        de cada fila (axis 0) y
        de cada columna (axis 1) 
        usando `.mean()`, `.median()`, `.max()` `.min()` y `.product()`.
    ● Calcular la transpuesta de un objeto `DataFrame` con `transpose()` o `T`.
    ● Regenera el index del `DataFrame` con la función `reset_index`
        1) Sin convertir los índices anteriores en una columna.
        2) Convertir los índices anteriores en una columna nueva.
    ● Obtener los tipos de datos de las columnas de un `DataFrame`.
    ● Obtener los las columnas de un `DataFrame` segun el critero posterior.
    ● Calcular el número de tipos de datos por cada categoría con `df.dtypes.value_counts()`.
    ● Convertir una columna de tipo string - cadena de caracteres a fecha con `to_datetime`.
    ● Obtenerar una `Serie` y un `DataFrame` con  fechas desde 1ro de enero de 2023 a 15 de enero de 2023 (ambos inclusive).
            utiliza las función `date_range`
            selecciona un periodo determinado con la función ` `between`
    ● Usar `first` y `last` para obtener los primeros y últimos registros para una cantidad de días arbitraria.
    ● Obtener las columnas de un determinado tipo de dato con 'select_dtypes'.
    ● Seleccionar registros que cumplan con una hora específica con `at_time`.
    ● Seleccionar un conjunto de registros a partir de un rango horario.
    ● Redondear valores reales con la función `DataFrame`.round`.
    ● Eliminar filas o columnas con la función `DataFrame`.drop`
        sobre selecciones directa, index,columns, loc e iloc
    ● Eliminar una columna con pop
    ● Eliminar duplicados `DataFrame`.drop_duplicates`
        selecciona una columna y compara
        selecciona mas de una columna y compara
        elimina el segundo duplicado
        elimina el primer duplicado keep='last')
    ● Dado un `DataFrame` genara in index con la función `set_index` .
    ● Dado un `DataFrame` genara in index con la función `set_index` sobre tres columnas
        selecciona elementos con xs
        utiliza level
    ● Encontrar la cantidad de elementos únicos por cada fila y columna con `nunique`.
    ● Reiniciar un índice numérico después de eliminar algunos registros con `reset_index`.
    ● Agregar un add_prefix y add_suffix a las columnas de un objeto `DataFrame`.
    ● Obtener los datos de una columna como una lista Python con `tolist`.
    ● Truncar un `DataFrame` por filas y columnas con la función `truncate`.
    ● Agregar una nueva columna a un `DataFrame` por medio de la función `assign`.
    ● Agregar una columna en una posición específica con la función `DataFrame`.insert`.
    ● Seleccionar el índice de una columna de un `DataFrame` con el elemento mayor.
    ● Comprobar en `DataFrame` con el operador Python `in` 
        si existe una fila 'a' y otra 'z'.
        si existe una columna 'X' y otra 'A'.
    ● Comprobar si una columna existe en un `DataFrame` con el operador Python `in`.
    ● Reemplazar valores en un `DataFrame` con la función `replace`.
    ● Eliminar valores infinitos (`-np.inf` y `np.inf`) de un `DataFrame` con `replace`.
    ● Ordenar los valores de las columnas de un `DataFrame` con `sort_values`.
    ● Ordenar los índices de un `DataFrame` con la función `sort_index`.
    ● Verificar con `equals` si dos objetos `DataFrame` contienen los mismos elementos.
    ● Obtener de un `DataFrame` los `n` registros 
        menores  con `nsmallest`.
        mayores  con `nlargest`.
    ● Cambiar el tipo de una columna de `float` a `int` con la función `astype`.
    ● Usar la función `agg` para realizar varias operaciones por un eje de un `DataFrame`.
    ● Selecciona los elementos de un `DataFrame` con `applymap`
    ● Selecciona los elementos de un `DataFrame` con `apply`
    ● Transformar los valores de un `DataFrame` con la función `transform`.
    ● Usar las funciones `all` y `any` sobre un objeto `DataFrame`.
    ● Incrementar el número de filas y columnas visibles de un `DataFrame`
    ● Usar `groupby` para agrupar datos por una columna específica y contar la cantidad de elementos.
    ● Escriba un programa Pandas para fusionar conjuntos de datos y verificar la unicidad.
    ● scriba un programa Pandas para fusionar conjuntos de datos con join entre dos `DataFrames`.
    ● Genera una consulta con la función cut dado un `DataFrame` con datos en una columna que tenemos que convertir 
            a otros categóricos segun condiciones enunciadas.
    ● Genera una consulta con la función `filter()`. 
    ● Genera una consulta con la función `query()` con mas de un filtro. 
    ● Selecciona los datos unicos de la columna Y.
    ● Encontrar registros de un `DataFrame` que cumplan una condición de métodos string respecto a una columna.
    ● Obtener los registros donde el `nombre` empiece con `A`.
    ● Obtener los registros donde el `nombre` empiece ya sea por `A` , `M` o `R`.
    ● Obtener los registros donde el `apellido` de un empleado no contengan *g*.
    ● Obtener los registros con la función `melt`.
    ● Calcula la correlación entre columnas con el método `.corr()`.
    ● Obtener los registros con la función `.isin()` e `.iterrows()`
    ● Seleciona de un objeto `DataFrame` la informacion númerica con la función select_dtypes.
    ● Mostrar el uso de memoria de un `DataFrame` dado y cada columna de este.
        cambiar los tipos de datos y volver a chequear el uso de memoria

    Parámetro	Descripción
            datos	        Los datos toman varias formas como ndarray, series, mapas, listas, dict, constantes y también otro `DataFrame`
            artículos	    eje = 0
            eje principal	eje = 1
            eje menor	    eje = 2
            dtype	        Un tipo de datos de cada columna.
            Copiar	        Copiar datos Predeterminado, falso
        ''')
    def Solución():
        pass
    #######################################################################################################
    atributos_de_un_df=['_accessors', '_accum_func', '_add_numeric_operations', '_agg_by_level', '_agg_examples_doc', '_agg_summary_and_see_also_doc', 
                        '_align_frame', '_align_series', '_append', '_arith_method', '_as_manager', '_attrs', '_box_col_values', '_can_fast_transpose', 
                        '_check_inplace_and_allows_duplicate_labels', '_check_inplace_setting', '_check_is_chained_assignment_possible', 
                        '_check_label_or_level_ambiguity', '_check_setitem_copy', '_clear_item_cache', '_clip_with_one_bound', '_clip_with_scalar', 
                        '_cmp_method', '_combine_frame', '_consolidate', '_consolidate_inplace', '_construct_axes_dict', '_construct_axes_from_arguments', 
                        '_construct_result', '_constructor', '_constructor_sliced', '_convert', '_count_level', '_data', '_dir_additions', '_dir_deletions', 
                        '_dispatch_frame_op', '_drop_axis', '_drop_labels_or_levels', '_ensure_valid_index', '_find_valid_index', '_flags', '_from_arrays', 
                        '_get_agg_axis', '_get_axis', '_get_axis_name', '_get_axis_number', '_get_axis_resolvers', '_get_block_manager_axis', '_get_bool_data', 
                        '_get_cleaned_column_resolvers', '_get_column_array', '_get_index_resolvers', '_get_item_cache', '_get_label_or_level_values', 
                        '_get_numeric_data', '_get_value', '_getitem_bool_array', '_getitem_multilevel', '_gotitem', '_hidden_attrs', '_indexed_same', '_info_axis', 
                        '_info_axis_name', '_info_axis_number', '_info_repr', '_init_mgr', '_inplace_method', '_internal_names', '_internal_names_set', '_is_copy', 
                        '_is_homogeneous_type', '_is_label_or_level_reference', '_is_label_reference', '_is_level_reference', '_is_mixed_type', '_is_view', 
                        '_iset_item', '_iset_item_mgr', '_iset_not_inplace', '_item_cache', '_iter_column_arrays', '_ixs', '_join_compat', '_logical_func', 
                        '_logical_method', '_maybe_cache_changed', '_maybe_update_cacher', '_metadata', '_mgr', '_min_count_stat_function', '_needs_reindex_multi', 
                        '_protect_consolidate', '_reduce', '_reduce_axis1', '_reindex_axes', '_reindex_columns', '_reindex_index', '_reindex_multi', 
                        '_reindex_with_indexers', '_rename', '_replace_columnwise', '_repr_data_resource_', '_repr_fits_horizontal_', '_repr_fits_vertical_', 
                        '_repr_html_', '_repr_latex_', '_reset_cache', '_reset_cacher', '_sanitize_column', '_series', '_set_axis', '_set_axis_name', 
                        '_set_axis_nocheck', '_set_is_copy', '_set_item', '_set_item_frame_value', '_set_item_mgr', '_set_value', '_setitem_array', 
                        '_setitem_frame', '_setitem_slice', '_slice', '_stat_axis', '_stat_axis_name', '_stat_axis_number', '_stat_function', 
                        '_stat_function_ddof', '_take', '_take_with_is_copy', '_to_dict_of_blocks', '_typ', '_update_inplace', '_validate_dtype', 
                        '_values', '_where'] 
    atributos_de_un_df_211=['abs', 'add', 'add_prefix', 'add_suffix', 'agg', 'aggregate', 'align', 'all', 'any', 'append', 'apply', 'applymap', 
                        'asfreq', 'asof', 'assign', 'astype', 'at', 'at_time', 'attrs', 'axes', 'backfill', 'between_time', 'bfill', 'bool', 'boxplot', 
                        'clip', 'columns', 'combine', 'combine_first', 'compare', 'convert_dtypes', 'copy', 'corr', 'corrwith', 'count', 'cov', 'cummax', 
                        'cummin', 'cumprod', 'cumsum', 'describe', 'diff', 'div', 'divide', 'dot', 'drop', 'drop_duplicates', 'droplevel', 'dropna', 
                        'dtypes', 'duplicated', 'empty', 'eq', 'equals', 'eval', 'ewm', 'expanding', 'explode', 'ffill', 'fillna', 'filter', 'first', 
                        'first_valid_index', 'flags', 'floordiv', 'from_dict', 'from_records', 'ge', 'get', 'groupby', 'gt', 'head', 'hist', 'iat', 
                        'idxmax', 'idxmin', 'iloc', 'index', 'infer_objects', 'info', 'insert', 'interpolate', 'isetitem', 'isin', 'isna', 'isnull', 
                        'items', 'iteritems', 'iterrows', 'itertuples', 'join', 'keys', 'kurt', 'kurtosis', 'last', 'last_valid_index', 'le', 'loc', 
                        'lookup', 'lt', 'mad', 'mask', 'max', 'mean', 'median', 'melt', 'memory_usage', 'merge', 'min', 'mod', 'mode', 'mul', 'multiply', 
                        'ndim', 'ne', 'nlargest', 'notna', 'notnull', 'nsmallest', 'nunique', 'pad', 'pct_change', 'pipe', 'pivot', 'pivot_table', 'plot', 
                        'pop', 'pow', 'prod', 'product', 'quantile', 'query', 'radd', 'rank', 'rdiv', 'reindex', 'reindex_like', 'rename', 'rename_axis', 
                        'reorder_levels', 'replace', 'resample', 'reset_index', 'rfloordiv', 'rmod', 'rmul', 'rolling', 'round', 'rpow', 'rsub', 
                        'rtruediv','sample', 'select_dtypes', 'sem', 'set_axis', 'set_flags', 'set_index', 'shape', 'shift', 'size', 
                        'skew', 'slice_shift', 'sort_index', 'sort_values', 'squeeze', 'stack', 'std', 'style', 'sub', 'subtract', 'sum', 'swapaxes', 
                        'swaplevel', 'tail', 'take', 'to_clipboard',  'to_csv', 'to_dict', 'to_excel', 'to_feather', 'to_gbq', 'to_hdf', 'to_html', 
                        'to_json', 'to_latex', 'to_markdoen', 'to_numpy', 'to_orc', 'to_parquet', 'to_period', 'to_pickle', 'to_records', 'to_sql', 
                        'to_stata', 'to_string', 'to_timestamp', 'to_xarray', 'to_xml', 'transform', 'transpose', 'truediv', 'truncate', 'tz_convert', 
                        'tz_localize', 'unstack', 'update', 'value_counts', 'values', 'var', 'where', 'xs']
    #'abs', 'add', 'add_prefix', 'add_suffix', 'agg', 'aggregate', 'align', 'all', 'any', 'append', 'apply', 'applymap', 'asfreq', 'asof', 'assign', 'astype', 'at', 'at_time', 'attrs', 'axes', 'backfill', 'between_time', 'bfill', 'bool', 'boxplot', 'clip', 'columns', 'combine', 'combine_first', 'compare', 'convert_dtypes', 'copy', 'corr', 'corrwith', 'count', 'cov', 'cummax', 'cummin', 'cumprod', 'cumsum', 'describe', 'diff', 'div', 'divide', 'dot', 'drop', 'drop_duplicates', 'droplevel', 'dropna', 'dtypes', 'duplicated', 'empty', 'eq', 'equals', 'eval', 'ewm', 'expanding', 'explode', 'ffill', 'fillna', 'filter', 'first', 'first_valid_index', 'flags', 'floordiv', 'from_dict', 'from_records', 'ge', 'get', 'groupby', 'gt', 'head', 'hist', 'iat', 'idxmax', 'idxmin', 'iloc', 'index', 'infer_objects', 'info', 'insert', 'interpolate', 'isetitem', 'isin', 'isna', 'isnull', 'items', 'iteritems', 'iterrows', 'itertuples', 'join', 'keys', 'kurt', 'kurtosis', 'last', 'last_valid_index', 'le', 'loc', 'lookup', 'lt', 'mad', 'mask', 'max', 'mean', 'median', 'melt', 'memory_usage', 'merge', 'min', 'mod', 'mode', 'mul', 'multiply', 'ndim', 'ne', 'nlargest', 'notna', 'notnull', 'nsmallest', 'nunique', 'pad', 'pct_change', 'pipe', 'pivot', 'pivot_table', 'plot', 'pop', 'pow', 'prod', 'product', 'quantile', 'query', 'radd', 'rank', 'rdiv', 'reindex', 'reindex_like', 'rename', 'rename_axis', 'reorder_levels', 'replace', 'resample', 'reset_index', 'rfloordiv', 'rmod', 'rmul', 'rolling', 'round', 'rpow', 'rsub', 'rtruediv', 'sample', 'select_dtypes', 'sem', 'set_axis', 'set_flags', 'set_index', 'shape', 'shift', 'size', 'skew', 'slice_shift', 'sort_index', 'sort_values', 'squeeze', 'stack', 'std', 'style', 'sub', 'subtract', 'sum', 'swapaxes', 'swaplevel', 'tail', 'take', 'to_clipboard', 'to_csv', 'to_dict', 'to_excel', 'to_feather', 'to_gbq', 'to_hdf', 'to_html', 'to_json', 'to_latex', 'to_markdoen', 'to_numpy', 'to_orc', 'to_parquet', 'to_period', 'to_pickle', 'to_records', 'to_sql', 'to_stata', 'to_string', 'to_timestamp', 'to_xarray', 'to_xml', 'transform', 'transpose', 'truediv', 'truncate', 'tz_convert', 'tz_localize', 'unstack', 'update', 'value_counts', 'values', 'var', 'where', 'xs']
    def Solución():
        pass
    print (atributos_de_un_df,len(atributos_de_un_df_211))
    print(f'''
    ● Crear un objeto de la clase `DataFrame`.
    ''')
    ## Solución.
    datos = {'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 1], 'Z': [2, 3, 5, 7, 11]}
    df = pd.DataFrame(datos)
    print(f"df:\n{df}")
    print("*"*100)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Especificar nombres de índices arbitrarios a un objeto `DataFrame`.
    ''')
    def Solución():
        pass
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos, index=indices)
    print(f"df.loc['c']=\n{df.loc['c']}")
    print(f"{type(df.loc['c'])=}")
    print("*"*100)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Crear un `DataFrame` a partir de listas varias.
    ''')
    lista_col = ['X', 'Y']
    lista_index = ['a', 'b']
    lista_datos = [[3, 2], [7,3]] 
    df = pd.DataFrame(data=lista_datos, columns = lista_col, index = lista_index) 
    #------------------------------------------------------------------------------------------------------
    print(f"df=\n{df}")
    pausa()
    #######################################################################################################
    print(f'''
    ● Crear un `DataFrame` a partir de Pandas Series.
    ''')
    series = {   'X': pd.Series([3, 2], 
                        index = ['a','b']), 
                 'Y': pd.Series([7, 3], 
                        index = ['a','b'])} 
    df = pd.DataFrame(data=series)
    #------------------------------------------------------------------------------------------------------
    print(f"df=\n{df}")
    pausa()
    #######################################################################################################
    print(f'''
    ● Crear un `DataFrame` a partir de una matriz (lista de listas) Python.
    ''')
    def Solución():
        pass
    matriz = [['X', 'Y'], [3, 2], [7, 3]]
    encabezado = matriz.pop(0)
    df = pd.DataFrame(data=matriz, columns=encabezado)
    #------------------------------------------------------------------------------------------------------
    print(f"df=\n{df}")
    pausa()
    #######################################################################################################
    print(f'''
    ● Crear un `DataFrame` a partir de un diccionario Python.
    ''')
    def Solución():
        pass
    dic = {'X':[3, 2], 'Y':[7, 3]}
    df = pd.DataFrame(data=dic, index=['a','b'])
    #------------------------------------------------------------------------------------------------------
    print(f"df=\n{df}")
    pausa()
    #######################################################################################################
    print(f'''
    ● Crear un `DataFrame` a partir de una lista de  diccionarios Python.
    ''')
    def Solución():
        pass
    dic = [{'X':3,'Y': 2},{'X':7, 'Y':3}]
    df = pd.DataFrame(data=dic, index=['a','b'])
    #------------------------------------------------------------------------------------------------------
    print(f"df=\n{df}")
    pausa()
    #######################################################################################################
    print(f'''
    ● Crear un `DataFrame` a partir de arreglos *NumPy* y genera columnas e índices.
    ''')
    def Solución():
        pass
    dtype = [('Columna1', 'int32'), ('Columna2', 'float32'), ('Columna3', 'float64')]
    np_arreglo = np.zeros(15, dtype=dtype)
    indices = [f'Indice-{i}' for i in range(1, len(np_arreglo) + 1)]
    df = pd.DataFrame(data=np_arreglo,index=indices)
    #------------------------------------------------------------------------------------------------------
    print(f"df=\n{df}")
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Crear un arreglos *NumPy* a partir de un `DataFrame`.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 1], 'Z': [2, 3, 5, 7, 11]}
    df = pd.DataFrame(data=datos)
    print(f"df=\n{df}")
    np_=df.to_numpy()
    print(f"np_=\n{np_}\n{type(np_)}")
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Obtener los ejes (atributos de filas y columnas) de un `DataFrame`.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 1], 'Z': [2, 3, 5, 7, 11]}
    df = pd.DataFrame(data=datos)
    print(f"df=\n{df}")
    print(f"df.axes=\n{df.axes}")
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Obtener los nombres de las filas y las columnas de un `DataFrame`.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 1], 'Z': [2, 3, 5, 7, 11]}
    df = pd.DataFrame(data=datos)
    print(f"{df.index=}")
    print(f"{df.columns=}")
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos, index=indices)
    print(f"{df.index=}")
    print(f"{df.columns=}")
    print("*"*100)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Obtener un reporte con la información básica de un objeto `DataFrame`.
    ''')
    def Solución():
        pass
    lenguajes = ['Python', 'Java', 'C#', 'JavaScript', 'C++', 'PHP']
    año_creacion = [1990, 1995, 2013, 1995, 1985, 1995]
    interpretado = [True, False, False, True, False, True]
    extension = ['.py', '.java', 'cs', 'js', 'cpp', 'php']
    indices = ['a', 'b', 'c', 'd', 'e', 'f']
    datos = {'lenguaje': lenguajes, 'año_creacion': año_creacion, 'interpretado': interpretado, 'extesion': extension}
    df = pd.DataFrame(data=datos, index=indices)
    print(f"df={df}")
    print(f"{df.columns=}")
    print(f"{df.index=}")
    print(f"df.info:{df.info}")
    print("*"*100)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Obtener estadísticas básicas en un objeto `DataFrame` con la función `describe`.
    ''')
    def Solución():
        pass
    nombre = ['Oliva', 'Daniela', 'Juan', 'Germán', 'Edward', 'Alex', 'Julio',  'Edgar', 'Angie', 'Irlesa']
    puntaje = [11.5, 8, 15.5, np.nan, 8, 19, 13.5, np.nan, 8, 18]
    intentos = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
    califico = ['Sí', 'No', 'Sí', 'No', 'No', 'Sí', 'Sí', 'No', 'No', 'Sí']
    indices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    jugadores = {'nombre': nombre, 'puntaje': puntaje, 'intentos': intentos,  'califico': califico}
    df = pd.DataFrame(data=jugadores, index=indices)
    print("df.describe()=\n",df.describe())
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Renombrar una columna de un `DataFrame` con la función `rename`.
    ''')
    def Solución():
        pass
    lenguajes = ['Python', 'Java', 'C#', 'JavaScript', 'C++', 'PHP']
    año_creacion = [1990, 1995, 2013, 1995, 1985, 1995]
    interpretado = [True, False, False, True, False, True]
    extension = ['.py', '.java', 'cs', 'js', 'cpp', 'php']
    indices = ['a', 'b', 'c', 'd', 'e', 'f']
    datos = {'lenguaje': lenguajes, 'año_creacion': año_creacion, 'interpretado': interpretado, 'extesion': extension}
    df = pd.DataFrame(data=datos, index=indices)
    print(f"df={df}")
    print(f"{df.columns=}")
    print(f"{df.index=}")
    print(f"df.info:{df.info}")
    print("*"*100)
    #------------------------------------------------------------------------------------------------------
    df=df.rename(columns={'año_creacion': 'Creación','extesion':'extesión','año_creacion':'Creación'})
    print(f"df={df}")
    print(f"{df.columns=}")
    print(f"{df.index=}")
    print(f"df.info:{df.info}")
    print("*"*100)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Seleccionar filas de un `DataFrame` a partir su composición.
    ''')
    datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    ww=df.Y>=3
    print(f"df.Y>=3=\n",ww)
    ww=df[df.Y>=3]
    print(f"df[df.Y>=3]=\n",ww)
    #------------------------------------------------------------------------------------------------------
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Usando las funciones `.iloc()` y `.loc()` 
    nota:
        df.iloc[0:3]                        # `Filas` Primera a tercera y `Columnas`       todas
        df.iloc[0:3,  : ]                   # `Filas` Primera a tercera y `Columnas`       todas       
        df.iloc[ : , 0:4]                   # `Filas`       todas       y `Columnas` cero  a cuarta
        df.iloc[       [0,2,4]]             # `Filas`       todas       y `Columnas` cero, segunda y cuarta
        df.iloc[[0:3], [0,2,4]]             # `Filas` Primera a tercera y `Columnas` cero, segunda y cuarta
        df.iloc[[0,2,4]]                    # `Filas` Primera a tercera y `Columnas` cero, segunda y cuarta
        df.iloc[ :   , [0,2,4]]             # `Filas`       todas       y `Columnas` cero, segunda y cuarta    
        
        1) Seleccionar las primeras `f` filas de un objeto `DataFrame`.
                de fila de inicio a 'f1'.
                `f1`, `f2` y `f3`.
                de `f1` a `f3`.            
        2) Seleccionar las primeras `c` columnas de un objeto `DataFrame`.
                de columna de inicio a 'c1'.'.
                `c1`, `c2` y `c3`.
                de `c1` a `c3`.
        2) Obtener un `nuevo `DataFrame` desde la seleccion de  filas y columnas de un objeto `DataFrame`.
                de fila de inicio a 'f1' y de columna de inicio a 'c1'.
                `f1`, `f2` y `f3` y `c1`, `c2` y `c3`.
                de `f1` a `f3` y de `c1` a `c3`.
    ''')
    def Solución():
        pass
    nombre =    ['Oliva', 'Daniela', 'Juan', 'Germán', 'Edward', 'Alex', 'Julio', 'Edgar', 'Angie', 'Irlesa']
    puntaje =   [11.5, 8, 15.5, np.nan, 8, 19, 13.5, np.nan, 8, 18]
    intentos =  [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
    califico =  ['Sí', 'No', 'Sí', 'No', 'No', 'Sí', 'Sí', 'No', 'No', 'Sí']
    indices =   ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    jugadores = {'nombre': nombre, 'puntaje': puntaje, 'intentos': intentos, 'califico': califico}
    df = pd.DataFrame(data=jugadores, index=indices)
    print("*"*54)
    print("*",'iloc'.center(50),"*")
    print("*"*54)
    print(f"df=\n{df}")
    print(f"df.iloc[:3]=\n{df.iloc[:3]}")# ~                    df.iloc[:3,:]}
    print(f"df.iloc[0:3]=\n{df.iloc[1:3]}")# ~                  df.iloc[0:3,:]
    print(f"df.iloc[[0,3]]=\n{df.iloc[[0,3]]}")# ~              df.iloc[[0,3],:]}
    print(f"df.iloc[[0,2,5]]=\n{df.iloc[[0,2,5]]}")# ~          df.iloc[[0,2,5],:]}
    print(f"df.iloc[-5:]=\n{df.iloc[-5:]}")# ~                  df.iloc[-5:,:]
    print("*"*50)
    print(f"df.iloc[:,:2]=\n{df.iloc[:,:2]}")
    print(f"df.iloc[:,1:3]=\n{df.iloc[:,1:3]}")
    print(f"df.iloc[:[0,2]]=\n{df.iloc[:,[0,2]]}")
    print(f"df.iloc[:,[0,2,3]]=\n{df.iloc[:,[0,2,3]]}")
    print(f"df.iloc[0,0:2]=\n{df.iloc[0,0:2]}")
    print("*"*50)
    print(f"df.iloc[:,2]=\n{df.iloc[:2,:2]}")
    print(f"df.iloc[1:3,1:3]=\n{df.iloc[1:3,1:3]}")   
    print(f"df.iloc[[0,3],[0,3]]=\n{df.iloc[[0,3],[0,3]]}")
    print(f"df.iloc[-5:,[0,2,3]]=\n{df.iloc[-5:,[0,2,3]]}")
    pausa()
    #------------------------------------------------------------------------------------------------------
    print("*"*54)
    print("*",'loc'.center(50),"*")
    print("*"*54)
    '''
    nota:
        df.loc[  : ,          :       ]     # `Filas`       todas               y `Columnas`      todas
        df.loc[ 0:3,          :       ]     # `Filas`    cero a tercera         y `Columnas`      todas
        df.loc[ 0:3,    'Name': 'sex' ]     # `Filas`    cero a tercera         y `Columnas` 'Name' a 'sex'
        df.loc[ 0:3,   ['name', 'sex']]     # `Filas`    cero a tercera         y `Columnas` 'Name' y 'sex'
        df.loc[  :  ,   'name': 'sex' ]     # `Filas`       todas               y `Columnas` 'Name' a 'sex'
        df.loc[  :    ,['name', 'sex']]     # `Filas`       todas               y `Columnas` 'Name' y 'sex'
        df.loc[[1,3,4], 'name': 'sex' ]     # `Filas` Primera, tercera y cuarto y `Columnas` 'Name' a 'sex'
        df.loc[[1,3,4],['name', 'sex']]     # `Filas` Primera, tercera y cuarto y `Columnas` 'Name' y 'sex'
        df.loc[df.loc[:, 'sex'] == 'male']
    '''
    print(f"df=\n{df}")
    print(f"df.loc[:'d']=\n{df.loc[:'d']}")# ~                      df.loc[:'d',:]}
    print(f"df.loc['a':'d']=\n{df.loc['b':'d']}")# ~                df.loc['a':'d',:]
    print(f"df.loc[['a','d']]=\n{df.loc[['a','d']]}")# ~            df.loc[['a','d'],:]}
    print(f"df.loc[['a','c','e']]=\n{df.loc[['a','c','e']]}")# ~    df.loc[['a','c',5],:]}
    print("*"*50)
    print(f"df.loc[:,:'intentos']=\n{df.loc[:,:'intentos']}")
    print(f"df.loc[:,'b':'califico']=\n{df.loc[:,'puntaje':'califico']}")
    print(f"df.loc[:['nombre','intentos']]=\n{df.loc[:,['nombre','intentos']]}")
    print(f"df.loc[:,['nombre','intentos','califico']]=\n{df.loc[:,['nombre','intentos','califico']]}")
    print(f"df.loc['a','nombre':'intentos']=\n{df.loc['a','nombre':'intentos']}")
    print("*"*50)
    print(f"df.loc[:,'intentos']=\n{df.loc[:'c',:'intentos']}")
    print(f"df.loc['b':'d','puntaje':'d']=\n{df.loc['b':'d','puntaje':'califico']}")
    print(f"df.loc[['a','d'],['a','d']]=\n{df.loc[['a','d'],['nombre','califico']]}")
    pausa()
    #------------------------------------------------------------------------------------------------------
    print("*"*54)
    print("*",'loc'.center(50),"*")
    print("*"*54)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    print(f"df.intentos=\n{df.nombre}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    print(f"df.intentos.c=\n{df.nombre.c}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)    
    ww = df.loc[df.intentos < 2, 'intentos'] = 0
    print("df.loc[df.intentos < 2, 'intentos']=",ww)
    print("-"*100)
    ww = df.loc[df.intentos >= 2, 'intentos'] = 1
    print("df.loc[df.intentos >= 2, 'intentos']=",ww)
    print("-"*100)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Escriba un programa Pandas para invertir el orden usando notación de slicing:
                                                        de las columnas de un `DataFrame` dado.
                                                        de las filas de un `DataFrame` dado.
                                                        de las filas reseteando el index de un `DataFrame` dado.
    ''')
    exam_data = {'col1': [1, 2, 3, 4, 7,11, 5, 9, 2,12], 
                 'col2': [4, 5, 1, 2, 3, 4, 7, 6, 9, 0], 
                 'col3': [7, 5, 8,12, 1,11, 7, 1, 5, 9]}
    etiquetas = ['a',  'b',  'c',  'd',  'e', 'f',  'g',  'h',  'i',  'j']
    df =pd.DataFrame(data=exam_data,index=etiquetas)
    print(f"df=\n",df)
    print("\nRevierta el orden de las columnas:")
    print(df.loc[:, ::-1])
    print("\nRevierta el orden de las filas:")
    print(df.loc[::-1])
    print("\nRevierta el orden de las filas y reseteando index:")
    print(df.loc[::-1].reset_index(drop = True))
    print("-"*100)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Seleccionar columnas de un objeto `DataFrame` usando notación de slicing.
    ''')
    def Solución():
        pass
    nombre =   ['Oliva', 'Daniela', 'Juan', 'Germán', 'Edward', 'Alex', 'Julio',  'Edgar', 'Angie', 'Irlesa']
    puntaje =  [11.5, 8, 15.5, np.nan, 8, 19, 13.5, np.nan, 8, 18]
    intentos = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
    califico = ['Sí', 'No', 'Sí', 'No', 'No', 'Sí', 'Sí', 'No', 'No', 'Sí']
    indices =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    jugadores = {'nombre': nombre, 'puntaje': puntaje, 'intentos': intentos,   'califico': califico}
    df = pd.DataFrame(data=jugadores, index=indices)
    print(f"df=\n{df}")
    ww=df[['nombre', 'califico']]
    print(f"df[['nombre', 'califico']]=\n",ww)
    ww= pd.DataFrame(df, columns=['nombre', 'califico'])
    print(f"pd.DataFrame(df, columns=['nombre', 'califico'])=\n",ww)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Seleccionar filas de 2 en 2 y resetea el index de un objeto `DataFrame` usando notación de slicing.
    ''')
    def Solución():
        pass
    nombre =   ['Oliva', 'Daniela', 'Juan', 'Germán', 'Edward', 'Alex', 'Julio',  'Edgar', 'Angie', 'Irlesa']
    puntaje =  [11.5, 8, 15.5, np.nan, 8, 19, 13.5, np.nan, 8, 18]
    intentos = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
    califico = ['Sí', 'No', 'Sí', 'No', 'No', 'Sí', 'Sí', 'No', 'No', 'Sí']
    indices =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    jugadores = {'nombre': nombre, 'puntaje': puntaje, 'intentos': intentos,   'califico': califico}
    df = pd.DataFrame(data=jugadores, index=indices)
    print(f"df=\n{df}")
    ww=df[::2].reset_index(drop = True)
    print(f"df[::2]=\n",ww)

    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Seleccionar todas las columnas de un `DataFrame`, excepto una en particular usando `loc`.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    ww = df.loc[:, df.columns != 'Y']
    print("*"*50)
    print(f"df.loc[:, df.columns != 'Y']=\n{ww}")
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Seleccionar los primeros, ultimos y resto `n` registros (filas) de un objeto `DataFrame` usando `iloc`.
    ''')
    datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    n=3
    ww = df.iloc[:n]
    print("*"*50)
    print(f"df.iloc[:{n}]=\n{ww}")
    #------------------------------------------------------------------------------------------------------
    n=3
    ww = df.iloc[-n:]
    print("*"*50)
    print(f"df.iloc[-{n}:]=\n{ww}")
    #------------------------------------------------------------------------------------------------------
    n=1
    ww = df.iloc[n:-n]
    print("*"*50)
    print(f"df.iloc[{n}:-{n}]=\n{ww}")
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Remover las últimas `n` filas (registros) de un objeto `DataFrame` usando `iloc`.
    ''')
    datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    n=1
    ww = df.iloc[n:-n]
    print("*"*50)
    print(f"df.iloc[:{n}]=\n{ww}")
    #------------------------------------------------------------------------------------------------------
    n=3
    ww = df.iloc[-n:]
    print("*"*50)
    print(f"df.iloc[-{n}:]=\n{ww}")
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Obtener la posición numérica de una columna a partir de su nombre con `get_loc`.
    ''')
    datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    print(f"df.columns.get_loc('X')=\n{df.columns.get_loc('X')}")
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Seleccionar filas de un `DataFrame` a partir su posición con `take`.
    ''')
    datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    ww=df.take([0, 3])        
    print(f"df.take([0, 3])=\n",ww)
    #------------------------------------------------------------------------------------------------------
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Seleccionar columnas de un `DataFrame` y colocalo como index con `set_index('X')`.
    ''')
    datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    ww=df.set_index('X')
    print(f"df.set_index('X')=\n",ww)
    #------------------------------------------------------------------------------------------------------
    ww=df.set_index(['X','Z'])
    print(f"df.set_index(['X','Z'])=\n",ww)
    #------------------------------------------------------------------------------------------------------
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Obtener los elementos entre el array seleccionando y un range, una serie y un df
    utiliza la función `isin`.
    ''')
    def Solución():
        pass
    df = pd.DataFrame({
                      'Name': ['John', 'Sam', 'Luna', 'Harry'],
                      'Age': [25, 45, 23, 32],
                      'Department': ['Sales', 'Engineering', 'Engineering', 'Human Resource']
                    })
    print(f"df=\n{df}")
    edad_base=20
    edad_fin=30
    rango = range(edad_base, edad_fin+1)
    ww = df[ df['Age'].isin(rango) ]
    print(f"range - df[ df['Age'].isin(range(edad_base, edad_fin+1)) ]=\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww = df[df[['Name','Department']].isin({'Name': ['Sam', 'Harry'], 'Department': ['Engineering','Human Resource']})]
    print("diccionario -  df[ df['Name','Department'].isin({'Name': ['Sam', 'Harry'], 'Department': ['Engineering','Human Resource']}) ]=\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww = df[df['Name'].isin(pd.Series(['John', 'Sam']))]
    print("serie - df[df['Name'].isin(pd.Series(['John', 'Sam']))]=\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    df_2 = pd.DataFrame({
                          'Name': ['John', 'Sam'],
                          'Department': ['Sales', 'Engineering']
                        })
    ww = df[df[['Name','Department']].isin(df_2)]
    print("df - df[df[['Name','Department']].isin(df_2)]=\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Seleccionar los registros donde las columnas de un `DataFrame` tengan los mismos valores.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 1], 'Z': [2, 3, 5, 7, 11]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos, index=indices)
    print(f"df=\n{df}")
    ww=df.where(df.X == df.Y)
    print(f"df.where(df.X == df.Y)=\n{ww}")
    ww=df.where(df.X == df.Y ,other =-df)
    print(f"df.where(df.X == df.Y)=\n{ww}")
    print("*"*100)
    #------------------------------------------------------------------------------------------------------ 
    filter1 = df.Y==3
    ww=df.where(filter1)#, inplace = True)
    print(f"df.Y==3=\n{ww}")
    ww=df.where(filter1, other=-df)#, inplace = True)
    print(f"df.Y==3=\n{ww}")
    print("*"*100)
    #------------------------------------------------------------------------------------------------------
    filter1 = df.Y % 2==0
    filter2 = df.Z <10
    ww=df.where(filter1 & filter2)#, inplace = True)
    print(f"df.where(df.Y % 2==0 & df.Z <10)=\n{ww}")
    ww=df.where(filter1 & filter2, other = -df.Y.mean())#, inplace = True)
    print(f"=\n{ww}")
    print("*"*100)
    #------------------------------------------------------------------------------------------------------
    ww = df['Y'].where(df['Y']<3, other='bajo')
    print(f"df['Y'].where(df['Y']>=3, other='bajo')=\n{ww}")
    print("*"*100)
    ww = df.where(df['Y']>df['Y'].mean(), other='Alto')
    print(f" df.where(df['Y']>df['Y'].mean(), other='Alto')=\n{ww}")
    print("*"*100)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Seleccionar los registros donde las columnas de un `DataFrame` tengan valores entre 2 y 4 utiliza la función `between`
        limites no incluidos
        limmites incluidos
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 1], 'Z': [2, 3, 5, 7, 11]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos, index=indices)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("-"*20,":)")
    ww=df[df.Y.between(2, 4)]
    print("df[df.Y.between(2, 4)]:\n ",ww)

    #------------------------------------------------------------------------------------------------------
    ww=df[df['Y'].between(2, 4, inclusive='both')]
    print("df[df.Y.between(2, 4)]  inclusive='both':\n ",ww)

    #------------------------------------------------------------------------------------------------------

    ww=df[df['Y'].between(2, 4, inclusive='neither')]
    print("df[df.Y.between(2, 4)]  inclusive='neither':\n ",ww)
    #------------------------------------------------------------------------------------------------------ 


    print("*"*100)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Obtener un `DataFrame` tengan fechas en un periodo de dias ajustable por 5 columnas en cada registro diario.
    Dataframe.shift(periods=0,frequency=none,axis=0)
    Los períodos representan la función de cambio de eje que se implementará y puede ser positiva o negativa.
    Deprecated La frecuencia representa los múltiples parámetros, como el desplazamiento de datos, timedelta,
        módulos de serie de tiempo y cadena de regla de tiempo.
    El eje representa 0 para representar filas y 1 para representar columnas.
    ''')
    def Solución():
        pass
    df = pd.DataFrame({"Col1": [10, 20, 15, 30, 45],
                       "Col2": [11, 23, 18, 30, 48],
                       "Col3": [12, 21, 19, 33, 38],
                       "Col4": [13, 27, 22, 11, 32],
                       "Col5": [14, 27, 10, 37, 52]},
                        index=pd.date_range("2023-01-01", "2023-01-05"))
    print(df.shift(0, axis = 0))
    print("*"*100)
    inicio =2
    print(df.shift(inicio, axis = 0))
    print("*"*100)
    inicio =-2
    print(df.shift(inicio, axis = 0))
    print("*"*100)
    df.index=pd.date_range("2023-06-01", periods = 5)
    print(df.shift(0, axis = 0))
    print(df.shift(0, axis = 1))
    print("*"*100)
    cantidad_de_registros=10
    df= pd.DataFrame(   np.random.randint(0,cantidad_de_registros*5,size=(cantidad_de_registros, 5)), 
                        columns=[f'Col_{num}' for num in range(1,6)]
                    )
    df.index=pd.date_range("2023-06-01", periods = cantidad_de_registros)
    print(df)
    print("*"*100)
    pausa()
    limpiar()
    print(f'''
    ● Combinar varios objetos  `Series` en un `DataFrame` con la función `concat` () 
    ''') 
    def Solucion():
        pass
    nombre=      pd.Series(  ['Anastasia', 'Anatolio', 'Katherine', 'Pepe', 'Gregorio', 'Tito', 'Luly', 'JJ ', 'Bebe', 'Bety'])
    puntuación=  pd.Series(  [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19])
    intentos=    pd.Series(  [1, 3, 2, 3, 2, 3, 1, 1, 2, 1])
    califico=    pd.Series(  ['sí', 'no', 'sí', 'no', 'no', 'sí', 'sí', 'no', 'no', 'sí'])
    etiquetas =  pd.Series(  ['a',  'b',  'c',  'd',  'e', 'f',  'g',  'h',  'i',  'j'])
    #------------------------------------------------------------------------------------------------------
    print("-"*20,":)")
    df= pd.DataFrame({'nombre':nombre,'puntuación':puntuación,"intentos":intentos,'califico':califico})
    df.index=etiquetas
    print(f"df=\n",df)  
    #------------------------------------------------------------------------------------------------------
    # ~ print("-"*20,":)")
    # ~ df = pd.DataFrame(nombre, puntuación,intentos, califico).reset_index()
    # ~ df.index=etiquetas
    # ~ print(f"df=\n",df)   
    #------------------------------------------------------------------------------------------------------
    print("-"*20,":)")
    df = pd.concat({'nombre':nombre,'puntuación':puntuación,'intentos':intentos,'califico':califico}, axis=1)
    df.index=etiquetas
    print(f"df=\n",df)
    #------------------------------------------------------------------------------------------------------
    print("-"*20,":)")
    df = pd.concat([nombre,puntuación,intentos,califico], axis=1)
    df.index=etiquetas
    df.columns=['nombre','puntuación','intentos','califico']
    print(f"df=\n",df)
    #------------------------------------------------------------------------------------------------------
    print("-"*20,":)")
    pausa()
    limpiar()

    #######################################################################################################
    print(f'''
    ● Combinar dos objetos `DataFrame` con la función `concat` () 
        deprecated `append`.    
        ''') 
    df_1 = pd.DataFrame({
                  'Name': ['John', 'Sam', 'Luna', 'Harry'],
                  'Age': [25, 45, 23, 32],
                  'Department': ['Sales', 'Engineering', 'Engineering', 'Human Resource']
                })
    print(f"df_1=\n{df_1}")
    df_2 = pd.DataFrame({
                      'Name': ['John', 'Sam'],
                      'Department': ['Sales', 'Engineering']
                    })
    print(f"df_2=\n{df_2}")
    ww = pd.concat([df_1, df_2], axis=0)
    print(f"pd.concat([df_1, df_2], axis=0)=\n",ww)
    #------------------------------------------------------------------------------------------------------
    ww = pd.concat([df_1, df_2], axis=1)
    print(f"pd.concat([df_1, df_2], axis=1)=\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Obtener los ejes (atributos de filas y columnas) de un `DataFrame` luego de indexar con ['a', 'b', 'c', 'd', 'e'] .
    ''') 
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 1], 'Z': [2, 3, 5, 7, 11]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos, index=indices)
    print(f"df=\n{df}")
    print(f"df.axes=\n{df.axes}")
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    Malditos NaN
    ● Confirmar si hay o no Nan en el `DataFrame`.
    ● Contar los elementos que son nulos (NaN) en el `DataFrame` usando la función `.isnull()` o `.isna()`que son alias.
    ● Reemplazar los NaN (nulo) con un valor específico usando las funciones `.fillna()` por 0 y por la media `.meam()`.
    ● Eliminar filas o registros con la función `DataFrame`.drop`.
    Ej el método dropna que elimina todas las filas (para axis=0) o todas las columnas (para axis=1) en las que hay valores perdidos. 
    Algunos de los argumentos de la función dropna son los siguientes:

        axis que especifica si se deben eliminar las filas (axis=0) o si se deben eliminar las columnas (axis=1)
        subset que especifica una lista de columnas para considerar los valores perdidos cuando axis=0
        inplace que especifica si se van a realizar cambios en el propio `DataFrame` existente
    ''')
    def Solución():
        pass
    nombre =   ['Oliva', 'Daniela', 'Juan', 'Germán', 'Edward', 'Alex', 'Julio', 'Edgar', 'Angie', 'Irlesa']
    puntaje =  [11.5, 8, 15.5, None, 8, 19, np.na, np.nan, 8, 18]
    intentos = [1, 3, 2, np.nan, 2, 3, None, 1, 2, 1]
    califico = ['Sí', 'No', 'Sí', 'No', 'No', np.nan, 'Sí', 'No', 'No', 'Sí']
    indices =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    jugadores = {'nombre': nombre, 'puntaje': puntaje, 'intentos': intentos,  'califico': califico}#np.nan
    df = pd.DataFrame(data=jugadores, index=indices)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    print(f"Hay nan?{df.isna()}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df.isnull()#df.isna()
    print(f"df.isnull()=\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=pd.isnull(df)
    print(f"pd.isnull(df)=\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df.isna().values.sum()#df.isnull().values.sum()
    print(f"df.isnull().values.sum()=\nla cantidad de Null o NaN encontrados es de {ww} elementos")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww = df.fillna(0)
    print(f"df.fillna(0)=\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww = df.fillna(df.mean(numeric_only=True))
    print(f"df.fillna(df.mean(numeric_only=True))=\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww = df.dropna()
    print(f"df.dropna()=\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww = df.dropna(subset=["puntaje", "intentos"], how="all")#, inplace=True)
    print(f"df.dropna()=\n",ww)
    #------------------------------------------------------------------------------------------------------
    ww=df.isnull().values.sum()
    print(f"df.isnull().values.sum())=\n",ww)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Eliminar registros que no cumplan con una condición sobre una columna específica.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 5], 'Z': [2, 3, 5, 7, 11]}
    df = pd.DataFrame(data=datos)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww =  df[df.Y != 5]
    print (f"df = df[df.Y != 5]:\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww =  ~df[df.Y == 5]
    print (f"df =  ~df[df.Y == 5]:\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww =  df[df.Y > 2]
    print (f"df = df[df.Y >= 2]:\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Calcular el promedio, la mediana, el maximo, el minimo y el producto 
        de cada fila (axis 0) y
        de cada columna (axis 1) 
        usando `.mean()`, `.median()`, `.max()` `.min()` y `.product()`.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 44], 'Y': [5, 4, 3, 2, 99], 'Z': [3, 3, 6, 12, 10]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos, index=indices)
    print(f"df=\n{df}")
    print(f"df.mean(axis=0)=\n{df.mean(axis=0)}")
    print(f"df.median(axis=0)=\n{df.median(axis=0)}")
    print(f"df.max(axis=0)=\n{df.max(axis=0)}")
    print(f"df.min(axis=0)=\n{df.min(axis=0)}")
    print(f"df.product(axis=0)=\n{df.product(axis=0)}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    print(f"df=\n{df}")
    print(f"df.mean(axis=1)=\n{df.mean(axis=1)}")
    print(f"df.median(axis=1)=\n{df.median(axis=1)}")
    print(f"df.max(axis=1)=\n{df.max(axis=1)}")
    print(f"df.min(axis=1)=\n{df.min(axis=1)}")
    print(f"df.product(axis=1)=\n{df.product(axis=1)}")
    # ~ df.product()
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Calcular la transpuesta de un objeto `DataFrame` con `transpose()` o `T`.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 44], 'Y': [5, 4, 3, 2, 99], 'Z': [3, 3, 6, 12, 10]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos, index=indices)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    ww=df.transpose()
    print(f"df.transpose()=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.T
    print(f"df.T()=\n",ww)
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Regenera el index del `DataFrame` con la función `reset_index`
        1) Sin convertir los índices anteriores en una columna.
        2) Convertir los índices anteriores en una columna nueva.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 44], 'Y': [5, 4, 3, 2, 99], 'Z': [3, 3, 6, 12, 10]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos, index=indices)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    print(f"df.reset_index(drop=True)=\n{df.reset_index(drop=True)}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    print(f"df.reset_index()//df.reset_index(drop=False)=\n{df.reset_index()}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    print(f"df.reset_index(level=0)=\n{df.reset_index(level=0)}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    print(f"df.reset_index(level=0).to_string(index=False)=\n{df.reset_index(level=0).to_string(index=False)}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()    
    #######################################################################################################
    print(f'''
    ● Obtener los tipos de datos de las columnas de un `DataFrame`.
    ''')
    def Solución():
        pass
    datos = {'real': [3.1415], 'entero': [0], 'fecha': [pd.Timestamp('20230101')], 'string': 'Python'}
    df = pd.DataFrame(data=datos)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*100)
    ww=df.dtypes
    print(f"df.dtypes:\n",ww)
    print(f"type(df.dtypes(:\n{type(ww)}")
    #------------------------------------------------------------------------------------------------------
    print("*"*100)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Obtener los las columnas de un `DataFrame` segun el critero posterior.
    ''')
    def Solución():
        pass
    datos = {'real': [3.1415], 'entero': [0], 'fecha': [pd.Timestamp('20230101')], 'string': 'Python'}
    df = pd.DataFrame(data=datos)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*100)
    df = df[['fecha' , 'entero', 'real' ]]
    print(f"df.dtypes:\n",df)
    #------------------------------------------------------------------------------------------------------
    print("*"*100)
    #######################################################################################################
    print(f'''
    ● Calcular el número de tipos de datos por cada categoría con `df.dtypes.value_counts()`.
    Deprecated `get_dtype_counts` since version 0.25.0.
    ''')
    def Solución():
        pass  
    nombre =   ['Anastasia', 'Anatolio', 'Katherine', 'Pepe', 'Gregorio', 'Tito', 'Luly', 'JJ ', 'Bebe', 'Bety']
    puntaje =  [11.5, 8, 15.5, np.nan, 8, 19, 13.5, np.nan, 8, 18]
    intentos = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
    califico = ['Sí', 'No', 'Sí', 'No', 'No', 'Sí', 'Sí', 'No', 'No', 'Sí']
    indices =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    jugadores = {'nombre': nombre, 'puntaje': puntaje, 'intentos': intentos,   'califico': califico}
    df = pd.DataFrame(data=jugadores, index=indices)
    print(f"df=\n{df}")
    ww=df.dtypes.value_counts()
    print(f"df.dtypes.value_counts():\n",ww)
    #------------------------------------------------------------------------------------------------------
    ww=df[['nombre','puntaje']].dtypes.value_counts()
    print(f"df[['nombre','puntaje']].dtypes.value_counts():\n",ww)
    #######################################################################################################
    print(f'''
    ● Convertir una columna de tipo string - cadena de caracteres a fecha con `to_datetime`.
    ''')
    def Solución():
        pass
    fechas = ['2018/12/31', '2022/01/31', '2023/05/21']
    serie = pd.Series(fechas)
    print(f"serie=\n{serie}")
    serie = pd.to_datetime(pd.Series(serie))
    #------------------------------------------------------------------------------------------------------
    print(f"serie=\n{serie}")
    df = pd.DataFrame(serie)
    df.index=['fechas 1','fechas 2','fechas 3']
    df.columns=['A']
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    print(f"df.info()=\n{df.info()}")
    df_2 = pd.DataFrame(serie, index=['fechas 1','fechas 2','fechas 3'], columns=['A'])
    print(f"df=\n{df_2}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
print(f'''
● Obtenerar una `Serie` y un `DataFrame` con  fechas desde 1ro de enero de 2023 a 15 de enero de 2023 (ambos inclusive).
        utiliza las función `date_range`
        selecciona un periodo determinado con la función ` `between`''')
def Solución():
    pass
date_series = pd.date_range(start = '01-01-2022', end = '15-01-2022')
print(f'series=\n',date_series)
df = pd.DataFrame(data=date_series,columns=['fecha'])
print(f'df=\n',df)
#------------------------------------------------------------------------------------------------------
ww=df[df['fecha'].between('01-01-2022','15-01-2022', inclusive='both')]
print(f'df between =\n',df)
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
● Usar `first` y `last` para obtener los primeros y últimos registros para una cantidad de días arbitraria.
''')
def Solución():
    pass
    indices = pd.date_range('2023-01-01', periods=8, freq='2D')
    print(f"indices=\n{indices}")
    contenido = list(range(1, 9))
    datos = {'A': contenido}
    df = pd.DataFrame(data=datos, index=indices)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    print(f"df.first('3D')=\n{df.first('3D')}")
    print(f"df.first('1D')=\n{df.first('1D')}")
    print(f"df.first('5D')=\n{df.first('5D')}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    print(f"df.last('3D')=\n{df.last('3D')}")
    print(f"df.last('1D')=\n{df.last('1D')}")
    print(f"df.last('5D')=\n{df.last('5D')}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Obtener las columnas de un determinado tipo de dato con 'select_dtypes'.
    ''')
    def Solución():
        pass
    datos = {'real': [3.1415], 'entero': [0], 'fecha': [pd.Timestamp('20230101')], 'string': ['Python']}
    df = pd.DataFrame(datos)
    print(f"df=\n{df}")
    ww=df.select_dtypes(include='int64')
    print(f"df.select_dtypes(include='int64')=\n",ww)
    ww=df.select_dtypes(include='float64')
    print(f"df.select_dtypes(include='float64')=\n",ww)
    print("*"*100)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Seleccionar registros que cumplan con una hora específica con `at_time`.
    ''')
    def Solución():
        pass
    datos = {'Item N~': list(range(1,61))}
    fechas = pd.date_range('2023-01-01', periods=60, freq='6H')
    df = pd.DataFrame(data=datos, index=fechas)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df.at_time('00:00')
    print(f"df.at_time('00:00')=\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df.at_time('12:00')
    print(f"df.at_time('12:00')=\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Seleccionar un conjunto de registros a partir de un rango horario.
    ''')
    indices = pd.date_range('2022-12-01', periods=4, freq='1D30min')
    df = pd.DataFrame({'A': [100, 200, 300, 400]}, index=indices)
    print(f"df=\n{df}")
    ww=df.between_time('00:30', '01:00')
    print(f"df.between_time('00:30', '01:00')=\n",ww)
    #------------------------------------------------------------------------------------------------------
    
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Redondear valores reales con la función `DataFrame`.round`.
    ''')
    def Solución():
        pass
    datos = {'X': [1.50, 2.51, 3.49, 4.0, 4.4], 'Y': [5.99, 4.51, 3.50001, 2.49, 9.9], 'Z': [3.1, 3.2, 6.5, 1.2, 1.0]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos, index=indices)
    print(f"df=\n{df}")
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.round()
    print(f"df.round()=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.round(1)
    print(f"df.round(1)=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.round(5)
    print(f"df.round(10)-ver el maximo de los valores decimales =\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Eliminar filas o columnas con la función `DataFrame`.drop`
        sobre selecciones directa, index,columns, loc e iloc
    ● Eliminar una columna con pop
    ''')
    def Solución():
        pass
    nombre =   ['Oliva', 'Daniela', 'Juan', 'Germán', 'Edward', 'Alex', 'Julio', 'Edgar', 'Angie', 'Irlesa']
    puntaje =  [11.5, 8, 15.5, np.nan, 8, 19, 13.5, np.nan, 8, 18]
    intentos = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
    califico = ['Sí', 'No', 'Sí', 'No', 'No', 'Sí', 'Sí', 'No', 'No', 'Sí']
    indices =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    jugadores = {'nombre': nombre, 'puntaje': puntaje, 'intentos': intentos, 'califico': califico}
    df = pd.DataFrame(data=jugadores, index=indices)
    print("*"*54)
    print("*",'filas'.center(50),"*")#                              filas
    print("*"*54)
    print(f"df=\n{df}")
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.drop('a')#, axis=0)
    print(f"df.drop('a')=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.drop(['a'])#, axis=0)
    print(f"df.drop(['a'])=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.drop(['a','c','e'])#, axis=0)
    print(f"df.drop(['a','c','e'])=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.drop(df.index[[0,2,4]])#, axis=0)#, inplace=True)
    print(f"df.drop(df.index[[0,2,4]])=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    # ~ ww=df.drop(df.loc[['a','c','e'],:])#, axis=0)
    # ~ print(f"=df.drop(df.loc[['a','c','e'],:])=\n",ww)
    # ~ print("*"*50)
    #------------------------------------------------------------------------------------------------------
    # ~ ww=df.drop(df.iloc[[0,2,4]])#, axis=0)
    # ~ print(f"=df.drop(df.iloc[:[0,2,4]])=\n",ww)
    # ~ print("*"*50)
    #------------------------------------------------------------------------------------------------------
    print("*"*54)
    print("*",'columnas'.center(50),"*")#                            columnas
    print("*"*54)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    ww=df.drop('nombre', axis=1)
    print(f"df.drop('nombre', axis=1)=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.drop(['nombre'], axis=1)
    print(f"df.drop(['nombre'], axis=1)=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.drop(['nombre','intentos'], axis=1)
    print(f"df.drop(['nombre','intentos'], axis=1)=\n",ww)
    print("*"*50)     
    #------------------------------------------------------------------------------------------------------
    ww=df.drop(df.columns[0], axis=1)#, inplace=True)
    print(f"df.drop(df.columns[0], axis=1)=\n",ww)
    print("*"*50)   
    #------------------------------------------------------------------------------------------------------
    ww=df.drop(df.columns[[0]], axis=1)#, inplace=True)
    print(f"df.drop(df.columns[[0]], axis=1)=\n",ww)
    print("*"*50)
    pausa()
    #------------------------------------------------------------------------------------------------------
    ww=df.drop(df.columns[[0, 1, 2]], axis=1)#, inplace=True)
    print(f"df.drop(df.columns[[0, 1, 2]], axis=1)=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.drop(df.loc[:,['nombre','intentos']], axis=1)
    print(f"=df.drop(df.loc[:,['nombre','intentos']])=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.drop(df.iloc[:,[0,2]], axis=1)
    print(f"=df.drop(df.iloc[:,[0,2]])=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.pop('nombre')
    print(f"df.pop('nombre')=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Eliminar duplicados `DataFrame`.drop_duplicates`
        selecciona una columna y compara
        selecciona mas de una columna y compara
        elimina el segundo duplicado
        elimina el primer duplicado keep='last')
    ''')
    def Solución():
        pass
    nombre   = ['Oliva', 'Daniela', 'Juan', 'Germán', 'Oliva', 'Daniela', 'Juan', 'Germán', 'Angie', 'Irlesa']
    puntaje  = [11.5, 8, 15.5, np.nan, 11.5, 8, 15.5, np.nan, 8, 18]
    intentos = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
    califico = ['Sí', 'No', 'Sí', 'No', 'No', 'Sí', 'Sí', 'No', 'No', 'Sí']
    indices  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    jugadores = {'nombre': nombre, 'puntaje': puntaje, 'intentos': intentos, 'califico': califico}
    df = pd.DataFrame(data=jugadores, index=indices)
    print(f"df=\n{df}")
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.duplicated('nombre')
    print(f"df.duplicated('nombre')=\n",ww)
    print("*"*50)
    ww=df.drop_duplicates('nombre')
    print(f"df.drop_duplicates('nombre')=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.duplicated('nombre')
    print(f"df.duplicated('nombre')=\n",ww)
    print("*"*50)
    ww=df.drop_duplicates('nombre',keep='last')
    print(f"df.drop_duplicates('nombre',keep='last')=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.duplicated(['nombre','califico'])
    print(f"df.duplicated(['nombre','califico'])=\n",ww)
    print("*"*50)
    ww=df.drop_duplicates(['nombre','califico'])
    print(f"df.drop_duplicates(['nombre','califico'])=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.duplicated(['nombre','califico'])
    print(f"df.duplicated(['nombre','califico'])=\n",ww)
    print("*"*50)
    ww=df.drop_duplicates(['nombre','califico'],keep='last')
    print(f"df.drop_duplicates(['nombre','califico'],keep='last')=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Dado un `DataFrame` genara in index con la función `set_index` .
    ''')
    def Solución():
        pass
    datos = {'X': [1.50, 2.51, 3.49, 4.0, 4.4], 'Y': [5.99, 4.51, 3.50001, 2.49, 9.9], 'Z': [3.1, 3.2, 6.5, 1.2, 1.0]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos, index=indices)
    print ("df=\n",df)
    df = df.set_index('X')
    print ("df=\n",df)
    #------------------------------------------------------------------------------------------------------
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Dado un `DataFrame` genara in index con la función `set_index` sobre tres columnas
        selecciona elementos con xs
        utiliza level
    ''')
    def Solución():
        pass
    datos = {'num_patas': [4, 4, 2, 4, 4, 2, 2, 0],
         'num_alas':    [0, 0, 2, 0, 0, 2, 2, 0],
         'clases':  ['mamíferos', 'mamíferos', 'mamíferos',  'reptiles','reptiles', 'Aves',     'Aves','peces'],
         'animal': ['gato',      'perro',     'murcielago', 'tortuga', 'iguana',   'pingüino', 'loro','tiburon'],
         'locomoción': ['camina', 'camina',    'vuela',      'camina', 'camina', 'camina','vuela' ,'nada']}
    indices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    df = pd.DataFrame(data=datos,index=indices)
    df = df.set_index(['clases', 'animal', 'locomoción'])
    print('''xs no se puede utilizar para establecer valores.
    MultiIndex Slicers es una forma genérica de obtener/establecer valores en cualquier nivel o niveles. 
    Es un superconjunto de la funcionalidad xs''')
    print(f"df=\n{df}")
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.xs('mamíferos')
    print(f"df.xs('mamíferos')=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.xs(('mamíferos', 'perro'))
    print(f"df.xs(('mamíferos', 'perro'))=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.xs('reptiles')
    print(f"df.xs('reptiles')=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.xs(('reptiles', 'iguana'))
    print(f"df.xs(('reptiles', 'iguana'))=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.xs('gato', level=1)
    print(f"df.xs('gato', level=1)=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.xs(('Aves', 'camina'), level=[0, 'locomoción'])
    print(f"df.xs(('Aves', 'camina'), level=[0, 'locomoción'])=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.xs('num_alas', axis=1)
    print(f"df.xs('num_alas', axis=1)=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Encontrar la cantidad de elementos únicos por cada fila y columna con `nunique`.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 2, 1], 'Y': [5, 2, 3, 1, 0], 'Z': [2, 2, 5, 7, 1]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.nunique(axis=0)
    print(f"df.nunique(axis=0)=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.nunique(axis=1)
    print(f"df.nunique(axis=1)=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww=df.X.nunique()
    print(f"df.X.nunique()=\n",ww)
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Reiniciar un índice numérico después de eliminar algunos registros con `reset_index`.
    ''')
    def Solución():
        pass
    nombre   = ['Oliva', 'Daniela', 'Juan', 'Germán', 'Edward', 'Alex', 'Julio', 'Edgar', 'Angie', 'Irlesa']
    puntaje  = [11.5, 8, 15.5, np.nan, 8, 19, 13.5, np.nan, 8, 18]
    intentos = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
    califico = ['Sí', 'No', 'Sí', 'No', 'No', 'Sí', 'Sí', 'No', 'No', 'Sí']
    estudiantes = {'nombre': nombre, 'puntaje': puntaje, 'intentos': intentos, 'califico': califico}
    # ~ indices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j']
    df = pd.DataFrame(data=estudiantes)#,index=indices)
    print(f"df=\n{df}")
    print("*"*50)
    #------------------------------------------------------------------------------------------------------
    ww = df.drop([5, 7])
    print(f"df=\n",ww)
    ww.reset_index(inplace=True,drop=True)
    print(f"df=\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    # ~ print(f"df=\n{df}")
    # ~ ww = df.drop([5, 7])
    # ~ print(f"df=\n",ww)
    # ~ ww.reset_index(inplace=True)
    # ~ print(f"df=\n",ww)
    # ~ print(f"df.columns=\n{ww.columns}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Agregar un add_prefix y add_suffix a las columnas de un objeto `DataFrame`.
    ''')
    def Solución():
        pass
    datos = {1: [1, 2, 3, 4, 5], 2: [5, 4, 3, 2, 0], 3: [2, 3, 5, 7, 11]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df.add_prefix('Col_')
    print(f"df.add_prefix('Col_')=\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df.add_suffix('_Col')
    print(f"df.add_suffix('_Col')=\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Obtener los datos de una columna como una lista Python con `tolist`.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    lista_valores = df['Y'].tolist()
    print (f"{lista_valores=}\n{type(lista_valores)=}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Truncar un `DataFrame` por filas y columnas con la función `truncate`.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
    indices = [1, 2, 3, 4, 5]
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    ww=df.truncate(before=2, after=4)
    print (f"df.truncate(before=2, after=4):\n",ww)
    #------------------------------------------------------------------------------------------------------
    ww=df['Y'].truncate(before=2, after=4)
    print (f"df['Y'].truncate(before=2, after=4):\n",ww)
    #------------------------------------------------------------------------------------------------------
    ww=df.truncate(before='Y', after='Z', axis=1 )
    print (f"df.truncate(before='Y', after='Z', axis=1):\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Agregar una nueva columna a un `DataFrame` por medio de la función `assign`.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    ww=df.assign(F=lambda df: df.Y * 3 / (2+df.X))
    print (f"df.assign(F=lambda df: df.Y * 3 / (2+df.X)):\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Agregar una columna en una posición específica con la función `DataFrame`.insert`.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    valores = [7, 8, 9, 2, 3]
    posicion = 0
    df.insert(loc=posicion, column='A', value=valores)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Seleccionar el índice de una columna de un `DataFrame` con el elemento mayor.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df.idxmax()
    print (f"df.idxmax():\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df.X.idxmax()
    print (f"df.X.idxmax():\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df['X'].idxmax()
    print (f"df['X'].idxmax():\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df[['X','Z']].idxmax()
    print (f"df['X','Z'].idxmax():\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Comprobar en `DataFrame` con el operador Python `in` 
        si existe una fila 'a' y otra 'z'.
        si existe una columna 'X' y otra 'A'.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    print(f"'X' in df.columns:{'X' in df.columns}")
    print(f"'A' in df.columns:{'A' in df.columns}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Comprobar si una columna existe en un `DataFrame` con el operador Python `in`.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print(f"'a' in df.index:{'a' in df.index}")
    print(f"'Z' in df.index:{'Z' in df.index}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Reemplazar valores en un `DataFrame` con la función `replace`.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df.replace(2, 0)
    print (f"df.replace(2, 0):\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df.replace([5, 2, 3], 0)
    print (f"df.replace([5, 2, 3], 0):\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df.replace([1, 5], [-1, -5])
    print (f"df.replace([1, 5], [-1, -5]):\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Eliminar valores infinitos (`-np.inf` y `np.inf`) de un `DataFrame` con `replace`.
    ''')
    def Solución():
        pass
    df = pd.DataFrame([2, np.nan, 5, 7, np.inf, 11, -np.inf])
    indices = ['a', 'b', 'c', 'd', 'e','f','g']
    df.index=indices
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww = df.replace([np.inf, -np.inf], np.nan)
    print (f"df.replace([np.inf, -np.inf], np.nan):\n",ww)
    ww.replace(np.nan,0,inplace=True)
    print(f"df.replace(np.nan,0,inplace=True)=\n{ww}")
    #------------------------------------------------------------------------------------------------------
    # ~ print(f"df=\n{df}")
    # ~ ww = df.loc[(df[0] == np.nan)|(df[0] == np.inf)] = 0
    # ~ ww = df[0].loc[df[0] == np.nan] = 0
    # ~ print(f"df[0].loc[df[0] = np.nan] = 0=\n{ww}")
    print("*"*50)

    pausa()
    limpiar()
    print("*"*50)
    #######################################################################################################
    print(f'''
    ● Ordenar los valores de las columnas de un `DataFrame` con `sort_values`.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 2, 1], 'Y': [1, 2, 0, 1, 0], 'Z': [2, 2, np.NaN, 7, 1]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df.sort_values(by=['X'])
    print (f"df.sort_values(by=['X']):\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df.sort_values(by=['X'], ascending=False)
    print (f"df.sort_values(by=['X'], ascending=False):\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df.sort_values(by=['Z'], ascending=False, na_position='first')
    print (f"df.sort_values(by=['Z'], ascending=False, na_position='first'):\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df.sort_values(by=['X','Y'])
    print (f"df.sort_values(by=['X','Y']):\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df.sort_values('X', ascending=True).head(3)
    print (f"df.sort_values('X', ascending=True).head(3):\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Ordenar los índices de un `DataFrame` con la función `sort_index`.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
    indices = [2, 3, 4, 0, 1]
    df = pd.DataFrame(data=datos, index=indices)
    #------------------------------------------------------------------------------------------------------
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww = df.sort_index()
    print(f"df.sort_index()=\n",ww)
    print("*"*50)
    df.index = ['d', 'e', 'a', 'c', 'b']
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww = df.sort_index()
    print(f"df.sort_index()=\n",ww)
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Verificar con `equals` si dos objetos `DataFrame` contienen los mismos elementos.
    ''')
    def Solución():
        pass
    datos = {'X': [12, 231, 3123, 2, 1], 'Y': [1121, 2, 123, 1, 0], 'Z': [2, 2, np.NaN, 7, 1]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df_1 = pd.DataFrame(data=datos,index=indices)
    print(f"df_1=\n{df_1}")
    df_2 = pd.DataFrame(data=datos,index=indices).copy()
    print(f"df_2=\n{df_2}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    print (f"df_1.equals(df_2):\n{df_1.equals(df_2)}")
    df_2['a','X']=99
    print ("df_2['a','X']=99")
    # ~ df_2['X']['a']=99
    print (f"df_1.equals(df_2):\n{df_1.equals(df_2)}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Obtener de un `DataFrame` los `n` registros 
        menores  con `nsmallest`.
        mayores  con `nlargest`.
    ''')
    def Solución():
        pass
    datos = {'X': [12, 231, 3123, 2, 1], 'Y': [1121, 2, 123, 1, 0], 'Z': [2, 2, np.NaN, 7, 1]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    ww=df.nsmallest(3, 'Y')
    print (f"df.nsmallest(3, 'Y'):\n",ww)
    ww=df.nsmallest(3, 'Y', keep='last')
    print (f"df.nsmallest(3, 'Y', keep='last'):\n",ww) 
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    print(f"df=\n{df}")
    ww=df.nlargest(3, 'Y')
    print (f"df.nlargest(3, 'Y'):\n",ww)
    ww=df.nlargest(3, 'Y', keep='last')
    print (f"df.nlargest(3, 'Y', keep='last'):\n",ww) 
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Cambiar el tipo de datos :
                                de una columna de `float` a `int` con la función `astype`.
                                de multiples columnas con la función `astype`.
                                errors='raise'
                                errors='ignore'
errors: es la forma en la que se manejan los posibles errores:
        * raise en el caso de que se produzca un error se lanzará una excepción y se parará la ejecución del código
        * ignore el error se ignora y se devuelve el valor original.
    ''')
    def Solución():
        pass
    nombre =   ['Anastasia', 'Anatolio', 'Katherine', 'Pepe', 'Gregorio', 'Tito', 'Luly', 'JJ ', 'Bebe', 'Bety']
    puntaje =  [11.5, 8, 15.5, np.nan, 8, 19, 13.5, np.nan, 8, 18]
    intentos = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
    califico = ['Sí', 'No', 'Sí', 'No', 'No', 'Sí', 'Sí', 'No', 'No', 'Sí']
    indices =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    jugadores = {'nombre': nombre, 'puntaje': puntaje, 'intentos': intentos,  'califico': califico}
    df = pd.DataFrame(data=jugadores, index=indices)
    print(f"df=\n{df}")
    print(f"df.dtypes=\n{df.dtypes}")
    df.puntaje = df.puntaje.fillna(0)
    df.puntaje = df.puntaje.astype(int)
    print(f"df=\n{df}")
    print(f"df.dtypes=\n{df.dtypes}")
    #------------------------------------------------------------------------------------------------------
    #######################################################################################################
    def Solucion():
        pass
    '''
    tipo de d	código de carácter	descripción
    int8	        i1	    entero con signo de 8 bits
    int16	        i2	    entero con signo de 16 bits
    int32	        i4	    entero con signo de 32 bits 
    int64	        i8	    entero con signo de 64 bits
    uint8	        u1	    entero sin signo de 8 bits
    uint16	        u2	    entero sin signo de 16 bits
    uint32	        u4	    entero sin signo de 32 bits
    uint64	        u8	    entero sin signo de 64 bits
    float16	        f2	    número de punto flotante de 16 bits
    float32	        f4	    número de coma flotante de 32 bits
    float64	        f8	    número de punto flotante de 64 bits
    float128	    f16	    número de punto flotante de 128 bits
    complex64	    c8	    número de punto flotante complejo de 64 bits
    complex128	    c16	    número de punto flotante complejo de 128 bits
    complex256	    c32	    número de punto flotante complejo de 256 bits
    bool	        ?	    Booleano (Verdadero o Falso)
    unicode	        tu	    Cadena Unicode
    object	        O	    Objetos de Python
    '''
    exam_data = {'nombre':      ['Anastasia', 'Anatolio', 'Katherine', 'Pepe', 'Gregorio', 'Tito', 'Luly', 'JJ ', 'Bebe', 'Bety'],
                 'puntuación':  [12.5, 9, 16.5, 5.7, 9, 20, 14.5, 9.3, 8, 19],
                 'intentos':    [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                 'edad':        [7,10, 4,18,72, 1,21,30,16,90],
                 'califico':    ['sí', 'no', 'sí', 'no', 'no', 'sí', 'sí', 'no', 'no', 'sí']}
    etiquetas =                 ['a',  'b',  'c',  'd',  'e', 'f',  'g',  'h',  'i',  'j']
    tipo_de_datos={'nombre':  'object','puntuación':'int8', 'intentos':  'float32','edad': 'int64','califico':'object'}
    # ~ tipo_de_datos={'nombre':  str,'puntuación':float, 'intentos':  int,'edad': int,'califico':str}
    df =pd.DataFrame(data=exam_data,index=etiquetas)

    print(f"df=\n",df)
    print ("df.dtype()=\n",df.dtypes)
    df=df.astype(tipo_de_datos)
    print(f"df=\n",df)
    print ("df.dtype()=\n",df.dtypes)
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Usar la función `agg` para realizar varias operaciones por un eje de un `DataFrame`.
    ''')
    def Solución():
        pass
    datos = {'W': [1, 2, 3, 4, 5], 'X': [2, 3, 5, 7, 11],
             'Y': [5, 4, 3, 2, 1], 'Z': [np.nan, np.nan, np.nan, np.nan, np.nan]}
    df = pd.DataFrame(data=datos)
    print(f"df=\n{df}")
    print(f"df.dtypes=\n{df.dtypes}")
    ww = df.agg(['sum', 'min', 'max'])#df.aggregate(['sum', 'min', 'max'])
    print(f"df.aggregate(['sum', 'min', 'max'])=\n",ww)
    ww = df.agg({'W': ['mean'], 'X': ['sum', 'min', 'max'], 'Y': ['min', 'max'], 'Z': ['sum']})
    print("df.agg({'W': ['sum'], 'X': ['sum', 'min', 'max'], 'Y': ['min', 'max'], 'Z': ['sum']})=\n",ww)

    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Selecciona los elementos de un `DataFrame` con `applymap`
    ''')
    def Solución():
        pass
    datos = {'X': [12, 231, 3123, 2, 1], 'Y': [1121, 2, 123, 1, 0], 'Z': [2, 2, np.NaN, 7, 1]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df.applymap(lambda x: len(str(x)))
    print (f"df.applymap(lambda x: len(str(x))):\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df.applymap(lambda x: x**2)
    print (f"df.applymap(lambda x: x**2):\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df**2
    print (f"df**2):\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Selecciona los elementos de un `DataFrame` con `apply`
    ''')
    def Solución():
        pass
    datos = {'X': [9, 99, 999,9999, 9999], 'Y': [100, 200, 250, 300, 400], 'Z': [11111,1111, 111, 11, 1]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    def is_delayed(x):
        return x > 250
    df['A'] = df['Z'].apply(is_delayed)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    ww=df[['X','Y','Z']].apply(lambda x: x['Z'] if x['Y']>250 else x['X'], axis=1)
    print(f"df=\n{ww}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Transformar los valores de un `DataFrame` con la función `transform`.
    ''')

    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 1], 'Z': [2, 3, 5, 7, 11]}
    indices = ['a', 'b', 'c', 'd', 'e']
    df = pd.DataFrame(data=datos,index=indices)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    def funcion_regular(x):
        return x + 2
    ww = df.transform(funcion_regular)
    print("df.transform(funcion_regular)=\n",ww)
    #------------------------------------------------------------------------------------------------------
    ww = df.transform(lambda x: x + 2)
    print("df.transform(lambda x: x + 2)=\n",ww)
    #------------------------------------------------------------------------------------------------------
    ww = df['X'].transform(lambda x: x*0 if x.mean()% 2!=0 else x)# x es una serie
    print("df.transform(lambda x: x + 2)=\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Agrupar un conjunto de datos y luego calcular su promedio con `groupby` y `mean`.
    ''')

    def Solución():
        pass
    animales = ['Águila', 'Alcón', 'Águila', 'Alcón']
    velocidades = [160, 390, 120, 385]
    df = pd.DataFrame({'animal': animales, 'velocidad': velocidades})
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    ww = df.groupby(['animal'])
    for grupo,datos in ww:
        print(grupo,datos)
    ww = df.groupby(['animal']).mean()
    print("df.groupby(['animal']).mean()=\n",ww)
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar() 
    #######################################################################################################
    print(f'''
    ● Usar las funciones `all` y `any` sobre un objeto `DataFrame`.
    ''')
    def Solución():
        pass
    datos = {'X': [1, 2, 3, 4, 5], 'Y': [3, 2, 1, 0, -1], 'Z': [5, 7, 11, 13, 17]}

    df = pd.DataFrame(data=datos)
    print(f"df=\n{df}")
    ww = df <= 3
    print(f"df <= 3=\n{ww}")
    ww = (df <= 3).all()
    print(f"(df <= 3).all()=\n{ww}")
    ww = (df <= 3).any()
    print(f"(df <= 3).any()=\n{ww}")
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar
    #######################################################################################################
    print(f'''
    ● Incrementar el número de filas y columnas visibles de un `DataFrame`
    con las funciones 
    ''')
    def Solución():
        pass
    datos=dict()
    for i in range(1, 91):
        datos[f'Columna {i}'] = list(range(1, 11))
    print ("""La función .set_option() nos permite cambiar un valor predeterminado a algo de nuestra elección.""")
    df = pd.DataFrame(data=datos)
    print(f"df=\n{df}")
    pd.set_option('display.max_columns', 100)
    print(f"df=\n{df}")
    pd.set_option('display.max_rows', 200)
    print(f"df=\n{df}")
    pd.set_option("display.max_rows",90)
    #------------------------------------------------------------------------------------------------------
    print (f"Con la ayuda de .reset_option en Pandas, puede recuperar los valores predeterminados que pueden cambiar anteriormente.")
    pd.reset_option("display.max_columns")
    data= pd.get_option("display.max_columns")
    print(f"display.max_columns:{data=}")
    print(f"df=\n{df}")
    pd.reset_option("display.max_rows")
    data= pd.get_option("display.max_rows")
    print(f"display.max_rows:{data=}")
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    print ("dasplay ")
    print(f'{pd.describe_option ( "display.max_columns" )=}')
    print(f'{pd.describe_option ( "display.max_rows" )=}')
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● 
    ''')

    def Solución():
        pass
        
    #------------------------------------------------------------------------------------------------------
    print("*"*50)
    pausa()
    limpiar()
    #######################################################################################################
    print(f'''
    ● Usar `groupby` para agrupar datos por una columna específica y contar la cantidad de elementos.
        El uso del método size() o count() con pandas.DataFrame.groupby() generará el recuento de una cantidad de ocurrencias
            de datos presentes en una columna particular del DF. 
        Sin embargo, esta operación también se puede realizar usando pandas.Series.value_counts() y pandas.Index.value_counts() .
        El enfoque básico para usar este método es asignar los nombres de columna como parámetros en el método groupby() y
            luego usar size() con él. 
            
    Acercarse

    Módulo de importación
    Crear o importar`DataFrame`
    Aplicar grupo por
    Usa cualquiera de los dos métodos.
    Mostrar resultado
    Método 1: Usar pandas.groupyby().si ze()
        Usa pandas `DataFrame`.groupby() para agrupar las filas por columna. 
        Usa el método count() para obtener el recuento de cada grupo ignorando los valores Ninguno y Nan. 
        También funciona con datos de tipo no flotante. 
        El siguiente ejemplo hace la agrupación en la Coursescolumna y calcula cuántas veces está presente cada valor.
      ● `DataFrame`.groupby(by=None, 
                            axis=0, 
                            level=None, 
                            as_index=True, 
                            sort=True, 
                            group_keys=True, 
                            squeeze=<no_default>, 
                            observed=False, 
                            dropna=True)
                by– Lista de nombres de columna para agrupar por
                axis – Predeterminado a 0. Toma 0 o ‘ índice ’, 1 o ‘ columnas ’
                level– Utilizado con MultiIndex.
                as_index– otput agrupado estilo sql.
                sort– Predeterminado a verdadero. Especifique si ordenar después del grupo
                group_keys– agregue claves de grupo o no
                squeeze– deprimente en nuevas versiones
                observed– Esto solo se aplica si alguno de los grupos son categóricos.
                dropna– Predeterminado a falso. Use True para soltar None / Nan en los valores
            
    RESUMEN :Aplicar función func en grupo y combinar los resultados juntos.

    GroupBy.agg == .aggregate  Agregado utilizando una o más operaciones sobre el eje especificado.

    `DataFrame`GroupBy.transform( func, * args [, ... ] )     Función de llamada que produce un DF de datos indexado en cada grupo.

    GroupBy.pipe( func, * args, ** kwargs )                 Aplicar un func con argumentos a este grupo Por objeto y devolver su resultado.
    El método groupby() devuelve un objeto `DataFrame`GroupBy después de recopilar los datos idénticos en grupos de pandas `DataFrame`. 
    Este objeto contiene varios métodos (sum(), mean() min(), max() ) que se puede usar para agregar las filas agrupadas.

    ● df.groupby(['zz']).reset_index (name='xx')
        Generalmante groupby se usa con varias columnas de `DataFrame`, puede hacerlo pasando una lista de etiquetas de columna que desea realizar en grupo.
        Por default groupby() no incluye el índice de fila en el resultado, se puede agregar el índice usando el método `DataFrame`.reset_index ().

    ● df.groupby(['zz'],dropna=False)
        También puede elegir si incluir o no los (NA / None / Nan) en el grupo. Por default el parámetro se establecer en True para no incluirloos
        Pero se pueden agregar con el parámetro dropna=False.


    ● df.groupby(by=['zz'], sort=False).sum()
        Por default groupby() groupby ( ) ordena los resultados. Si el rendimiento es bajo con sort=False permite mayor velocidad.
    otra opción
        df_agrupados = df.groupby('zz',sort=False).sum()
        sortedDF=groupedDF.sort_values('zz', ascending=False)
        
    Los siguientes métodos están disponibles en ambos SeriesGroupBy y `DataFrame`GroupBy objetos, pero pueden diferir ligeramente, 
        generalmente en eso la `DataFrame`GroupBy la versión generalmente permite la especificación de un argumento del eje, 
        y a menudo un argumento que indica si restringir aplicación a columnas de un tipo de datos específico.
        
            `DataFrame`GroupBy.all( [ skipna ] )                      Regrese verdadero si todos los valores en el grupo son veraces, de lo contrario falso.
            `DataFrame`GroupBy.any( [ skipna ] )                      Volver Verdadero si algún valor en el grupo es veraz, de lo contrario Falso.
            `DataFrame`GroupBy.bfill( [ límite ] )                    Retroceda los valores.
            `DataFrame`GroupBy.corr                                   Calcule la correlación por pares de columnas, excluyendo los valores de NA / nulo.
            `DataFrame`GroupBy.count( )                               Recuento de grupo de cómputo, excluyendo valores faltantes.
            `DataFrame`GroupBy.cov                                    Calcule la covarianza por pares de columnas, excluyendo los valores de NA / nulo.
            `DataFrame`GroupBy.cumcount( [ ascendente ] )             Numere cada elemento en cada grupo de 0 a la longitud de ese grupo - 1.
            `DataFrame`GroupBy.cummaxEje ( [, numeric_only ] )        Máx. Acumulativo para cada grupo.
            `DataFrame`GroupBy.cumminEje ( [, numeric_only ] )        Min acumulativo para cada grupo.
            `DataFrame`GroupBy.cumprodEje ( [ ] )                     Producto acumulativo para cada grupo.
            `DataFrame`GroupBy.cumsumEje ( [ ] )                      Suma acumulada para cada grupo.
            `DataFrame`GroupBy.describe( ** kwargs )                  Generar estadísticas descriptivas.
            `DataFrame`GroupBy.diffPeríodos ( [, eje ] )              Primera diferencia discreta de elemento.
            `DataFrame`GroupBy.ffill( [ límite ] )                    Reenviar rellena los valores.
            `DataFrame`GroupBy.fillna                                 Rellene los valores de NA / NaN utilizando el método especificado.
            `DataFrame`GroupBy.filter( func [, dropna ] )             Devuelva una copia de un `DataFrame` excluyendo elementos filtrados.
            `DataFrame`GroupBy.hist                                   Haga un histograma de las columnas del Marco de datos.
            `DataFrame`GroupBy.idxmaxEje ( [, skipna, ... ] )         Índice de retorno de la primera ocurrencia del máximo sobre el eje solicitado.
            `DataFrame`GroupBy.idxminEje ( [, skipna, ... ] )         Índice de retorno de la primera ocurrencia del mínimo sobre el eje solicitado.
            `DataFrame`GroupBy.nunique( [ dropna ] )                  Devuelva `DataFrame` con recuentos de elementos únicos en cada posición.
            `DataFrame`GroupBy.pct_changePeríodos ( [, ... ] )        Calcule pct_change de cada valor a la entrada anterior en grupo.
            `DataFrame`GroupBy.plot                                   Clase que implementa el atributo .plot para objetos groupby.
            `DataFrame`GroupBy.quantile( [ q, ... ] )                 Devuelva los valores del grupo en el cuantil dado, a la numpy.percentile.
            `DataFrame`GroupBy.rankMétodo ( [, ascendente, ... ] )    Proporcione el rango de valores dentro de cada grupo.
            `DataFrame`GroupBy.resample( regla, * args, ** kwargs )   Proporcione un nuevo muestreo cuando use un TimeGrouper.
            `DataFrame`GroupBy.sample( [ n, frac, reemplazar, ... ] ) Devuelva una muestra aleatoria de elementos de cada grupo.
            `DataFrame`GroupBy.shiftPeríodos ( [, freq, ... ] )       Cambie cada grupo por períodos de observaciones.
            `DataFrame`GroupBy.size( )                                Calcular tamaños de grupo.
            `DataFrame`GroupBy.skew                                   Devuelva el sesgo imparcial sobre el eje solicitado.
            `DataFrame`GroupBy.take                                   Devuelve los elementos en el dado posicional índices a lo largo de un eje.
            `DataFrame`GroupBy.value_counts( [ subconjunto, ... ] )   Devuelva una serie o un`DataFrame` que contenga recuentos de filas únicas.
    ''')
    def Solución():
        pass

    lenguajes =     ['Python', 'Python',  'Python', 'Java',   'Java',  'PHP',     'JScript','JScript',  'JScript', 'Java',  'C#', 'C#']
    programadores = ['Edward', 'Daniela', 'Oliva',  'Edward', 'Daniela', 'Pete', 'Edward', 'Daniela',  'Oliva', 'Edward', 'Daniela', 'Oliva']
    sueldo =        [    99.9,   22,       35,       54.32  ,   111,      25,    33.33,    123,        98,       78, 88, 98]
    seccion=        ['A', 'A', 'A','A', 'B', 'B', 'B', 'C', 'C', 'D','E', 'F']
    # ~ cursos=         [10,  12,  11, 10,  12,  10,  11,  11,  9 , 10, 12, 10]
    cursos=         [10,  12,  np.nan, 10,  12,  10,  11,  11,  np.nan , 10, 12, 10]

    datos = {'programadores': programadores, 'cursos':cursos,'lenguajes': lenguajes,'sueldo':sueldo,'seccion': seccion}
    df = pd.DataFrame(data=datos)
    print(f"df=\n{df}")
    #------------------------------------------------------------------------------------------------------
    pausa()
    print("*"*104)
    print("*",'groupby'.center(100),"*")
    print("*"*104)
    print('''
    Use `DataFrame`.groupby().sum() para agrupar filas en función de una o varias columnas y calcular la función suma total. 
    La función groupby() devuelve un `DataFrame`GroupByobjeto que contiene una función agregada sum()para calcular la suma de una columna 
    dada para cada grupo.
    ''')
    print("""
        SQL: SELECT * FROM df GROUP BY seccion 
    """)
    ww=df.groupby('seccion')
    print(f"df.groupby('seccion')=\n",ww)
    print("*"*100)
    print("ww.describe()",ww.describe())
    for agrupado,datos in ww:
        print(f"'seccion' ={agrupado}")
        print(f"datos=\n",datos)
    print("-"*100)
    print(f"df.groupby(['seccion']).max()=\n{ww.max()}")
    print("-"*100)
    print(f"df.groupby(['seccion']).get_group('A')=\n{ww.get_group('A')}")#el df de los maximos
    print("-"*100)
    print(f"df.groupby(['seccion']).get_group('A').max()=\n{ww.get_group('A').max()}")#los maximos de cada columna 
    print("-"*100)
    print(f"df.groupby(['seccion'])['sueldo'].mean()=\n",ww['sueldo'].mean())#las medias de cada columna 
    print(f"df.groupby(['seccion'])['sueldo'].mean()=\n",df.groupby(['seccion'])['sueldo'].mean())
    print("-"*100)
    #------------------------------------------------------------------------------------------------------
    ww = df.loc[df.cursos < 11, 'cursos'] = 0
    print("df.groupby('cursos').count()=",ww)
    print("-"*100)
    ww = df.loc[df.cursos >= 11, 'cursos'] = 1
    print("df.groupby('cursos').count()=",ww)
    print("-"*100)
    ww = df.groupby('cursos').count()
    print("-"*100)
    print("df.groupby('cursos').count()=\n",ww)
    print("-"*100)
    #------------------------------------------------------------------------------------------------------
    print("""
        SQL: SELECT * FROM df GROUP BY cursos 
    """)
    ww = df.groupby('cursos')
    print(f"df.groupby(['cursos'])=\n",ww)#==print(f"df.groupby(['cursos'])=\n",ww)
    print("*"*100)
    print("ww.describe()",ww.describe())
    for agrupado,datos in ww:
        print(f"con {agrupado} 'cursos'")
        print(f"datos=\n",datos)
    print("-"*100)
    print(f"df.groupby(['cursos']).max()=\n{ww.max()}")
                                                                                        # ~ print("-"*100)
                                                                                        # ~ print(f"df.groupby(['cursos']).get_group(10)=\n{ww.get_group(10)}")#el df de los maximos 
                                                                                        # ~ print("-"*100)
                                                                                        # ~ print(f"df.groupby(['cursos']).get_group(10).max()=\n{ww.get_group(10).max(numeric_only=True)}")#los maximos de cada columna
                                                                                        # ~ print("-"*100)
                                                                                        # ~ print(f"df.groupby(['cursos']).get_group(10).mean()=\n{ww.get_group(10).mean(numeric_only=True)}")#los media de cada columna
                                                                                        # ~ print("-"*100)
    #------------------------------------------------------------------------------------------------------
    # Using groupby() and sum()
    ww = df.groupby(['cursos','lenguajes']).sum(numeric_only = True)
    print(f"df.groupby(['cursos','lenguajes']).sum(numeric_only = True)=\n",ww)
    #------------------------------------------------------------------------------------------------------
    # Using groupby() and sum()
    ww = df.groupby(['cursos','lenguajes'], dropna=False).sum(numeric_only = True)
    print(f"df.groupby(['cursos','lenguajes'], dropna=False).sum(numeric_only = True)=\n",ww)
    #------------------------------------------------------------------------------------------------------
    # Using groupby() and sum()
    ww = df.groupby(['cursos','lenguajes'])['cursos'].sum(numeric_only = True)
    print(f"df.groupby(['cursos','lenguajes'])['cursos'].sum(numeric_only = True)=\n",ww)
    ww = df.groupby(['cursos','lenguajes'], dropna=False)['cursos'].sum(numeric_only = True)
    print(f"df.groupby(['cursos','lenguajes'], dropna=False)['cursos'].sum(numeric_only = True)=\n",ww)
    #------------------------------------------------------------------------------------------------------
    # Using groupby with `DataFrame`.rename() Method.
    ww= df.groupby(['cursos', 'lenguajes'])['sueldo'].sum(numeric_only=True).rename("cant")
    print("df.groupby(['cursos', 'lenguajes'])['lenguajes'].sum(numeric_only=True).rename('cant')=\n",ww)
    #------------------------------------------------------------------------------------------------------
    pausa()
    print("*"*104)
    print("*",'count'.center(100),"*")
    print("*"*104)
    #------------------------------------------------------------------------------------------------------
    # Using groupby() and count()
    ww = df.groupby(['cursos'])['cursos'].count()
    print(f"df.groupby(['cursos'])['cursos'].count()=\n",ww)
    ww = df.groupby(['cursos'], dropna=False)['cursos'].count()
    print(f"df.groupby(['cursos'])['cursos'].count()=\n",ww)
    #------------------------------------------------------------------------------------------------------
    # Using GroupBy & count() on multiple column
    ww = df.groupby(['cursos','lenguajes'])['sueldo'].count()
    print(f"df.groupby(['cursos','lenguajes'])['sueldo'].count()=\n",ww)
    ww = df.groupby(['cursos','lenguajes'], dropna=False)['sueldo'].count()
    print(f"df.groupby(['cursos','lenguajes'])['sueldo'].count()=\n",ww)
    #------------------------------------------------------------------------------------------------------
    # Using GroupBy & size() on multiple column
    ww = df.groupby(['cursos','lenguajes'])['sueldo'].size()
    print(f"df.groupby(['cursos','lenguajes'])['sueldo'].size()=\n",ww)
    #------------------------------------------------------------------------------------------------------
    # using `DataFrame`.size() and max()
    ww = df.groupby(['cursos','lenguajes']).size().groupby(level=0).max() 
    print(f"df.groupby(['cursos','lenguajes']).size().groupby(level=0).max() =\n",ww)
    #------------------------------------------------------------------------------------------------------
    # Use size().reset_index() method
    ww = df.groupby(['lenguajes']).size().reset_index(name='cant.prog')
    print(f"df.groupby(['lenguajes']).size().reset_index(name='cant.prog')=\n",ww)
    #------------------------------------------------------------------------------------------------------
    ww = df.groupby(['programadores']).size().reset_index(name='cant.leng')
    print(f"df.groupby(['programadores']).size().reset_index(name='cant.leng')=\n",ww)
    #------------------------------------------------------------------------------------------------------
    ww = df.groupby(['cursos','lenguajes']).size().reset_index(name='counts')
    print(f"df.groupby(['cursos','lenguajes']).size().reset_index(name='counts')=\n",ww)
    pausa()
    print("*"*104)
    print("*",'agg==aggregate'.center(100),"*")
    print("*"*104)
    print ('''agg == aggregate utilizando una o más operaciones sobre el eje especificado.
        operaciones - max , min , mean , count , sum .''')
    #------------------------------------------------------------------------------------------------------
    # Using pandas `DataFrame`.reset_index()
    ww = df.groupby(['lenguajes'])['sueldo'].agg('count').reset_index()
    print("df.groupby(['sueldo','lenguajes'])['sueldo'].agg('count').reset_index()=\n",ww)
    #------------------------------------------------------------------------------------------------------
    ww = df.groupby(['lenguajes'])['sueldo'].agg(['min','max']).reset_index()
    print("df.groupby(['sueldo','lenguajes'])['sueldo'].agg(['min','max']).reset_index()=\n",ww)
    #------------------------------------------------------------------------------------------------------
    ww = df.groupby('lenguajes').aggregate({'programadores':'count','sueldo':['min','max']})
    print("df.groupby('lenguajes').aggregate({'programadores':'count','sueldo':['min','max']})=\n",ww)
    #------------------------------------------------------------------------------------------------------
    ww = df.groupby('lenguajes').aggregate({'programadores':'count','sueldo':'mean'})
    print("df.groupby('lenguajes').aggregate({'programadores':'count','sueldo':['min','max']})=\n",ww)
    # ~ df.agg("mean", axis="columns")
    #------------------------------------------------------------------------------------------------------
    ww = df.groupby('lenguajes').aggregate({'programadores':'count','sueldo':'mean'})
    print("df.groupby('lenguajes').aggregate({'programadores':'count','sueldo':['min','max']})=\n",ww)
    #------------------------------------------------------------------------------------------------------
    pausa()
    print("*"*104)
    print("*",'transform',"*")
    print("*"*104)
    print ('''
        a.empty, a.bool(), a.item(), a.any() or a.all()
    ''')
    # Using `DataFrame`.transform()
    ww = df.groupby(['cursos','lenguajes']).cursos.transform('count')
    print(f"df.groupby(['cursos','lenguajes']).cursos.transform('count')=\n",ww)
    #------------------------------------------------------------------------------------------------------
    ww = df.groupby(['lenguajes','sueldo'])['sueldo'].transform(lambda x: x.mean()).reset_index(name='x')
    print(f"df.groupby(['lenguajes','sueldo'])['sueldo'].transform(lambda x: x.mean())=\n",ww)
    #------------------------------------------------------------------------------------------------------
    def add_cols_value(df_col,value):
        '''this work only on apply() funtion'''
        return df_col['sueldo']+value

    def add_value(df_col,value):
        return df_col+value
    ww = df.groupby(['cursos','lenguajes']).sueldo.transform(add_value,45)
    print(f"df.groupby(['cursos','lenguajes']).sueldo.transform(add_value,45)=\n",ww)
    ww = df.groupby(['cursos','lenguajes']).apply(add_cols_value,45)
    print(f"df.groupby(['cursos','lenguajes']).apply(add_cols_value,45)=\n",ww)
    #------------------------------------------------------------------------------------------------------
    print (f"df.groupby('lenguajes').apply(print)")
    df.groupby('lenguajes').apply(print)
    #------------------------------------------------------------------------------------------------------
    ww = df.groupby(['cursos','lenguajes','sueldo']).sueldo.transform(lambda x: x/x.mean())
    print("df.groupby(['cursos','lenguajes','sueldo']).sueldo.transform(lambda x: x/x.mean())=\n",ww)
    #------------------------------------------------------------------------------------------------------
    ww = df.groupby(['sueldo','lenguajes'], group_keys=False)['sueldo'].apply(lambda x: df.sueldo.mean()-x).reset_index(name='x')
    print("df.groupby(['sueldo','lenguajes'], group_keys=False)['sueldo'].apply(lambda x: df.sueldo.mean()-x).reset_index(name='x')=\n",ww)
    #------------------------------------------------------------------------------------------------------
    df['nivel_sueldo'] = df['sueldo'].apply(lambda x:'Alto' if  x> df['sueldo'].mean() else 'Bajo')
    ww = df.groupby(['nivel_sueldo','programadores','lenguajes'])['programadores'].size()
    #------------------------------------------------------------------------------------------------------
    print("df.groupby(['nivel_sueldo','programadores','lenguajes'])['programadores'].size()=\n",ww)
    df['margen_sueldo'] = df['sueldo'].apply(lambda sueldo_:sueldo_-df['sueldo'].mean())
    #------------------------------------------------------------------------------------------------------
    ww = df.groupby(['nivel_sueldo','margen_sueldo','programadores','lenguajes'])['programadores'].size()
    print("df.groupby(['nivel_sueldo','margen_sueldo','programadores','lenguajes'])['programadores'].size()=\n",ww)
    # ~ df_2 = pd.DataFrame({'Name': ['John', 'Jack', 'Shri',   'Krishna', 'Smith', 'Tessa'],
                       # ~ 'Maths': [5, 3, 9, 10, 6, 3]})
    # ~ df_2['Result'] = df_2['Maths'].apply(lambda x: 'Alto' if x>=df_2['Maths'].mean() else 'Bajo')
    # ~ print(df_2)
    '''
    df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                              'foo', 'bar'],
                       'B' : ['one', 'one', 'two', 'three',
                              'two', 'two'],
                       'C' : [1, 5, 5, 2, 5, 5],
                       'D' : [2.0, 5., 8., 1., 2., 9.]})
    grouped = df.groupby('A')[['C', 'D']]
    grouped.transform(lambda x: (x - x.mean()) / x.std())
              C         D
    0 -1.154701 -0.577350
    1  0.577350  0.000000
    2  0.577350  1.154701
    3 -1.154701 -1.000000
    4  0.577350 -0.577350
    5  0.577350  1.000000
    Broadcast result of the transformation

    grouped.transform(lambda x: x.max() - x.min())
         C    D
    0  4.0  6.0
    1  3.0  8.0
    2  4.0  6.0
    3  3.0  8.0
    4  4.0  6.0
    5  3.0  8.0
    Changed in version 1.3.0: The resulting dtype will reflect the return value of the passed func, for example:

    grouped.transform(lambda x: x.astype(int).max())
    '''


    #------------------------------------------------------------------------------------------------------
    # Use `DataFrame`.groupby() and Size() 
    print(df.groupby(['programadores','lenguajes']).size() 
                                                   .sort_values(ascending=False) 
                                                   .reset_index(name='count') 
                                                   .drop_duplicates(subset='lenguajes'))
    print("*"*50)
    pausa()
    limpiar()
#######################################################################################################
print(f'''
●  Escriba un programa Pandas para fusionar conjuntos de datos y verificar la unicidad.
''')
def Solucion():
    pass
exam_data = {'nombre':      ['Anastasia', 'Anatolio', 'Katherine', 'Pepe', 'Gregorio'],
             'puntuación':  [20, 14.5, 9.3, 8, 19],
             'intentos':    [1, 3, 2, 3, 2 ],
             'califico':    ['sí', 'no', 'sí', 'no', 'no']}
etiquetas =                 ['a',  'b',  'c',  'd',  'e']
df_1 =pd.DataFrame(data=exam_data,index=etiquetas)
print(f"df=\n",df_1)
exam_data = {'nombre':      [ 'Tito', 'Luly', 'JJ ', 'Bebe', 'Bety'],
             'puntuación':  [12.5, 9, 16.5, 5.7, 9],
             'intentos':    [ 3, 1, 1, 2, 1],
             'califico':    ['sí', 'sí', 'no', 'no', 'sí']}
etiquetas =                 ['f',  'g',  'h',  'i',  'j']
df_2 =pd.DataFrame(data=exam_data,index=etiquetas)
print(f"df=\n",df_2)
df = df_1.append(df_2, ignore_index=False, verify_integrity=True, sort=False)
print(f"df=\n",df)
#------------------------------------------------------------------------------------------------------
print("-"*20,":)")
exam_data = {'nombre':      ['Anastasia', 'Anatolio', 'Katherine', 'Pepe', 'Gregorio', 'Tito', 'Luly'],
             'puntuación':  [12.5, 9, 16.5, 5.7, 9, 20, 14.5],
             'intentos':    [1, 3, 2, 3, 2, 3, 1],
             'edad':        [11, 12, 13, 14, 15, 16, 17]}
etiquetas =                 ['a',  'b',  'c',  'd',  'e', 'f',  'g']
df_1 =pd.DataFrame(data=exam_data,index=etiquetas)
print(f"df_1=\n",df_1)
exam_data = {'nombre':      ['Pepe', 'Gregorio', 'Tito', 'Luly', 'JJ ', 'Bebe', 'Bety'],
             'puntuación':  [5.7, 9, 20, 14.5, 9.3, 8, 19],
             'intentos':    [3, 2, 3, 1, 1, 2, 1],
             'califico':    ['no', 'no', 'sí', 'sí', 'no', 'no', 'sí']}
etiquetas =                 ['d',  'e', 'f',  'g',  'h',  'i',  'j']
df_2 =pd.DataFrame(data=exam_data,index=etiquetas)
print(f"df_2=\n",df_2)
print('\n"one_to_one”: check if merge keys are unique in both left and right datasets:"')
df_one_to_one = pd.merge(df_1, df_2, validate = "one_to_one")
print('pd.merge(df_1, df_2, validate = "one_to_one")=\n',df_one_to_one)
#------------------------------------------------------------------------------------------------------
print("-"*20,":)")                     
print('\n"one_to_many” or “1:m”: check if merge keys are unique in left dataset:')
df_one_to_many = pd.merge(df_1, df_2, validate = "one_to_many")
print('pd.merge(df_1, df_2, validate = "one_to_many")=\n',df_one_to_many)
#------------------------------------------------------------------------------------------------------
print("-"*20,":)")
print('“many_to_one” or “m:1”: check if merge keys are unique in right dataset:')
df_many_to_one = pd.merge(df_2, df_1, validate = "many_to_one")
print('pd.merge(df_2, df_1, validate = "many_to_one"=\n',df_many_to_one)
#------------------------------------------------------------------------------------------------------
print("-"*20,":)")
pausa()
limpiar()
#######################################################################################################
print(f'''
●  Escriba un programa Pandas para fusionar conjuntos de datos con join entre dos `DataFrames`
    1) Alinear en columnas.
    2) Alinearnos en el índice.
''')

def Solución():
    pass
print(f'''
`DataFrame`.join(self, other, on=None, how='left', ='', rsuffix='', sort=False)
Parámetro	    Descripción
    self    	Es el objeto que la unión tiene que ocurrir en el mismo `DataFrame`
    other	    Menciona el otro `DataFrame`, Serie o lista que debe unirse
    on          Especifica la clave en la que tiene que ocurrir la unión.
    how	        Menciona el tipo de unión.
                                            'left' -> ( Default )
                                            'right'
                                            'outer'
                                            'inner
    lsuffix     sufijo_izquierdo	Sufijo a usar de las columnas superpuestas del marco izquierdo.
    rsuffix     sufijo derecho	    Sufijo a usar de las columnas superpuestas del marco derecho.
    sort        Ordenar la salida
''')
df_1 = pd.DataFrame({'A':   ['K0','K1','K4','K7'],
                     'B':   [45,23,45,2]})
df_2 = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                     'A':   ['1', '2', '4', '23', '2', '78'],
                     'B':   ['4', '41', '32', '23', '74', '5']})
print(f"df=\n{df_1}")
print(f"df=\n{df_2}")
print(f"{df_1.set_index('A').join(df_2.set_index('key'),lsuffix='_caller', rsuffix='_other')=}")
print(f"{df_2.set_index('key').join(df_1.set_index('A'),lsuffix='_caller', rsuffix='_other')=}")
#------------------------------------------------------------------------------------------------------
print("*"*50)
df_1 = pd.DataFrame({'DF1_key': ['K0','K1','K4','K7','K9'],
                     'B':       [45,23,45,56,5]})
df_2 = pd.DataFrame({'DF2_key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                     'A':       ['1', '2', '4', '23', '2', '78'],
                     'B':       ['4', '41', '32', '23', '74', '5']})
print(f'df_1=\n',df_1)
print(f'df_2=\n',df_2)
print("  LEFT  JOIN: \n",df_1.join(df_2,how='left' , lsuffix='_caller', rsuffix='_other'))
print("  RIGHT JOIN: \n",df_1.join(df_2,how='right', lsuffix='_caller', rsuffix='_other'))
print("  INNER JOIN: \n",df_1.join(df_2,how='inner', lsuffix='_caller', rsuffix='_other'))
print("  OUTER JOIN: \n",df_1.join(df_2,how='outer', lsuffix='_caller', rsuffix='_other'))
#------------------------------------------------------------------------------------------------------
print("*"*50)

left_df = pd.DataFrame({'key':['K0','K1','K4','K7'],
                        'B':[45,23,45,2]})
right_df= pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                        'A': ['1', '2', '4', '23', '2', '78'],
                        'B': ['4', '41', '32', '23', '74', '5']})

print(f'left_df=\n',left_df)
print(f'right_df=\n',right_df)
print("_"*50)
print("Unión interna  \n  inner join/merge: ")

'''
Inner merge
Igual que en SQL podemos hacer un inner join con Pandas usando el método .merge. El método .merge busca las columnas que son comunes entre dos data frames y luego mira las filas donde esos valores de las columnas son iguales. Luego combina las columnas que hacen match en una sola fila en una nueva tabla.
new_df = pd.merge(orders, customers)
print(new_df)
Hagamos algunos ejercicios más con otros dataframes antes de continuar usando los importados.
Dados los siguientes dataframes:
sales = pd.DataFrame({
'month': ['January', 'February', 'March', 'April', 'May', 'June'],
'revenue': [300, 290, 310, 325, 475, 495]
})

targets = pd.DataFrame({
'month': ['January', 'February', 'March', 'April', 'May', 'June'],
'target': [310, 270, 300, 350, 475, 500]
})
usted necesita analizar las ventas. Creemos un nuevo data frame llamado sales_vs_targets el cual contiene el inner join entre sales y targets
sales_vs_targets = pd.merge(sales, targets)
print(sales_vs_targets)
La empresa quiere saber los meses en que alcanzaron sus objetivos (targets) de ventas (revenue). Para ello seleccionamos las filas de sales_vs_targets donde revenue es mayor a target. Guárdelo en una variable llamada lo_logramos
lo_logramos = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]
print(lo_logramos)
Inner merge II
Volvamos a los datos que importamos al principio. Adicional a usar pd.merge, cada data frame tiene su propio método merge. Si queremos hacer merge entre orders y customers, podemos usar:
new_df = orders.merge(customers)

print(new_df)
Esto produce el mismo data frame que sí hemos llamado pd.merge(orders, customers). Usamos la última sintaxis generalmente cuando estamos haciendo merge en más de dos dataframes, a los que llamamos encadenar los comandos. Miremos un ejemplo:
big_df = orders.merge(customers).merge(products)
print(big_df)
Este comando hizo merge primero entre orders y customers y luego ese resultado (nuevo data frame) le hace merge con products.
¿Es importante el orden del merge? Si. El orden de los merge afectan el orden de las filas y columnas del data frame resultante. Cuando usamos el método merge() se preservará el orden de las llaves de la izquierda.
df1.merge(df2).merge(df3) => preservará el orden del df1 cuando hace el merge con el df2. E igual será preservado cuando haga merge con df3
Sin embargo, si ese orden no nos interesa mantenerlo, podemos hacer algo como:
df3.merge(df1).merge(df2) => mismo resultado con diferente orden.
Merge en columnas específicas
En el anterior ejemplo de products y orders ambos tenían una columna llamada product_id. Sin embargo, normalmente cada tabla tiene es una columna llamada simplemente id. El id puede significar algo diferente en cada tabla, y esto podría generarnos un error al hacer merge. Una forma que tenemos para solucionar esto es con el método .rename para renombrar las columnas de nuestro merge.
En el siguiente ejemplo vamos a renombrar la columna id por customer_id, así orders y customers tienen una columna en común para el merge
pd.merge(orders, customers.rename(columns={'id': 'customer_id'}))
Hagamos ahora un merge sobre orders y products usando rename. Guardemos el resultado en la variable orders_products e imprímala
orders_products = pd.merge(orders, products.rename(columns={'id': 'product_id'}))

print(orders_products)
Pregunta: Es la columna id similar a los primary keys de SQL? Son similares, pero la funcionalidad no es la misma que para SQL. En SQL las primary key proveen un “constraint” (validación) en donde los valores de esa columna deben ser únicos. Y dará un error si no lo son. En Pandas no hay en sí una primary key constraint, y la columna con el id puede tener valores duplicados
Entonces cuando trabajemos con dataframes necesitamos asignarle a la columna algo como “actúe como primary key” y prevenir valores duplicados en esa columna
Mismatched Merges
Anteriormente vimos que siempre las columnas hacen match, pero qué pasa si no? Imaginemos que nuestra tabla product está desactualizada y no tiene el producto más nuevo: “Product 5”. Que pasara en este caso? Lo que sucederá es simplemente que este nuevo producto no será incluido en el data frame resultante. Recuerden que es un inner merge igual a SQL, y sólo retorna valores que hacen match
Outer Merge
Ya vimos que perdemos datos si hay filas que no hacen match. Supongamos que dos empresas se van a fusionar. Cada una tiene un listado de clientes, pero con algunos datos diferentes. La compañía A tiene nombre e email. Y la B tiene nombre y teléfono. Así mismo tienen algunos clientes en común, pero otros son diferentes
Si queremos combinar los datos sin perder los datos de ambas empresas, usamos un “Outer merge”. Incluirá todas las filas de ambas tablas, incluso si no hacen match. Los valores faltantes se reemplazan con None o nan
pd.merge(company_a, company_b, how='outer')
Left Merge
Supongamos que queremos identificar cuáles consumidores no tienen el teléfono. Podríamos querer una lista de todos los consumidores que tienen email, pero no tienen phone. Podemos hacer esto corriendo un Left Merge. Los left incluyen todas las filas de la primera tabla (left) pero solo las filas de la segunda tabla (right) que hacen match con la primera tabla.
En este caso el orden SÍ importa, porque la primera tabla será la de la izquierda
pd.merge(company_a, company_b, how='left')
Right Merge
Es exactamente lo opuesto al left merge. Aquí la tabla final va a contener todas las filas de la tabla de la derecha, pero solo las filas de la primera con las que haga match

'''



print("pd.merge(left_df,right_df,on=['key','key'])\n",pd.merge(left_df,right_df,on=['key','key']))
print("pd.merge(right_df,left_df,on=['key','key'])\n",pd.merge(right_df,left_df,on=['key','key']))
print("pd.merge(right_df,left_df,on=['key','key'],how='inner')\n",pd.merge(left_df,right_df,on=['key','key'],how='inner'))
print("_"*50)
print("pd.DataFrame.join(left_df,right_df,lsuffix='key')\n",pd.DataFrame.join(left_df,right_df,lsuffix='key',rsuffix='key',how='inner'))
print("pd.DataFrame.join(left_df,right_df,rsuffix='key')\n",pd.DataFrame.join(right_df,left_df,lsuffix='key',rsuffix='key',how='inner'))
print("pd.DataFrame.join(left_df,right_df,how='inner',lsuffix='key',rsuffix='key')n",pd.DataFrame.join(left_df,right_df,how='inner',lsuffix='key',rsuffix='key'))
print("Unión externa  \n  outer join/merge: ")
print("pd.DataFrame.join(left_df,right_df,rsuffix='key')\n",pd.DataFrame.join(right_df,left_df,lsuffix='key',rsuffix='key',how='outer'))
print("pd.merge(right_df,left_df,on=['key','key'],how='outer')\n",pd.merge(left_df,right_df,on=['key','key'],how='outer'))
print("_"*50)
print("Unión izquierda\n  left join/merge: ")
print("pd.merge(right_df,left_df,on=['key','key'],how='left' )\n",pd.merge(left_df,right_df,on=['key','key'],how='left'))
print("left_df.join(right_df,how='left', lsuffix='_caller', rsuffix='_other')=\n",left_df.join(right_df,how='left', lsuffix='_caller', rsuffix='_other'))
print("pd.DataFrame.join(left_df,other =right_df,how='left', lsuffix='_caller', rsuffix='_other')=\n",pd.DataFrame.join(left_df,other =right_df,how='left', lsuffix='_caller', rsuffix='_other'))
print("left_df.set_index('key').join(right_df.set_index('key'),lsuffix='_caller', rsuffix='_other')=\n",left_df.set_index('key').join(right_df.set_index('key'),lsuffix='_caller', rsuffix='_other'))
print("_"*50)
print("Unión derecha  \n  right join/merge: ")
print("pd.merge(right_df,left_df,on=['key','key'],how='right')\n",pd.merge(left_df,right_df,on=['key','key'],how='right'))
print("left_df.join(right_df,how='right', lsuffix='_caller', rsuffix='_other')=\n",left_df.join(right_df,how='right', lsuffix='_caller', rsuffix='_other'))
print("pd.DataFrame.join(left_df,other =right_df,how='right', lsuffix='_caller', rsuffix='_other')=\n",pd.DataFrame.join(left_df,other =right_df,how='right', lsuffix='_caller', rsuffix='_other'))
print("right_df.set_index('key').join(left_df.set_index('key'),lsuffix='_caller', rsuffix='_other')=\n",right_df.set_index('key').join(left_df.set_index('key'),lsuffix='_caller', rsuffix='_other'))
#------------------------------------------------------------------------------------------------------

df1 = pd.DataFrame({'a1': [1, 1, 2, 2, 3],
                     'b': [1, 1, 2, 2, 2],
                     'c': [13, 9, 12, 5, 5]})
df2 = pd.DataFrame({'a2': [1, 2, 2, 2, 3],
                     'c': [1, 1, 1, 2, 2],
                     'd': [15, 16, 17, 18, 13]})
pd.merge(df1, df2, how='left', left_on=['a1', 'c'], right_on = ['a2','c'])
print(pd.merge(df1, df2, how='left', left_on=['a1', 'c'], right_on = ['a2','c']))

#------------------------------------------------------------------------------------------------------
print("*"*50)
df_1 = pd.DataFrame(
    {   'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
        'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
df_2 = pd.DataFrame(
    {   'key': ['K0', 'K1', 'K2'],
        'B': ['B0', 'B1', 'B2']} )
print(f"df=\n{df_1}")
print(f"df=\n{df_2}")
print('''
Unir a `DataFrames` usando sus índices.
''')
ww=df_1.join(df_2, lsuffix='_caller', rsuffix='_df_2')
print("df_1.join(df_2, lsuffix='_caller', rsuffix='_df_2')",ww)
#------------------------------------------------------------------------------------------------------
print("*"*50)
print('''
Unilos usando las columnas clave, debemos configurar la clave para que sea el índice tanto en df_1 como en otro. 
    El df unido tendrá una clave como índice.
''')
ww = df_1.set_index('key').join(df_2.set_index('key'))
print("df_1.set_index('key').join(df_2.set_index('key')=\n",ww)
#------------------------------------------------------------------------------------------------------
print("*"*50)
print('''
Otra opción para unirse usando las columnas clave es usar el parámetro on . 
    df.join siempre usa el índice de otros , pero podemos usar cualquier columna en df_1 . 
    Este método conserva el índice del `DataFrame` original en el resultado.
''')
ww=df_1.join(df_2.set_index('key'), on='key')
print("df_1.join(df_2.set_index('key'), on='key')=\n",ww)
#------------------------------------------------------------------------------------------------------
print("*"*50)
print('''
El uso de valores clave no únicos muestra cómo se combinan.
''')
df_1 = pd.DataFrame({'key': ['K0', 'K1', 'K1', 'K3', 'K0', 'K1'],
                   'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})

ww = df_1.join(df_2.set_index('key'), on='key', validate='m:1')
print("df_1.join(df_2.set_index('key'), on='key', validate='m:1')=\n",ww)
#------------------------------------------------------------------------------------------------------
print("*"*50)
df_1 = pd.DataFrame(
    [[1, 2, 3, 4], [6, 7, 8, 9]], 
    columns=["A", "B", "C", "D"], 
    index=[1, 2]
)
df_2 = pd.DataFrame(
    [[10, 20, 30, 40], [60, 70, 80, 90], [600, 700, 800, 900]],
    columns=["A", "B", "D", "E"],
    index=[2, 3, 4],
)
print(f"df=\n{df_1}")
print(f"df=\n{df_2}")
#------------------------------------------------------------------------------------------------------
print("*"*104)
print("*",'outer'.center(100),"*")
print("*"*104)
left_join, right_join = df_1.align(df_2, join="outer", axis=None)
print("left_join, right_join = df_1.align(df_2, join='outer', axis=1)\nleft_join=\n",left_join)
print("left_join, right_join = df_1.align(df_2, join='outer', axis=1)\nright_join=\n",right_join)
#------------------------------------------------------------------------------------------------------
print("*"*50)
left_join, right_join = df_1.align(df_2, join="outer", axis=0)
print("left_join, right_join = df_1.align(df_2, join='outer', axis=1)\nleft_join=\n",left_join)
print("left_join, right_join = df_1.align(df_2, join='outer', axis=1)\nright_join=\n",right_join)
#------------------------------------------------------------------------------------------------------
print("*"*50)
left_join, right_join = df_1.align(df_2, join='outer', axis=1)
print("left_join, right_join = df_1.align(df_2, join='outer', axis=1)\nleft_join=\n",left_join)
print("left_join, right_join = df_1.align(df_2, join='outer', axis=1)\nright_join=\n",right_join)
#------------------------------------------------------------------------------------------------------
print("*"*50)
#------------------------------------------------------------------------------------------------------
print("*"*50)
left_join, right_join = df_1.align(df_2, join="inner", axis=None)
print("left_join, right_join = df_1.align(df_2, join='inner', axis=1)\nleft_join=\n",left_join)
print("left_join, right_join = df_1.align(df_2, join='inner', axis=1)\nright_join=\n",right_join)
#------------------------------------------------------------------------------------------------------
print("*"*104)
print("*",'inner'.center(100),"*")
print("*"*104)
left_join, right_join = df_1.align(df_2, join="inner", axis=0)
print("left_join, right_join = df_1.align(df_2, join='inner', axis=1)\nleft_join=\n",left_join)
print("left_join, right_join = df_1.align(df_2, join='inner', axis=1)\nright_join=\n",right_join)
#------------------------------------------------------------------------------------------------------
print("*"*50)
left_join, right_join = df_1.align(df_2, join='inner', axis=1)
print("left_join, right_join = df_1.align(df_2, join='inner', axis=1)\nleft_join=\n",left_join)
print("left_join, right_join = df_1.align(df_2, join='inner', axis=1)\nright_join=\n",right_join)
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
print(f"df=\n",df)
#######################################################################################################
print(f'''
●  Genera una consulta con la función cut dado un `DataFrame` con datos en una columna que tenemos que convertir 
            a otros categóricos segun condiciones enunciadas.
''')
def Solucion():
    pass
exam_data = {'nombre':      ['Anastasia', 'Anatolio', 'Katherine', 'Pepe', 'Gregorio', 'Tito', 'Luly', 'JJ ', 'Bebe', 'Bety'],
             'puntuación':  [12.5, 9, 16.5, 5.7, 9, 20, 14.5, 9.3, 8, 19],
             'intentos':    [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'edad':        [7,10, 4,18,72, 1,21,30,16,90],
             'califico':    ['sí', 'no', 'sí', 'no', 'no', 'sí', 'sí', 'no', 'no', 'sí']}
etiquetas =                 ['a',  'b',  'c',  'd',  'e', 'f',  'g',  'h',  'i',  'j']
df =pd.DataFrame(data=exam_data,index=etiquetas)

df["grupo_edad"] = pd.cut(df["edad"], bins = [0,2,18, 65, 99], labels = ["bebes","niños", "adultos", "anciano"])
print(f"df=\n",df)
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
● Genera una consulta con la función `filter(). 
Esto permite al usuario realizar consultas más avanzadas y complicadas con filtros en el `DataFrame`. 
Estas son abstracciones de nivel superior a df.loc 
''')
def Solución():
    pass
nombre =   ['Oliva', 'Daniela', 'Juan', 'Germán', 'Edward', 'Alex', 'Julio', 'Edgar', 'Angie', 'Irlesa']
puntaje =  [11.5, 8, 15.5, np.nan, 8, 19, 13.5, np.nan, 8, 18]
intentos = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
califico = ['Sí', 'No', 'Sí', 'No', 'No', 'Sí', 'Sí', 'No', 'No', 'Sí']
indices =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
jugadores = {'nombre': nombre, 'puntaje': puntaje, 'intentos': intentos, 'califico': califico}
df = pd.DataFrame(data=jugadores, index=indices)
print("*"*54)
print("*",'filter'.center(50),"*")#                              filter
print("*"*54)
print(f"df=\n{df}")
#------------------------------------------------------------------------------------------------------
print("*"*50)
ww = df.filter(items=["nombre","califico"])
print(f"df.filter(items=['nombre','califico'])=\n",ww)
#------------------------------------------------------------------------------------------------------
print("*"*50)
ww = df.filter(items=["nombre","califico"]).groupby('califico')
for filtro,grupo in ww:
    print (filtro,grupo)
print("*"*50)
# We can specify the regex literal under regex in the function
# ~ df.filter(regex="^C")
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
● Genera una consulta con la función df.query() con mas de un filtro. 
Esto permite al usuario realizar consultas más avanzadas y complicadas con multiples filtros en el `DataFrame`. 
Estas son abstracciones de nivel superior a df.loc 
''')
def Solución():
    pass
nombre =   ['Oliva', 'Daniela', 'Juan', 'Germán', 'Edward', 'Alex', 'Julio', 'Edgar', 'Angie', 'Irlesa']
puntaje =  [11.5, 8, 15.5, np.nan, 8, 19, 13.5, np.nan, 8, 18]
intentos = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
califico = ['Sí', 'No', 'Sí', 'No', 'No', 'Sí', 'Sí', 'No', 'No', 'Sí']
indices =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
jugadores = {'nombre': nombre, 'puntaje': puntaje, 'intentos': intentos, 'califico': califico}
df = pd.DataFrame(data=jugadores, index=indices)
print("*"*54)
print("*",'query'.center(50),"*")#                              query
print("*"*54)
print(f"df=\n{df}")
#------------------------------------------------------------------------------------------------------
print("*"*50)
ww = df.query("califico=='Sí' & puntaje>10 & intentos <=2" )
print("""df.query("califico=='Sí' & puntaje>10 & intentos <=2" )=\n""",ww)
#------------------------------------------------------------------------------------------------------
print("*"*50)
ww = df.query("califico=='Sí' & puntaje>10 & intentos <=2").groupby('califico')
for filtro,grupo in ww:
    print (filtro,grupo)
    

valor=1.5
# Seleccionar filas que cumplan cierta condición
filtro = df['intentos'] > valor
seleccion = df[filtro]
valor_1 = 10
valor_2 = 2
# Filtrar filas basándose en varias condiciones
filtro_multiple = (df['puntaje'] >= valor_1) & (df['intentos'] >= valor_2)
seleccion = df[filtro_multiple]
 
    
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
● Selecciona los datos unicos de la columna Y.
''')
def Solución():
    pass
datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)
ww = df.Y.unique()
print(f"df.Y.unique()=\n{ww}") 
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
● Encontrar registros de un `DataFrame` que cumplan una condición de métodos string respecto a una columna.
''')
def Solución():
        pass
datos = {'nombre': ["Rebeca", "Pedro", "Humberto", "Anatolio", "Morticia"], 'apellido': ["Gonzalez", "Gomez", "Garcia", "Perez", "Addams"], 'salario': [2500, 3000, 5000, 7000, 1000],'turno':[1,2,3,1,2] }
indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)
print(f"{df.head(10)=}")
resultado = df[df.salario <= 3000]
print(f"{resultado=}")
print(f"{len(resultado)=}")
print(f"{len(df)=}")
for index, registro in resultado.iterrows():
    print(f"{registro['nombre']:<10}{registro['apellido']:>30}{registro['salario']:>20}")
#------------------------------------------------------------------------------------------------------
print(f'''
● Obtener los registros donde el `nombre` empiece con `A`.
''')
resultado = df[df['nombre'].str[:1] == 'A']
print(f"{resultado}")
#------------------------------------------------------------------------------------------------------
print(f'''
● Obtener los registros donde el `nombre` empiece ya sea por `A` , `M` o `R`.
''')
resultado = df[df['nombre'].str[:1].isin(['A','M','R'])]
print(f"{resultado}")
print("*"*50)
#------------------------------------------------------------------------------------------------------
print(f'''
● Obtener los registros donde el `apellido` de un empleado no contengan *g*.
''')
resultado = df[df['apellido'].str.lower().str.find('g') == -1]
print(f"{resultado}")
print("*"*50)
#------------------------------------------------------------------------------------------------------
print(f'''
● Ordenar en modo descendente los empleados a partir de su `turno`.  
''')
resultado = df.sort_values('turno', ascending=False)
print(f"{resultado}")
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
● crea una con la función `melt`.
''')
def Solución():
    pass
df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                   'B': {0: 1, 1: 3, 2: 5},
                   'C': {0: 2, 1: 4, 2: 6}})
print(f"df=\n{df}")
ww = pd.melt(df, id_vars=['A'], value_vars=['B'])
print(f"df=\n{ww}")
ww = pd.melt(df, id_vars=['A'], value_vars=['B', 'C'])
print(f"df=\n{ww}")
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
●  calcula la correlación entre columnas con el método `.corr()`.
''')

def Solución():
    pass
datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)
print(f"df=\n{df}")
#------------------------------------------------------------------------------------------------------
df.plot.scatter(x='X', y='Y')
plt.show(block=False)
plt.pause(3)
plt.close() 
#------------------------------------------------------------------------------------------------------
ww = df.corr()
print(f"df=\n{ww}")
# create a scatter plot to visualize the relationship between two columns
ww.plot.scatter(x='X', y='Y')
plt.show(block=False)
plt.pause(3)
plt.close()
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
●  resultado = df[df['Z'].isin([2, 3])] in resultado.iterrows():
''')

def Solución():
    pass
datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)
#------------------------------------------------------------------------------------------------------
resultado = df[df['Z'].isin([2, 1])]

print("*"*50)
print("df[df['Z'].isin([2, 1])]")
print('X'.ljust(5), 'Y'.ljust(5), 'Z'.center(5))
for index, f in resultado.iterrows():
    print(str(f['X']).ljust(5), str(f['Y']).ljust(5), str(f['Z']).center(5))
resultado = df[~df['Z'].isin([2, 1])]
print("*"*50)
print("df[ ~ df['Z'].isin([2, 1])]")
print('X'.ljust(5), 'Y'.ljust(5), 'Z'.center(5))
for index, f in resultado.iterrows():
    print(str(f['X']).ljust(5), str(f['Y']).ljust(5), str(f['Z']).center(5))
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
● 
''')

def Solución():
    pass
datos = {'X': [1, 2, 3, 4, 1], 'Y': [5, 2, 3, 2, 0], 'Z': [2, 2, 5, 7, 1]}
indices = ['a', 'b', 'c', 'd', 'e']
df = pd.DataFrame(data=datos, index=indices)

#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
print(f'''
● Seleciona de un objeto `DataFrame` la informacion númerica con la función select_dtypes.
''')
def Solución():
    pass
lenguajes =    ['Python', 'Java', 'C#', 'JavaScript', 'C++', 'PHP']
año_creacion = [1990, 1995, 2013, 1995, 1985, 1995]
interpretado = [True, False, False, True, False, True]
extension =    ['.py', '.java', 'cs', 'js', 'cpp', 'php']
indices =      ['a', 'b', 'c', 'd', 'e', 'f']
datos = {'lenguaje': lenguajes, 'año_creacion': año_creacion, 'interpretado': interpretado, 'extesion': extension}
df = pd.DataFrame(data=datos, index=indices)
print(f"df={df}")
print(f"{df.columns=}")
print(f"{df.index=}")
print(f"df.info:{df.info}")
ww = df.select_dtypes(include = ["number"])
print(f"df.select_dtypes(include = ['number'])=\n",ww)
print("*"*100)
pausa()
limpiar()
#######################################################################################################
#######################################################################################################
print(f'''
● Mostrar el uso de memoria de un `DataFrame` dado y cada columna de este.
    cambiar los tipos de datos y volver a chequear el uso de memoria
''')
def Solucion():
    pass
'''
tipo de d	código de carácter	descripción
int8	        i1	    entero con signo de 8 bits
int16	        i2	    entero con signo de 16 bits
int32	        i4	    entero con signo de 32 bits 
int64	        i8	    entero con signo de 64 bits
uint8	        u1	    entero sin signo de 8 bits
uint16	        u2	    entero sin signo de 16 bits
uint32	        u4	    entero sin signo de 32 bits
uint64	        u8	    entero sin signo de 64 bits
float16	        f2	    número de punto flotante de 16 bits
float32	        f4	    número de coma flotante de 32 bits
float64	        f8	    número de punto flotante de 64 bits
float128	    f16	    número de punto flotante de 128 bits
complex64	    c8	    número de punto flotante complejo de 64 bits
complex128	    c16	    número de punto flotante complejo de 128 bits
complex256	    c32	    número de punto flotante complejo de 256 bits
bool	        ?	    Booleano (Verdadero o Falso)
unicode	        tu	    Cadena Unicode
object	        O	    Objetos de Python
'''
exam_data = {'nombre':      ['Anastasia', 'Anatolio', 'Katherine', 'Pepe', 'Gregorio', 'Tito', 'Luly', 'JJ ', 'Bebe', 'Bety'],
             'puntuación':  [12.5, 9, 16.5, 5.7, 9, 20, 14.5, 9.3, 8, 19],
             'intentos':    [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'edad':        [7,10, 4,18,72, 1,21,30,16,90],
             'califico':    ['sí', 'no', 'sí', 'no', 'no', 'sí', 'sí', 'no', 'no', 'sí']}
etiquetas =                 ['a',  'b',  'c',  'd',  'e', 'f',  'g',  'h',  'i',  'j']
tipo_de_datos={'nombre':  'object','puntuación':'int8', 'intentos':  'float16','edad': 'int8','califico':'object'}
# ~ tipo_de_datos={'nombre':  str,'puntuación':float, 'intentos':  int,'edad': int,'califico':str}
df =pd.DataFrame(data=exam_data,index=etiquetas)

print(f"df=\n",df)
print ("df.dtype()=\n",df.dtypes)
print("\nUso total de memoria del DataFrame:",df.info(memory_usage = "deep"))
print("\nUso de memoria en cada columna del DataFrame:",df.memory_usage(deep = True))
#------------------------------------------------------------------------------------------------------
print("-"*20,":)")
print("cambio tipo de datos".center(50))
df=df.astype(tipo_de_datos)

print(f"df=\n",df)
print ("df.dtype()=\n",df.dtypes)
print("\nUso total de memoria del DataFrame:",df.info(memory_usage = "deep"))
print("\nUso de memoria en cada columna del DataFrame:",df.memory_usage(deep = True))
# ~ print(f"df.applymap(type)=\n",df.applymap(type))
#------------------------------------------------------------------------------------------------------
print("-"*20,":)")
pausa()
limpiar()

