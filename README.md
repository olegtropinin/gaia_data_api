# Relative URLs
http://cdn.gea.esac.esa.int/Gaia/gdr2/
https://gea.esac.esa.int/archive/documentation/GDR2/pdf/GaiaDR2_documentation_1.2.pdf


# PostgreSQL

CREATE DATABASE gaia_data;
CREATE USER gaia_data WITH PASSWORD 'SOME_PASSWORD';
ALTER USER gaia_data CREATEDB;
GRANT ALL PRIVILEGES ON DATABASE gaia_data TO gaia_data;


# Environment variables

DATABASE_PASSWORD

# Generate test Gaia Source file

cd var/gaia_source/
head -n 30 GaiaSource_1000172165251650944_1000424567594791808.csv > ../../tests/gaia_source.csv