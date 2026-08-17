CREATE TABLE django_migrations (
    id SERIAL PRIMARY KEY,
    app varchar(255) NOT NULL,
    name varchar(255) NOT NULL,
    applied datetime NOT NULL
);

CREATE TABLE django_content_type (
    id SERIAL PRIMARY KEY,
    app_label varchar(100) NOT NULL,
    model varchar(100) NOT NULL
);

CREATE TABLE auth_permission (
    id SERIAL PRIMARY KEY,
    content_type_id integer NOT NULL REFERENCES django_content_type (id),
    codename varchar(100) NOT NULL,
    name varchar(255) NOT NULL
);

CREATE TABLE auth_group (
    id SERIAL PRIMARY KEY,
    name varchar(150) NOT NULL UNIQUE
);

CREATE TABLE auth_user (
    id SERIAL PRIMARY KEY,
    password varchar(128) NOT NULL,
    last_login datetime NULL,
    is_superuser boolean NOT NULL,
    username varchar(150) NOT NULL UNIQUE,
    last_name varchar(150) NOT NULL,
    email varchar(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined datetime NOT NULL,
    first_name varchar(150) NOT NULL
);

CREATE TABLE auth_group_permissions (
    id SERIAL PRIMARY KEY,
    group_id integer NOT NULL REFERENCES auth_group (id),
    permission_id integer NOT NULL REFERENCES auth_permission (id)
);

CREATE TABLE auth_user_groups (
    id SERIAL PRIMARY KEY,
    user_id integer NOT NULL REFERENCES auth_user (id),
    group_id integer NOT NULL REFERENCES auth_group (id)
);

CREATE TABLE auth_user_user_permissions (
    id SERIAL PRIMARY KEY,
    user_id integer NOT NULL REFERENCES auth_user (id),
    permission_id integer NOT NULL REFERENCES auth_permission (id)
);

CREATE TABLE django_admin_log (
    id SERIAL PRIMARY KEY,
    object_id text NULL,
    object_repr varchar(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer NULL REFERENCES django_content_type (id),
    user_id integer NOT NULL REFERENCES auth_user (id),
    action_time datetime NOT NULL
);

CREATE TABLE django_session (
    session_key varchar(40) NOT NULL PRIMARY KEY,
    session_data text NOT NULL,
    expire_date datetime NOT NULL
);

CREATE TABLE catalogo_autor (
    id SERIAL PRIMARY KEY,
    nombre varchar(150) NOT NULL,
    nacionalidad varchar(100) NOT NULL,
    bio text NOT NULL,
    foto varchar(100) NULL
);

CREATE TABLE catalogo_libro (
    id SERIAL PRIMARY KEY,
    titulo varchar(200) NOT NULL,
    slug varchar(220) NOT NULL UNIQUE,
    genero varchar(3) NOT NULL,
    formato varchar(3) NOT NULL,
    editorial varchar(150) NOT NULL,
    precio integer NOT NULL,
    anio smallint NOT NULL,
    idioma varchar(50) NOT NULL,
    dimensiones varchar(50) NOT NULL,
    isbn varchar(20) NOT NULL,
    paginas smallint NOT NULL,
    imagen varchar(100) NOT NULL,
    etiqueta varchar(3) NOT NULL,
    descripcion text NOT NULL,
    frase text NOT NULL,
    separador boolean NOT NULL,
    nuevo boolean NOT NULL,
    destacado boolean NOT NULL,
    autor_id bigint NOT NULL REFERENCES catalogo_autor (id)
);

CREATE TABLE equipo_miembroequipo (
    id SERIAL PRIMARY KEY,
    nombre varchar(150) NOT NULL,
    cargo varchar(150) NOT NULL,
    foto varchar(100) NOT NULL,
    bio text NOT NULL
);

CREATE TABLE home_fraseeditorial (
    id SERIAL PRIMARY KEY,
    mensaje text NOT NULL,
    autor varchar(150) NULL,
    activo boolean NOT NULL
);

CREATE TABLE home_slidehero (
    id SERIAL PRIMARY KEY,
    titulo_interno varchar(100) NOT NULL,
    imagen_fondo varchar(100) NOT NULL,
    documento_descarga varchar(100) NULL,
    orden integer NOT NULL,
    activo boolean NOT NULL,
    etiqueta varchar(50) NULL
);

CREATE TABLE home_anunciopremio (
    id SERIAL PRIMARY KEY,
    frase varchar(255) NOT NULL,
    color_fondo varchar(7) NOT NULL,
    imagen varchar(100) NOT NULL,
    documento_pdf varchar(100) NULL,
    activo boolean NOT NULL,
    texto_boton_pdf varchar(50) NOT NULL
);

CREATE TABLE contacto_mensajeeditorial (
    id SERIAL PRIMARY KEY,
    nombre varchar(150) NOT NULL,
    correo varchar(254) NOT NULL,
    asunto varchar(200) NOT NULL,
    mensaje text NOT NULL,
    fecha_creacion datetime NOT NULL,
    leido boolean NOT NULL
);

CREATE TABLE noticias_etiquetarol (
    id SERIAL PRIMARY KEY,
    nombre varchar(100) NOT NULL UNIQUE,
    color_css varchar(30) NOT NULL
);

CREATE TABLE noticias_noticia (
    id SERIAL PRIMARY KEY,
    titulo varchar(200) NOT NULL,
    slug varchar(220) NOT NULL UNIQUE,
    resumen varchar(300) NOT NULL,
    contenido text NOT NULL,
    imagen varchar(100) NULL,
    fecha date NOT NULL,
    categoria varchar(20) NOT NULL,
    enlace_pdf varchar(200) NULL
);

CREATE TABLE noticias_albumgaleria (
    id SERIAL PRIMARY KEY,
    titulo varchar(200) NOT NULL,
    libro varchar(200) NULL,
    autor_id bigint NULL REFERENCES catalogo_autor (id),
    noticia_id bigint NOT NULL REFERENCES noticias_noticia (id)
);

CREATE TABLE noticias_multimediagaleria (
    id SERIAL PRIMARY KEY,
    tipo varchar(15) NOT NULL,
    imagen varchar(100) NULL,
    video_archivo varchar(100) NULL,
    video_url varchar(200) NULL,
    archivo_documento varchar(100) NULL,
    titulo_o_descripcion varchar(200) NOT NULL,
    orden integer NOT NULL,
    album_id bigint NOT NULL REFERENCES noticias_albumgaleria (id)
);

CREATE TABLE noticias_participacion (
    id SERIAL PRIMARY KEY,
    autor_id bigint NOT NULL REFERENCES catalogo_autor (id),
    etiqueta_id bigint NULL REFERENCES noticias_etiquetarol (id),
    noticia_id bigint NOT NULL REFERENCES noticias_noticia (id)
);