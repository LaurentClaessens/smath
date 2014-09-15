Ces fichiers sont les png à partir desquels certains pdf sont produits.

Ils sont ici parce que je veux pouvoir faire 
rm *.pdf
dans le répertoire smath. 

Ils sont à convertir en pdf avec
for f in * ; do convert $f $f.pdf;done
cp png_to_pdf/*.pdf .

Les extensions .png ne sont pas mises parce que ce convert ajoute ".pdf". Cela donnerait des ".png.pdf" que LaTeX n'aime pas.
