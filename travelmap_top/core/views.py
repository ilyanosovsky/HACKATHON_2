from django.shortcuts import render
from rest_framework import generics
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Country
from .serializers import CountrySerializer
from django.http import JsonResponse
from .utils import bulk_insert_countries

# Create your views here.
class CountryAPIList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
#     # permission_classes = (IsAuthenticatedOrReadOnly, )

class CountryAPIUpdate(generics.UpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
#     # permission_classes = (IsOwnerOrReadOnly, )

class CountryAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
#     # permission_classes = (IsAdminOrReadOnly, )

def countries(self, request):
    if request.method == 'GET':
        queryset = Country.objects.all()
        serializer = CountrySerializer(queryset, many=True)
        serialized_data = serializer.data
        return JsonResponse(serialized_data, safe=False)
        
class HomePageView(ListView):
    template_name = 'core/home.html'
    model = Country
    context_object_name = 'countries'

    def get_queryset(self):
        return Country.objects.order_by('name')

# def bulk_insert(request):
#     country_names = [{"name":"Afghanistan", "png":"https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Flag_of_the_Taliban.svg/320px-Flag_of_the_Taliban.svg.png"},{"name":"Albania","png":"https://flagcdn.com/w320/al.png"},{"name":"Algeria","png":"https://flagcdn.com/w320/dz.png"},{"name":"American Samoa","png":"https://flagcdn.com/w320/as.png"},{"name":"Andorra","png":"https://flagcdn.com/w320/ad.png"},{"name":"Angola","png":"https://flagcdn.com/w320/ao.png"},{"name":"Anguilla","png":"https://flagcdn.com/w320/ai.png"},{"name":"Antigua and Barbuda","png":"https://flagcdn.com/w320/ag.png"},{"name":"Argentina","png":"https://flagcdn.com/w320/ar.png"},{"name":"Armenia","png":"https://flagcdn.com/w320/am.png"},{"name":"Aruba","png":"https://flagcdn.com/w320/aw.png"},{"name":"Australia","png":"https://flagcdn.com/w320/au.png"},{"name":"Austria","png":"https://flagcdn.com/w320/at.png"},{"name":"Azerbaijan","png":"https://flagcdn.com/w320/az.png"},{"name":"Bahamas","png":"https://flagcdn.com/w320/bs.png"},{"name":"Bahrain","png":"https://flagcdn.com/w320/bh.png"},{"name":"Bangladesh","png":"https://flagcdn.com/w320/bd.png"},{"name":"Barbados","png":"https://flagcdn.com/w320/bb.png"},{"name":"Belarus","png":"https://flagcdn.com/w320/by.png"},{"name":"Belgium","png":"https://flagcdn.com/w320/be.png"},{"name":"Belize","png":"https://flagcdn.com/w320/bz.png"},{"name":"Benin","png":"https://flagcdn.com/w320/bj.png"},{"name":"Bermuda","png":"https://flagcdn.com/w320/bm.png"},{"name":"Bhutan","png":"https://flagcdn.com/w320/bt.png"},{"name":"Bolivia","png":"https://flagcdn.com/w320/bo.png"},{"name":"Bosnia and Herzegovina","png":"https://flagcdn.com/w320/ba.png"},{"name":"Botswana","png":"https://flagcdn.com/w320/bw.png"},{"name":"Bouvet Island","png":"https://flagcdn.com/w320/bv.png"},{"name":"Brazil","png":"https://flagcdn.com/w320/br.png"},{"name":"British Indian Ocean Territory","png":"https://flagcdn.com/w320/io.png"},{"name":"British Virgin Islands","png":"https://flagcdn.com/w320/vg.png"},{"name":"Brunei","png":"https://flagcdn.com/w320/bn.png"},{"name":"Bulgaria","png":"https://flagcdn.com/w320/bg.png"},{"name":"Burkina Faso","png":"https://flagcdn.com/w320/bf.png"},{"name":"Burundi","png":"https://flagcdn.com/w320/bi.png"},{"name":"Cambodia","png":"https://flagcdn.com/w320/kh.png"},{"name":"Cameroon","png":"https://flagcdn.com/w320/cm.png"},{"name":"Canada","png":"https://flagcdn.com/w320/ca.png"},{"name":"Cape Verde","png":"https://flagcdn.com/w320/cv.png"},{"name":"Caribbean Netherlands","png":"https://flagcdn.com/w320/bq.png"},{"name":"Cayman Islands","png":"https://flagcdn.com/w320/ky.png"},{"name":"Central African Republic","png":"https://flagcdn.com/w320/cf.png"},{"name":"Chad","png":"https://flagcdn.com/w320/td.png"},{"name":"Chile","png":"https://flagcdn.com/w320/cl.png"},{"name":"China","png":"https://flagcdn.com/w320/cn.png"},{"name":"Christmas Island","png":"https://flagcdn.com/w320/cx.png"},{"name":"Cocos (Keeling) Islands","png":"https://flagcdn.com/w320/cc.png"},{"name":"Colombia","png":"https://flagcdn.com/w320/co.png"},{"name":"Comoros","png":"https://flagcdn.com/w320/km.png"},{"name":"Cook Islands","png":"https://flagcdn.com/w320/ck.png"},{"name":"Costa Rica","png":"https://flagcdn.com/w320/cr.png"},{"name":"Croatia","png":"https://flagcdn.com/w320/hr.png"},{"name":"Cuba","png":"https://flagcdn.com/w320/cu.png"},{"name":"Curaçao","png":"https://flagcdn.com/w320/cw.png"},{"name":"Cyprus","png":"https://flagcdn.com/w320/cy.png"},{"name":"Czechia","png":"https://flagcdn.com/w320/cz.png"},{"name":"Denmark","png":"https://flagcdn.com/w320/dk.png"},{"name":"Djibouti","png":"https://flagcdn.com/w320/dj.png"},{"name":"Dominica","png":"https://flagcdn.com/w320/dm.png"},{"name":"Dominican Republic","png":"https://flagcdn.com/w320/do.png"},{"name":"DR Congo","png":"https://flagcdn.com/w320/cd.png"},{"name":"Ecuador","png":"https://flagcdn.com/w320/ec.png"},{"name":"Egypt","png":"https://flagcdn.com/w320/eg.png"},{"name":"El Salvador","png":"https://flagcdn.com/w320/sv.png"},{"name":"Equatorial Guinea","png":"https://flagcdn.com/w320/gq.png"},{"name":"Eritrea","png":"https://flagcdn.com/w320/er.png"},{"name":"Estonia","png":"https://flagcdn.com/w320/ee.png"},{"name":"Eswatini","png":"https://flagcdn.com/w320/sz.png"},{"name":"Ethiopia","png":"https://flagcdn.com/w320/et.png"},{"name":"Falkland Islands","png":"https://flagcdn.com/w320/fk.png"},{"name":"Faroe Islands","png":"https://flagcdn.com/w320/fo.png"},{"name":"Fiji","png":"https://flagcdn.com/w320/fj.png"},{"name":"Finland","png":"https://flagcdn.com/w320/fi.png"},{"name":"France","png":"https://flagcdn.com/w320/fr.png"},{"name":"French Guiana","png":"https://flagcdn.com/w320/gf.png"},{"name":"French Polynesia","png":"https://flagcdn.com/w320/pf.png"},{"name":"French Southern and Antarctic Lands","png":"https://flagcdn.com/w320/tf.png"},{"name":"Gabon","png":"https://flagcdn.com/w320/ga.png"},{"name":"Gambia","png":"https://flagcdn.com/w320/gm.png"},{"name":"Georgia","png":"https://flagcdn.com/w320/ge.png"},{"name":"Germany","png":"https://flagcdn.com/w320/de.png"},{"name":"Ghana","png":"https://flagcdn.com/w320/gh.png"},{"name":"Gibraltar","png":"https://flagcdn.com/w320/gi.png"},{"name":"Greece","png":"https://flagcdn.com/w320/gr.png"},{"name":"Greenland","png":"https://flagcdn.com/w320/gl.png"},{"name":"Grenada","png":"https://flagcdn.com/w320/gd.png"},{"name":"Guadeloupe","png":"https://flagcdn.com/w320/gp.png"},{"name":"Guam","png":"https://flagcdn.com/w320/gu.png"},{"name":"Guatemala","png":"https://flagcdn.com/w320/gt.png"},{"name":"Guernsey","png":"https://flagcdn.com/w320/gg.png"},{"name":"Guinea","png":"https://flagcdn.com/w320/gn.png"},{"name":"Guinea-Bissau","png":"https://flagcdn.com/w320/gw.png"},{"name":"Guyana","png":"https://flagcdn.com/w320/gy.png"},{"name":"Haiti","png":"https://flagcdn.com/w320/ht.png"},{"name":"Honduras","png":"https://flagcdn.com/w320/hn.png"},{"name":"Hong Kong","png":"https://flagcdn.com/w320/hk.png"},{"name":"Hungary","png":"https://flagcdn.com/w320/hu.png"},{"name":"Iceland","png":"https://flagcdn.com/w320/is.png"},{"name":"India","png":"https://flagcdn.com/w320/in.png"},{"name":"Indonesia","png":"https://flagcdn.com/w320/id.png"},{"name":"Iran","png":"https://flagcdn.com/w320/ir.png"},{"name":"Iraq","png":"https://flagcdn.com/w320/iq.png"},{"name":"Ireland","png":"https://flagcdn.com/w320/ie.png"},{"name":"Isle of Man","png":"https://flagcdn.com/w320/im.png"},{"name":"Israel","png":"https://flagcdn.com/w320/il.png"},{"name":"Italy","png":"https://flagcdn.com/w320/it.png"},{"name":"Ivory Coast","png":"https://flagcdn.com/w320/ci.png"},{"name":"Jamaica","png":"https://flagcdn.com/w320/jm.png"},{"name":"Japan","png":"https://flagcdn.com/w320/jp.png"},{"name":"Jersey","png":"https://flagcdn.com/w320/je.png"},{"name":"Jordan","png":"https://flagcdn.com/w320/jo.png"},{"name":"Kazakhstan","png":"https://flagcdn.com/w320/kz.png"},{"name":"Kenya","png":"https://flagcdn.com/w320/ke.png"},{"name":"Kiribati","png":"https://flagcdn.com/w320/ki.png"},{"name":"Kosovo","png":"https://flagcdn.com/w320/xk.png"},{"name":"Kuwait","png":"https://flagcdn.com/w320/kw.png"},{"name":"Kyrgyzstan","png":"https://flagcdn.com/w320/kg.png"},{"name":"Laos","png":"https://flagcdn.com/w320/la.png"},{"name":"Latvia","png":"https://flagcdn.com/w320/lv.png"},{"name":"Lebanon","png":"https://flagcdn.com/w320/lb.png"},{"name":"Lesotho","png":"https://flagcdn.com/w320/ls.png"},{"name":"Liberia","png":"https://flagcdn.com/w320/lr.png"},{"name":"Libya","png":"https://flagcdn.com/w320/ly.png"},{"name":"Liechtenstein","png":"https://flagcdn.com/w320/li.png"},{"name":"Lithuania","png":"https://flagcdn.com/w320/lt.png"},{"name":"Luxembourg","png":"https://flagcdn.com/w320/lu.png"},{"name":"Macau","png":"https://flagcdn.com/w320/mo.png"},{"name":"Madagascar","png":"https://flagcdn.com/w320/mg.png"},{"name":"Malawi","png":"https://flagcdn.com/w320/mw.png"},{"name":"Malaysia","png":"https://flagcdn.com/w320/my.png"},{"name":"Maldives","png":"https://flagcdn.com/w320/mv.png"},{"name":"Mali","png":"https://flagcdn.com/w320/ml.png"},{"name":"Malta","png":"https://flagcdn.com/w320/mt.png"},{"name":"Marshall Islands","png":"https://flagcdn.com/w320/mh.png"},{"name":"Martinique","png":"https://flagcdn.com/w320/mq.png"},{"name":"Mauritania","png":"https://flagcdn.com/w320/mr.png"},{"name":"Mauritius","png":"https://flagcdn.com/w320/mu.png"},{"name":"Mayotte","png":"https://flagcdn.com/w320/yt.png"},{"name":"Mexico","png":"https://flagcdn.com/w320/mx.png"},{"name":"Micronesia","png":"https://flagcdn.com/w320/fm.png"},{"name":"Moldova","png":"https://flagcdn.com/w320/md.png"},{"name":"Monaco","png":"https://flagcdn.com/w320/mc.png"},{"name":"Mongolia","png":"https://flagcdn.com/w320/mn.png"},{"name":"Montenegro","png":"https://flagcdn.com/w320/me.png"},{"name":"Montserrat","png":"https://flagcdn.com/w320/ms.png"},{"name":"Morocco","png":"https://flagcdn.com/w320/ma.png"},{"name":"Mozambique","png":"https://flagcdn.com/w320/mz.png"},{"name":"Myanmar","png":"https://flagcdn.com/w320/mm.png"},{"name":"Namibia","png":"https://flagcdn.com/w320/na.png"},{"name":"Nauru","png":"https://flagcdn.com/w320/nr.png"},{"name":"Nepal","png":"https://flagcdn.com/w320/np.png"},{"name":"Netherlands","png":"https://flagcdn.com/w320/nl.png"},{"name":"New Caledonia","png":"https://flagcdn.com/w320/nc.png"},{"name":"New Zealand","png":"https://flagcdn.com/w320/nz.png"},{"name":"Nicaragua","png":"https://flagcdn.com/w320/ni.png"},{"name":"Niger","png":"https://flagcdn.com/w320/ne.png"},{"name":"Nigeria","png":"https://flagcdn.com/w320/ng.png"},{"name":"Niue","png":"https://flagcdn.com/w320/nu.png"},{"name":"Norfolk Island","png":"https://flagcdn.com/w320/nf.png"},{"name":"North Korea","png":"https://flagcdn.com/w320/kp.png"},{"name":"North Macedonia","png":"https://flagcdn.com/w320/mk.png"},{"name":"Northern Mariana Islands","png":"https://flagcdn.com/w320/mp.png"},{"name":"Norway","png":"https://flagcdn.com/w320/no.png"},{"name":"Oman","png":"https://flagcdn.com/w320/om.png"},{"name":"Pakistan","png":"https://flagcdn.com/w320/pk.png"},{"name":"Palau","png":"https://flagcdn.com/w320/pw.png"},{"name":"Palestine","png":"https://flagcdn.com/w320/ps.png"},{"name":"Panama","png":"https://flagcdn.com/w320/pa.png"},{"name":"Papua New Guinea","png":"https://flagcdn.com/w320/pg.png"},{"name":"Paraguay","png":"https://flagcdn.com/w320/py.png"},{"name":"Peru","png":"https://flagcdn.com/w320/pe.png"},{"name":"Philippines","png":"https://flagcdn.com/w320/ph.png"},{"name":"Pitcairn Islands","png":"https://flagcdn.com/w320/pn.png"},{"name":"Poland","png":"https://flagcdn.com/w320/pl.png"},{"name":"Portugal","png":"https://flagcdn.com/w320/pt.png"},{"name":"Puerto Rico","png":"https://flagcdn.com/w320/pr.png"},{"name":"Qatar","png":"https://flagcdn.com/w320/qa.png"},{"name":"Republic of the Congo","png":"https://flagcdn.com/w320/cg.png"},{"name":"Romania","png":"https://flagcdn.com/w320/ro.png"},{"name":"Russia","png":"https://flagcdn.com/w320/ru.png"},{"name":"Rwanda","png":"https://flagcdn.com/w320/rw.png"},{"name":"Réunion","png":"https://flagcdn.com/w320/re.png"},{"name":"Saint Barthélemy","png":"https://flagcdn.com/w320/bl.png"},{"name":"Saint Helena, Ascension and Tristan da Cunha","png":"https://flagcdn.com/w320/sh.png"},{"name":"Saint Kitts and Nevis","png":"https://flagcdn.com/w320/kn.png"},{"name":"Saint Lucia","png":"https://flagcdn.com/w320/lc.png"},{"name":"Saint Martin","png":"https://flagcdn.com/w320/mf.png"},{"name":"Saint Pierre and Miquelon","png":"https://flagcdn.com/w320/pm.png"},{"name":"Saint Vincent and the Grenadines","png":"https://flagcdn.com/w320/vc.png"},{"name":"Samoa","png":"https://flagcdn.com/w320/ws.png"},{"name":"San Marino","png":"https://flagcdn.com/w320/sm.png"},{"name":"Saudi Arabia","png":"https://flagcdn.com/w320/sa.png"},{"name":"Senegal","png":"https://flagcdn.com/w320/sn.png"},{"name":"Serbia","png":"https://flagcdn.com/w320/rs.png"},{"name":"Seychelles","png":"https://flagcdn.com/w320/sc.png"},{"name":"Sierra Leone","png":"https://flagcdn.com/w320/sl.png"},{"name":"Singapore","png":"https://flagcdn.com/w320/sg.png"},{"name":"Sint Maarten","png":"https://flagcdn.com/w320/sx.png"},{"name":"Slovakia","png":"https://flagcdn.com/w320/sk.png"},{"name":"Slovenia","png":"https://flagcdn.com/w320/si.png"},{"name":"Solomon Islands","png":"https://flagcdn.com/w320/sb.png"},{"name":"Somalia","png":"https://flagcdn.com/w320/so.png"},{"name":"South Africa","png":"https://flagcdn.com/w320/za.png"},{"name":"South Georgia","png":"https://flagcdn.com/w320/gs.png"},{"name":"South Korea","png":"https://flagcdn.com/w320/kr.png"},{"name":"South Sudan","png":"https://flagcdn.com/w320/ss.png"},{"name":"Spain","png":"https://flagcdn.com/w320/es.png"},{"name":"Sri Lanka","png":"https://flagcdn.com/w320/lk.png"},{"name":"Sudan","png":"https://flagcdn.com/w320/sd.png"},{"name":"Suriname","png":"https://flagcdn.com/w320/sr.png"},{"name":"Svalbard and Jan Mayen","png":"https://flagcdn.com/w320/sj.png"},{"name":"Sweden","png":"https://flagcdn.com/w320/se.png"},{"name":"Switzerland","png":"https://flagcdn.com/w320/ch.png"},{"name":"Syria","png":"https://flagcdn.com/w320/sy.png"},{"name":"São Tomé and Príncipe","png":"https://flagcdn.com/w320/st.png"},{"name":"Taiwan","png":"https://flagcdn.com/w320/tw.png"},{"name":"Tajikistan","png":"https://flagcdn.com/w320/tj.png"},{"name":"Tanzania","png":"https://flagcdn.com/w320/tz.png"},{"name":"Thailand","png":"https://flagcdn.com/w320/th.png"},{"name":"Timor-Leste","png":"https://flagcdn.com/w320/tl.png"},{"name":"Togo","png":"https://flagcdn.com/w320/tg.png"},{"name":"Tokelau","png":"https://flagcdn.com/w320/tk.png"},{"name":"Tonga","png":"https://flagcdn.com/w320/to.png"},{"name":"Trinidad and Tobago","png":"https://flagcdn.com/w320/tt.png"},{"name":"Tunisia","png":"https://flagcdn.com/w320/tn.png"},{"name":"Turkey","png":"https://flagcdn.com/w320/tr.png"},{"name":"Turkmenistan","png":"https://flagcdn.com/w320/tm.png"},{"name":"Turks and Caicos Islands","png":"https://flagcdn.com/w320/tc.png"},{"name":"Tuvalu","png":"https://flagcdn.com/w320/tv.png"},{"name":"Uganda","png":"https://flagcdn.com/w320/ug.png"},{"name":"Ukraine","png":"https://flagcdn.com/w320/ua.png"},{"name":"United Arab Emirates","png":"https://flagcdn.com/w320/ae.png"},{"name":"United Kingdom","png":"https://flagcdn.com/w320/gb.png"},{"name":"United States","png":"https://flagcdn.com/w320/us.png"},{"name":"United States Minor Outlying Islands","png":"https://flagcdn.com/w320/um.png"},{"name":"United States Virgin Islands","png":"https://flagcdn.com/w320/vi.png"},{"name":"Uruguay","png":"https://flagcdn.com/w320/uy.png"},{"name":"Uzbekistan","png":"https://flagcdn.com/w320/uz.png"},{"name":"Vanuatu","png":"https://flagcdn.com/w320/vu.png"},{"name":"Vatican City","png":"https://flagcdn.com/w320/va.png"},{"name":"Venezuela","png":"https://flagcdn.com/w320/ve.png"},{"name":"Vietnam","png":"https://flagcdn.com/w320/vn.png"},{"name":"Wallis and Futuna","png":"https://flagcdn.com/w320/wf.png"},{"name":"Western Sahara","png":"https://flagcdn.com/w320/eh.png"},{"name":"Yemen","png":"https://flagcdn.com/w320/ye.png"},{"name":"Zambia","png":"https://flagcdn.com/w320/zm.png"},{"name":"Zimbabwe","png":"https://flagcdn.com/w320/zw.png"},{"name":"Åland Islands","png":"https://flagcdn.com/w320/ax.png"}]
#     bulk_insert_countries(country_names)
#     return JsonResponse({'message': 'Done!'}, status=201)