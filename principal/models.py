from django.db import models

# Create your models here.
class codeProgramme (models.Model):
    domaine = models.CharField(max_length=3)
    mention = models.CharField(max_length=2)
    specialite = models.CharField(max_length=5)
    typecours = models.CharField(max_length=2)
    langue = models.CharField(max_length=2)

    def __unicode__(self):
        return u' %s-%s-%s-%s-%s' % (self.domaine, self.mention,self.specialite,self.typecours,self.langue)

class Etablissement (models.Model):
    nom = models.CharField(max_length=150, unique=True)
    lieu = models.CharField(max_length=100)

    def __unicode__(self):
        return u' %s ' % (self.nom)


class codeCours (models.Model):
    ecole = models.ForeignKey(Etablissement)
    grade = models.CharField(max_length=2)
    semestre = models.CharField(max_length=4)
    nomcours = models.CharField(max_length=60)
    codeProgramme = models.ForeignKey(codeProgramme)

    def __unicode__(self):
        return u' %s-%s%s-%s' % (Etablissement(self.ecole).nom, self.grade,self.semestre,self.nomcours)



class Professeur (models.Model):
    nom = models.CharField(max_length=15)
    prenom = models.CharField(max_length=20)
    no_identite = models.CharField(max_length=15)
    cv = models.CharField(max_length=400)

def __unicode__(self):
     return u' %s %s %s' % (self.nom, self.prenom,self.no_identite)



class Cours (models.Model):
    codeCours = models.ForeignKey(codeCours)
    codeProfesseur = models.ForeignKey(Professeur)
    titreducours = models.CharField(max_length=100)
    credit = models.CharField(max_length=10)
    lieu = models.CharField(max_length=100)
    publiccible = models.CharField(max_length=600)
    prerequis= models.CharField(max_length=200)
    objectifs = models.TextField(max_length=300)
    description = models.TextField(max_length=500)
    planducours = models.TextField(max_length=400)
    format = models.TextField(max_length=50)
    ressources = models.TextField(max_length=100)
    evaluation = models.TextField(max_length=250)

    def __unicode__(self):
        return u' %s %s %s %s' % (codeCours(self.codeCours),codeCours(self.codeCours).nomcours, Professeur(self.codeProfesseur), self.credit)






