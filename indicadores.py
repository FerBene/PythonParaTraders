
# se usan las librerias pandas, numpy, 


def indicador_tipo_de_vela(data):
  """ 
    Esta funcion recibe una matriz de datos, que posee la serie historica con los valores encolumnados por
    Open, High, Low, Close
  """
  df = data . copy()
  df["vela"] = np.where(df.Open < df.Close, "verde", np.where(df.Open == df.Close, "doji", "roja"))
  return df

def contar_positivos_negativos_neutros(data):
  positivos = 0
  negativos = 0
  neutros = 0
  for i in range(len(df)) :
    row = data.iloc[i]
    color = row["vela"]
    if color == "verde":
      positivos += 1
    elif color == "roja":
      negativos += 1 
    else:
      neutros +=1
  return positivos, negativos, neutros

def devolver_top_n_variacion(data, n=10, es_de_baja=True):
  df = data . copy() 
  df["variacion"]  = df["Close"].pct_change() * 100 
  df.dropna(inplace=True)
  return df.sort_values("variacion", ascending = es_de_baja ).head(n)

def devolver_con_percentil(data):
  df = data . copy()
  df["variacion"]  = df["Close"].pct_change() * 100 
  df.dropna(inplace=True)
  df["rank_variacion"] = df["variacion"].rank()
  df["rank_variacion_pct"] = df["variacion"].rank(pct= True)
  return df

def agregar_media_exponencial(data, periodos):
  df = data . copy()
  df[f"ewm_{periodos}"] = df["Close"].ewm(span= periodos)
  return df
