import re
from typing import Optional

from attr import define

from detectpii.detector.column_name_regex import Detector
from detectpii.model import Column
from detectpii.pii_type import (
    Email,
    BirthDate,
    Gender,
    Nationality,
    ZipCode,
    UserName,
    SSN,
    PoBox,
    CreditCard,
    Phone,
    PiiType,
    Person,
    Address,
    Password,
)

@define(kw_only=True)
class SpanishColumnNameRegexDetector(Detector):
    """Detect PII columns by matching them against known patterns.

    This class has been borrowed from piicatcher and modified for use with this library.
    """

    regex: dict = {
        Person: re.compile(
            "^.*(primernombre|pnombre|apellido|"
            "nombrecompleto|nombre_completo|_nombre|"
            "apodo|nombre|cliente|nombreapellido).*$",
            re.IGNORECASE,
        ),
        Email: re.compile(
            "^.*(email|e-mail|mail|correo_electronico|"
            "correoelectronico|correo|direccion_de_correo|"
            "email_address|correo_de_contacto|contact_email|"
            "contacto_email).*$",
            re.IGNORECASE,
        ),
        BirthDate: re.compile(
            "^.*(fecha_de_nacimiento|fechanacimiento|fnac|"
            "fechanac|fnacimiento|nacimiento|cumpleanios|"
            "cumpleaños|cumple|fecha_fallecimiento|ffallecimiento|"
            "fecha_defuncion|defuncion|muerte|fecha_muerte|fdefuncion|"
            "edad|aniodenacimiento|ano_nacimiento|anodenacimiento|fecha_nac).*$",
            re.IGNORECASE,
        ),
        Gender: re.compile(
            "^.*(genero|sexo|gender|identidad|identidad_genero|"
            "genero_biologico|sexo_biologico|sexo_natal|"
            "genero_autopercibido|identidad_sexual).*$",
            re.IGNORECASE,
        ),
        Nationality: re.compile(
            "^.*(nacionalidad|pais_origen|pais_de_origen|ciudadania|"
            "nacion|pais_nacimiento|nacional).*$",
            re.IGNORECASE,
        ),
        Address: re.compile(
            "^.*(direccion|ciudad|localidad|poblacion|provincia|"
            "comarca|pais|zona|barrio|vecindad|calle|avenida|"
            "domicilio|colonia|region|distrito|municipio|sector|parroquia).*$",
            re.IGNORECASE,
        ),
        ZipCode: re.compile(
            "^.*(codigo\s*postal|cod\s*postal|cp|cpa|postal|codigo\s*zip|"
            "cod\s*zip|zip|distrito\s*postal|cod\s*post).*$",
            re.IGNORECASE,
        ),
        UserName: re.compile(
            "^.*(user(id|name|)|usuario|nombre_usuario|nombre_de_usuario|"
            "username|login|account|alias|nick|nickname|"
            "identificador_usuario|id_usuario|iduser).*$",
            re.IGNORECASE,
        ),
        Password: re.compile(
            "^.*(pass|password|passwd|contrasena|clave|clave_acceso|"
            "clave_secreta|contrasenia|security_code|"
            "codigo_seguridad|secret|secret_key|auth_key|"
            "password_hash|hashed_password).*$",
            re.IGNORECASE,
        ),
        SSN: re.compile(
            "^.*(ssn|social_number|social_security|"
            "social_security_number|social_security_no).*$",
            re.IGNORECASE,
        ),
        PoBox: re.compile(
            "^.*(casilla_postal|casilla_correo|"
            "casilla|apartado_postal|apartado|apdo_postal|"
            "direccion_postal|direccion_correo|dir_postal).*$",
            re.IGNORECASE,
        ),
        CreditCard: re.compile(
            "^.*(tarjeta_credito|numero_tarjeta|num_tarjeta|"
            "num_tarjeta_credito|tarjeta_cc|credit_card_no|creditcard_no|"
            "tarjeta_bancaria).*$",
            re.IGNORECASE,
        ),
        Phone: re.compile(
            "^.*(telefono|numero_telefono|num_telefono|tel|"
            "celular|cel|mobile|mobile_number|mobile_num|mobile_no|"
            "contact_number|contacto_telefono).*$",
            re.IGNORECASE,
        ),
    }

    name: str = "SpanishColumnNameRegexDetector"

    def detect(
        self,
        column: Column,
        *args,
        **kwargs,
    ) -> Optional[PiiType]:
        for pii_type, ex in self.regex.items():
            if ex.match(column.name) is not None:
                return pii_type()

        return None
