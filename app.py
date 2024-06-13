import folium
from flask import Flask, render_template

def create_map():
    # Membuat objek peta
    my_map = folium.Map(location=[-7.9294126,112.6472604], zoom_start=14)  # Koordinat Polowijen, Malang
    
    # Tambahkan marker
    folium.Marker(
        location=[-7.9294126,112.6472604],
        popup="Kelurahan Polowijen",
        icon=folium.Icon(icon="info-sign", color="blue"),
    ).add_to(my_map)
    
    # Simpan peta sebagai file HTML
    my_map.save("static/map.html")

create_map()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
