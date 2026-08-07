# 📄 Romina Samaniego - Casos de Prueba_plantilla de reporte de pruebas- Contactos-DRahorro.xlsx

## 📑 Hoja: Casos de Prueba - Contactos

<table>
  <thead>
    <tr>
      <th>PLANTILLA DE CASOS DE PRUEBA</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Escenario: Listado</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>ID</td>
      <td>Titulo</td>
      <td>Precondiciones</td>
      <td>Pasos</td>
      <td>Datos</td>
      <td>Resultado Esperado</td>
      <td>Resultado Obtenido</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Listado de contactos vacío</td>
      <td>El usuario no tiene contactos guardados en el sistema.</td>
      <td>1. Abrir la aplicación.</td>
      <td></td>
      <td>La pantalla debe mostrar el título "Contactos", una grilla vacía y el mensaje "No hay contactos guardados".</td>
      <td></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Listado de contactos con datos</td>
      <td>Es necesario contar con 5 contactos guardados - Ejecutar el CP Nº5 Alta de contacto con datos válidos</td>
      <td>1. Abrir la aplicación. 2. Verificar el contenido de la grilla.</td>
      <td></td>
      <td>La pantalla debe mostrar el título "Contactos", la grilla con los 5 contactos agregados y las opciones "Editar" y "Borrar" para cada contacto.</td>
      <td></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Ordenar contactos por nombre</td>
      <td>El usuario no tiene contactos guardados en el sistema.</td>
      <td>1. Agregar 5 contactos con diferentes nombres. 2. Abrir la aplicación. 3. Hacer clic en la columna "Nombre".</td>
      <td></td>
      <td>La grilla debe mostrar los contactos ordenados alfabéticamente por nombre.</td>
      <td></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Ordenar contactos por correo electrónico</td>
      <td>El usuario no tiene contactos guardados en el sistema.</td>
      <td>1. Agregar 5 contactos con diferentes correos electrónicos. 2. Abrir la aplicación. 3. Hacer clic en la columna "Mail".</td>
      <td></td>
      <td>La grilla debe mostrar los contactos ordenados alfabéticamente por correo electrónico.</td>
      <td></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Agregar nuevo contacto</td>
      <td>El usuario no tiene contactos guardados en el sistema.</td>
      <td>1. El usuario ingresa al sistema. 2. Seleccionar la opción para agregar un nuevo contacto.</td>
      <td>Nombre y correo electrónico del nuevo contacto.</td>
      <td>El sistema agrega el nuevo contacto a la lista de contactos y lo muestra en la grilla.</td>
      <td>El nuevo contacto se agrega correctamente a la lista de contactos y se muestra en la grilla.</td>
    </tr>
    <tr>
      <td>Escenario: Alta de contacto</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>ID</td>
      <td>Titulo</td>
      <td>Precondiciones</td>
      <td>Pasos</td>
      <td>Datos</td>
      <td>Resultado Esperado</td>
      <td>Resultado Obtenido</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Alta de contacto con datos válidos</td>
      <td>El usuario debe ingresar datos nuevos inexistentes</td>
      <td>1.Ingresar a la aplicación. 2.Hacer clic en la opción "Nuevo Contacto". 3. Completar los campos "Nombre" y "Mail" con datos válidos. 4. Hacer clic en el botón "Guardar".</td>
      <td>Nombre: Hernan - hernan@chicos.net - Link: https://nahual.github.io/qc-contactos/contactos.html?v=1</td>
      <td>El sistema debe almacenar el contacto y mostrarlo en la grilla.</td>
      <td></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Alta de contacto con nombre vacío</td>
      <td></td>
      <td>1. Hacer clic en la opción "Nuevo Contacto". 2. Completar el campo "Mail" con datos válidos. 3. Hacer clic en el botón "Guardar".</td>
      <td></td>
      <td>El sistema debe mostrar un mensaje informando que el campo "Nombre" es obligatorio.</td>
      <td></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Alta de contacto con correo electrónico vacío</td>
      <td></td>
      <td>1. Hacer clic en la opción "Nuevo Contacto". 2. Completar el campo "Nombre" con datos válidos. 3. Hacer clic en el botón "Guardar".</td>
      <td></td>
      <td>El sistema debe mostrar un mensaje informando que el campo "Mail" es obligatorio.</td>
      <td></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Alta de contacto con correo electrónico con formato inválido</td>
      <td></td>
      <td>1. Hacer clic en la opción "Nuevo Contacto". 2. Completar los campos "Nombre" y "Mail" con un correo electrónico con formato inválido. 3. Hacer clic en el botón "Guardar".</td>
      <td>Romina/gmail.com</td>
      <td>El sistema debe mostrar un mensaje informando que el valor ingresado no es un correo electrónico.</td>
      <td></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Alta de contacto con correo electrónico duplicado</td>
      <td></td>
      <td>1. Agregar un contacto con un correo electrónico determinado. 2. Hacer clic en la opción "Nuevo Contacto". 3. Completar los campos "Nombre" y "Mail" con el mismo correo electrónico que el contacto agregado anteriormente. 4. Hacer clic en el botón "Guardar".</td>
      <td>rominad@gmail.com</td>
      <td>El sistema debe mostrar un mensaje informando que no es posible almacenar direcciones de correo electrónico duplicadas.</td>
      <td></td>
    </tr>
    <tr>
      <td>Escenario: Edicion de contacto</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>ID</td>
      <td>Titulo</td>
      <td>Precondiciones</td>
      <td>Pasos</td>
      <td>Datos</td>
      <td>Resultado Esperado</td>
      <td>Resultado Obtenido</td>
    </tr>
    <tr>
      <td>11</td>
      <td>Ediciòn de contacto con datos válidos</td>
      <td>es necesario tener contactos ya agendados y si se sale sin guardar los datos mostrar en pantalla un mensaje informando que "se perderán los cambios"</td>
      <td>1. Abrir la aplicación. 2.El usuario selecciona la opción contacto. 3. El sistema muestra los "contactos". 4. El usuario selecciona la opción " EDITAR contacto". 5.El sistema muestra un pantalla con la siguiente información "EDITAR NOMBRE, MAIL". 7. Selecciona opcion "GUARDAR". 6 En la pantalla muestra un mensaje "contacto editado y guardado"</td>
      <td>El usuario está en el formulario para editar un contacto existente.</td>
      <td>La pantalla debe mostrar el título "Contactos". En la pantalla muestra un mensaje "contacto editado y guardado".</td>
      <td></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Ediciòn de contacto con nombre vacío</td>
      <td>es necesario tener contactos ya agendados y si se sale sin guardar los datos mostrar en pantalla un mensaje informando que "se perderán los cambios"</td>
      <td>1. Abrir la aplicación. 2.El usuario selecciona la opción contacto. 3. El sistema muestra los "contactos". 4. El usuario selecciona la opción " EDITAR contacto". 5.El sistema muestra un pantalla con la siguiente información "EDITAR NOMBRE. 6. El usuario deja campo nombre "Vacio" . 7.Selecciona opcion "GUARDAR". 8 En la pantalla muestra un mensaje "CAMPO NOMBRE VACIO ". 9. En la pantalla muestra no es posible guardar cambios.</td>
      <td></td>
      <td>El sistema debe mostrar un mensaje informando que el campo "Nombre" es obligatorio.</td>
      <td></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Ediciòn de contacto con correo electrónico vacío</td>
      <td>es necesario tener contactos ya agendados y si se sale sin guardar los datos mostrar en pantalla un mensaje informando que "se perderán los cambios"</td>
      <td>1. Abrir la aplicación. 2.El usuario selecciona la opción contacto. 3. El sistema muestra los "contactos". 4. El usuario selecciona la opción " EDITAR contacto". 5.El sistema muestra un pantalla con la siguiente información "EDITAR NOMBRE,MAIL. 7. El usuario deja campo "MAIL", "Vacio" . 8.Selecciona opcion "GUARDAR". 6 En la pantalla muestra un mensaje "CAMPO MAIL VACIO ". 9. En la pantalla muestra no es posible guardar cambios.</td>
      <td></td>
      <td>El sistema debe mostrar un mensaje informando que el campo "Correo electronico" es obligatorio.</td>
      <td></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Ediciòn de contacto con correo electrónico con formato inválido</td>
      <td>es necesario tener contactos ya agendados y si se sale sin guardar los datos mostrar en pantalla un mensaje informando que "se perderán los cambios"</td>
      <td>1. Abrir la aplicación. 2.El usuario selecciona la opción contacto. 3. El sistema muestra los "contactos". 4. El usuario selecciona la opción " EDITAR contacto". 5.El sistema muestra un pantalla con la siguiente información "EDITAR NOMBRE,MAIL. 7. El usuario coloca correo elctronico sin "@". 8.Selecciona opcion "GUARDAR". 6 En la pantalla muestra un mensaje " correo electrónico con formato inválido ". 9. En la pantalla muestra no es posible guardar cambios.</td>
      <td>ROMINA/GMAIL.COM</td>
      <td>El sistema debe mostrar un mensaje informando que el valor ingresado no es un correo electrónico.</td>
      <td></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Ediciòn de contacto con correo electrónico duplicado</td>
      <td>es necesario tener contactos ya agendados y si se sale sin guardar los datos mostrar en pantalla un mensaje informando que "se perderán los cambios"</td>
      <td>1. Abrir la aplicación. 2.El usuario selecciona la opción contacto. 3. El sistema muestra los "contactos". 4. El usuario selecciona la opción " EDITAR contacto". 5.El sistema muestra un pantalla con la siguiente información "EDITAR NOMBRE,MAIL. 7. El usuario coloca correo elctronico "duplicado". 8.Selecciona opcion "GUARDAR". 6 En la pantalla muestra un mensaje " el correo electronico esta duplicado por favor coloque nuevo correo".</td>
      <td></td>
      <td>El sistema debe mostrar un mensaje informando que el valor ingresado ya existe. Muestra en el pantalla "coloque nuevo correo electrónico".</td>
      <td></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Ediciòn de contactos con mas de 35 caracteres</td>
      <td>es necesario tener contactos ya agendados y si se sale sin guardar los datos mostrar en pantalla un mensaje informando que "se perderán los cambios"</td>
      <td>1. Abrir la aplicación. 2.El usuario selecciona la opción contacto. 3. El sistema muestra los "contactos". 4. El usuario selecciona la opción " EDITAR contacto". 5.El sistema muestra un pantalla con la siguiente información "EDITAR NOMBRE,MAIL. 7. El usuario coloca mas de "35 caracteres". 8.Selecciona opcion "GUARDAR". 6 En la pantalla muestra un mensaje " No fue posible guardar datos, solo hatas 35 caracteres".</td>
      <td>El usuario coloca un n ombre mas de 35 caracteres</td>
      <td>En la pantalla muestra un mensaje " No fue posible guardar datos, solo hatas 35 caracteres".</td>
      <td></td>
    </tr>
    <tr>
      <td>17</td>
      <td>ediciòn de contacto con texto numerico</td>
      <td>es necesario tener contactos ya agendados y si se sale sin guardar los datos mostrar en pantalla un mensaje informando que "se perderán los cambios"</td>
      <td>1. Abrir la aplicación. 2.El usuario selecciona la opción contacto. 3. El sistema muestra los "contactos". 4. El usuario selecciona la opción " EDITAR contacto". 5.El sistema muestra un pantalla con la siguiente información "EDITAR NOMBRE,MAIL. 7. El usuario coloca ene el campo nombre caracteres "alfanumerico" 8.Selecciona opcion "GUARDAR".</td>
      <td>Nombre: 12123123423</td>
      <td>En la pantalla muestra un mensaje " NO ES POSIBLE GUARDAR NUMEROS EN EL CAMPO NOMBRE,SOLO SE PERMITE LETRAS ".</td>
      <td></td>
    </tr>
    <tr>
      <td>Escenario: Baja de Contacto</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>ID</td>
      <td>Titulo</td>
      <td>Precondiciones</td>
      <td>Pasos</td>
      <td>Datos</td>
      <td>Resultado Esperado</td>
      <td>Resultado Obtenido</td>
    </tr>
    <tr>
      <td>18</td>
      <td>baja de contacto exitoso</td>
      <td>El usuario tiene al menos un contacto en el sistema.</td>
      <td>1. Abrir la aplicación. 2.El usuario selecciona la opción contacto. 3. El sistema muestra los "contactos". 4. El usuario selecciona la opción " ELIMINAR contacto". 5.El Usuario selecciona un contacto. en la pantalla se muestra "Está seguro que quiere borrar el contacto <Nombre del contacto>".hace click en confirmar.</td>
      <td>Nombre del contacto a eliminar: "ROMINA SAMANIEGO"</td>
      <td>se muestra en la pantalla contacto eliminado</td>
      <td>se elimino contacto</td>
    </tr>
    <tr>
      <td>19</td>
      <td>Cancelar eliminación</td>
      <td>El usuario tiene al menos un contacto en el sistema.</td>
      <td>1. Abrir la aplicación. 2.El usuario selecciona la opción contacto. 3. El sistema muestra los "contactos". 4. El usuario selecciona la opción " ELIMINAR contacto". 5.El Usuario selecciona un contacto. en la pantalla se muestra "Está seguro que quiere borrar el contacto <Nombre del contacto>". El usuario cancela y no se elimina el contacto El usuario selecciona la opción para eliminar un contacto.<br>El usuario selecciona la opción para eliminar un contacto Los datos del contacto no se eliminan y permanecen sin cambios.</td>
      <td>Nombre del contacto a eliminar: "ROMINA SAMANIEGO"</td>
      <td>se muestra en la pantalla "no se elimino ningun contacto"</td>
      <td>guardo la lista sin cambios</td>
    </tr>
    <tr>
      <td>20</td>
      <td>confirmacion incorrecta</td>
      <td>El usuario tiene al menos un contacto en el sistema.</td>
      <td>1. Abrir la aplicación. 2.El usuario selecciona la opción contacto. 3. El sistema muestra los "contactos". 4. El usuario selecciona la opción " ELIMINAR contacto". 5.El Usuario selecciona un contacto. en la pantalla se muestra "Está seguro que quiere borrar el contacto <Nombre del contacto>". 6. Seleccionar la opción de eliminar. 7. Confirmar el mensaje con un nombre incorrecto</td>
      <td>Nombre del contacto a eliminar: "ROMINA SAMANIEGO"</td>
      <td>El sistema muestra un mensaje de error indicando que el nombre del contacto no coincide.</td>
      <td>El sistema muestra un mensaje de error indicando que el nombre del contacto no coincide.</td>
    </tr>
    <tr>
      <td>21</td>
      <td>Confirmación vacía</td>
      <td>El usuario tiene al menos un contacto en el sistema.</td>
      <td>1. Abrir la aplicación. 2.El usuario selecciona la opción contacto. 3. El sistema muestra los "contactos". 4. El usuario selecciona la opción " ELIMINAR contacto". 5. en la pantalla se muestra ". 6. Seleccionar la opción de eliminar. 7. Confirmar el mensaje sin especificar un nombre de contacto.</td>
      <td>Nombre del contacto a eliminar: "ROMINA SAMANIEGO"</td>
      <td>Los datos del contacto "ROMINA SAMANIEGO" no se eliminan y permanecen sin cambios.</td>
      <td>La eliminación del contacto "Romina" es cancelada correctamente.</td>
    </tr>
    <tr>
      <td>22</td>
      <td>Confirmación de eliminación múltiple</td>
      <td>El usuario tiene varios contactos en el sistema.</td>
      <td>1. Seleccionar múltiples contactos para eliminar. 2. Confirmar cada mensaje de eliminación.</td>
      <td>Lista de contactos a eliminar: "Alice", "Bob", "Charlie"</td>
      <td>Todos los contactos seleccionados se eliminan correctamente.</td>
      <td>Todos los contactos seleccionados se eliminan correctamente.</td>
    </tr>
  </tbody>
</table>

## 📑 Hoja: plantilla de reporte de pruebas

<table>
  <thead>
    <tr>
      <th>Plantilla de reporte de pruebas</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ID</td>
      <td>Titulos</td>
      <td>Severidad</td>
      <td>Pasos</td>
      <td>Datos</td>
      <td>Resultados esperados</td>
      <td>Resultado obtenido</td>
      <td>Evidencia</td>
    </tr>
    <tr>
      <td></td>
      <td>El sist.no guarda contacto con dominio .net</td>
      <td>alta</td>
      <td>1-ingresar a la aplicacion. 2-hacer click en en la opcion "nuevo contacto". 3-completar los campos "nombre " y "mail" con datos . 4-hacer click en el boton guardar</td>
      <td>https://nahual.github.io/qc-contactos/contactos.html?v=1</td>
      <td>el sist. debe almacenar el contacto y mostrarlo en la grilla</td>
      <td>el valor ingresado no es un email</td>
      <td></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Alta de contacto con datos válidos</td>
      <td>alta</td>
      <td>1.Ingresar a la aplicación. 2.Hacer clic en la opción "Nuevo Contacto". 3. Completar los campos "Nombre" y "Mail" con datos válidos. 4. Hacer clic en el botón "Guardar".</td>
      <td>nombre:daniel</td>
      <td>el sist. debe almacenar el contacto y mostrarlo en la grilla</td>
      <td>almacena el contacto con exito</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>mail:dadani@gmail.com</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Alta de contacto con nombre vacío</td>
      <td>alta</td>
      <td>1. Hacer clic en la opción "Nuevo Contacto". 2. Completar el campo "Mail" con datos válidos. 3. Hacer clic en el botón "Guardar".</td>
      <td>nombre:vacio</td>
      <td>El sistema debe mostrar un mensaje informando que el campo "Nombre" es obligatorio.</td>
      <td>guarda contacto sin el nombre no muestra pantalla con aviso de error</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>mail:jose@gmail.com</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Alta de contacto con correo electrónico vacío</td>
      <td>alta</td>
      <td>1. Hacer clic en la opción "Nuevo Contacto". 2. Completar el campo "Nombre" con datos válidos. 3. Hacer clic en el botón "Guardar".</td>
      <td>nombre:juan</td>
      <td>El sistema debe mostrar un mensaje informando que el campo "Mail" es obligatorio.</td>
      <td>muestra en la oantalla un mensaje de error "mail obligatorio"</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>mail: vacio</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Alta de contacto con correo electrónico con formato inválido</td>
      <td>alta</td>
      <td>1. Hacer clic en la opción "Nuevo Contacto". 2. Completar el campo "Nombre" con datos válidos. 3. Hacer clic en el botón "Guardar".</td>
      <td>nombre:juan</td>
      <td>El sistema debe mostrar un mensaje informando que el valor ingresado no es un correo electrónico.</td>
      <td>muestra en la pantalla un mensaje de error "El valor ingresado no es un email"</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>mail:juan/ajaj.com</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Alta de contacto con correo electrónico duplicado</td>
      <td>alta</td>
      <td>1. Agregar un contacto con un correo electrónico determinado. 2. Hacer clic en la opción "Nuevo Contacto". 3. Completar los campos "Nombre" y "Mail" con el mismo correo electrónico que el contacto agregado anteriormente. 4. Hacer clic en el botón "Guardar".</td>
      <td>nombre:pepito</td>
      <td>El sistema debe mostrar un mensaje informando que no es posible almacenar direcciones de correo duplicadas o existentes.</td>
      <td>en la pantalla se muestra este mensaje "Ya existe un contacto con este mail"</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>mail:jose@gmail.com</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

