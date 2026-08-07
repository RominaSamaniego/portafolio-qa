# 📄 Documento: Plantilla de reporte de pruebas-DRahorro.xlsx

## 📑 Hoja: Hoja 1

| Plantilla de reporte de pruebas | Unnamed: 1 | Unnamed: 2 | Unnamed: 3 | Unnamed: 4 | Unnamed: 5 | Unnamed: 6 | Unnamed: 7 |
|---|---|---|---|---|---|---|---|
| ID | Titulos | Severidad | Pasos | Datos | Resultados esperados | Resultado obtenido | Evidencia |
|  | El sist.no guarda contacto con dominio .net | alta | 1-ingresar a la aplicacion. 2-hacer click en en la opcion "nuevo contacto". 3-completar los campos "nombre " y "mail" con datos . 4-hacer click en el boton guardar | https://nahual.github.io/qc-contactos/contactos.html?v=1 | el sist. debe almacenar el contacto y mostrarlo en la grilla | el valor ingresado no es un email |  |
| 6 | Alta de contacto con datos válidos | alta | 1.Ingresar a la aplicación. 2.Hacer clic en la opción "Nuevo Contacto". 3. Completar los campos "Nombre" y "Mail" con datos válidos. 4. Hacer clic en el botón "Guardar". | nombre:daniel | el sist. debe almacenar el contacto y mostrarlo en la grilla | almacena el contacto con exito |  |
|  |  |  |  | mail:dadani@gmail.com |  |  |  |
| 7 | Alta de contacto con nombre vacío | alta | 1. Hacer clic en la opción "Nuevo Contacto". 2. Completar el campo "Mail" con datos válidos. 3. Hacer clic en el botón "Guardar". | nombre:vacio | El sistema debe mostrar un mensaje informando que el campo "Nombre" es obligatorio. | guarda contacto sin el nombre no muestra pantalla con aviso de error |  |
|  |  |  |  | mail:jose@gmail.com |  |  |  |
| 8 | Alta de contacto con correo electrónico vacío | alta | 1. Hacer clic en la opción "Nuevo Contacto". 2. Completar el campo "Nombre" con datos válidos. 3. Hacer clic en el botón "Guardar". | nombre:juan | El sistema debe mostrar un mensaje informando que el campo "Mail" es obligatorio. | muestra en la oantalla un mensaje de error "mail obligatorio" |  |
|  |  |  |  | mail: vacio |  |  |  |
| 8 | Alta de contacto con correo electrónico con formato inválido | alta | 1. Hacer clic en la opción "Nuevo Contacto". 2. Completar el campo "Nombre" con datos válidos. 3. Hacer clic en el botón "Guardar". | nombre:juan | El sistema debe mostrar un mensaje informando que el valor ingresado no es un correo electrónico. | muestra en la pantalla un mensaje de error "El valor ingresado no es un email" |  |
|  |  |  |  | mail:juan/ajaj.com |  |  |  |
| 10 | Alta de contacto con correo electrónico duplicado | alta | 1. Agregar un contacto con un correo electrónico determinado. 2. Hacer clic en la opción "Nuevo Contacto". 3. Completar los campos "Nombre" y "Mail" con el mismo correo electrónico que el contacto agregado anteriormente. 4. Hacer clic en el botón "Guardar". | nombre:pepito | El sistema debe mostrar un mensaje informando que no es posible almacenar direcciones de correo duplicadas o existentes. | en la pantalla se muestra este mensaje "Ya existe un contacto con este mail" |  |
|  |  |  |  | mail:jose@gmail.com |  |  |  |

