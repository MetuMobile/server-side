from flask.views import MethodView
from flask import jsonify

from Config import Config


class Root(MethodView):
    def get(self, bookletId):
        if bookletId==None:
            return jsonify(Booklets=self.getBooklets())
        else:
            return jsonify(Booklet=self.getBooklets()[bookletId])

    def getBooklets(self):
        bookletRecords = []
        counter = 0
        for record in self._getBookletData():
            try:
                record.append(counter)
                recordDict = self._recordToDict(record)
                bookletRecords.append(recordDict)
            except:
                pass
            counter += 1
        return bookletRecords

    def _recordToDict(self, record):
        dict = {}
        dict['img'] = Config.serverRootLink +"/images/" + record[0]
        dict['tr_title'] = record[1]
        dict['tr_url'] = record[2]
        dict['en_title'] = record[3]
        dict['en_url'] = record[4]
        dict['id'] = record[5]
        return dict

    def _getBookletData(self):
        return [
            ["defaultbookletpicture.jpg", "ÇEVRE TELEFON REHBERİ","http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/CEVRE-TELEFON-REHBERI-TR.pdf", "PHONE GUIDE","http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/CEVRE-TELEFON-REHBERI-ENG.pdf"],
            ["food.jpg", "MERKEZ KAFETERYA VE KANTİNLER","http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/KAFETERYA-TR.pdf", "MAIN CAFETERIA AND CANTEENS", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/KAFETERYA-ENG.pdf"],
            ["health.jpg", "SAĞLIK MERKEZİ","http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/SAGLIK-MERKEZI-TR.pdf", "HEALTH CENTRE", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/09/SAGLIK-MERKEZI-ENG.pdf"],
            ["sports.jpg", "SPOR TESİSLERİ","http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/SPOR-MERKEZI-TR.pdf", "SPORTS AND RECREATION", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/SPOR-MERKEZI-ENG.pdf"],
            ["kkm.jpg", "KÜLTÜR VE KONGRE MERKEZİ","http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/KULTUR-VE-KONGRE-MERKEZI-TR.pdf", "CULTURE AND CONVENTION CENTER", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/KULTUR-VE-KONGRE-MERKEZI-ENG.pdf"],
            ["library.jpg", "KÜTÜPHANE","http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/KUTUPHANE-TR.pdf", "LIBRARY", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/KUTUPHANE-ENG.pdf"],
            ["dorm.jpg", "YURTLAR","http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/YURTLAR-TR.pdf", "DORMITORIES", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/YURTLAR-ENG.pdf"],
            ["academicbuildings.jpg", "AKADEMİK BLOKLAR","http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/AKADEMIK-BLOKLAR-TR.pdf", "ACADEMIC BLOCKS", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/AKADEMIK-BLOKLAR-ENG.pdf"],
            ["technical services.jpg", "TEKNİK HİZMETLER","http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/TEKNIK-HIZMETLER-KILAVUZU-TR.pdf", "TECHNICAL SERVICES GUIDE", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/TEKNIK-HIZMETLER-KILAVUZU-ENG.pdf"],
            ["it.jpg", "BİLİŞİM TEKNİKLERİ","http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/BILISIM-TEKNIKLERI-KILAVUZU-1-TR.pdf", "TECHNICAL GUIDE FOR IT SERVICES 1", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/BILISIM-TEKNIKLERI-KILAVUZU-1-ENG.pdf"],
            ["it.jpg", "BİLİŞİM TEKNİKLERİ-2","http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/BILISIM-TEKNIKLERI-KILAVUZU-2-TR.pdf", "TECHNICAL GUIDE FOR IT SERVICES 2", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/BILISIM-TEKNIKLERI-KILAVUZU-2-ENG.pdf"],
            ["administrativeservices.jpg", "İDARİ HİZMET VE KURALLAR","http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/IDARI-HIZMET-VE-KURALLAR-1-TR.pdf", "ADMINISTRATIVE SERVICES AND RULES 1", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/IDARI-HIZMET-VE-KURALLAR-1-ENG.pdf"],
            ["administrativeservices.jpg", "İDARİ HİZMET VE KURALLAR-2","http://intranet.ncc.metu.edu.tr/wp-content/uploads/2015/09/IDARI-HIZMET-VE-KURALLAR-2-TR.pdf", "ADMINISTRATIVE SERVICES AND RULES 2", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2015/09/IDARI-HIZMET-VE-KURALLAR-2-ENG.pdf"],
            ["administrativeservices.jpg", "İDARİ HİZMET VE KURALLAR-3","http://intranet.ncc.metu.edu.tr/wp-content/uploads/2015/10/IDARI-HIZMET-VE-KURALLAR-3-TR.pdf", "ADMINISTRATIVE SERVICES AND RULES 3", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2015/10/IDARI-HIZMET-VE-KURALLAR-3-ENG.pdf"],
            ["guest.jpg", "MİSAFİRHANE", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2015/09/MISAFIRHANE-TR.pdf", "GUEST HOUSE", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2015/09/MISAFIRHANE-ENG.pdf"],
            ["defaultbookletpicture.jpg", "YEŞİL KAMPUS", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/YESIL-KAMPUS-TR.pdf", "GREEN CAMPUS", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/YESIL-KAMPUS-ENG.pdf"],
            ["defaultbookletpicture.jpg", "TRAFİK KURALLARI", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2015/09/TRAFIK-KURALLARI-TR-.pdf", "TRAFFIC REGULATIONS", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2015/09/TRAFIK-KURALLARI-ENG.pdf"],
            ["defaultbookletpicture.jpg", "İS SAGLIĞI VE GÜVENLİĞİ", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/IS-SAGLIGI-VE-GUVENLIGI-TR.pdf", "OCCUPATIONAL HEALTH AND SAFETY", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/08/IS-SAGLIGI-VE-GUVENLIGI-ENG.pdf"],
            ["technical services.jpg", "1. YURT TEKNİK KILAVUZU", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2015/09/1-YURT-TEKNIK-KILAVUZU-TR.pdf", "TECHNICAL GUIDELINES DORM I", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2015/09/1-YURT-TEKNIK-KILAVUZU-ENG.pdf"],
            ["technical services.jpg", "2. YURT TEKNİK KILAVUZU", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2015/09/2-YURT-TEKNIK-KILAVUZU-TR.pdf", "TECHNICAL GUIDELINES DORM II", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2015/09/2-YURT-TEKNIK-KILAVUZU-ENG.pdf"],
            ["technical services.jpg", "3. YURT TEKNİK KILAVUZU", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2015/09/3-YURT-TEKNIK-KILAVUZU-TR.pdf", "TECHNICAL GUIDELINES DORM III", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2015/09/3-YURT-TEKNIK-KILAVUZU-ENG.pdf"],
            ["defaultbookletpicture.jpg", "ÖĞRENCİ GELİŞİM VE PSİKOLOJİK DANIŞMA MERKEZİ", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/09/OGRENCI-GEL-VE-PSI-DANIS-MRK-TR-1.pdf", "STUDENT DEVELOPMENT AND COUNSELING CENTER", "http://intranet.ncc.metu.edu.tr/wp-content/uploads/2016/09/OGRENCI-GEL-VE-PSI-DANIS-MRK-ENG-.pdf"]
        ]