# AutomatedTestingProject

# Proyecto de Pruebas Automatizadas con Selenium 

Este proyecto contiene pruebas automatizadas utilizando Selenium para interactuar con una aplicación web.


# Historias de usuario 

# Historia de Usuario 1: Interacción con Elementos por Clase

Criterios de Aceptación:

Deseo poder hacer clic en un elemento de la página identificado por su clase.

Después de hacer clic, la página debe esperar durante al menos 10 segundos para permitir una inspección visual manual.

Criterios de Rechazo:

La clase especificada no existe en la página.

El elemento identificado por la clase no es interactuable (por ejemplo, está deshabilitado).


# Historia de Usuario 2: Interacción con Elementos por ID

Criterios de Aceptación:

Deseo poder ingresar texto en un campo de entrada identificado por su ID.

El texto ingresado debe ser "Texto de prueba".

Después de ingresar el texto, la página debe esperar durante al menos 10 segundos para permitir una inspección visual manual.

Criterios de Rechazo:

El ID especificado no existe en la página.

El campo de entrada identificado por el ID no es interactuable.


# Historia de Usuario 3: Interacción con Calendario

Criterios de Aceptación:

Deseo poder hacer clic en un campo de calendario en la página.

Después de hacer clic, la página debe esperar al menos 2 segundos.

Deseo poder seleccionar una fecha del calendario mediante un clic en un día específico.

Después de seleccionar la fecha, la página debe esperar al menos 4 segundos.

Deseo poder limpiar el campo de calendario.

Después de limpiar el campo, deseo poder ingresar la fecha "12/31/2023".

Después de ingresar la fecha, la página debe esperar al menos 4 segundos.

Criterios de Rechazo:

El campo de calendario no es interactuable.

La fecha seleccionada no es válida.

No se puede limpiar el campo de calendario.


# Historia de Usuario 4: Interacción con Checkbox

Criterios de Aceptación:

Deseo poder hacer clic en un checkbox en la página.

Después de hacer clic, la página debe esperar al menos 5 segundos.

Deseo verificar el estado del checkbox antes y después del clic.

Después de hacer clic, el estado del checkbox debe cambiar de no seleccionado a seleccionado.

Criterios de Rechazo:

El checkbox especificado no existe en la página.

El checkbox está deshabilitado y no puede ser seleccionado.


# Historia de Usuario 5: Navegación del Navegador

Criterios de Aceptación:

Deseo poder navegar a una URL específica.

Después de la navegación, deseo verificar y mostrar la URL actual.

Deseo poder hacer clic en un enlace en la página.

Después de hacer clic, deseo verificar y mostrar la URL actual.

Deseo poder regresar a la página anterior.

Después de regresar, deseo verificar y mostrar la URL actual.

Deseo poder avanzar a la página siguiente.

Después de avanzar, deseo verificar y mostrar la URL actual.

Deseo poder actualizar la página actual.

Después de la actualización, deseo verificar y mostrar la URL actual.

Criterios de Rechazo:

La URL esperada después de la navegación, clic en enlace, regreso, avance o actualización no coincide.

