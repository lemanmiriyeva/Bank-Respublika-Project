var Chaine;
var a = "http://images.all-free-download.com/images/graphicthumb/letter_a_89083.jpg";
var b = "https://upload.wikimedia.org/wikipedia/commons/2/25/Arabesque-letter-b-icon.png";
var c = "http://icons.iconarchive.com/icons/iconarchive/arabesque-alphabet/256/letter-c-icon.png";
var d = "http://icons.iconarchive.com/icons/iconarchive/arabesque-alphabet/256/letter-d-icon.png";
var e = "http://icons.iconarchive.com/icons/iconarchive/arabesque-alphabet/256/letter-e-icon.png";
var f = "http://icons.iconarchive.com/icons/iconarchive/arabesque-alphabet/256/letter-f-icon.png";
var g = "http://icons.iconarchive.com/icons/iconarchive/arabesque-alphabet/256/letter-g-icon.png";
var h = "http://icons.iconarchive.com/icons/iconarchive/arabesque-alphabet/256/letter-h-icon.png";
var i = ""; //etant un bug inconnu la lettre I n'est pas réactualisé donc pas affichée
var j = "https://upload.wikimedia.org/wikipedia/commons/b/be/Arabesque-letter-i-icon.png";
var k = "http://icons.iconarchive.com/icons/iconarchive/arabesque-alphabet/256/letter-k-icon.png";
var l = "http://images.gofreedownload.net/letter-l-33980.jpg";
var m = "http://icons.iconarchive.com/icons/iconarchive/arabesque-alphabet/256/letter-m-icon.png";
var n = "http://icons.iconarchive.com/icons/iconarchive/arabesque-alphabet/256/letter-n-icon.png";
var o = "http://icons.iconarchive.com/icons/iconarchive/arabesque-alphabet/256/letter-o-icon.png";
var p = "http://icons.veryicon.com/ico/System/Arabesque%20Alphabet/Letter%20p.ico";
var q = "http://icons.iconarchive.com/icons/iconarchive/arabesque-alphabet/256/letter-q-icon.png";
var r = "http://icons.iconarchive.com/icons/iconarchive/arabesque-alphabet/256/letter-r-icon.png";
var s = "http://icons.iconarchive.com/icons/iconarchive/arabesque-alphabet/256/letter-s-icon.png";
var t = "http://icons.iconarchive.com/icons/iconarchive/arabesque-alphabet/256/letter-t-icon.png";
var u = "http://icons.iconarchive.com/icons/iconarchive/arabesque-alphabet/256/letter-u-icon.png";
var v = "http://icons.iconarchive.com/icons/iconarchive/arabesque-alphabet/256/letter-v-icon.png";
var w = "http://icons.iconarchive.com/icons/iconarchive/arabesque-alphabet/256/letter-w-icon.png";
var x = "http://icons.iconarchive.com/icons/iconarchive/arabesque-alphabet/256/letter-x-icon.png";
var y = "http://icons.iconarchive.com/icons/iconarchive/arabesque-alphabet/256/letter-y-icon.png";
var z = "http://icons.iconarchive.com/icons/iconarchive/arabesque-alphabet/256/letter-z-icon.png";
var un = "http://serge-alibert.fr/wp-content/uploads/2016/01/2016-01-21-chiffre-1-20182.jpg";
var de = "http://stickeramoi.com/6209-6740-large/sticker-chiffre-deux.jpg";
var tr = "https://www.educolorir.com/imagem-numero-3-p20177.jpg";
var qu = "http://cm2f.com/497-large_default/plaque-edwardian-chiffre-4.jpg";
var ci = "http://www2.mes-coloriages-preferes.biz/colorino/Images/Large/Chiffres-et-formes-Tous-les-chiffres-Chiffre-5-622785.png";
var si = "http://cdn.deguisetoi.fr/images/rep_art/gra/229/7/229750/ballon-geant-chiffre-6-noir-96-cm_229750.jpg";
var se = "http://api.education-et-numerique.fr/3.0/blob/556739423361eb7e616eb292/draft";
var hu = "http://csimg.webmarchand.com/srv/FR/28012220abb00336/T/340x340/C/FFFFFF/url/ballon-animalon-gacant-chiffre.jpg";
var ne = "http://www2.mes-coloriages-preferes.biz/colorino/Images/Large/Chiffres-et-formes-Tous-les-chiffres-Chiffre-9-670997.png";
var ze = "https://media.cdnws.com/_i/19708/1859/790/62/ballon-alu-dore-chiffre-0.jpeg";



function generate_captcha(limit){
  doc = document.getElementById("captcha");
   
  var characteres = new Array("a", "b", "c", "d", "e", "f", "g", "h", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", 'y', "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0");
  var characterev = new Array(a, b, c, d, e, f, g, h, j, k, l, m, n, o, p, q, r, s, t, u, v, w, y, z, un, de, tr, qu, ci, si, se, hu, ne, ze); // Tableau à 2 entrées, une en version variable et une en version texte, l'ordre DOIT etre respecté car une valeur dans 1 vaut une valeur dans l'autre
  var Chainea = ''; // Réinitialisation des images
  Chaine = ''; //Réinitioalisation de la chaine courante
      for(i=0; i<limit; i++){ //rééxecute ce code autant de fois que limit
        rando = Math.floor(Math.random() * characteres.length);//génere une valeur aléatoire par rapport à la taille des 2 tableaux
        Chainea = Chainea + "<img src='" + characterev[rando] + "' alt='" + characteres[rando] + "'/>"; //met les images à la suites des autres, characteres valant pour la source
       
        Chaine = Chaine + characteres[rando]; // recupere la valeur à recuperer
      }
    doc.innerHTML = Chainea; // affiche les images
}
  function verifvalue_captcha(){
    inp = document.getElementById("check");
     recu = inp.value.toLowerCase();
    if(recu === Chaine){
      reponse = "Demande réussie";
       inp.style.border = '2px solid green';
      inp.value = ""; //executer le code voulu ici si c'est réussis
    }else{
      reponse = "Demande echouée";
      inp.style.border = '2px solid red';
      inp.value = "";
      generate_captcha(9);  
    }
     document.getElementById("captchaverif").innerHTML = reponse;
  }
  generate_captcha(8);
  