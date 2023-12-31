from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class DoneForm(ModelForm):
    class Meta:
        model = models.Doone
        fields = ('id', 'nomcapteur', 'piece', 'emplacement')
        labels = {
            'id': _('Id'),
            'nomcapteur': _('Nomcapteur'),
            'piece': _('Piece'),
            'emplacement': _('Emplacement'),
        }

class stampForm(ModelForm):
    class Meta:
        model = models.stamp
        fields = ('idd', 't1')
        labels = {
            'idd': _("Idd"),
            't1': _('t1'),
        }