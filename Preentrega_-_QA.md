# 📄 Preentrega - QA.xlsx

## 📑 Hoja: Portada

<table>
  <thead>
    <tr>
      <th>PROYECTO: TALENTO LAB CONSULTORA</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th>StoryTelling</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>Romina es una diseñadora gráfica junior que busca su primer empleo remoto. Después de varios intentos fallidos enviando currículums por correo, descubre la plataforma Talento Lab. Romina crea una cuenta, completa su perfil profesional y carga su CV. Luego explora las ofertas laborales disponibles y encuentra una vacante que coincide con sus habilidades.</td>
    </tr>
    <tr>
      <td>PR-ID</td>
      <td>Título</td>
      <td>Descripción</td>
      <td>Fecha de inicio</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>PR-01</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td># Épicas</td>
      <td># Features</td>
      <td># Historias de usuario</td>
      <td># Conjunto de pruebas</td>
      <td># Casos de prueba</td>
      <td></td>
    </tr>
    <tr>
      <td>2</td>
      <td>4</td>
      <td>6</td>
      <td>1</td>
      <td>11</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

## 📑 Hoja: Épicas & Features

<table>
  <thead>
    <tr>
      <th>ÉPICAS</th>
      <th></th>
      <th></th>
      <th>FEATURES (Funcionalidades)</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>EP-ID (EP-#)</td>
      <td>Título</td>
      <td>Descripción</td>
      <td>FEAT-ID (FEAT-#)</td>
      <td>Título</td>
      <td>Descripción</td>
      <td>EP-ID</td>
    </tr>
    <tr>
      <td>EP-01</td>
      <td>Onboarding y Gestion de perfil de candidatos(cuentas)</td>
      <td>Permite a los usuarios registrarse, iniciar sesión y administrar su cuenta dentro de Talento Lab.</td>
      <td>FEAT-01</td>
      <td>Registro de usuario</td>
      <td>Permite crear una cuenta nueva mediante un formulario de registro.</td>
      <td>EP-01</td>
    </tr>
    <tr>
      <td>EP-02</td>
      <td>Gestion de perfil y postulacion laboral</td>
      <td>Permite completar información profesional, cargar CV y postularse a vacantes laborales.</td>
      <td>FEAT-02</td>
      <td>Inicio de sesión y validación de acceso</td>
      <td>Permite autenticar usuarios registrados y validar credenciales de acceso.</td>
      <td>EP-02</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>FEAT-03</td>
      <td>Carga y gestión de CV</td>
      <td>Permite cargar información profesional y currículum vitae.</td>
      <td>EP-03</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>FEAT-04</td>
      <td>Postulación a vacantes</td>
      <td>Permite aplicar a ofertas laborales publicadas en la plataforma.</td>
      <td>EP-04</td>
    </tr>
  </tbody>
</table>

## 📑 Hoja: TS-Conjunto de pruebas

<table>
  <thead>
    <tr>
      <th>SET DE PRUEBAS</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>TS-ID (TS-#)</td>
      <td>Título</td>
      <td>Objetivo</td>
      <td>Datos de prueba</td>
      <td></td>
    </tr>
    <tr>
      <td>TS-01</td>
      <td>Pruebas funcionales del modulo de registro de usuario</td>
      <td>Validar nombre, email, contraseña y archivo de cv</td>
      <td>Email Valido</td>
      <td>asdQ@gmail.com</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>Email invalido</td>
      <td>test-registrado@gmail.com (existe en la base de dato)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>contraseña vadilo</td>
      <td>RLJ#2923</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>contraseña invadilo</td>
      <td>111</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>CV_ valido</td>
      <td>caaguazu.pdf</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>Cv_invalido</td>
      <td>Archivo_grande.pdf (12MB)/Archivo no valido(vacaciones.jpg)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>cv-invalido</td>
      <td>campo vacio</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>cv-invalido</td>
      <td>archivo jpg</td>
    </tr>
    <tr>
      <td>Entorno de ejecución</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Ambiente</td>
      <td>QA</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>SO</td>
      <td>Windows 11 24H</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Navegadro</td>
      <td>Google Chrome v12e</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

## 📑 Hoja: US-Historias de Usuario

<table>
  <thead>
    <tr>
      <th>HISTORIAS DE USUARIO</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>US-ID (US-#)</td>
      <td>Título</td>
      <td>Descripción</td>
      <td>Criterios de aceptación</td>
    </tr>
    <tr>
      <td>US-01</td>
      <td>Registro de usuario</td>
      <td>Como candidato, quiero ingresar mi nombre completo, email, contraseña para registrarme en la plataforma.</td>
      <td>1-Los campos nombre completo, correo electrónico y contraseña deben ser obligatorios.</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>2-En el campo nombre debe contener minimo 3 caracteres</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>3- El correo electrónico debe validar el formato estándar (ejemplo@dominio.com)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>4-En el campo contraseña debe ser segura con convinaciones de numeros, letras,caracteres especiales</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>5-En el campo contraseña debe mostrar un maximo de caracteres permitidos</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>6- Al finalizar el registro correctamente, el sistema debe mostrar un mensaje de confirmación.</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>7- El registro del usuario debe completarse en menos de 2 segundos.</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>8-Al hacer click en registrar y los campos estan vacios debe mostrar un mensaje "campos obligatorios "</td>
    </tr>
    <tr>
      <td>Us-02</td>
      <td>Visualización de contraseña</td>
      <td>Como candidato, quiero visualizar mi contraseña mediante el ícono de ojo para verificar que esté escrita correctamente.</td>
      <td>1- Al hacer clic en el ícono de ojo, la contraseña debe mostrarse en texto visible</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>2-Al volver a hacer clic, la contraseña debe ocultarse nuevamente.</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>3-El cambio visual debe realizarse inmediatamente.</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>4-El ícono debe cambiar visualmente para indicar si la contraseña está visible u oculta.</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td>5-La visualización de la contraseña no debe modificar ni borrar el texto ingresado por el usuario.</td>
    </tr>
    <tr>
      <td>US-3</td>
      <td>Carga de cv</td>
      <td>Como candidato, quiero adjuntar mi CV desde mi computadora para completar mi perfil laboral.</td>
      <td>1-El sistema debe permitir cargar archivos PDF y DOCX.<br>2-El tamaño máximo permitido debe ser de 5 MB.<br>3-El archivo debe cargarse correctamente sin generar errores.<br>4-El sistema debe mostrar confirmación de carga exitosa. 5-Si el archivo supera el tamaño permitido, el sistema debe mostrar un mensaje de error.<br>6-Si el formato del archivo no es válido, el sistema debe impedir la carga y notificar al usuario.</td>
    </tr>
    <tr>
      <td>US-4</td>
      <td>Inicio de sesión</td>
      <td>Como usuario, quiero iniciar sesión con mi correo electrónico y contraseña para acceder a mi perfil y funcionalidades de la plataforma.</td>
      <td>1- El sistema debe permitir ingresar con credenciales válidas.<br>2-El correo electrónico debe validar el formato correcto antes de iniciar sesión.<br>3-Si las credenciales son incorrectas, el sistema debe mostrar un mensaje de error.<br>4-El inicio de sesión debe completarse en menos de 2 segundos.<br>5-Después de iniciar sesión correctamente, el usuario debe ser redirigido al panel principal. 6-El campo de contraseña debe ocultar los caracteres ingresados.<br>7-El sistema no debe permitir el acceso si algún campo está vacío.</td>
    </tr>
    <tr>
      <td>US-5</td>
      <td>Postulación a vacante</td>
      <td>Como candidato, quiero postularme a una vacante laboral para participar en procesos de selección.</td>
      <td>1-El usuario debe haber iniciado sesión para postularse a una vacante.<br>2-El sistema debe permitir seleccionar una oferta laboral disponible.<br>3-Al hacer clic en “Postularme”, la solicitud debe enviarse correctamente.<br>4-La postulación debe registrarse en la base de datos sin errores. 5-El sistema debe permitir que únicamente los usuarios autenticados puedan postularse a una vacante laboral.<br>6-El sistema debe mostrar al candidato las vacantes disponibles para postulación.<br>7-Cuando el candidato seleccione una vacante y haga clic en el botón “Postularme”, el sistema debe registrar correctamente la postulación.<br>8-El sistema debe mostrar un mensaje de confirmación indicando que la postulación fue realizada exitosamente.<br>9-El sistema debe almacenar la información de la postulación en la base de datos sin errores ni duplicados.<br>10-El candidato no debe poder postularse más de una vez a la misma vacante.<br>11-El sistema debe asociar la postulación al perfil del candidato autenticado.<br>12-Si ocurre un error durante la postulación, el sistema debe mostrar un mensaje indicando que la operación no pudo completarse.<br>13-El candidato debe poder visualizar el estado de su postulación después de registrarse.</td>
    </tr>
    <tr>
      <td>US-6</td>
      <td>Formulario de contacto</td>
      <td>Como usuario, quiero enviar consultas mediante el formulario de contacto para comunicarme con el equipo de soporte.</td>
      <td>1-Todos los campos obligatorios deben validarse antes del envío.<br>2-El correo electrónico debe tener un formato válido.<br>3-El sistema debe enviar correctamente el formulario al completar los datos.<br>4-Después del envío exitoso, debe mostrarse un mensaje de confirmación.<br>5-Si ocurre un error, el sistema debe mostrar un mensaje informativo al usuario indicando que la solicitud no pudo procesarse. <br>6-El sistema no debe permitir el envío del formulario con campos vacíos obligatorios.<br>7-El usuario debe poder ingresar mensajes dentro del límite de caracteres permitido por el sistema.<br>8-El sistema debe proteger el formulario contra el envío de datos inválidos o caracteres no permitidos.</td>
    </tr>
  </tbody>
</table>

## 📑 Hoja: TC-Casos de Prueba

<table>
  <thead>
    <tr>
      <th>CASOS DE PRUEBA</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Detalles</td>
      <td></td>
      <td>Referencia</td>
      <td></td>
      <td>Datos de Prueba</td>
      <td></td>
    </tr>
    <tr>
      <td>Autor:</td>
      <td>Romina</td>
      <td>(Juan Perez)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Revisor:</td>
      <td>Daniel</td>
      <td>(María Lopez)</td>
      <td></td>
      <td>Campo</td>
      <td>Nombre</td>
    </tr>
    <tr>
      <td>Prioridad:</td>
      <td>Alta</td>
      <td>(Alta, Media, Baja)</td>
      <td></td>
      <td>Nombre</td>
      <td>Romina</td>
    </tr>
    <tr>
      <td>Tipo de Test:</td>
      <td>test manual</td>
      <td>(Funcional, No funcional...)</td>
      <td></td>
      <td>Email Valido</td>
      <td>asdQ@gmail.com</td>
    </tr>
    <tr>
      <td>Fecha:</td>
      <td>2026-03-12 00:00:00</td>
      <td></td>
      <td></td>
      <td>contraseña vadilo</td>
      <td>RLJ#2923</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>CV_ valido</td>
      <td>formato pdf</td>
    </tr>
    <tr>
      <td>ID</td>
      <td>Título</td>
      <td>Precondiciones</td>
      <td>Pasos</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>TC-01</td>
      <td>Registro exitoso con datos válidos</td>
      <td>1-Estar en la pantalla de registro</td>
      <td>1-Abrir la pagina de registro</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>2-El usuario no debe estar registrado</td>
      <td>1. Ingresar nombre válido "Romina"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>3-Existe conexión a Internet.</td>
      <td>2. Ingresar email válido "asdQ@gmail.com"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>4-La pagina debe funcionar correctamente.</td>
      <td>3. Ingresar contraseña válida "RLJ#2923"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>5-El usuario no está autenticado.</td>
      <td>4. Cargar CV " formato pdf"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>6-el Cv debe estar descargado</td>
      <td>4. Click en “Registrarse”</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Resultado Esperado</td>
      <td>Resultado Obtenido</td>
      <td>Evidencias</td>
      <td>Estado (Pasó/Falló/ Bloqueado)</td>
      <td>Comentarios</td>
      <td></td>
    </tr>
    <tr>
      <td>El sistema debe permitir el registro y guardar datos en la base de dato</td>
      <td>acepta el registro</td>
      <td></td>
      <td>Pasó</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Detalles</td>
      <td></td>
      <td>Referencia</td>
      <td></td>
      <td>Datos de Prueba</td>
      <td></td>
    </tr>
    <tr>
      <td>Autor:</td>
      <td>Romina</td>
      <td>(Juan Perez)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Revisor:</td>
      <td>Daniel</td>
      <td>(María Lopez)</td>
      <td></td>
      <td>Campo</td>
      <td>Nombre</td>
    </tr>
    <tr>
      <td>Prioridad:</td>
      <td>Alta</td>
      <td>(Alta, Media, Baja)</td>
      <td></td>
      <td>Nombre</td>
      <td>ad</td>
    </tr>
    <tr>
      <td>Tipo de Test:</td>
      <td></td>
      <td>(Funcional, No funcional...)</td>
      <td></td>
      <td>Email Válido</td>
      <td>asdQ@gmail.com</td>
    </tr>
    <tr>
      <td>Fecha:</td>
      <td>2026-03-12 00:00:00</td>
      <td></td>
      <td></td>
      <td>contraseña vadilo</td>
      <td>RLJ#2923</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>CV_ válido</td>
      <td>formato pdf</td>
    </tr>
    <tr>
      <td>ID</td>
      <td>Título</td>
      <td>Precondiciones</td>
      <td>Pasos</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>TC-02</td>
      <td>Registro de usuario (NOMBRE )invalido</td>
      <td>1-Estar en la pantalla de registro</td>
      <td>1-Abrir la página de registro</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>2-El usuario no debe estar registrado</td>
      <td>1. Ingresar nombre válido "ad"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>3-Existe conexión a Internet.</td>
      <td>2. Ingresar email válido "asdQ@gmail.com"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>4-La pagina debe funcionar correctamente.</td>
      <td>3. Ingresar contraseña válida "RLJ#2923"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>5-El usuario no está autenticado.</td>
      <td>4. Cargar CV "formato pdf"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>6-el cv debe estar descargado</td>
      <td>4. Click en “Registrarse”</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Resultado Esperado</td>
      <td>Resultado Obtenido</td>
      <td>Evidencias</td>
      <td>Estado (Pasó/Falló/ Bloqueado)</td>
      <td>Comentarios</td>
      <td></td>
    </tr>
    <tr>
      <td>El sistema debe impedir el registro y mostrar un mensaje de error.</td>
      <td>acepta el registro</td>
      <td></td>
      <td>Falló</td>
      <td>El sistema debe mostrar un mensaje de error indicando que el nombre ingresado no es válido y no debe permitir que el usuario continúe con el proceso de registro hasta ingresar un nombre válido.</td>
      <td></td>
    </tr>
    <tr>
      <td>Detalles</td>
      <td></td>
      <td>Referencia</td>
      <td></td>
      <td>Datos de Prueba</td>
      <td></td>
    </tr>
    <tr>
      <td>Autor:</td>
      <td>Romina</td>
      <td>(Juan Perez)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Revisor:</td>
      <td>Daniel</td>
      <td>(María Lopez)</td>
      <td></td>
      <td>Campo</td>
      <td>Nombre</td>
    </tr>
    <tr>
      <td>Prioridad:</td>
      <td>Alta</td>
      <td>(Alta, Media, Baja)</td>
      <td></td>
      <td>Nombre</td>
      <td>Romina</td>
    </tr>
    <tr>
      <td>Tipo de Test:</td>
      <td></td>
      <td>(Funcional, No funcional...)</td>
      <td></td>
      <td>Email válido</td>
      <td>asdQ@gmail.com</td>
    </tr>
    <tr>
      <td>Fecha:</td>
      <td>2026-03-12 00:00:00</td>
      <td></td>
      <td></td>
      <td>contraseña válido</td>
      <td>RLJ#2923</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>CV_ válido</td>
      <td>formato pdf</td>
    </tr>
    <tr>
      <td>ID</td>
      <td>Título</td>
      <td>Precondiciones</td>
      <td>Pasos</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>TC-03</td>
      <td>Registro de usuario (CORREO ELECTRONICO) valido</td>
      <td>1-Estar en la pantalla de registro</td>
      <td>1-Abrir la pagina de registro</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>2-El usuario no debe estar registrado</td>
      <td>1. Ingresar nombre válido "Romina"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>3-Existe conexión a Internet.</td>
      <td>2. Ingresar email válido "asdQ@gmail.com"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>4-La pagina debe funcionar correctamente.</td>
      <td>3. Ingresar contraseña válida "RLJ#2923"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>5-El usuario no está autenticado.</td>
      <td>4. Cargar CV "formato.pdf"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>6-el cv debe estar descargado</td>
      <td>4. Click en “Registrarse”</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Resultado Esperado</td>
      <td>Resultado Obtenido</td>
      <td>Evidencias</td>
      <td>Estado (Pasó/Falló/ Bloqueado)</td>
      <td>Comentarios</td>
      <td></td>
    </tr>
    <tr>
      <td>El sistema debe permitir el registro y guardar datos en la base de dato</td>
      <td>acepta el registro</td>
      <td></td>
      <td>Pasó</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Detalles</td>
      <td></td>
      <td>Referencia</td>
      <td></td>
      <td>Datos de Prueba</td>
      <td></td>
    </tr>
    <tr>
      <td>Autor:</td>
      <td>Romina</td>
      <td>(Juan Perez)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Revisor:</td>
      <td>Daniel</td>
      <td>(María Lopez)</td>
      <td></td>
      <td>Campo</td>
      <td>Nombre</td>
    </tr>
    <tr>
      <td>Prioridad:</td>
      <td>Alta</td>
      <td>(Alta, Media, Baja)</td>
      <td></td>
      <td>Nombre</td>
      <td>Romina</td>
    </tr>
    <tr>
      <td>Tipo de Test:</td>
      <td></td>
      <td>(Funcional, No funcional...)</td>
      <td></td>
      <td>Email inválido</td>
      <td>asdQgmail.com</td>
    </tr>
    <tr>
      <td>Fecha:</td>
      <td>2026-03-12 00:00:00</td>
      <td></td>
      <td></td>
      <td>contraseña válido</td>
      <td>RLJ#2923</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>CV_ válido</td>
      <td>formato pdf</td>
    </tr>
    <tr>
      <td>ID</td>
      <td>Título</td>
      <td>Precondiciones</td>
      <td>Pasos</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>TC-04</td>
      <td>Registro de usuario (CORREO ELECTRONICO) invalido</td>
      <td>1-Estar en la pantalla de registro</td>
      <td>1-Abrir la pagina de registro</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>2-El usuario no debe estar registrado</td>
      <td>2. Ingresar nombre válido "Romina"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>3-Existe conexión a Internet.</td>
      <td>3. Ingresar email inválido "asdQgmail.com"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>4-La página debe funcionar correctamente.</td>
      <td>4. Ingresar contraseña válida "RLJ#2923"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>5-El usuario no está autenticado.</td>
      <td>5. Cargar CV "formato.pdf"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>6-el cv debe estar descargado</td>
      <td>6. Click en “Registrarse”</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Resultado Esperado</td>
      <td>Resultado Obtenido</td>
      <td>Evidencias</td>
      <td>Estado (Pasó/Falló/ Bloqueado)</td>
      <td>Comentarios</td>
      <td></td>
    </tr>
    <tr>
      <td>El sistema debe impedir el registro y mostrar un mensaje de error.</td>
      <td>acepta el registro</td>
      <td></td>
      <td>Falló</td>
      <td>El sistema debe mostrar el mensaje: "El correo electrónico ingresado no es válido. Verifique el formato e intente nuevamente." Además, no debe permitir que el usuario continúe con el registro hasta corregir el correo electrónico.</td>
      <td></td>
    </tr>
    <tr>
      <td>Detalles</td>
      <td></td>
      <td>Referencia</td>
      <td></td>
      <td>Datos de Prueba</td>
      <td></td>
    </tr>
    <tr>
      <td>Autor:</td>
      <td>Romina</td>
      <td>(Juan Perez)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Revisor:</td>
      <td>Daniel</td>
      <td>(María Lopez)</td>
      <td></td>
      <td>Campo</td>
      <td>Nombre</td>
    </tr>
    <tr>
      <td>Prioridad:</td>
      <td>Alta</td>
      <td>(Alta, Media, Baja)</td>
      <td></td>
      <td>Nombre</td>
      <td>Romina</td>
    </tr>
    <tr>
      <td>Tipo de Test:</td>
      <td></td>
      <td>(Funcional, No funcional...)</td>
      <td></td>
      <td>Email Válido</td>
      <td>asdQ@gmail.com</td>
    </tr>
    <tr>
      <td>Fecha:</td>
      <td>2026-03-12 00:00:00</td>
      <td></td>
      <td></td>
      <td>contraseña vádila</td>
      <td>RLJ#2923</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>CV_ válido</td>
      <td>formato pdf</td>
    </tr>
    <tr>
      <td>ID</td>
      <td>Título</td>
      <td>Precondiciones</td>
      <td>Pasos</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>TC-05</td>
      <td>Registro de usuario (CONTRASEÑA) válido</td>
      <td>1-Estar en la pantalla de registro</td>
      <td>1-Abrir la pagina de registro</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>2-El usuario no debe estar registrado</td>
      <td>2. Ingresar nombre válido "Romina"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>3-Existe conexión a Internet.</td>
      <td>3. Ingresar email válido "asdQ@gmail.com"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>4-La pagina debe funcionar correctamente.</td>
      <td>4. Ingresar contraseña válida "RLJ#2923"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>5-El usuario no está autenticado.</td>
      <td>5. Cargar CV "formato.pdf"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>6-el cv debe estar descargado</td>
      <td>6. Click en “Registrarse”</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Resultado Esperado</td>
      <td>Resultado Obtenido</td>
      <td>Evidencias</td>
      <td>Estado (Pasó/Falló/ Bloqueado)</td>
      <td>Comentarios</td>
      <td></td>
    </tr>
    <tr>
      <td>El sistema debe registrar al usuario, almacenar correctamente la información y mostrar un mensaje de confirmación de registro exitoso.</td>
      <td>acepta el registro</td>
      <td></td>
      <td>Pasó</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Detalles</td>
      <td></td>
      <td>Referencia</td>
      <td></td>
      <td>Datos de Prueba</td>
      <td></td>
    </tr>
    <tr>
      <td>Autor:</td>
      <td>Romina</td>
      <td>(Juan Perez)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Revisor:</td>
      <td>Daniel</td>
      <td>(María Lopez)</td>
      <td></td>
      <td>Campo</td>
      <td>Nombre</td>
    </tr>
    <tr>
      <td>Prioridad:</td>
      <td>Alta</td>
      <td>(Alta, Media, Baja)</td>
      <td></td>
      <td>Nombre</td>
      <td>Romina</td>
    </tr>
    <tr>
      <td>Tipo de Test:</td>
      <td></td>
      <td>(Funcional, No funcional...)</td>
      <td></td>
      <td>Email Valido</td>
      <td>asdQ@gmail.com</td>
    </tr>
    <tr>
      <td>Fecha:</td>
      <td>2026-03-12 00:00:00</td>
      <td></td>
      <td></td>
      <td>contraseña invádilo</td>
      <td>111</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>CV_ válido</td>
      <td>formato pdf</td>
    </tr>
    <tr>
      <td>ID</td>
      <td>Título</td>
      <td>Precondiciones</td>
      <td>Pasos</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>TC-06</td>
      <td>Registro de usuario (CONTRASEÑA) inválido</td>
      <td>1-Estar en la pantalla de registro</td>
      <td>1-Abrir la página de registro</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>2-El usuario no debe estar registrado</td>
      <td>1. Ingresar nombre válido "Romina"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>3-Existe conexión a Internet.</td>
      <td>3. Ingresar email válido "asdQ@gmail.com"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>4-La pagina debe funcionar correctamente.</td>
      <td>4. Ingresar contraseña inválida "111"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>5-El usuario no está autenticado.</td>
      <td>5. Cargar CV "formato.pdf"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>6-el cv debe estar descargado</td>
      <td>6. Click en “Registrarse”</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Resultado Esperado</td>
      <td>Resultado Obtenido</td>
      <td>Evidencias</td>
      <td>Estado (Pasó/Falló/ Bloqueado)</td>
      <td>Comentarios</td>
      <td></td>
    </tr>
    <tr>
      <td>El sistema debe impedir el registro y mostrar un mensaje de error.</td>
      <td>acepta el registro</td>
      <td></td>
      <td>Falló</td>
      <td>El sistema debe mostrar un mensaje de validación indicando que la contraseña es poco segura e informar al usuario que debe ingresar una contraseña con mayor longitud y al menos un carácter especial antes de continuar con el registro.</td>
      <td></td>
    </tr>
    <tr>
      <td>Detalles</td>
      <td></td>
      <td>Referencia</td>
      <td></td>
      <td>Datos de Prueba</td>
      <td></td>
    </tr>
    <tr>
      <td>Autor:</td>
      <td>Romina</td>
      <td>(Juan Perez)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Revisor:</td>
      <td>Daniel</td>
      <td>(María Lopez)</td>
      <td></td>
      <td>Campo</td>
      <td>Nombre</td>
    </tr>
    <tr>
      <td>Prioridad:</td>
      <td>Alta</td>
      <td>(Alta, Media, Baja)</td>
      <td></td>
      <td>Nombre</td>
      <td>Romina</td>
    </tr>
    <tr>
      <td>Tipo de Test:</td>
      <td></td>
      <td>(Funcional, No funcional...)</td>
      <td></td>
      <td>Email válido</td>
      <td>asdQ@gmail.com</td>
    </tr>
    <tr>
      <td>Fecha:</td>
      <td>2026-03-12 00:00:00</td>
      <td></td>
      <td></td>
      <td>contraseña válido</td>
      <td>RLJ#2923</td>
    </tr>
    <tr>
      <td>ID</td>
      <td>Título</td>
      <td>Precondiciones</td>
      <td>Pasos</td>
      <td>CV vacio</td>
      <td>vacio</td>
    </tr>
    <tr>
      <td>TC-07</td>
      <td>Validación de carga vacia de Cv</td>
      <td>1-Estar en la pantalla de registro</td>
      <td>1-Abrir la página de registro</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>2-El usuario no debe estar registrado</td>
      <td>1. Ingresar nombre válido "Romina"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>3-Existe conexión a Internet.</td>
      <td>2. Ingresar email válido "asdQ@gmail.com"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>4-La pagina debe funcionar correctamente.</td>
      <td>3. Ingresar contraseña válida "RLJ#2923"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>5-El usuario no está autenticado.</td>
      <td>4. Cargar CV "vacio"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>6-el cv debe estar descargado</td>
      <td>4. Click en “Registrarse”</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Resultado Esperado</td>
      <td>Resultado Obtenido</td>
      <td>Evidencias</td>
      <td>Estado (Pasó/Falló/ Bloqueado)</td>
      <td>Comentarios</td>
      <td></td>
    </tr>
    <tr>
      <td>El sistema debe mostrar un mensaje indicando que el campo Cv esta vacio</td>
      <td>Registra al usuario</td>
      <td></td>
      <td>Falló</td>
      <td>El sistema válida que el campo de carga de CV esté completo.</td>
      <td></td>
    </tr>
    <tr>
      <td>Detalles</td>
      <td></td>
      <td>Referencia</td>
      <td></td>
      <td>Datos de Prueba</td>
      <td></td>
    </tr>
    <tr>
      <td>Autor:</td>
      <td>Romina</td>
      <td>(Juan Perez)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Revisor:</td>
      <td>Daniel</td>
      <td>(María Lopez)</td>
      <td></td>
      <td>Campo</td>
      <td>Nombre</td>
    </tr>
    <tr>
      <td>Prioridad:</td>
      <td>Alta</td>
      <td>(Alta, Media, Baja)</td>
      <td></td>
      <td>Nombre</td>
      <td>Romina</td>
    </tr>
    <tr>
      <td>Tipo de Test:</td>
      <td></td>
      <td>(Funcional, No funcional...)</td>
      <td></td>
      <td>Email válido</td>
      <td>asdQ@gmail.com</td>
    </tr>
    <tr>
      <td>Fecha:</td>
      <td>2026-03-12 00:00:00</td>
      <td></td>
      <td></td>
      <td>contraseña válido</td>
      <td>RLJ#2923</td>
    </tr>
    <tr>
      <td>ID</td>
      <td>Título</td>
      <td>Precondiciones</td>
      <td>Pasos</td>
      <td>CV formato pfd</td>
      <td>formato png</td>
    </tr>
    <tr>
      <td>TC-08</td>
      <td>Validación de carga de Cv con formato png</td>
      <td>1-Estar en la pantalla de registro</td>
      <td>1-Abrir la página de registro</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>2-El usuario no debe estar registrado</td>
      <td>1. Ingresar nombre válido "Romina"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>3-Existe conexión a Internet.</td>
      <td>2. Ingresar email válido "asdQ@gmail.com"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>4-La pagina debe funcionar correctamente.</td>
      <td>3. Ingresar contraseña válida "RLJ#2923"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>5-El usuario no está autenticado.</td>
      <td>4. Cargar CV "formato png"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>6-el cv debe estar descargado</td>
      <td>4. Click en “Registrarse”</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Resultado Esperado</td>
      <td>Resultado Obtenido</td>
      <td>Evidencias</td>
      <td>Estado (Pasó/Falló/ Bloqueado)</td>
      <td>Comentarios</td>
      <td></td>
    </tr>
    <tr>
      <td>El sistema no debe permitir el registro del usuario, ya que el archivo adjunto no cumple con el formato PDF requerido.</td>
      <td>Registra al usuario con Cv con formato png no correspondiente</td>
      <td></td>
      <td>Falló</td>
      <td>El sistema debe mostrar un mensaje indicando que el archivo seleccionado no cumple con el formato PDF requerido e impedir que el usuario continúe con el proceso de registro hasta cargar un archivo válido.</td>
      <td></td>
    </tr>
    <tr>
      <td>Detalles</td>
      <td></td>
      <td>Referencia</td>
      <td></td>
      <td>Datos de Prueba</td>
      <td></td>
    </tr>
    <tr>
      <td>Autor:</td>
      <td>Romina</td>
      <td>(Juan Perez)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Revisor:</td>
      <td>Daniel</td>
      <td>(María Lopez)</td>
      <td></td>
      <td>Campo</td>
      <td>Nombre</td>
    </tr>
    <tr>
      <td>Prioridad:</td>
      <td>Alta</td>
      <td>(Alta, Media, Baja)</td>
      <td></td>
      <td>Nombre</td>
      <td>vacio</td>
    </tr>
    <tr>
      <td>Tipo de Test:</td>
      <td>manual</td>
      <td>(Funcional, No funcional...)</td>
      <td></td>
      <td>Email válido</td>
      <td>vacio</td>
    </tr>
    <tr>
      <td>Fecha:</td>
      <td>2026-03-12 00:00:00</td>
      <td></td>
      <td></td>
      <td>contraseña válido</td>
      <td>vacio</td>
    </tr>
    <tr>
      <td>ID</td>
      <td>Título</td>
      <td>Precondiciones</td>
      <td>Pasos</td>
      <td>CV formato pfd</td>
      <td>vacio</td>
    </tr>
    <tr>
      <td>TC-09</td>
      <td>Validar que todos los campos sean obligatorios</td>
      <td>1-Estar en la pantalla de registro</td>
      <td>1-Abrir la página de registro</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>2-El usuario no debe estar registrado</td>
      <td>1. Ingresar nombre "vacio"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>3-Existe conexión a Internet.</td>
      <td>2. Ingresar email "vacio"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>4-La pagina debe funcionar correctamente.</td>
      <td>3. Dejar campo contraseña vacia</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>5-El usuario no está autenticado.</td>
      <td>4. Dejar campo CV "vacio"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>6-el cv debe estar descargado</td>
      <td>4. Click en “Registrarse”</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Resultado Esperado</td>
      <td>Resultado Obtenido</td>
      <td>Evidencias</td>
      <td>Estado (Pasó/Falló/ Bloqueado)</td>
      <td>Comentarios</td>
      <td></td>
    </tr>
    <tr>
      <td>el sistema muestra el mensaje y no permite le registro</td>
      <td>El sistema muestra el mensaje "Campos obligatorios" y no permite el registro.</td>
      <td></td>
      <td>Pasó</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Detalles</td>
      <td></td>
      <td>Referencia</td>
      <td></td>
      <td>Datos de Prueba</td>
      <td></td>
    </tr>
    <tr>
      <td>Autor:</td>
      <td>Romina</td>
      <td>(Juan Perez)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Revisor:</td>
      <td>Daniel</td>
      <td>(María Lopez)</td>
      <td></td>
      <td>Campo</td>
      <td>Nombre</td>
    </tr>
    <tr>
      <td>Prioridad:</td>
      <td>Alta</td>
      <td>(Alta, Media, Baja)</td>
      <td></td>
      <td>Nombre</td>
      <td>Romina</td>
    </tr>
    <tr>
      <td>Tipo de Test:</td>
      <td>manual</td>
      <td>(Funcional, No funcional...)</td>
      <td></td>
      <td>Email válido</td>
      <td>asdQ@gmail.com</td>
    </tr>
    <tr>
      <td>Fecha:</td>
      <td>2026-03-12 00:00:00</td>
      <td></td>
      <td></td>
      <td>contraseña</td>
      <td>1</td>
    </tr>
    <tr>
      <td>ID</td>
      <td>Título</td>
      <td>Precondiciones</td>
      <td>Pasos</td>
      <td>CV formato pfd</td>
      <td>formato pdf</td>
    </tr>
    <tr>
      <td>TC-10</td>
      <td>Validar longitud miníma de la contraseña</td>
      <td>1-Estar en la pantalla de registro</td>
      <td>1-Abrir la página de registro</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>2-El usuario no debe estar registrado</td>
      <td>1. Ingresar nombre válido "Romina"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>3-Existe conexión a Internet.</td>
      <td>2. Ingresar email válido "asdQ@gmail.com"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>4-La pagina debe funcionar correctamente.</td>
      <td>3. Ingresar contraseña de 1 solo caracter "1"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>5-El usuario no está autenticado.</td>
      <td>4. Cargar CV "formato pdf"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>6-el cv debe estar descargado</td>
      <td>4. Click en “Registrarse”</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Resultado Esperado</td>
      <td>Resultado Obtenido</td>
      <td>Evidencias</td>
      <td>Estado (Pasó/Falló/ Bloqueado)</td>
      <td>Comentarios</td>
      <td></td>
    </tr>
    <tr>
      <td>El sistema impide el registro, muestra un mensaje indicando que se debe ingresar 3 caracteres o mas .</td>
      <td>muestra el mensaje en pantalla diciendo que debo extender mi contraseña</td>
      <td></td>
      <td>Pasó</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Detalles</td>
      <td></td>
      <td>Referencia</td>
      <td></td>
      <td>Datos de Prueba</td>
      <td></td>
    </tr>
    <tr>
      <td>Autor:</td>
      <td>Romina</td>
      <td>(Juan Perez)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Revisor:</td>
      <td>Daniel</td>
      <td>(María Lopez)</td>
      <td></td>
      <td>Campo</td>
      <td>Nombre</td>
    </tr>
    <tr>
      <td>Prioridad:</td>
      <td>Alta</td>
      <td>(Alta, Media, Baja)</td>
      <td></td>
      <td>Nombre</td>
      <td>Romina</td>
    </tr>
    <tr>
      <td>Tipo de Test:</td>
      <td>manual</td>
      <td>(Funcional, No funcional...)</td>
      <td></td>
      <td>Email válido</td>
      <td>asdQ@gmail.com</td>
    </tr>
    <tr>
      <td>Fecha:</td>
      <td>2026-03-12 00:00:00</td>
      <td></td>
      <td></td>
      <td>contraseña</td>
      <td>RLJ#2923</td>
    </tr>
    <tr>
      <td>ID</td>
      <td>Título</td>
      <td>Precondiciones</td>
      <td>Pasos</td>
      <td>Cv formato pfd</td>
      <td>formato pdf</td>
    </tr>
    <tr>
      <td>TC-11</td>
      <td>El registro del usuario debe completarse en menos de 2 segundos.</td>
      <td>1-Estar en la pantalla de registro</td>
      <td>1-Abrir la página de registro</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>2-El usuario no debe estar registrado</td>
      <td>1. Ingresar nombre válido "Romina"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>3-Existe conexión a Internet.</td>
      <td>2. Ingresar email válido "asdQ@gmail.com"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>4-La pagina debe funcionar correctamente.</td>
      <td>3. Ingresar contraseña válida "RLJ#2923"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>5-El usuario no está autenticado.</td>
      <td>4. Cargar Cv "formato pdf"</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>6-el cv debe estar descargado</td>
      <td>4. Click en “Registrarse”</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Resultado Esperado</td>
      <td>Resultado Obtenido</td>
      <td>Evidencias</td>
      <td>Estado (Pasó/Falló/ Bloqueado)</td>
      <td>Comentarios</td>
      <td></td>
    </tr>
    <tr>
      <td>El registro del usuario debe completarse en menos de 2 segundos.</td>
      <td>el sistema tarda en registrar al usuario mas de 10 seg</td>
      <td></td>
      <td>Falló</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

## 📑 Hoja: RB- Reporte de Bugs

<table>
  <thead>
    <tr>
      <th>Reporte de Bugs</th>
      <th></th>
      <th></th>
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
      <td>N° identificador</td>
      <td>Tipo</td>
      <td>Título</td>
      <td>Descripción</td>
      <td>Severidad</td>
      <td>Prioridad</td>
      <td>Pasos para reproducir</td>
      <td>Resultado esperado</td>
      <td>Resultado obtenido</td>
      <td>Evidencia</td>
    </tr>
    <tr>
      <td>TC-02</td>
      <td>Defecto</td>
      <td>Registro de usuario (NOMBRE )invalido</td>
      <td>Permite registrar nombres con menos de 3 caracteres.</td>
      <td>Alta</td>
      <td>Alta</td>
      <td>1.ingresar a la pagina de talento lab 2. Ingresar nombre inválido "ad" 3. Ingresar email válido "asdQ@gmail.com 4. Ingresar contraseña válida "RLJ#2923" 5. Cargar Cv formato pdf 6.Hacer click en registarme</td>
      <td>El sistema debe validar que el nombre ingresado tenga como mínimo 3 caracteres y debe mostrar un mensaje de validación si no cumple con este requisito. El usuario no debe poder completar el registro hasta ingresar un nombre válido.</td>
      <td>El sistema permite ingresar y registrar un nombre con menos de 3 caracteres sin mostrar ningún mensaje de validación.</td>
      <td>https://drive.google.com/drive/folders/1yQhHp46vUhOffQZpxIqvK4wGlzvcyOl_?usp=sharing</td>
    </tr>
    <tr>
      <td>TC-04</td>
      <td>Defecto</td>
      <td>Registro de usuario (CORREO ELECTRONICO) invalido</td>
      <td>El sistema permite hacer registro con correo invalido sin el "@"</td>
      <td>Alta</td>
      <td>Alta</td>
      <td>1.ingresar a la pagina de talento lab 2. Ingresar nombre inválido "Romina" 3. Ingresar email inválido "asdQgmail.com" 4. Ingresar contraseña válida "RLJ#2923" 5. Cargar Cv formato pdf 6.Hacer click en registarme</td>
      <td>El sistema debe validar que el correo electrónico tenga un formato válido, incluyendo el carácter "@", y debe mostrar un mensaje de error cuando el formato sea incorrecto. El usuario no debe poder completar el registro con un correo inválido.</td>
      <td>El sistema permite ingresar un correo electrónico sin el carácter "@" y continuar con el proceso de registro sin mostrar un mensaje de validación.</td>
      <td></td>
    </tr>
    <tr>
      <td>TC-06</td>
      <td>Defecto</td>
      <td>Registro de usuario (CONTRASEÑA) invalido</td>
      <td>Permite contraseñas inseguras.</td>
      <td>Alta</td>
      <td>Alta</td>
      <td>1.ingresar a la pagina de talento lab 2. Ingresar nombre inválido "Romina" 3. Ingresar email inválido "asdQ@gmail.com" 4. Ingresar contraseña inválida "111" 5. Cargar Cv formato pdf 6.Hacer click en registarme</td>
      <td>El sistema debe validar que la contraseña cumpla con los requisitos mínimos de seguridad establecidos y debe impedir el registro cuando la contraseña no cumpla con dichos requisitos.</td>
      <td>El sistema permite registrar al usuario utilizando una contraseña de solo 3 caracteres (111), sin mostrar ningún mensaje de validación ni advertencia sobre la seguridad de la contraseña.</td>
      <td></td>
    </tr>
    <tr>
      <td>TC-08</td>
      <td>Defecto</td>
      <td>Validacion de carga de Cv con formato png</td>
      <td>El sistema permite completar el registro utilizando un archivo con un formato diferente a PDF, incumpliendo el criterio de aceptación que establece que el CV debe cargarse únicamente en formato PDF.</td>
      <td>Alta</td>
      <td>Alta</td>
      <td>1.ingresar a la pagina de talento lab 2. Ingresar nombre válido "Romina" 3. Ingresar email válido "asdQ@gmail.com 4. Ingresar contraseña válida "RLJ#2923" 5. dejar campo Cv formato png 6.Hacer click en registarme</td>
      <td>El sistema debe permitir cargar únicamente archivos en formato PDF, de acuerdo con el criterio establecido para la postulación. Si el usuario intenta cargar un archivo con un formato diferente, el sistema debe rechazarlo y mostrar un mensaje indicando que el formato no es válido.</td>
      <td>El sistema permite cargar y completar el registro utilizando un archivo en formato PNG, aunque el criterio establecido indica que el CV debe cargarse únicamente en formato PDF.</td>
      <td></td>
    </tr>
    <tr>
      <td>TC-07</td>
      <td>Defecto</td>
      <td>Validación de carga vacia de Cv</td>
      <td>El sistema permite completar el registro utilizando un archivo vacio, incumpliendo el criterio de aceptación que establece que el CV debe cargarse, ya que es un requisito fundamental para la postulacion de vacantes que proporciona Talento Lab.</td>
      <td>Alta</td>
      <td>Alta</td>
      <td>1.ingresar a la pagina de talento lab 2. Ingresar nombre válido "Romina" 3. Ingresar email válido "asdQ@gmail.com 4. Ingresar contraseña válida "RLJ#2923" 5. dejar campo Cv "vacio" 6.Hacer click en registarme</td>
      <td>El sistema debe validar que el usuario haya cargado un archivo de CV antes de completar el registro. Si el campo se encuentra vacío, debe impedir el registro y mostrar un mensaje indicando que el CV es obligatorio.</td>
      <td>El sistema permite completar el registro sin cargar ningún archivo de CV, aunque este campo es obligatorio para completar la postulación.</td>
      <td></td>
    </tr>
  </tbody>
</table>

