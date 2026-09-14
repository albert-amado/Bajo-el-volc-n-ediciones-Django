document.addEventListener('DOMContentLoaded', () => {

  // Función central que arma y abre el cliente de correo
  const procesarEnvio = (idNombre, idCorreo, idAsunto, idMensaje) => {
    const nombre = document.getElementById(idNombre).value;
    const correo = document.getElementById(idCorreo).value;
    const asunto = document.getElementById(idAsunto).value;
    const mensaje = document.getElementById(idMensaje).value;

    const cuerpo = `Hola bajo el volcan ediciones, mi nombre es ${nombre} y mi asunto es ${asunto} y me podrias ayudar con ${mensaje}.\n\nPueden responderme a este correo: ${correo}`;

    const mailtoUrl = `mailto:bajoelvolcane@gmail.com?subject=${encodeURIComponent(asunto)}&body=${encodeURIComponent(cuerpo)}`;
    window.location.href = mailtoUrl;
  };

  // 1. Detectar y procesar el formulario de libros
  const btnLibros = document.getElementById('btnEnviarLibros');
  if (btnLibros) {
    btnLibros.addEventListener('click', () => {
      procesarEnvio('inputNombre', 'inputCorreo', 'inputAsunto', 'inputMensaje');
    });
  }

  // 2. Detectar y procesar el formulario de la página de contacto (Django)
  const btnContacto = document.getElementById('btnEnviarContacto');
  if (btnContacto) {
    btnContacto.addEventListener('click', () => {
      procesarEnvio('id_nombre', 'id_correo', 'id_asunto', 'id_mensaje');
    });
  }
});