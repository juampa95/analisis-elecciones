import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)


df2 = pd.read_csv('data/agrupacion_por_circuito.csv')

print(df2.head())

agrupaciones = df2.columns[1:]

df2[agrupaciones] = df2[agrupaciones].astype(float)

for agrupacion in agrupaciones:
    df2[f'Porcentaje_{agrupacion}'] = (df2[agrupacion] / df2[agrupaciones].sum(axis=1))

df2.sort_values(by='Porcentaje_UNION POR LA PATRIA', ascending=False).head(50)

df2.sort_values(by='Porcentaje_LA LIBERTAD AVANZA', ascending=False).head(10)


def analisis(df, porcentaje:float ,partido:str):
    escuelas_filtradas = df[(df[f'Porcentaje_{partido}'] > porcentaje)]
    cant_escuelas = len(escuelas_filtradas)
    votos_escuelas_filtradas = escuelas_filtradas[partido].sum()
    return print(f'En una cantidad de {cant_escuelas} escuelas la agrupacion {partido} \n'
                 f'obtuvo mas del {porcentaje*100}% de los '
                 f'votos, sumando un total de {votos_escuelas_filtradas} votos')


analisis(df2, 0.9, 'UNION POR LA PATRIA')