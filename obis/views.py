#from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets, filters, serializers
from rest_framework.renderers import BrowsableAPIRenderer, JSONPRenderer,JSONRenderer,XMLRenderer,YAMLRenderer #, filters
from rest_framework_csv.renderers import CSVRenderer
#from renderer import CustomBrowsableAPIRenderer
from obis.filters import AcctaxFilter
from obis.models import Acctax, Comtax, Syntax 
from serializer import AcctaxSerializer


class AcctaxViewSet(viewsets.ModelViewSet):
    """
    This is the Acctax list with source table hyperlinked.

    """
    model = Acctax
    queryset = Acctax.objects.all()
    serializer_class = AcctaxSerializer 
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer,CSVRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filter_class = AcctaxFilter
    search_fields =('acode','sname','scientificnameauthorship','kingdom','phylum','taxclass','taxorder','family','genus','species','subspecies','variety','forma',
                    'elcode','gelcode','iunccode','g_rank','s_rank','nativity','source')
    ordering_fields = ('acode','sname','scientificnameauthorship','kingdom','phylum','taxclass','taxorder','family','genus','species','subspecies','variety','forma',
                    'elcode','gelcode','iunccode','g_rank','s_rank','nativity','source')

class ComtaxViewSet(viewsets.ModelViewSet):
    """
    This is the Comtaxlist with source table hyperlinked.

    """
    model = Comtax
    queryset = Comtax.objects.all()
    #serializer_class = serializers.HyperlinkedModelSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)

class SyntaxViewSet(viewsets.ModelViewSet):
    """
    This is the Comtaxlist with source table hyperlinked.

    """
    model = Syntax
    queryset = Syntax.objects.all()
    #serializer_class = serializers.HyperlinkedModelSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,JSONPRenderer,XMLRenderer,YAMLRenderer)
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)

#class LuSourceViewSet(viewsets.ModelViewSet):
#    model = LuSource
#    queryset = LuSource.objects.all() #.using('purple').all()
#    serializer_class = LuSourceSerializer
