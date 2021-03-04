set -xe
python manage.py initdb 
cd integration/
npx cypress run --spec cypress/integration/sample_spec.js --config-file cypress.integration.json