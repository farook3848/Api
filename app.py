from flask import Flask,jsonify

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
Naruto = {
        "status_code" :200,
    "poster": "https://wallpapercave.com/wp/wp5875837.jpg",
    "series":"",
    "movies":{
        "Naruto Movie 1":"Ninja Clash in the Land of Snow (2004)",
        "Naruto Movie 2":"Legend of the Stone of Gelel (2005)",
        "Naruto Movie 3":"Guardians of the Crescent Moon Kingdom (2006)",
        "Naruto Shippuden Movie 1":"The Movie (2007)",
        "Naruto Shippuden Movie 2":"Bonds (2008)",
        "Naruto Shippuden Movie 3":"The Will of Fire (2009)",
        "Naruto Shippuden Movie 4":"The Lost Tower (2010)",
        "Naruto Shippuden Movie 5":"Blood Prison (2011)",
        "Naruto Shippuden Movie 6":"Road to Ninja (2012)",
        "Movie1":"The Last: Naruto the Movie (2014)",
        "Movie2": "Boruto: Naruto the Movie (2015)",
    },
        "data":[
            {
"id":1,
        "name": "Uzumaki Naruto",
        "image": "https://bit.ly/2XKL7ZZ",
       "history":"Naruto Uzumaki (うずまき ナルト Uzumaki Naruto?) is the main protagonist in the Naruto series created by Masashi Kishimoto. He is a teenage ninja from the fictional village of Konohagakure. The villagers ostracize Naruto because of the Nine-Tailed Demon Fox—a malevolent creature that attacked Konohagakure—sealed in his body. To be recognized, he aspires to become the village's leader, the Hokage.",
     "relatives" :"Namikaze Minato (father, deceased), Uzumaki Kushina (mother, deceased), Hyuuga Hinata (wife), Uzumaki Boruto (son), Uzumaki Himawari (daughter)",
     "power_stats":{
         "intelligence": 65,
         "strength": 100,
         "speed": 80,
         "durability": 75,
         "power": 90,
         "combat": 95
     }
            },
            {
                "id":2,
                "name":"Sasuke Uchiha",
                "images":"https://bit.ly/3zJVQB8",
                "history" :"Sasuke Uchiha (うちは サスケ Uchiha Sasuke?) is a deuteragonist of the Naruto series created by Masashi Kishimoto. In the story, Sasuke is the sole survivor of the Uchiha clan, a highly skilled clan of ninjas allied to the village of Konohagakure. His primary motivation throughout the series is to avenge the destruction of his entire clan by killing his brother, Itachi Uchiha, a task he pursues at all costs. While he was initially cold and singularly driven by his revenge, he becomes more empathetic through his relationships with other characters, notably Naruto Uzumaki, whom he comes to consider as a rival.",
                "relatives":"Uchiha Fugaku (father, deceased), Uchiha Mikoto (mother, deceased), Uchiha Itachi (older brother, deceased), Haruno Sakura (wife), Uchiha Sarada (daughter)",
                "power_stats" :{
                    "intelligence":65,
                    "strength":60,
                    "speed":90,
                    "durability":70,
                    "power" :80,
                    "combat" : 90,
                } ,



            }
        ]
    }


@app.route("/")
def get():
    return jsonify({'Naruto': Naruto})

if __name__ == '__main__':
    app.run(debug=True)