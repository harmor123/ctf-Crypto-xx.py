# -*- coding: utf-8 -*-
# Time: 2023/6/8 21:19
# Editor:harmor

"""
VGhlIGdlb@xvZ#kgb@YgdGhlIEVhcnRoJ#Mgc#VyZmFjZSBpcyBkb@!pbmF)
ZWQgYnkgdGhlIHBhcnRpY#VsYXIgcHJvcGVydGllcyBvZiB#YXRlci$gUHJlc@VudCBvbiBFYXJ)
aCBpbiBzb@xpZCwgbGlxdWlkLCBhbmQgZ@FzZW(!cyBzdGF)ZXMsIHdhdGVyIGlzIGV$Y@VwdGlvbmFsbHkgcmVhY#RpdmUuIEl)
IGRpc#NvbHZlcywgdHJhbnNwb#J)cywgYW%kIHByZWNpcGl)YXRlcyBtYW%%IGNoZW!pY@FsIGNvbXBvdW%
kcyBhbmQgaXMgY@(uc#RhbnRseSBtb@RpZnlpbmcgdGhlIGZhY@Ugb@YgdGhlIEVhcnRoLiBFdmFwb#JhdGVkIGZyb@)
gdGhlIG(jZWFucywgd@F)ZXIgdmFwb#IgZm(ybXMgY@xvdWRzLCBzb@!lIG(mIHdoaWNoIGFyZSB)cmFuc#BvcnRlZCBieSB#aW%
kIG(@ZXIgdGhlIGNvbnRpbmVudHMuIENvbmRlbnNhdGlvbiBmcm(tIHRoZSBjbG(!
ZHMgcHJvdmlkZXMgdGhlIGVzc@VudGlhbCBhZ@VudCBvZiBjb@%)aW%lbnRhbCBlcm(zaW(uOiByYWluLlRoZSByYXRlIGF)
IHdoaWNoIGEgbW(sZWN!bGUgb@Ygd@F)ZXIgcGFzc@VzIHRob#VnaCB)aGUgY#ljbGUgaXMgbm()
IHJhbmRvbQpBbmQgdGhlIGZsYWcgaXM^IENURnsyMi!RV)VSVFlVSU*tUExLSkhHRkRTLUFaWENWQk%NfQ==
"""
import base64
m = 'VGhlIGdlb@xvZ#kgb@YgdGhlIEVhcnRoJ#Mgc#VyZmFjZSBpcyBkb@!pbmF)ZWQgYnkgdGhlIHBhcnRpY#VsYXIgcHJvcGVydGllcyBvZiB#YXRlci$gUHJlc@VudCBvbiBFYXJ)aCBpbiBzb@xpZCwgbGlxdWlkLCBhbmQgZ@FzZW(!cyBzdGF)ZXMsIHdhdGVyIGlzIGV$Y@VwdGlvbmFsbHkgcmVhY#RpdmUuIEl)IGRpc#NvbHZlcywgdHJhbnNwb#J)cywgYW%kIHByZWNpcGl)YXRlcyBtYW%%IGNoZW!pY@FsIGNvbXBvdW%kcyBhbmQgaXMgY@(uc#RhbnRseSBtb@RpZnlpbmcgdGhlIGZhY@Ugb@YgdGhlIEVhcnRoLiBFdmFwb#JhdGVkIGZyb@)gdGhlIG(jZWFucywgd@F)ZXIgdmFwb#IgZm(ybXMgY@xvdWRzLCBzb@!lIG(mIHdoaWNoIGFyZSB)cmFuc#BvcnRlZCBieSB#aW%kIG(@ZXIgdGhlIGNvbnRpbmVudHMuIENvbmRlbnNhdGlvbiBmcm(tIHRoZSBjbG(!ZHMgcHJvdmlkZXMgdGhlIGVzc@VudGlhbCBhZ@VudCBvZiBjb@%)aW%lbnRhbCBlcm(zaW(uOiByYWluLlRoZSByYXRlIGF)IHdoaWNoIGEgbW(sZWN!bGUgb@Ygd@F)ZXIgcGFzc@VzIHRob#VnaCB)aGUgY#ljbGUgaXMgbm()IHJhbmRvbQpBbmQgdGhlIGZsYWcgaXM^IENURnsyMi!RV)VSVFlVSU*tUExLSkhHRkRTLUFaWENWQk%NfQ=='
c = ')!@#$%^&*('
for i in m:
    for j in range(10):
        if i == c[j]:
            m = m.replace(i,str(j))
print(base64.b64decode(m))