#!/usr/bin/env python
# coding: utf-8

# # Análise Exploratória

# In[38]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


# In[39]:


df = pd.read_csv('../../dados/dadosCompletos_2021.csv', sep=';')


# In[40]:


pd.set_option('display.max_columns',999)
pd.set_option("display.max_rows", 999)


# In[41]:


df.sample(5)


# In[ ]:





# ## 1. Dimensões do data frame e tipos de dados

# In[42]:


print('A base de dados apresenta {} registros e {} características.'.format(df.shape[0], df.shape[1]))


# In[43]:


df.info(verbose=True)


# <p>Resultado do dtypes: float64(92), int64(5), object(28). 97 Características numéricas e 28 categóricas.</p>

# ### Característica classificadora

# In[44]:


categorias = df.categoria.value_counts()
categorias


# <p><b>Quadro classificação novilho precoce</b></p>

# <table style="width:100%; border: 1px solid black">
#     <tr>
#         <th style="border: 1px solid black; background:#90b3f0">Sexo</th>
#         <th style="border: 1px solid black; background:#90b3f0">PESO MACHO (MIN)</th>
#         <th style="border: 1px solid black; background:#90b3f0">PESO FEMEA (MIN)</th>
#         <th style="border: 1px solid black; background:#90b3f0">MATURIDADE</th>
#         <th style="border: 1px solid black; background:#90b3f0">ACABAMENTO</th>
#         <th style="border: 1px solid black; background:#90b3f0">INCENTIVO</th>
#         <th style="border: 1px solid black; background:#90b3f0" >CLASSIFICAÇÃO</th>
#     </tr>
#     <tr>
#         <td style="border: 1px solid black">M, C, F</td>
#         <td style="border: 1px solid black">225</td>
#         <td style="border: 1px solid black">180</td>
#         <td style="border: 1px solid black">j0</td>
#         <td style="border: 1px solid black">3 OU 4</td>
#         <td style="border: 1px solid black">67%</td>
#         <td style="border: 1px solid black">AAA</td>
#     </tr>
#     <tr>
#         <td style="border: 1px solid black">M, C, F</td>
#         <td style="border: 1px solid black">225</td>
#         <td style="border: 1px solid black">180</td>
#         <td style="border: 1px solid black">j2</td>
#         <td style="border: 1px solid black">3 OU 4</td>
#         <td style="border: 1px solid black">62%</td>
#         <td style="border: 1px solid black">AA</td>
#     </tr>
#     <tr>
#         <td style="border: 1px solid black">M, C, F</td>
#         <td style="border: 1px solid black">225</td>
#         <td style="border: 1px solid black">180</td>
#         <td style="border: 1px solid black">j0</td>
#         <td style="border: 1px solid black">2</td>
#         <td style="border: 1px solid black">62%</td>
#         <td style="border: 1px solid black">AA</td>
#     </tr>
#     <tr>
#         <td style="border: 1px solid black">C, F</td>
#         <td style="border: 1px solid black">225</td>
#         <td style="border: 1px solid black">180</td>
#         <td style="border: 1px solid black">j4</td>
#         <td style="border: 1px solid black">3 OU 4</td>
#         <td style="border: 1px solid black">48%</td>
#         <td style="border: 1px solid black">BBB</td>
#     </tr>
#     <tr>
#         <td style="border: 1px solid black">M, C, F</td>
#         <td style="border: 1px solid black">225</td>
#         <td style="border: 1px solid black">180</td>
#         <td style="border: 1px solid black">j2</td>
#         <td style="border: 1px solid black">2</td>
#         <td style="border: 1px solid black">39%</td>
#         <td style="border: 1px solid black">BB</td>
#     </tr>
#     <tr>
#         <td style="border: 1px solid black">C, F</td>
#         <td style="border: 1px solid black">225</td>
#         <td style="border: 1px solid black">180</td>
#         <td style="border: 1px solid black">j4</td>
#         <td style="border: 1px solid black">2</td>
#         <td style="border: 1px solid black">22%</td>
#         <td style="border: 1px solid black">C</td>
#     </tr>
#     <tr>
#         <td style="border: 1px solid black">M, C, F</td>
#         <td style="border: 1px solid black">>225</td>
#         <td style="border: 1px solid black">180</td>
#         <td style="border: 1px solid black">j6/j8</td>
#         <td style="border: 1px solid black">3 OU 4</td>
#         <td style="border: 1px solid black">0%</td>
#         <td style="border: 1px solid black">D</td>
#     </tr>
#     <tr>
#         <td style="border: 1px solid black">M, C, F</td>
#         <td style="border: 1px solid black">>225</td>
#         <td style="border: 1px solid black">180</td>
#         <td style="border: 1px solid black">j6/j8</td>
#         <td style="border: 1px solid black">>10</td>
#         <td style="border: 1px solid black">0%</td>
#         <td style="border: 1px solid black">D</td>
#     </tr>
#     <tr>
#         <td style="border: 1px solid black">M, C, F</td>
#         <td style="border: 1px solid black">>225</td>
#         <td style="border: 1px solid black">180</td>
#         <td style="border: 1px solid black">j6/j8</td>
#         <td style="border: 1px solid black">2</td>
#         <td style="border: 1px solid black">0%</td>
#         <td style="border: 1px solid black">D</td>
#     </tr>
# </table>

# <p>Há poucos registros das categorias caracteríscas classificadoras C e BB. A categoria D, a qual desclassifica a carcaça, esta em maior quantidade se comparada com as categoias C e B.</p>

# In[45]:


sns.catplot(x = "categoria", data = df, 
            kind="count", 
            aspect=2,
            order = categorias.index)


# ### 1.1 Observações: 

# <p style="color:#1155cc"><strong>Características identificadores: </strong>id_animal, estabelecimento_identificador e identificador_lote, desta forma podem ser retiradas.</p>

# ## 2.  Visualizando principais valores estatísticos

# In[46]:


df.describe().T


# ### 2.1 Possíveis outliers

# #### 2.1.1 Dados de precipitações - Total de chuvas - 7 dias

# In[47]:


def plotarBoxplot (titulo,x, dataset):
    sns.set_palette('Accent')
    sns.set_style('darkgrid')
    box_plot = sns.boxplot(x= x, data = dataset, orient = 'h')
    box_plot.figure.set_size_inches(18,8)
    box_plot.set_title(titulo, fontsize = 20)
    box_plot


# In[48]:


plotarBoxplot ('Total de chuvas - 7 dias', 'tot7d_chuva', df )


# <p>Quantidade de registros a acima do limite máximo:</p> 

# In[49]:


len(df.query('tot7d_chuva > 81.18'))


# <p>Quantidade de registros a acima de 600:</p> 

# In[50]:


len(df.query('tot7d_chuva > 600'))


# <p>Todos registro com valor maior que 600 correspondem a mesma data de abate:</p>

# In[51]:


#Seleção dos dados considerados outliers
df_outlier_preceptacao =  df.query('tot7d_chuva > 600')


# In[52]:


df_outlier_preceptacao.data_abate.value_counts()


# #### Dados de precipitações - Total de chuvas - média de 7 dias à 12meses

# In[53]:


def plotarBoxplotAgrupado (titulo, xlabel, dataset):
    sns.set_palette('Accent')
    sns.set_style('darkgrid')
    box_plot = sns.boxplot(x="variable", y="value", data=pd.melt(dataset))
    box_plot.set_xlabel(xlabel, fontsize=14)
    box_plot.figure.set_size_inches(20,15)
    box_plot.set_title(titulo, fontsize = 20)
    box_plot    


# In[54]:


df_chuva = pd.DataFrame(data = df, columns = ['tot7d_chuva','tot1m_chuva','tot3m_chuva', 'tot6m_chuva', 'tot12m_chuva'])


# In[55]:


plotarBoxplotAgrupado ('Total de precipitacao de chuva','total de chuva por período', df_chuva )


# #### 2.1.2 Temperatura Mínima

# In[56]:


df_tempmin = pd.DataFrame(data = df, columns = ['med7d_tempmin','med1m_tempmin','med3m_tempmin', 'med6m_tempmin', 'med12m_tempmin'])


# In[57]:


plotarBoxplotAgrupado ('Temperatura mínima','Temperatura mínima por período', df_tempmin )


# #### 2.1.3 Umidade instantânea

# In[58]:


df_umidinst = pd.DataFrame(data = df, columns = ['med7d_umidinst','med1m_umidinst','med3m_umidinst', 'med6m_umidinst', 'med12m_umidinst'])


# In[59]:


plotarBoxplotAgrupado ('Umidade instantânea','Umidade instantânea por período', df_umidinst )


# #### 2.1.4 Preço do Boi

# In[60]:


df_pre_boi = pd.DataFrame(data = df, columns = ['med7d_prer_boi','med1m_prer_boi','med3m_prer_boi', 'med6m_prer_boi', 'med12m_prer_boi'])


# In[61]:


plotarBoxplotAgrupado ('Preço da arroba do boi','Preço da arroba do boi por período', df_pre_boi )


# #### 2.1.5 Dados de Peso da carcaça

# In[62]:


plotarBoxplot ('Peso da carcaça', 'peso', df )


# In[63]:


def limitesBoxplot (caracteristica):
    Q1 = df[caracteristica].quantile(0.25)
    Q3 = df[caracteristica].quantile(0.75)
    IQR = Q3 - Q1
    LS = Q3 + ( 1.5 * IQR)
    LI = Q1 - ( 1.5 * IQR)
    print('Limite Infeiror: ',LI,' Limite Superior: ',LS)


# In[64]:


limitesBoxplot ('peso')


# ### 2.1.6 Observações:

# <p style="color:#1155cc">Foram encontrados valores discrepantes para as características acima, conforme apresentado nos respectivos gráficos Boxplot. Precisamos saber se condizem com a realidade ou serão considerados outliers.</p>

# ### 2.2 Valores repetidos: Dados do múmero de pixels

# In[65]:


df_num_pixels = pd.DataFrame(data = df, columns = ['med7d_num_pixels','med1m_num_pixels','med3m_num_pixels', 'med6m_num_pixels', 'med12m_num_pixels'])


# In[66]:


df_num_pixels.describe().T


# ### 2.2.1 Observações:

# <p style="color:#1155cc"> <strong>Valores repetidos: </strong>As características med7d_num_pixels, med1m_num_pixels, med3m_num_pixels, med6m_num_pixels e med12m_num_pixels possuem os mesmo valores, podemos manter uma característica.</p>

# ## 3. Dados ausentes

# <p>Calcular a porcentagem de valores ausentes.</p>

# In[67]:


round(df.isnull().mean() * 100,2).sort_values(ascending=False)


# <p>Calcular a quantidade de valores ausentes.</p>

# In[68]:


df.isnull().sum().sort_values(ascending=False)


# ### 3.1 Observações

# <p style="color:#1155cc"> É necessário o suporte técnico do especialista para nos dizer a relevância dessas características dentro da análise, ou se podemos imputar algum valor.</p>

# ## 4. Matriz de correlação

# <p>Para garantir melhor visualização as variáveis mensuradas por períodos diferentes não foram todas inclusas a matriz, foram considerados os registros referente ao período de mês</p> 

# In[69]:


selecao_mes = ['estabelecimento_municipio', 'data_abate',
       'tipificacao', 'maturidade', 'acabamento', 'peso',
       'motivo_desclassificacao', 'q_classificacao_estabel',
       'q_outros_incentiv', 'q_pratica_recuperacao_pa',
       'q_fertiirrigacao', 'q_ilp', 'q_ilpf', 'q_ifp', 'q_fabrica_racao',
       'q_identificacao_individual', 'q_regua_manejo', 'q_bpa',
       'q_aliancas_mercadolog', 'q_qual_alianca',
       'q_cobertura_vegetal_80_area', 'q_erosaoo_sulco_20_area',
       'q_sisbov', 'q_lista_trace', 'data12m', 'data6m', 'data3m',
       'data1m', 'data7d', 'tot7d_chuva', 'med7d_tempinst',
       'med7d_tempmax', 'med7d_tempmin', 'med7d_umidinst',
       'med7d_umidmax', 'med7d_umidmin', 'med7d_velventomax',
       'med7d_formituinst', 'med7d_formitumax', 'med7d_num_pixels',
       'med7d_ndvi', 'med7d_evi', 'med7d_prer_soja', 'med7d_prer_milho',
       'med7d_prer_boi', 'cnt7d_cl_itumax', 'cnt7d_cl_ituinst', 'ano', 'categoria', 'classificacao']


# In[70]:


df_matriz = pd.read_csv('../../dados/dadosCompletos.csv', encoding='ISO-8859-1', sep=';', usecols=selecao_mes)


# In[71]:


plt.figure(figsize=(20,15)) 
sns_plot = sns.heatmap(data=df_matriz.corr(),annot=True,cmap='coolwarm', square=True);
fig = sns_plot.get_figure()
fig.savefig("Matriz_Corr_resumido.png")


# ### Caracaterísticas com alta correlação:

# <table style="width:100%">
#   <tr>
#     <th>Caracterísica 1</th>
#     <th>Caracterísica 2</th>
#     <th>Correlação</th>
#   </tr>
#   <tr>
#     <td>Temperatura instantânea (tempinst)</td>
#     <td>Temperatura máxima (tempmax)</td>
#     <td>0,82</td>
#   </tr>
#   <tr>
#     <td>Temperatura instantânea (tempinst)</td>
#     <td>Temperatura mínima (tempmin)</td>
#     <td>0,88</td>
#   </tr>
#   <tr>
#     <td>Temperatura instantânea (tempinst)</td>
#     <td>Fómrula, índice de temperatura e umidade instantanea (formituint)</td>
#     <td>0,78</td>
#   </tr>
#   <tr>
#     <td>Temperatura instantânea (tempinst)</td>
#     <td>Classe na qual o ITU maximo se encontra (cl_itumax)</td>
#     <td>0,73</td>
#   </tr>
#   <tr>
#     <td>Temperatura máxima (tempmax)</td>
#     <td>Fórmula, índice de temperatura e umidade maxima (formintumax)</td>
#     <td>0,76</td>
#   </tr>
#   <tr>
#     <td>Temperatura máxima (tempmax)</td>
#     <td>Classe na qual o ITU máximo se encontra (cl_itumax)</td>
#     <td>0,79</td>
#   </tr>
#   <tr>
#     <td>Temperatura mínima (tempmin)</td>
#     <td>Fórmula, índice de temperatura e umidade instantânea (formituinst)</td>
#     <td>0,77</td>
#   </tr>
#   <tr>
#     <td>Umidade instantânea do ar (umidinst)</td>
#     <td>Umidade máxima (umidmax)</td>
#     <td>0,85</td>
#   </tr>
#   <tr>
#     <td>Umidade instantânea do ar (umidinst)</td>
#     <td>Umidade mínima do ar (umidmin)</td>
#     <td>0,87</td>
#   </tr>
#   <tr>
#     <td>Fórmula, índice de temperatura e umidade instantânea (formituinst)</td>
#     <td>Fórmula, índice de temperatura e umidade maxima (fomitumax)</td>
#     <td>0,92</td>
#   </tr>
#   <tr>
#     <td>Fórmula, índice de temperatura e umidade máxima (formituinst)</td>
#     <td>Classe na qual o ITU máximo se encontra (cl_itumax)</td>
#     <td>0,7</td>
#   </tr>
#   <tr>
#     <td>Índice de Vegetação da Diferença Normalizada (ndvi)</td>
#     <td>Índice de Vegetação Melhorado (evi)</td>
#     <td>0,95</td>
#   </tr>
#   <tr>
#     <td>Preço da Soja (prer_soja)</td>
#     <td>Preço do milho (prer_milho)</td>
#     <td>0,81</td>
#   </tr>
#   <tr>
#     <td>Classe na qual o ITU máximo (cl_itumax) </td>
#     <td>Fórmula, índice de temperatura e umidade máxima (formitumax)</td>
#     <td>0,69</td>
#   </tr>
# </table>
# 

# ### 4.1 Observações

# <p style="color:#1155cc"> Algumas características poussem um algo grau de correlação, podemos considera-las reundantes e manter apenas uma delas.</p>

# In[ ]:


names = df.columns[8:len(df)].tolist()
df.fillna(df.mean(), inplace=True)
array = df.values
X = array[:,8:len(df)]

