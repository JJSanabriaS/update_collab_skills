gsudo apt-get update && sudo apt-get -y install wkhtmltopdf
git clone https://www.github.com/odoo/odoo --depth 1 --branch 18.0 odoo18
python3 -m venv odoo18-venv
source odoo18-venv/bin/activatepip3 install wheel
source odoo18-venv/bin/activate
pip3 install wheel
pip3 install pandas
pip3 install -r odoo18/requirements.txt
deactivate
mkdir /opt/odoo18/odoo18/custom-addons
sudo chmod -R 777 /opt/odoo18/odoo18/
exit
