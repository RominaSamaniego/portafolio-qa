# 📄 Documento: Preentrega - QA.xlsx

## 📑 Hoja: Portada

| PROYECTO: TALENTO LAB CONSULTORA | Unnamed: 1 | Unnamed: 2 | Unnamed: 3 | Unnamed: 4 | StoryTelling |
|---|---|---|---|---|---|
|  |  |  |  |  | Romina es una diseñadora gráfica junior que busca su primer empleo remoto. Después de varios intentos fallidos enviando currículums por correo, descubre la plataforma Talento Lab. Romina crea una cuenta, completa su perfil profesional y carga su CV. Luego explora las ofertas laborales disponibles y encuentra una vacante que coincide con sus habilidades. |
| PR-ID | Título | Descripción | Fecha de inicio |  |  |
| PR-01 |  |  |  |  |  |
| # Épicas | # Features | # Historias de usuario | # Conjunto de pruebas | # Casos de prueba |  |
| 2 | 4 | 6 | 1 | 11 |  |
|  |  |  |  |  |  |

## 📑 Hoja: Épicas & Features

| ÉPICAS | Unnamed: 1 | Unnamed: 2 | FEATURES (Funcionalidades) | Unnamed: 5 | Unnamed: 6 | Unnamed: 7 |
|---|---|---|---|---|---|---|
| EP-ID (EP-#) | Título | Descripción | FEAT-ID (FEAT-#) | Título | Descripción | EP-ID |
| EP-01 | Onboarding y Gestion de perfil de candidatos(cuentas) | Permite a los usuarios registrarse, iniciar sesión y administrar su cuenta dentro de Talento Lab. | FEAT-01 | Registro de usuario | Permite crear una cuenta nueva mediante un formulario de registro. | EP-01 |
| EP-02 | Gestion de perfil y postulacion laboral | Permite completar información profesional, cargar CV y postularse a vacantes laborales. | FEAT-02 | Inicio de sesión y validación de acceso | Permite autenticar usuarios registrados y validar credenciales de acceso. | EP-02 |
|  |  |  | FEAT-03 | Carga y gestión de CV | Permite cargar información profesional y currículum vitae. | EP-03 |
|  |  |  | FEAT-04 | Postulación a vacantes | Permite aplicar a ofertas laborales publicadas en la plataforma. | EP-04 |

## 📑 Hoja: TS-Conjunto de pruebas

| SET DE PRUEBAS | Unnamed: 1 | Unnamed: 2 | Unnamed: 4 | Unnamed: 5 |
|---|---|---|---|---|
| TS-ID (TS-#) | Título | Objetivo | Datos de prueba |  |
| TS-01 | Pruebas funcionales del modulo de registro de usuario | Validar nombre, email, contraseña y archivo de cv | Email Valido | asdQ@gmail.com |
|  |  |  | Email invalido | test-registrado@gmail.com (existe en la base de dato) |
|  |  |  | contraseña vadilo | RLJ#2923 |
|  |  |  | contraseña invadilo | 111 |
|  |  |  | CV_ valido | caaguazu.pdf |
|  |  |  | Cv_invalido | Archivo_grande.pdf (12MB)/Archivo no valido(vacaciones.jpg) |
|  |  |  | cv-invalido | campo vacio |
|  |  |  | cv-invalido | archivo jpg |
| Entorno de ejecución |  |  |  |  |
| Ambiente | QA |  |  |  |
| SO | Windows 11 24H |  |  |  |
| Navegadro | Google Chrome v12e |  |  |  |

## 📑 Hoja: US-Historias de Usuario

| HISTORIAS DE USUARIO | Unnamed: 1 | Unnamed: 2 | Unnamed: 3 |
|---|---|---|---|
| US-ID (US-#) | Título | Descripción | Criterios de aceptación |
| US-01 | Registro de usuario | Como candidato, quiero ingresar mi nombre completo, email, contraseña para registrarme en la plataforma. | 1-Los campos nombre completo, correo electrónico y contraseña deben ser obligatorios. |
|  |  |  | 2-En el campo nombre debe contener minimo 3 caracteres |
|  |  |  | 3- El correo electrónico debe validar el formato estándar (ejemplo@dominio.com) |
|  |  |  | 4-En el campo contraseña debe ser segura con convinaciones de numeros, letras,caracteres especiales |
|  |  |  | 5-En el campo contraseña debe mostrar un maximo de caracteres permitidos |
|  |  |  | 6- Al finalizar el registro correctamente, el sistema debe mostrar un mensaje de confirmación. |
|  |  |  | 7- El registro del usuario debe completarse en menos de 2 segundos. |
|  |  |  | 8-Al hacer click en registrar y los campos estan vacios debe mostrar un mensaje "campos obligatorios " |
| Us-02 | Visualización de contraseña | Como candidato, quiero visualizar mi contraseña mediante el ícono de ojo para verificar que esté escrita correctamente. | 1- Al hacer clic en el ícono de ojo, la contraseña debe mostrarse en texto visible |
|  |  |  | 2-Al volver a hacer clic, la contraseña debe ocultarse nuevamente. |
|  |  |  | 3-El cambio visual debe realizarse inmediatamente. |
|  |  |  | 4-El ícono debe cambiar visualmente para indicar si la contraseña está visible u oculta. |
|  |  |  | 5-La visualización de la contraseña no debe modificar ni borrar el texto ingresado por el usuario. |
| US-3 | Carga de cv | Como candidato, quiero adjuntar mi CV desde mi computadora para completar mi perfil laboral. | 1-El sistema debe permitir cargar archivos PDF y DOCX.<br>2-El tamaño máximo permitido debe ser de 5 MB.<br>3-El archivo debe cargarse correctamente sin generar errores.<br>4-El sistema debe mostrar confirmación de carga exitosa. 5-Si el archivo supera el tamaño permitido, el sistema debe mostrar un mensaje de error.<br>6-Si el formato del archivo no es válido, el sistema debe impedir la carga y notificar al usuario. |
| US-4 | Inicio de sesión | Como usuario, quiero iniciar sesión con mi correo electrónico y contraseña para acceder a mi perfil y funcionalidades de la plataforma. | 1- El sistema debe permitir ingresar con credenciales válidas.<br>2-El correo electrónico debe validar el formato correcto antes de iniciar sesión.<br>3-Si las credenciales son incorrectas, el sistema debe mostrar un mensaje de error.<br>4-El inicio de sesión debe completarse en menos de 2 segundos.<br>5-Después de iniciar sesión correctamente, el usuario debe ser redirigido al panel principal. 6-El campo de contraseña debe ocultar los caracteres ingresados.<br>7-El sistema no debe permitir el acceso si algún campo está vacío. |
| US-5 | Postulación a vacante | Como candidato, quiero postularme a una vacante laboral para participar en procesos de selección. | 1-El usuario debe haber iniciado sesión para postularse a una vacante.<br>2-El sistema debe permitir seleccionar una oferta laboral disponible.<br>3-Al hacer clic en “Postularme”, la solicitud debe enviarse correctamente.<br>4-La postulación debe registrarse en la base de datos sin errores. 5-El sistema debe permitir que únicamente los usuarios autenticados puedan postularse a una vacante laboral.<br>6-El sistema debe mostrar al candidato las vacantes disponibles para postulación.<br>7-Cuando el candidato seleccione una vacante y haga clic en el botón “Postularme”, el sistema debe registrar correctamente la postulación.<br>8-El sistema debe mostrar un mensaje de confirmación indicando que la postulación fue realizada exitosamente.<br>9-El sistema debe almacenar la información de la postulación en la base de datos sin errores ni duplicados.<br>10-El candidato no debe poder postularse más de una vez a la misma vacante.<br>11-El sistema debe asociar la postulación al perfil del candidato autenticado.<br>12-Si ocurre un error durante la postulación, el sistema debe mostrar un mensaje indicando que la operación no pudo completarse.<br>13-El candidato debe poder visualizar el estado de su postulación después de registrarse. |
| US-6 | Formulario de contacto | Como usuario, quiero enviar consultas mediante el formulario de contacto para comunicarme con el equipo de soporte. | 1-Todos los campos obligatorios deben validarse antes del envío.<br>2-El correo electrónico debe tener un formato válido.<br>3-El sistema debe enviar correctamente el formulario al completar los datos.<br>4-Después del envío exitoso, debe mostrarse un mensaje de confirmación.<br>5-Si ocurre un error, el sistema debe mostrar un mensaje informativo al usuario indicando que la solicitud no pudo procesarse. <br>6-El sistema no debe permitir el envío del formulario con campos vacíos obligatorios.<br>7-El usuario debe poder ingresar mensajes dentro del límite de caracteres permitido por el sistema.<br>8-El sistema debe proteger el formulario contra el envío de datos inválidos o caracteres no permitidos. |

## 📑 Hoja: TC-Casos de Prueba

| CASOS DE PRUEBA | Unnamed: 1 | Unnamed: 2 | Unnamed: 3 | Unnamed: 4 | Unnamed: 5 |
|---|---|---|---|---|---|
| Detalles |  | Referencia |  | Datos de Prueba |  |
| Autor: | Romina | (Juan Perez) |  |  |  |
| Revisor: | Daniel | (María Lopez) |  | Campo | Nombre |
| Prioridad: | Alta | (Alta, Media, Baja) |  | Nombre | Romina |
| Tipo de Test: | test manual | (Funcional, No funcional...) |  | Email Valido | asdQ@gmail.com |
| Fecha: | 2026-03-12 00:00:00 |  |  | contraseña vadilo | RLJ#2923 |
|  |  |  |  | CV_ valido | formato pdf |
| ID | Título | Precondiciones | Pasos |  |  |
| TC-01 | Registro exitoso con datos válidos | 1-Estar en la pantalla de registro | 1-Abrir la pagina de registro |  |  |
|  |  | 2-El usuario no debe estar registrado | 1. Ingresar nombre válido "Romina" |  |  |
|  |  | 3-Existe conexión a Internet. | 2. Ingresar email válido "asdQ@gmail.com" |  |  |
|  |  | 4-La pagina debe funcionar correctamente. | 3. Ingresar contraseña válida "RLJ#2923" |  |  |
|  |  | 5-El usuario no está autenticado. | 4. Cargar CV " formato pdf" |  |  |
|  |  | 6-el Cv debe estar descargado | 4. Click en “Registrarse” |  |  |
| Resultado Esperado | Resultado Obtenido | Evidencias | Estado (Pasó/Falló/ Bloqueado) | Comentarios |  |
| El sistema debe permitir el registro y guardar datos en la base de dato | acepta el registro |  | Pasó |  |  |
| Detalles |  | Referencia |  | Datos de Prueba |  |
| Autor: | Romina | (Juan Perez) |  |  |  |
| Revisor: | Daniel | (María Lopez) |  | Campo | Nombre |
| Prioridad: | Alta | (Alta, Media, Baja) |  | Nombre | ad |
| Tipo de Test: |  | (Funcional, No funcional...) |  | Email Válido | asdQ@gmail.com |
| Fecha: | 2026-03-12 00:00:00 |  |  | contraseña vadilo | RLJ#2923 |
|  |  |  |  | CV_ válido | formato pdf |
| ID | Título | Precondiciones | Pasos |  |  |
| TC-02 | Registro de usuario (NOMBRE )invalido | 1-Estar en la pantalla de registro | 1-Abrir la página de registro |  |  |
|  |  | 2-El usuario no debe estar registrado | 1. Ingresar nombre válido "ad" |  |  |
|  |  | 3-Existe conexión a Internet. | 2. Ingresar email válido "asdQ@gmail.com" |  |  |
|  |  | 4-La pagina debe funcionar correctamente. | 3. Ingresar contraseña válida "RLJ#2923" |  |  |
|  |  | 5-El usuario no está autenticado. | 4. Cargar CV "formato pdf" |  |  |
|  |  | 6-el cv debe estar descargado | 4. Click en “Registrarse” |  |  |
| Resultado Esperado | Resultado Obtenido | Evidencias | Estado (Pasó/Falló/ Bloqueado) | Comentarios |  |
| El sistema debe impedir el registro y mostrar un mensaje de error. | acepta el registro |  | Falló | El sistema debe mostrar un mensaje de error indicando que el nombre ingresado no es válido y no debe permitir que el usuario continúe con el proceso de registro hasta ingresar un nombre válido. |  |
| Detalles |  | Referencia |  | Datos de Prueba |  |
| Autor: | Romina | (Juan Perez) |  |  |  |
| Revisor: | Daniel | (María Lopez) |  | Campo | Nombre |
| Prioridad: | Alta | (Alta, Media, Baja) |  | Nombre | Romina |
| Tipo de Test: |  | (Funcional, No funcional...) |  | Email válido | asdQ@gmail.com |
| Fecha: | 2026-03-12 00:00:00 |  |  | contraseña válido | RLJ#2923 |
|  |  |  |  | CV_ válido | formato pdf |
| ID | Título | Precondiciones | Pasos |  |  |
| TC-03 | Registro de usuario (CORREO ELECTRONICO) valido | 1-Estar en la pantalla de registro | 1-Abrir la pagina de registro |  |  |
|  |  | 2-El usuario no debe estar registrado | 1. Ingresar nombre válido "Romina" |  |  |
|  |  | 3-Existe conexión a Internet. | 2. Ingresar email válido "asdQ@gmail.com" |  |  |
|  |  | 4-La pagina debe funcionar correctamente. | 3. Ingresar contraseña válida "RLJ#2923" |  |  |
|  |  | 5-El usuario no está autenticado. | 4. Cargar CV "formato.pdf" |  |  |
|  |  | 6-el cv debe estar descargado | 4. Click en “Registrarse” |  |  |
| Resultado Esperado | Resultado Obtenido | Evidencias | Estado (Pasó/Falló/ Bloqueado) | Comentarios |  |
| El sistema debe permitir el registro y guardar datos en la base de dato | acepta el registro |  | Pasó |  |  |
| Detalles |  | Referencia |  | Datos de Prueba |  |
| Autor: | Romina | (Juan Perez) |  |  |  |
| Revisor: | Daniel | (María Lopez) |  | Campo | Nombre |
| Prioridad: | Alta | (Alta, Media, Baja) |  | Nombre | Romina |
| Tipo de Test: |  | (Funcional, No funcional...) |  | Email inválido | asdQgmail.com |
| Fecha: | 2026-03-12 00:00:00 |  |  | contraseña válido | RLJ#2923 |
|  |  |  |  | CV_ válido | formato pdf |
| ID | Título | Precondiciones | Pasos |  |  |
| TC-04 | Registro de usuario (CORREO ELECTRONICO) invalido | 1-Estar en la pantalla de registro | 1-Abrir la pagina de registro |  |  |
|  |  | 2-El usuario no debe estar registrado | 2. Ingresar nombre válido "Romina" |  |  |
|  |  | 3-Existe conexión a Internet. | 3. Ingresar email inválido "asdQgmail.com" |  |  |
|  |  | 4-La página debe funcionar correctamente. | 4. Ingresar contraseña válida "RLJ#2923" |  |  |
|  |  | 5-El usuario no está autenticado. | 5. Cargar CV "formato.pdf" |  |  |
|  |  | 6-el cv debe estar descargado | 6. Click en “Registrarse” |  |  |
| Resultado Esperado | Resultado Obtenido | Evidencias | Estado (Pasó/Falló/ Bloqueado) | Comentarios |  |
| El sistema debe impedir el registro y mostrar un mensaje de error. | acepta el registro |  | Falló | El sistema debe mostrar el mensaje: "El correo electrónico ingresado no es válido. Verifique el formato e intente nuevamente." Además, no debe permitir que el usuario continúe con el registro hasta corregir el correo electrónico. |  |
| Detalles |  | Referencia |  | Datos de Prueba |  |
| Autor: | Romina | (Juan Perez) |  |  |  |
| Revisor: | Daniel | (María Lopez) |  | Campo | Nombre |
| Prioridad: | Alta | (Alta, Media, Baja) |  | Nombre | Romina |
| Tipo de Test: |  | (Funcional, No funcional...) |  | Email Válido | asdQ@gmail.com |
| Fecha: | 2026-03-12 00:00:00 |  |  | contraseña vádila | RLJ#2923 |
|  |  |  |  | CV_ válido | formato pdf |
| ID | Título | Precondiciones | Pasos |  |  |
| TC-05 | Registro de usuario (CONTRASEÑA) válido | 1-Estar en la pantalla de registro | 1-Abrir la pagina de registro |  |  |
|  |  | 2-El usuario no debe estar registrado | 2. Ingresar nombre válido "Romina" |  |  |
|  |  | 3-Existe conexión a Internet. | 3. Ingresar email válido "asdQ@gmail.com" |  |  |
|  |  | 4-La pagina debe funcionar correctamente. | 4. Ingresar contraseña válida "RLJ#2923" |  |  |
|  |  | 5-El usuario no está autenticado. | 5. Cargar CV "formato.pdf" |  |  |
|  |  | 6-el cv debe estar descargado | 6. Click en “Registrarse” |  |  |
| Resultado Esperado | Resultado Obtenido | Evidencias | Estado (Pasó/Falló/ Bloqueado) | Comentarios |  |
| El sistema debe registrar al usuario, almacenar correctamente la información y mostrar un mensaje de confirmación de registro exitoso. | acepta el registro |  | Pasó |  |  |
| Detalles |  | Referencia |  | Datos de Prueba |  |
| Autor: | Romina | (Juan Perez) |  |  |  |
| Revisor: | Daniel | (María Lopez) |  | Campo | Nombre |
| Prioridad: | Alta | (Alta, Media, Baja) |  | Nombre | Romina |
| Tipo de Test: |  | (Funcional, No funcional...) |  | Email Valido | asdQ@gmail.com |
| Fecha: | 2026-03-12 00:00:00 |  |  | contraseña invádilo | 111 |
|  |  |  |  | CV_ válido | formato pdf |
| ID | Título | Precondiciones | Pasos |  |  |
| TC-06 | Registro de usuario (CONTRASEÑA) inválido | 1-Estar en la pantalla de registro | 1-Abrir la página de registro |  |  |
|  |  | 2-El usuario no debe estar registrado | 1. Ingresar nombre válido "Romina" |  |  |
|  |  | 3-Existe conexión a Internet. | 3. Ingresar email válido "asdQ@gmail.com" |  |  |
|  |  | 4-La pagina debe funcionar correctamente. | 4. Ingresar contraseña inválida "111" |  |  |
|  |  | 5-El usuario no está autenticado. | 5. Cargar CV "formato.pdf" |  |  |
|  |  | 6-el cv debe estar descargado | 6. Click en “Registrarse” |  |  |
| Resultado Esperado | Resultado Obtenido | Evidencias | Estado (Pasó/Falló/ Bloqueado) | Comentarios |  |
| El sistema debe impedir el registro y mostrar un mensaje de error. | acepta el registro |  | Falló | El sistema debe mostrar un mensaje de validación indicando que la contraseña es poco segura e informar al usuario que debe ingresar una contraseña con mayor longitud y al menos un carácter especial antes de continuar con el registro. |  |
| Detalles |  | Referencia |  | Datos de Prueba |  |
| Autor: | Romina | (Juan Perez) |  |  |  |
| Revisor: | Daniel | (María Lopez) |  | Campo | Nombre |
| Prioridad: | Alta | (Alta, Media, Baja) |  | Nombre | Romina |
| Tipo de Test: |  | (Funcional, No funcional...) |  | Email válido | asdQ@gmail.com |
| Fecha: | 2026-03-12 00:00:00 |  |  | contraseña válido | RLJ#2923 |
| ID | Título | Precondiciones | Pasos | CV vacio | vacio |
| TC-07 | Validación de carga vacia de Cv | 1-Estar en la pantalla de registro | 1-Abrir la página de registro |  |  |
|  |  | 2-El usuario no debe estar registrado | 1. Ingresar nombre válido "Romina" |  |  |
|  |  | 3-Existe conexión a Internet. | 2. Ingresar email válido "asdQ@gmail.com" |  |  |
|  |  | 4-La pagina debe funcionar correctamente. | 3. Ingresar contraseña válida "RLJ#2923" |  |  |
|  |  | 5-El usuario no está autenticado. | 4. Cargar CV "vacio" |  |  |
|  |  | 6-el cv debe estar descargado | 4. Click en “Registrarse” |  |  |
| Resultado Esperado | Resultado Obtenido | Evidencias | Estado (Pasó/Falló/ Bloqueado) | Comentarios |  |
| El sistema debe mostrar un mensaje indicando que el campo Cv esta vacio | Registra al usuario |  | Falló | El sistema válida que el campo de carga de CV esté completo. |  |
| Detalles |  | Referencia |  | Datos de Prueba |  |
| Autor: | Romina | (Juan Perez) |  |  |  |
| Revisor: | Daniel | (María Lopez) |  | Campo | Nombre |
| Prioridad: | Alta | (Alta, Media, Baja) |  | Nombre | Romina |
| Tipo de Test: |  | (Funcional, No funcional...) |  | Email válido | asdQ@gmail.com |
| Fecha: | 2026-03-12 00:00:00 |  |  | contraseña válido | RLJ#2923 |
| ID | Título | Precondiciones | Pasos | CV formato pfd | formato png |
| TC-08 | Validación de carga de Cv con formato png | 1-Estar en la pantalla de registro | 1-Abrir la página de registro |  |  |
|  |  | 2-El usuario no debe estar registrado | 1. Ingresar nombre válido "Romina" |  |  |
|  |  | 3-Existe conexión a Internet. | 2. Ingresar email válido "asdQ@gmail.com" |  |  |
|  |  | 4-La pagina debe funcionar correctamente. | 3. Ingresar contraseña válida "RLJ#2923" |  |  |
|  |  | 5-El usuario no está autenticado. | 4. Cargar CV "formato png" |  |  |
|  |  | 6-el cv debe estar descargado | 4. Click en “Registrarse” |  |  |
| Resultado Esperado | Resultado Obtenido | Evidencias | Estado (Pasó/Falló/ Bloqueado) | Comentarios |  |
| El sistema no debe permitir el registro del usuario, ya que el archivo adjunto no cumple con el formato PDF requerido. | Registra al usuario con Cv con formato png no correspondiente |  | Falló | El sistema debe mostrar un mensaje indicando que el archivo seleccionado no cumple con el formato PDF requerido e impedir que el usuario continúe con el proceso de registro hasta cargar un archivo válido. |  |
| Detalles |  | Referencia |  | Datos de Prueba |  |
| Autor: | Romina | (Juan Perez) |  |  |  |
| Revisor: | Daniel | (María Lopez) |  | Campo | Nombre |
| Prioridad: | Alta | (Alta, Media, Baja) |  | Nombre | vacio |
| Tipo de Test: | manual | (Funcional, No funcional...) |  | Email válido | vacio |
| Fecha: | 2026-03-12 00:00:00 |  |  | contraseña válido | vacio |
| ID | Título | Precondiciones | Pasos | CV formato pfd | vacio |
| TC-09 | Validar que todos los campos sean obligatorios | 1-Estar en la pantalla de registro | 1-Abrir la página de registro |  |  |
|  |  | 2-El usuario no debe estar registrado | 1. Ingresar nombre "vacio" |  |  |
|  |  | 3-Existe conexión a Internet. | 2. Ingresar email "vacio" |  |  |
|  |  | 4-La pagina debe funcionar correctamente. | 3. Dejar campo contraseña vacia |  |  |
|  |  | 5-El usuario no está autenticado. | 4. Dejar campo CV "vacio" |  |  |
|  |  | 6-el cv debe estar descargado | 4. Click en “Registrarse” |  |  |
| Resultado Esperado | Resultado Obtenido | Evidencias | Estado (Pasó/Falló/ Bloqueado) | Comentarios |  |
| el sistema muestra el mensaje y no permite le registro | El sistema muestra el mensaje "Campos obligatorios" y no permite el registro. |  | Pasó |  |  |
| Detalles |  | Referencia |  | Datos de Prueba |  |
| Autor: | Romina | (Juan Perez) |  |  |  |
| Revisor: | Daniel | (María Lopez) |  | Campo | Nombre |
| Prioridad: | Alta | (Alta, Media, Baja) |  | Nombre | Romina |
| Tipo de Test: | manual | (Funcional, No funcional...) |  | Email válido | asdQ@gmail.com |
| Fecha: | 2026-03-12 00:00:00 |  |  | contraseña | 1 |
| ID | Título | Precondiciones | Pasos | CV formato pfd | formato pdf |
| TC-10 | Validar longitud miníma de la contraseña | 1-Estar en la pantalla de registro | 1-Abrir la página de registro |  |  |
|  |  | 2-El usuario no debe estar registrado | 1. Ingresar nombre válido "Romina" |  |  |
|  |  | 3-Existe conexión a Internet. | 2. Ingresar email válido "asdQ@gmail.com" |  |  |
|  |  | 4-La pagina debe funcionar correctamente. | 3. Ingresar contraseña de 1 solo caracter "1" |  |  |
|  |  | 5-El usuario no está autenticado. | 4. Cargar CV "formato pdf" |  |  |
|  |  | 6-el cv debe estar descargado | 4. Click en “Registrarse” |  |  |
| Resultado Esperado | Resultado Obtenido | Evidencias | Estado (Pasó/Falló/ Bloqueado) | Comentarios |  |
| El sistema impide el registro, muestra un mensaje indicando que se debe ingresar 3 caracteres o mas . | muestra el mensaje en pantalla diciendo que debo extender mi contraseña |  | Pasó |  |  |
| Detalles |  | Referencia |  | Datos de Prueba |  |
| Autor: | Romina | (Juan Perez) |  |  |  |
| Revisor: | Daniel | (María Lopez) |  | Campo | Nombre |
| Prioridad: | Alta | (Alta, Media, Baja) |  | Nombre | Romina |
| Tipo de Test: | manual | (Funcional, No funcional...) |  | Email válido | asdQ@gmail.com |
| Fecha: | 2026-03-12 00:00:00 |  |  | contraseña | RLJ#2923 |
| ID | Título | Precondiciones | Pasos | Cv formato pfd | formato pdf |
| TC-11 | El registro del usuario debe completarse en menos de 2 segundos. | 1-Estar en la pantalla de registro | 1-Abrir la página de registro |  |  |
|  |  | 2-El usuario no debe estar registrado | 1. Ingresar nombre válido "Romina" |  |  |
|  |  | 3-Existe conexión a Internet. | 2. Ingresar email válido "asdQ@gmail.com" |  |  |
|  |  | 4-La pagina debe funcionar correctamente. | 3. Ingresar contraseña válida "RLJ#2923" |  |  |
|  |  | 5-El usuario no está autenticado. | 4. Cargar Cv "formato pdf" |  |  |
|  |  | 6-el cv debe estar descargado | 4. Click en “Registrarse” |  |  |
| Resultado Esperado | Resultado Obtenido | Evidencias | Estado (Pasó/Falló/ Bloqueado) | Comentarios |  |
| El registro del usuario debe completarse en menos de 2 segundos. | el sistema tarda en registrar al usuario mas de 10 seg |  | Falló |  |  |

## 📑 Hoja: RB- Reporte de Bugs

| Reporte de Bugs | Unnamed: 1 | Unnamed: 2 | Unnamed: 3 | Unnamed: 4 | Unnamed: 5 | Unnamed: 6 | Unnamed: 7 | Unnamed: 8 | Unnamed: 9 |
|---|---|---|---|---|---|---|---|---|---|
| N° identificador | Tipo | Título | Descripción | Severidad | Prioridad | Pasos para reproducir | Resultado esperado | Resultado obtenido | Evidencia |
| TC-02 | Defecto | Registro de usuario (NOMBRE )invalido | Permite registrar nombres con menos de 3 caracteres. | Alta | Alta | 1.ingresar a la pagina de talento lab 2. Ingresar nombre inválido "ad" 3. Ingresar email válido "asdQ@gmail.com 4. Ingresar contraseña válida "RLJ#2923" 5. Cargar Cv formato pdf 6.Hacer click en registarme | El sistema debe validar que el nombre ingresado tenga como mínimo 3 caracteres y debe mostrar un mensaje de validación si no cumple con este requisito. El usuario no debe poder completar el registro hasta ingresar un nombre válido. | El sistema permite ingresar y registrar un nombre con menos de 3 caracteres sin mostrar ningún mensaje de validación. | https://drive.google.com/drive/folders/1yQhHp46vUhOffQZpxIqvK4wGlzvcyOl_?usp=sharing |
| TC-04 | Defecto | Registro de usuario (CORREO ELECTRONICO) invalido | El sistema permite hacer registro con correo invalido sin el "@" | Alta | Alta | 1.ingresar a la pagina de talento lab 2. Ingresar nombre inválido "Romina" 3. Ingresar email inválido "asdQgmail.com" 4. Ingresar contraseña válida "RLJ#2923" 5. Cargar Cv formato pdf 6.Hacer click en registarme | El sistema debe validar que el correo electrónico tenga un formato válido, incluyendo el carácter "@", y debe mostrar un mensaje de error cuando el formato sea incorrecto. El usuario no debe poder completar el registro con un correo inválido. | El sistema permite ingresar un correo electrónico sin el carácter "@" y continuar con el proceso de registro sin mostrar un mensaje de validación. |  |
| TC-06 | Defecto | Registro de usuario (CONTRASEÑA) invalido | Permite contraseñas inseguras. | Alta | Alta | 1.ingresar a la pagina de talento lab 2. Ingresar nombre inválido "Romina" 3. Ingresar email inválido "asdQ@gmail.com" 4. Ingresar contraseña inválida "111" 5. Cargar Cv formato pdf 6.Hacer click en registarme | El sistema debe validar que la contraseña cumpla con los requisitos mínimos de seguridad establecidos y debe impedir el registro cuando la contraseña no cumpla con dichos requisitos. | El sistema permite registrar al usuario utilizando una contraseña de solo 3 caracteres (111), sin mostrar ningún mensaje de validación ni advertencia sobre la seguridad de la contraseña. |  |
| TC-08 | Defecto | Validacion de carga de Cv con formato png | El sistema permite completar el registro utilizando un archivo con un formato diferente a PDF, incumpliendo el criterio de aceptación que establece que el CV debe cargarse únicamente en formato PDF. | Alta | Alta | 1.ingresar a la pagina de talento lab 2. Ingresar nombre válido "Romina" 3. Ingresar email válido "asdQ@gmail.com 4. Ingresar contraseña válida "RLJ#2923" 5. dejar campo Cv formato png 6.Hacer click en registarme | El sistema debe permitir cargar únicamente archivos en formato PDF, de acuerdo con el criterio establecido para la postulación. Si el usuario intenta cargar un archivo con un formato diferente, el sistema debe rechazarlo y mostrar un mensaje indicando que el formato no es válido. | El sistema permite cargar y completar el registro utilizando un archivo en formato PNG, aunque el criterio establecido indica que el CV debe cargarse únicamente en formato PDF. |  |
| TC-07 | Defecto | Validación de carga vacia de Cv | El sistema permite completar el registro utilizando un archivo vacio, incumpliendo el criterio de aceptación que establece que el CV debe cargarse, ya que es un requisito fundamental para la postulacion de vacantes que proporciona Talento Lab. | Alta | Alta | 1.ingresar a la pagina de talento lab 2. Ingresar nombre válido "Romina" 3. Ingresar email válido "asdQ@gmail.com 4. Ingresar contraseña válida "RLJ#2923" 5. dejar campo Cv "vacio" 6.Hacer click en registarme | El sistema debe validar que el usuario haya cargado un archivo de CV antes de completar el registro. Si el campo se encuentra vacío, debe impedir el registro y mostrar un mensaje indicando que el CV es obligatorio. | El sistema permite completar el registro sin cargar ningún archivo de CV, aunque este campo es obligatorio para completar la postulación. |  |

