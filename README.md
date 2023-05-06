# Build Gestion bibliothéque | Python & PyQt5

Il s'agit d'un code Python utilisant PyQt5 pour créer un système de connexion qui se connecte à une base de données MySQL. Le code permet à l'utilisateur de se connecter, de créer un compte et de réinitialiser le mot de passe si nécessaire, visualiser livres avec possibilité d’ajouter ou supprimer un livre.

****Les fonctionnalités principales****

    ▪ L'application doit permettre aux utilisateurs de créer un compte avec un nom d'utilisateur et un mot de passe ;
    ▪ Stocker les informations des utilisateurs dans une table de la base de données ;
    ▪ Permettre aux utilisateurs de se connecter avec leur nom d'utilisateur et leur mot de passe ;
    ▪ Afficher la liste des livres avec les attributs suivants titre, image, auteur et année de publication ;
    ▪ Stocker les informations des livres dans une table de la base de données ;
    ▪ Permettre aux utilisateurs de rechercher des livres par titre, auteur ou année de publication ;
    ▪ Gérer les stocks de livres en ajoutant et en supprimant des livres de la base de données.




****Dépendances:*****

  Ce code dépend des bibliothèques suivantes :

   ▪PyQt5
   ▪pymysql
   ▪PyQt5.uic
   ▪PyQt5.QtGui
   ▪PyQt5.QtCore
   ▪PyQt5.QtWidgets

   Le code dépend des modules suivants :

    ▪PyQt5 : une liaison Python de la boîte à outils d'interface graphique multiplateforme Qt
    ▪mysql-connector-python : Ce module est utilisé pour se connecter à la base de données MySQL et exécuter des requêtes SQL.
    ▪res.py : un fichier de ressources contenant des images et d'autres fichiers non-Python
    
****Usage:***

1-Assurez-vous que toutes les dépendances sont installées.
2-Créez une base de données MySQL nommée 'library' et importez la table 'user' à partir du fichier 'library.sql'.
3-Exécutez le fichier 'main.py' à l'aide d'un IDE Python ou de la ligne de commande.
4-L'utilisateur sera dirigé vers la page de connexion où il pourra saisir son adresse e-mail et son mot de passe.
5-Si l'utilisateur n'a pas de compte, il peut cliquer sur le bouton "sign up" pour créer un nouveau compte.
6-Si l'utilisateur a oublié son mot de passe, il peut cliquer sur le lien “ forgot password “  bouton pour le réinitialiser.
7-L'utilisateur sera dirigé vers la fenêtre principale après clicker sur button login in login page où il peut chercher,lister ou afficher, ajouter et supprimer livres
  

Une fois que vous avez configuré votre base de données(etape numero 2), vous pouvez lancer l'application en exécutant la commande suivante dans le terminal :
      ------> "python main.py"

Cela lancera l'application et affichera la fenêtre de connexion du système de gestion bibliothéque.

****Dossiers****
    ▪'login.ui' : un fichier d'interface utilisateur créé à l'aide de Qt Designer qui définit l'interface utilisateur du système de connexion.
    ▪'singup.ui' : un fichier d'interface utilisateur créé à l'aide de Qt Designer qui définit l'interface utilisateur du système de creeatin de compte.
    ▪'forgetpass.ui' : un fichier d'interface utilisateur créé à l'aide de Qt Designer qui définit l'interface utilisateur du système de  réinitialisation mot de pass.
    ▪'home.ui' : un fichier d'interface utilisateur créé à l'aide de Qt Designer qui définit main page.
    ▪'add.ui' : un fichier d'interface utilisateur créé à l'aide de Qt Designer qui définit l'interface  du système de ajouter livre.
    ▪'main.py' : un fichier Python qui charge les fichiers d'interface utilisateur et implémente la fonctionnalité du système de connexion.
    ▪'library.sql' : un fichier SQL qui crée la base de données et la table nécessaires au système de connexion.
    ▪'res.py' : un fichier de ressources qui contient des images et d'autres fichiers non-Python utilisés dans le système de connexion.

****Les classes et méthodes****

   _______▪Login :_______

  La classe appelée Login qui hérite de QMainWindow et possède plusieurs méthodes dont __init__(), loginfunction(), gotocreate() et forget().

Dans la méthode __init__(), la fonction loadUi() est utilisée pour charger une interface utilisateur à partir d'un fichier nommé login.ui et configurer divers widgets et connexions entre eux.

La méthode loginfunction() est déclenchée lorsque l'utilisateur clique sur un bouton nommé "login". Il récupère l'e-mail et le mot de passe de l'utilisateur à partir des champs de texte, exécute une requête SQL pour vérifier si ces informations d'identification sont valides, puis affiche un message d'erreur ou navigue vers une nouvelle page à l'aide des méthodes addWidget() et setCurrentIndex() d'un QStackedWidget appelé widget .

La méthode gotocreate() est déclenchée lorsque l'utilisateur clique sur un bouton intitulé "singup". Il crée une nouvelle instance d'une classe appelée CreateAcc et y accède en utilisant addWidget() et setCurrentIndex().

La méthode forget() est déclenchée lorsque l'utilisateur clique sur un bouton intitulé "forgot". Il récupère l'e-mail de l'utilisateur à partir d'un champ de texte, exécute une requête SQL pour vérifier si l'e-mail existe dans la base de données et affiche un message d'erreur ou navigue vers une nouvelle page pour réinitialiser le mot de passe de l'utilisateur à l'aide de addWidget() et setCurrentIndex().

_______▪forgetpass :_______

  La classe appelée forgetpass qui hérite de la classe QMainWindow de la bibliothèque PyQt5. Le but de cette classe est de permettre aux utilisateurs ayant oublié leur mot de passe de le réinitialiser. La méthode __init__ initialise la classe, charge l'interface utilisateur à partir du fichier forgetpass.ui et configure les widgets et gestionnaires d'événements nécessaires.

La méthode de vérification vérifie si la réponse de l'utilisateur à la question de sécurité est correcte. Il récupère la réponse du widget rep QLineEdit et la compare à la réponse dans la base de données à l'aide d'une requête SQL. Si la réponse est correcte, le widget chp QLabel s'affiche.

La méthode de modification modifie le mot de passe de l'utilisateur si le nouveau mot de passe répond aux exigences et que la confirmation du mot de passe correspond au nouveau mot de passe. Il récupère le nouveau mot de passe et le mot de passe de confirmation à partir des widgets newp et confirm QLineEdit, respectivement. Il vérifie si le nouveau mot de passe répond aux critères requis à l'aide d'une expression régulière. Si le nouveau mot de passe répond aux exigences et que la confirmation du mot de passe correspond au nouveau mot de passe, le mot de passe est mis à jour dans la base de données à l'aide d'une requête SQL et l'utilisateur est ramené à la page de connexion.

Dans l'ensemble, cette classe fait partie d'une application plus vaste qui comprend une page de connexion et une page d'inscription, et elle fournit des fonctionnalités pour réinitialiser les mots de passe oubliés.

_______▪CreateAcc :_______

classe nommée CreateAcc qui hérite de la classe QMainWindow dans le module QtWidgets. Le but de cette classe est de créer une interface utilisateur graphique (GUI) pour l'inscription d'un nouveau compte utilisateur.

La méthode __init__ est le constructeur de la classe qui initialise l'interface graphique en chargeant un fichier d'interface utilisateur ("singup.ui") à l'aide de la méthode loadUi. Il connecte également le signal cliqué d'un bouton nommé singup à une méthode nommée validation.

La méthode de validation est appelée lorsque l'utilisateur clique sur le bouton singup. Cette méthode extrait les valeurs saisies par l'utilisateur dans les champs e-mail, nom, mot de passe, confirmation du mot de passe et réponse de l'interface graphique. Il vérifie ensuite si l'e-mail est déjà pris ou s'il ne correspond pas à une expression régulière définissant un format d'e-mail valide. Si l'une de ces conditions est vraie, un message d'erreur s'affiche à côté du champ e-mail. De même, si le mot de passe ne respecte pas le format requis ou si le champ nom ou réponse est vide, un message d'erreur s'affiche à côté des champs correspondants. Si les champs de mot de passe et de confirmation du mot de passe ne correspondent pas, un message d'erreur s'affiche à côté du champ de confirmation du mot de passe. Si tous les champs sont valides, la méthode createaccfunction est appelée.

La méthode createaccfunction insère l'e-mail, le nom, le mot de passe, la réponse et la question de sécurité de l'utilisateur dans une table de base de données nommée user. Si l'insertion réussit, une boîte de message s'affiche pour informer l'utilisateur que le compte a été ajouté avec succès.

Dans l'ensemble, cette classe fournit une validation de base pour l'entrée de l'utilisateur et insère les détails du compte dans une base de données.

_______▪CustomTableWidgetItem :_______

Cette classe CustomTableWidgetItem hérite de la classe QTableWidgetItem de Qt, qui permet de créer des cellules personnalisées pour les tableaux Qt. La classe CustomTableWidgetItem ajoute une image pixmap en arrière-plan de la cellule, en plus de l'affichage du contenu de la cellule.

La méthode __init__ initialise la classe CustomTableWidgetItem. Elle prend en paramètre un pixmap (une image sous forme de tableau de pixels) et appelle le constructeur de la classe parent QTableWidgetItem. Elle définit également la variable d'instance self.pixmap pour stocker l'image.

La méthode data est appelée lorsqu'il est temps de récupérer les données de la cellule personnalisée. Elle prend en paramètre le rôle de la donnée demandée, qui peut être Qt.DisplayRole (pour le contenu visible de la cellule) ou Qt.BackgroundRole (pour l'image d'arrière-plan). Dans le cas où le rôle est Qt.BackgroundRole, la méthode retourne un objet QBrush créé à partir de l'image stockée dans self.pixmap. L'image est mise à l'échelle pour correspondre à la taille de la cellule à l'aide de la méthode scaled, et l'objet QBrush est renvoyé pour définir l'arrière-plan de la cellule. Si le rôle est autre que Qt.BackgroundRole, la méthode appelle la méthode data de la classe parent QTableWidgetItem pour récupérer les données de la cellule par défaut.

_______▪Page(QMainWindow) :_______

La classe est une sous-classe de la classe QMainWindow qui représente une fenêtre principale d'application avec une barre de menus, une barre d'outils et un espace pour afficher les widgets principaux de l'application.

La méthode __init__ est le constructeur de la classe Page qui initialise les attributs de la fenêtre principale, charge l'interface utilisateur à partir du fichier home.ui en utilisant la fonction loadUi() de la classe UiLoader, connecte les signaux de bouton aux slots et appelle la méthode Showb() pour afficher les données de la table "books".

La méthode Showb() exécute une requête SQL pour sélectionner toutes les données de la table "books", récupère les données en utilisant la méthode fetchall() de l'objet mycursor qui représente le curseur de base de données, et affiche les données dans un tableau QTableWidget dans la fenêtre principale en utilisant la méthode setRowCount(), setColumnCount(), insertRow(), setItem() et setCellWidget(). Elle charge également une image de couverture de livre à partir de la base de données et l'affiche dans une cellule de tableau en utilisant un widget QLabel.

La méthode searchf() est un slot de bouton qui récupère les critères de recherche de l'utilisateur pour les champs "title", "author" et "year", intégré une requête SQL en fonction de ces critères, exécute la requête SQL en en utilisant l'objet mycursor, récupère les données en utilisant la méthode fetchall() et affiche les données dans le tableau QTableWidget de la même manière que la méthode Showb(). Si la requête ne renvoie aucune donnée, elle affiche une boîte de dialogue d'avertissement.

La méthode goadd() est un slot de bouton qui crée une instance de la classe Page2 et l'ajoute à un widget QStackedWidget pour afficher la page suivante de l'application.

La méthode delete_row() est un slot de bouton qui supprime la ligne sélectionnée dans le tableau QTableWidget et supprime également l'enregistrement correspondant dans la table "books" de la base de données. Si aucune ligne n'est sélectionnée, elle affiche une boîte de dialogue d'avertissement.

_______▪Page2(QMainWindow) :_______

La classe Page2 est une classe dérivée de QMainWindow de la bibliothèque PyQt5, qui est utilisée pour construire une fenêtre d'interface graphique (GUI) avec une barre de menus, une barre d'outils et une zone centrale pour contenir d'autres widgets.

Dans le constructeur __init__, la méthode super() est appelée pour appeler le constructeur parent __init__() de QMainWindow. La méthode loadUi() charge l'interface utilisateur (UI) à partir d'un fichier .ui et définit la structure de la fenêtre en y ajoutant des widgets.

Les boutons add et imgc sont connectés aux méthodes add_book() et choose_cover_image() respectivement à l'aide de la méthode clicked.connect(), ce qui signifie que chaque fois que l'utilisateur clique sur l'un des boutons, la méthode correspondante sera appelée.

La méthode choose_cover_image() ouvre une boîte de dialogue de sélection de fichier et permet à l'utilisateur de sélectionner une image de couverture pour le livre. Si l'utilisateur sélectionne un fichier, la méthode lit le fichier d'image, crée un objet QPixmap pour afficher l'image dans la fenêtre, et définit le chemin d'accès au fichier dans la variable filename.

La méthode add_book() extrait le titre, l'auteur et l'année à partir des widgets correspondants, puis effectuée si les champs sont remplis correctement en vérifiant s'ils sont vides ou égaux à zéro. Si les champs ne sont pas remplis correctement, un message d'erreur est affiché à côté de chaque widget. Si tous les champs sont remplis correctement, la méthode insère les données du livre (titre, auteur, année et couverture) dans une base de données MySQL. Si l'opération est réussie, un message de confirmation est affiché, sinon un message d'erreur est affiché.

Enfin, l'objet mainwindow de la classe Login() est ajouté à un objet widget de la classe QStackedWidget, qui s'affiche en tant qu'interface graphique principale.
