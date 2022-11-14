echo "Creating virtual env:"
python3 -m venv ./venv
echo "Activating virtual env:"
source ./venv/bin/activate
echo "Installing deps:"
pip install -r requirements.txt
echo "Starting application:"
streamlit run app.py --server.maxUploadSize=500