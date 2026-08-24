CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);

CREATE TABLE sqlite_sequence(name,seq);

CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_time" datetime NOT NULL);

CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);

CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);

CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);

CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "first_name" varchar(150) NOT NULL);

CREATE TABLE "catalogo_autor" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(150) NOT NULL, "nacionalidad" varchar(100) NOT NULL, "bio" text NOT NULL, "foto" varchar(100) NULL);

CREATE TABLE "catalogo_libro" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "titulo" varchar(200) NOT NULL, "slug" varchar(220) NOT NULL UNIQUE, "genero" varchar(3) NOT NULL, "formato" varchar(3) NOT NULL, "editorial" varchar(150) NOT NULL, "precio" integer unsigned NOT NULL CHECK ("precio" >= 0), "anio" smallint unsigned NOT NULL CHECK ("anio" >= 0), "idioma" varchar(50) NOT NULL, "dimensiones" varchar(50) NOT NULL, "isbn" varchar(20) NOT NULL, "paginas" smallint unsigned NOT NULL CHECK ("paginas" >= 0), "imagen" varchar(100) NOT NULL, "etiqueta" varchar(3) NOT NULL, "descripcion" text NOT NULL, "frase" text NOT NULL, "separador" bool NOT NULL, "nuevo" bool NOT NULL, "destacado" bool NOT NULL, "autor_id" bigint NOT NULL REFERENCES "catalogo_autor" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "equipo_miembroequipo" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(150) NOT NULL, "cargo" varchar(150) NOT NULL, "foto" varchar(100) NOT NULL, "bio" text NOT NULL);

CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);

CREATE TABLE "home_fraseeditorial" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "mensaje" text NOT NULL, "autor" varchar(150) NULL, "activo" bool NOT NULL);

CREATE TABLE "home_slidehero" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "titulo_interno" varchar(100) NOT NULL, "imagen_fondo" varchar(100) NOT NULL, "documento_descarga" varchar(100) NULL, "orden" integer unsigned NOT NULL CHECK ("orden" >= 0), "activo" bool NOT NULL, "etiqueta" varchar(50) NULL);

CREATE TABLE "home_anunciopremio" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "frase" varchar(255) NOT NULL, "color_fondo" varchar(7) NOT NULL, "imagen" varchar(100) NOT NULL, "documento_pdf" varchar(100) NULL, "activo" bool NOT NULL, "texto_boton_pdf" varchar(50) NOT NULL);

CREATE TABLE "contacto_mensajeeditorial" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(150) NOT NULL, "correo" varchar(254) NOT NULL, "asunto" varchar(200) NOT NULL, "mensaje" text NOT NULL, "fecha_creacion" datetime NOT NULL, "leido" bool NOT NULL);

CREATE TABLE "noticias_etiquetarol" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(100) NOT NULL UNIQUE, "color_css" varchar(30) NOT NULL);

CREATE TABLE "noticias_albumgaleria" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "titulo" varchar(200) NOT NULL, "libro" varchar(200) NULL, "autor_id" bigint NULL REFERENCES "catalogo_autor" ("id") DEFERRABLE INITIALLY DEFERRED, "noticia_id" bigint NOT NULL REFERENCES "noticias_noticia" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "noticias_multimediagaleria" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "tipo" varchar(15) NOT NULL, "imagen" varchar(100) NULL, "video_archivo" varchar(100) NULL, "video_url" varchar(200) NULL, "archivo_documento" varchar(100) NULL, "titulo_o_descripcion" varchar(200) NOT NULL, "orden" integer unsigned NOT NULL CHECK ("orden" >= 0), "album_id" bigint NOT NULL REFERENCES "noticias_albumgaleria" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "noticias_participacion" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "autor_id" bigint NOT NULL REFERENCES "catalogo_autor" ("id") DEFERRABLE INITIALLY DEFERRED, "etiqueta_id" bigint NULL REFERENCES "noticias_etiquetarol" ("id") DEFERRABLE INITIALLY DEFERRED, "noticia_id" bigint NOT NULL REFERENCES "noticias_noticia" ("id") DEFERRABLE INITIALLY DEFERRED);

CREATE TABLE "noticias_noticia" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "titulo" varchar(200) NOT NULL, "slug" varchar(220) NOT NULL UNIQUE, "resumen" varchar(300) NOT NULL, "contenido" text NOT NULL, "imagen" varchar(100) NULL, "fecha" date NOT NULL, "categoria" varchar(20) NOT NULL, "enlace_pdf" varchar(200) NULL);

CREATE TABLE "home_bannercarrusel" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "titulo" varchar(200) NOT NULL, "descripcion" text NOT NULL, "imagen" varchar(100) NOT NULL, "enlace_url" varchar(200) NOT NULL, "archivo_pdf" varchar(100) NULL, "texto_boton" varchar(50) NOT NULL, "orden" smallint unsigned NOT NULL CHECK ("orden" >= 0), "activo" bool NOT NULL);

