# 📄 Documento: 5 Casos de prueba - tabla de equivalencia - Buscador-DRahorro--.xlsx

## 📑 Hoja: buscador-clase equivalencia

| Tabla de Equivalencia   | Unnamed: 1           | Unnamed: 2   | Unnamed: 3               | Unnamed: 4         | Unnamed: 5                        |
|:------------------------|:---------------------|:-------------|:-------------------------|:-------------------|:----------------------------------|
| ID                      | Variables            | Número       | Clase Equivalencia       | Válida o Inválida  | Valores Interesantes a Considerar |
| CE003                   | buscador             | 1            | caracteres alfanumerico  | válido             | actron                            |
|                         |                      | 2            | caracteres especiales    | inválido           | !"###                             |
|                         |                      | 3            | que no permita campo ""  | inválido           | ""                                |
| 2                       | tabla caso de prueba |              |                          |                    |                                   |
| Casos de Prueba         |                      |              |                          |                    |                                   |
| ID                      | buscador             |              | NUMERO CLAS EQUIVALENCIA | RESULTADO ESPERADO |                                   |
| CP1                     | actron               |              | 1                        | VALIDO             |                                   |
| CP2                     | !"###                |              | 2                        | INPUT ERROR        |                                   |
| CP3                     | ""                   |              | 3                        | INPUT ERROR        |                                   |

