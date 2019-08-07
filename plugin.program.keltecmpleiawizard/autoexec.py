# encoded by pyprotecao
# http://keltecmp.tk/pyprotecao

import base64, codecs
magic = 'IyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKIyAgICAgIENvcHlyaWdodCAoQykgMjAxNSBTdXJmYWNpbmd4L05hTiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgVGhpcyBQcm9ncmFtIGlzIGZyZWUgc29mdHdhcmU7IHlvdSBjYW4gcmVkaXN0cmlidXRlIGl0IGFuZC9vciBtb2RpZnkgICAgICAgICMKIyAgaXQgdW5kZXIgdGhlIHRlcm1zIG9mIHRoZSBHTlUgR2VuZXJhbCBQdWJsaWMgTGljZW5zZSBhcyBwdWJsaXNoZWQgYnkgICAgICAgICMKIyAgdGhlIEZyZWUgU29mdHdhcmUgRm91bmRhdGlvbjsgZWl0aGVyIHZlcnNpb24gMiwgb3IgKGF0IHlvdXIgb3B0aW9uKSAgICAgICAgICMKIyAgYW55IGxhdGVyIHZlcnNpb24uICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgVGhpcyBQcm9ncmFtIGlzIGRpc3RyaWJ1dGVkIGluIHRoZSBob3BlIHRoYXQgaXQgd2lsbCBiZSB1c2VmdWwsICAgICAgICAgICAgICMKIyAgYnV0IFdJVEhPVVQgQU5ZIFdBUlJBTlRZOyB3aXRob3V0IGV2ZW4gdGhlIGltcGxpZWQgd2FycmFudHkgb2YgICAgICAgICAgICAgICMKIyAgTUVSQ0hBTlRBQklMSVRZIG9yIEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFLiBTZWUgdGhlICAgICAgICAgICAgICAgICMKIyAgR05VIEdlbmVyYWwgUHVibGljIExpY2Vuc2UgZm9yIG1vcmUgZGV0YWlscy4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgWW91IHNob3VsZCBoYXZlIHJlY2VpdmVkIGEgY29weSBvZiB0aGUgR05VIEdlbmVyYWwgUHVibGljIExpY2Vuc2UgICAgICAgICAgICMKIyAgYWxvbmcgd2l0aCBYQk1DOyBzZWUgdGhlIGZpbGUgQ09QWUlORy4gIElmIG5vdCwgd3JpdGUgdG8gICAgICAgICAgICAgICAgICAgICMKIyAgdGhlIEZyZWUgU29mdHdhcmUgRm91bmRhdGlvbiwgNjc1IE1hc3MgQXZlLCBDYW1icmlkZ2UsIE1BIDAyMTM5LCBVU0EuICAgICAgICMKIyAgaHR0cDovL3d3dy5nbnUub3JnL2NvcHlsZWZ0L2dwbC5odG1sICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKIyBDcmVkaXRzIAojIC0tLS0tLS0tLS0KIyBUb2JpYXMgVXNzaW5nIEFuZCBIZW5yaWsgTW9zZ2FhcmQgSmVuc2VuIGZvciBwYXJzZURPTQojIFdoaXRlQ3JlYW0gdGhyZWFkIGZvciBjbGlja2luZyB5ZXMgb24gZGlhbG9nIGZvciB1bmtub3duIHNvdXJjZXMKCmltcG9ydCB4Ym1jLCB4Ym1jdmZzLCB4Ym1jYWRkb24sIHhibWNndWkscmUsIG9zLCBnbG9iLCB0aHJlYWQKZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUKdHJ5OiAgICBmcm9tIHNxbGl0ZTMgaW1wb3J0IGRiYXBpMiBhcyBkYXRhYmFzZQpleGNlcHQ6IGZyb20gcHlzcWxpdGUyIGltcG9ydCBkYmFwaTIgYXMgZGF0YWJhc2UKCmRlZiBtYWluKCk6CgljbGFzcyBlbmFibGVBbGwoKToKCQlkZWYgX19pbml0X18oc2VsZik6CgkJCXNlbGYuZGF0YWJhc2VwYXRoID0geGJtYy50cmFuc2xhdGVQYXRoKCdzcGVjaWFsOi8vZGF0YWJhc2UvJykKCQkJc2VsZi5hZGRvbnMgICAgICAgPSB4Ym1jLnRyYW5zbGF0ZVBhdGgoJ3NwZWNpYWw6Ly9ob21lL2FkZG9ucy8nKQoJCQlzZWxmLmRiZmlsZW5hbWUgICA9IHNlbGYubGF0ZXN0REIoKQoJCQlzZWxmLmRiZmlsZW5hbWUgICA9IG9zLnBhdGguam9pbihzZWxmLmRhdGFiYXNlcGF0aCwgc2VsZi5kYmZpbGVuYW1lKQoJCQlzZWxmLnN3YXBVUygpCgkJCWlmIG5vdCBvcy5wYXRoLmV4aXN0cyhvcy5wYXRoLmpvaW4oc2VsZi5kYXRhYmFzZXBhdGgsIHNlbGYuZGJmaWxlbmFtZSkpOgoJCQkJeGJtY2d1aS5EaWFsb2coKS5ub3RpZmljYXRpb24oIkF1dG9FeGVjLnB5IiwgIk5vIEFkZG9uczI3LmRiIGZpbGUiKQoJCQkJc2VsZi5sb2coIkRCIEZpbGUgbm9'
love = '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'
god = 'JVRykKCQkKCQlkZWYgZGlhbG9nV2F0Y2goc2VsZik6CgkJCXggPSAwCgkJCXdoaWxlIG5vdCB4Ym1jLmdldENvbmRWaXNpYmlsaXR5KCJXaW5kb3cuaXNWaXNpYmxlKHllc25vZGlhbG9nKSIpIGFuZCB4IDwgMTAwOgoJCQkJeCArPSAxCgkJCQl4Ym1jLnNsZWVwKDEwMCkKCQkJCgkJCWlmIHhibWMuZ2V0Q29uZFZpc2liaWxpdHkoIldpbmRvdy5pc1Zpc2libGUoeWVzbm9kaWFsb2cpIik6CgkJCQl4Ym1jLmV4ZWN1dGVidWlsdGluKCdTZW5kQ2xpY2soMTEpJykKCQkKCQlkZWYgYWRkb25EYXRhYmFzZShzZWxmLCBhZGRvbj1Ob25lLCBzdGF0ZT0xLCBhcnJheT1GYWxzZSk6CgkJCWluc3RhbGxlZHRpbWUgPSBzdHIoZGF0ZXRpbWUubm93KCkpWzotN10KCQkJaWYgb3MucGF0aC5leGlzdHMoc2VsZi5kYmZpbGVuYW1lKToKCQkJCXRyeToKCQkJCQl0ZXh0ZGIgPSBkYXRhYmFzZS5jb25uZWN0KHNlbGYuZGJmaWxlbmFtZSkKCQkJCQl0ZXh0ZXhlID0gdGV4dGRiLmN1cnNvcigpCgkJCQlleGNlcHQgRXhjZXB0aW9uLCBlOgoJCQkJCXNlbGYubG9nKCJEQiBDb25uZWN0aW9uIEVycm9yOiAlcyIgJSBzdHIoZSksIHhibWMuTE9HRVJST1IpCgkJCQkJcmV0dXJuIEZhbHNlCgkJCWVsc2U6IHJldHVybiBGYWxzZQoJCQl0cnk6CgkJCQlpZiBhcnJheSA9PSBGYWxzZToKCQkJCQl0ZXh0ZXhlLmV4ZWN1dGUoJ0lOU0VSVCBvciBJR05PUkUgaW50byBpbnN0YWxsZWQgKGFkZG9uSUQgLCBlbmFibGVkLCBpbnN0YWxsRGF0ZSkgVkFMVUVTICg/LD8sPyknLCAoYWRkb24sIHN0YXRlLCBpbnN0YWxsZWR0aW1lLCkpCgkJCQkJdGV4dGV4ZS5leGVjdXRlKCdVUERBVEUgaW5zdGFsbGVkIFNFVCBlbmFibGVkID0gPyBXSEVSRSBhZGRvbklEID0gPyAnLCAoc3RhdGUsIGFkZG9uLCkpCgkJCQllbHNlOgoJCQkJCWZvciBpdGVtIGluIGFkZG9uOgoJCQkJCQl0ZXh0ZXhlLmV4ZWN1dGUoJ0lOU0VSVCBvciBJR05PUkUgaW50byBpbnN0YWxsZWQgKGFkZG9uSUQgLCBlbmFibGVkLCBpbnN0YWxsRGF0ZSkgVkFMVUVTICg/LD8sPyknLCAoaXRlbSwgc3RhdGUsIGluc3RhbGxlZHRpbWUsKSkKCQkJCQkJdGV4dGV4ZS5leGVjdXRlKCdVUERBVEUgaW5zdGFsbGVkIFNFVCBlbmFibGVkID0gPyBXSEVSRSBhZGRvbklEID0gPyAnLCAoc3RhdGUsIGl0ZW0sKSkKCQkJCXRleHRkYi5jb21taXQoKQoJCQkJdGV4dGV4ZS5jbG9zZSgpCgkJCWV4Y2VwdCBFeGNlcHRpb24sIGU6CgkJCQlzZWxmLmxvZygiRXJyb3JpbmcgZW5hYmxpbmcgYWRkb246ICVzIiAlIGFkZG9uLCB4Ym1jLkxPR0VSUk9SKQoJCgl0cnk6CgkJeGJtY2d1aS5EaWFsb2coKS5ub3RpZmljYXRpb24oIkF1dG9FeGVjLnB5IiwgIlN0YXJ0aW5nIFNjcmlwdC4uLiIpCgkJZmlyc3RSdW4gPSBlbmFibGVBbGwoKQoJCXhibWNndWkuRGlhbG9nKCkubm90aWZpY2F0aW9uKCJBdXRvRXhlYy5weSIsICJBbGwgQWRkb25zIEVuYWJsZWQiKQoJCXhibWN2ZnMuZGVsZXRlKCdzcGVjaWFsOi8vdXNlcmRhdGEvYXV0b2V4ZWMucHknKQoJZXhjZXB0IEV4Y2VwdGlvbiwgZToKCQl4Ym1jZ3VpLkRpYWxvZygpLm5vdGlmaWNhdGlvbigiQXV0b0V4ZWMucHkiLCAiRXJyb3IgQ2hlY2sgTG9nRmlsZSIpCgkJeGJtYy5sb2coc3RyKGUpLCB4Ym1jLkxPR0VSUk9SKQoJCXhibWN2ZnMuZGVsZXRlKCdzcGVjaWFsOi8vdXNlcmRhdGEvYXV0b2V4ZWMucHknKQoKZGVmIHBhcnNlRE9NKGh0bWwsIG5hbWU9dSIiLCBhdHRycz17fSwgcmV0PUZhbHNlKToKCSMgQ29weXJpZ2h0IChDKSAyMDEwLTIwMTEgVG9iaWFzIFVzc2luZyBBbmQgSGVucmlrIE1vc2dhYXJkIEplbnNlbgoJaWYgaXNpbnN0YW5jZShodG1sLCBzdHIpOgoJCXRyeToKCQkJaHRtbCA9IFtodG1sLmRlY29kZSgidXRmLTgiKV0KCQlleGNlcHQ6CgkJCWh0bWwgPSBbaHRtbF0KCWVsaWYgaXNpbnN0YW5jZShodG1sLCB1bmljb2RlKToKCQlodG1sID0gW2h0bWxdCgllbGlmIG5vdCBpc2luc3RhbmNlKGh0bWwsIGxpc3QpOgoJCXJldHVybiB1IiIKCglpZiBub3QgbmFtZS5zdHJpcCgpOgoJCXJldHVybiB1IiIKCglyZXRfbHN0ID0gW10KCWZvciBpdGVtIGluIGh0bWw6CgkJdGVtcF9pdGVtID0gcmUuY29tcGlsZSgnKDxbXj5dKj9cbltePl0qPz4pJykuZmluZGFsbChpdGVtKQoJCWZvciBtYXRjaCBpbiB0ZW1wX2l0ZW06CgkJCWl0ZW0gPSBpdGVtLnJlcGxhY2UobWF0Y2gsIG1hdGNoLnJlcGxhY2UoIlxuIiwgIiAiKSkKCgkJbHN0ID0gW10KCQlmb3Iga2V5IGluIGF0dHJzOgoJCQlsc3QyID0gcmUuY29tcGlsZSgnKDwnICsgbmFtZSArICdbXj5dKj8oPzonI'
destiny = 'Pftn2I5VPftWm1oKPpvKFptXlOuqUElp1geMKyqVPftW1gpWlWqYvb/CvxcWljtpzHhGFO8VUWyYyZcYzMcozEuoTjbnKEyoFxXPDxWnJLtoTIhXTkmqQVcVQ09VQNtLJ5xVTS0qUWmJ2gyrI0hMzyhMPtvVPVcVQ09VP0kBtbWPDxWoUA0ZvN9VUWyYzAioKOcoTHbWlt8WlNeVT5uoJHtXlNaJ14+KFb/XQ86WlNeVTgyrFNeVPp9WlNeVTS0qUWmJ2gyrI0tXlNaYvb/CvxcWljtpzHhGFO8VUWyYyZcYzMcozEuoTjbnKEyoFxXPtxWPJyzVTkyovufp3DcVQ09VQN6PtxWPDyfp3DtCFOfp3DlPtxWPDyfp3DlVQ0tJ10XPDxWMJkmMGbXPDxWPKEyp3DtCFOlLJ5aMFufMJ4boUA0XFxXPDxWPKEyp3DhpzI2MKWmMFtcPtxWPDyzo3VtnFOcovO0MKA0BtbWPDxWPJyzVT5iqPOfp3EonI0tnJ4toUA0ZwbXPDxWPDxWMTIfXTkmqSgcKFxXPtxWnJLtoTIhXTkmqPxtCG0tZPOuozDtLKE0paZtCG0tr306PtxWPJkmqPN9VUWyYzAioKOcoTHbWlt8WlNeVT5uoJHtXlNaCvxaYPOlMF5AVUjtpzHhHlxhMzyhMTSfoPucqTIgXDbWPDycMvOfMJ4boUA0XFN9CFNjBtbWPDxWoUA0VQ0tpzHhL29gpTyfMFtaXQjaVPftozSgMFNeVPptYvb/CvxaYPOlMF5AVUjtpzHhHlxhMzyhMTSfoPucqTIgXDbXPDycMvOcp2yhp3EuozAyXUWyqPjtp3ElXGbXPDxWoUA0ZvN9VSgqPtxWPJMipvOgLKEwnPOcovOfp3D6PtxWPDyuqUElK2kmqPN9VUWyYzAioKOcoTHbWmjaVPftozSgMFNeVPphXw8aVPftpzI0VPftWm0bJ1jaVy0hJ14+KFb/J1jaVy0cCvpfVUWyYx0tsPOlMF5GXF5znJ5xLJkfXT1uqTAbXDbWPDxWnJLtoTIhXTS0qUWsoUA0XFN9CFNjBtbWPDxWPJS0qUWsoUA0VQ0tpzHhL29gpTyfMFtaCPptXlOhLJ1yVPftWl4dClptXlOlMKDtXlNaCFthJ14+KFb/XG4aYPOlMF5AVUjtpzHhHlxhMzyhMTSfoPugLKEwnPxXPDxWPJMipvO0oKNtnJ4tLKE0py9fp3D6PtxWPDxWL29hqS9wnTSlVQ0tqT1jJmOqPtxWPDxWnJLtL29hqS9wnTSlVTyhVPVaKPVvBtbWPDxWPDycMvO0oKNhMzyhMPtaCFptXlOwo250K2AbLKVfVUEgpP5znJ5xXTAioaEsL2uupvjtZFxcVQ4tYGR6PtxWPDxWPDy0oKNtCFO0oKOoBaEgpP5znJ5xXPp9WlNeVTAioaEsL2uupvjtqT1jYzMcozDbL29hqS9wnTSlYPNkXFyqPtbWPDxWPDycMvO0oKNhpzMcozDbL29hqS9wnTSlYPNkXFN+VP0kBtbWPDxWPDxWqT1jVQ0tqT1jJmR6qT1jYaWznJ5xXTAioaEsL2uupvyqPtxWPDxWMJkmMGbXPDxWPDxWnJLtqT1jYzMcozDbVvNvXFN+VQN6PtxWPDxWPDy0oKNtCFO0oKOoBaEgpP5znJ5xXPVtVvyqPtxWPDxWPJIfnJLtqT1jYzMcozDbVv8vXFN+VQN6PtxWPDxWPDy0oKNtCFO0oKOoBaEgpP5znJ5xXPViVvyqPtxWPDxWPJIfnJLtqT1jYzMcozDbVw4vXFN+VQN6PtxWPDxWPDy0oKNtCFO0oKOoBaEgpP5znJ5xXPV+VvyqPtbWPDxWPJkmqQVhLKOjMJ5xXUEgpP5mqUWcpPtcXDbWPDyfp3DtCFOfp3DlPtxWMJkmMGbXPDxWoUA0ZvN9VSgqPtxWPJMipvOgLKEwnPOcovOfp3D6PtxWPDyyozEmqUVtCFO1VwjiVvNeVT5uoJHXPtxWPDymqTSlqPN9VTy0MJ0hMzyhMPugLKEwnPxXPDxWPJIhMPN9VTy0MJ0hMzyhMPuyozEmqUVfVUA0LKW0XDbWPDxWpT9mVQ0tnKEyoF5znJ5xXPV8VvNeVT5uoJHfVUA0LKW0VPftZFNcPtbWPDxWq2ucoTHtpT9mVQjtMJ5xVTShMPOjo3ZtVG0tYGR6PtxWPDxWqTIhMPN9VTy0MJ0hMzyhMPuyozEmqUVfVTIhMPNeVTkyovuyozEmqUVcXDbWPDxWPJyzVUEyozDtVG0tYGR6PtxWPDxWPJIhMPN9VUEyozDXPDxWPDyjo3ZtCFOcqTIgYzMcozDbVwjvVPftozSgMFjtpT9mVPftZFxXPtxWPDycMvOmqTSlqPN9CFNgZFOuozDtMJ5xVQ09VP0kBtbWPDxWPKEyoKNtCFO1VvVXPDxWPJIfnJLtp3EupaDtCvNgZFOuozDtMJ5xVQ4tYGR6PtxWPDxWqTIgpPN9VTy0MJ1op3EupaDtXlOfMJ4boJS0L2tcBzIhMS0XPDxWPJIfnJLtMJ5xVQ4tYGR6PtxWPDxWqTIgpPN9VTy0MJ1oBzIhMS0XPDxWPJIfnJLtp3EupaDtCvNgZGbXPDxWPDy0MJ1jVQ0tnKEyoIgmqTSlqPNeVTkyovugLKEwnPx6KDbXPDxWPJyzVUWyqQbXPDxWPDyyozEmqUVtCFOcqTIgJ2IhMQccqTIgYzMcozDbVw4vYPOcqTIgYzMcozDbMJ5xp3ElXFxtXlNkKDbWPDxWPKEyoKNtCFOgLKEwnPNeVUEyoKNtXlOyozEmqUVXPtxWPDycqTIgVQ0tnKEyoIgcqTIgYzMcozDbqTIgpPjtnKEyoF5znJ5xXT1uqTAbXFxtXlOfMJ4bqTIgpPx6KDbWPDxWoUA0Zv5upUOyozDbqTIgpPxXPDxWoUA0VQ0toUA0ZtbWPKWyqS9fp3DtXm0toUA0PtbWpzI0qKWhVUWyqS9fp3DXPDccMvOsK25uoJIsKlN9CFNaK19gLJyhK18aBtbWoJScovtc'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))