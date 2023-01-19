!/bin/bash
curl "https://www.omdbapi.com/?t=$1&apikey=$2"| jq '[.Title,.Genre, .Language, .imdbRating]' >> file.txt
