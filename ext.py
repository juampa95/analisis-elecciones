import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)

dtype_options = {
    7: 'str',
    10: 'str',
    11: 'str',
    20: 'str'
}
df = pd.read_csv('data/ResultadosElectorales_2023.csv',
                 dtype=dtype_options)

print(df.describe(include='all').T)

print(df.sort_values(by='votos_cantidad', ascending=False).head(10))

print(df[df['mesa_electores'] == 350].head(40))

result = df[
    (df['cargo_nombre'] == 'PRESIDENTE Y VICE')
].groupby('agrupacion_nombre')['votos_cantidad'].sum().reset_index()

print(result)


result_por_mesa = df[
    (df['cargo_nombre'] == 'PRESIDENTE Y VICE')
].groupby(['agrupacion_nombre',
           'circuito_id'])['votos_cantidad'].sum().reset_index()

print(result_por_mesa.head(10))

### FILTRADO POR CIRCUITO_ID o ESCUELA

filtered_df = df[df['cargo_nombre'] == 'PRESIDENTE Y VICE']
pivot_df = pd.pivot_table(filtered_df,
                          index='circuito_id',
                          columns='agrupacion_nombre',
                          values='votos_cantidad',
                          aggfunc='sum')
pivot_df = pivot_df.reset_index().fillna(0)


print(pivot_df.head(10))


pivot_df.to_csv('data/agrupacion_por_circuito.csv', index=False)


## FILTRADO POR MESA

filtered_df = df[df['cargo_nombre'] == 'PRESIDENTE Y VICE']
pivot_df = pd.pivot_table(filtered_df,
                          index=['mesa_electores', 'mesa_id'],
                          columns='agrupacion_nombre',
                          values='votos_cantidad',
                          aggfunc='sum')
pivot_df = pivot_df.reset_index().fillna(0)


print(pivot_df.sort_values(by='UNION POR LA PATRIA',
                           ascending=False).head(10))

pivot_df.describe()

print(pivot_df.head(50))

print(pivot_df.sum())

pivot_df.to_csv('data/agrupacion_por_mesa.csv', index=False)

