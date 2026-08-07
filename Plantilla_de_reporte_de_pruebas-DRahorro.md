# 📄 Plantilla de reporte de pruebas-DRahorro.xlsx

## 📑 Hoja: Hoja 1

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

