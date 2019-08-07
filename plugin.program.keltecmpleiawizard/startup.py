# encoded by pyprotecao
# http://keltecmp.tk/pyprotecao

import base64, codecs
magic = 'IyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwojICAgICAgICAgICAgICAgICAgICAgICAgICAgICAvVCAvSSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAjCiMgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAvIHwvIHwgLi1+LyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgICAgICAgICAgICAgICAgICAgICAgICAgVFwgWSAgSSAgfC8gIC8gIF8gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIwojICAgICAgICAgL1QgICAgICAgICAgICAgICB8IFxJICB8ICBJICBZLi1+LyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAjCiMgICAgICAgIEkgbCAgIC9JICAgICAgIFRcIHwgIHwgIGwgIHwgIFQgIC8gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgICAgVFwgfCAgXCBZIGwgIC9UICAgfCBcSSAgbCAgIFwgYCAgbCBZICAgICAgIElmIHlvdXIgZ29pbmcgdG8gY29weSAgICAgIwojIF9fICB8IFxsICAgXGwgIFxJIGwgX19sICBsICAgXCAgIGAgIF8uIHwgICAgICAgdGhpcyBhZGRvbiBqdXN0ICAgICAgICAgICAjCiMgXCB+LWwgIGBcICAgYFwgIFwgIFwgflwgIFwgICBgLiAuLX4gICB8ICAgICAgICBnaXZlIGNyZWRpdCEgICAgICAgICAgICAgICMKIyAgXCAgIH4tLiAiLS4gIGAgIFwgIF4uXyBeLiAiLS4gIC8gIFwgICB8ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIwojLi0tfi0uXyAgfi0gIGAgIF8gIH4tXy4tIi0uIiAuXyAvLl8gLiIgLi8gICAgICAgIFN0b3AgRGVsZXRpbmcgdGhlICAgICAgICAjCiMgPi0tLiAgfi0uICAgLl8gIH4+LSIgICAgIlwgICA3ICAgNyAgIF0gICAgICAgICAgY3JlZGl0cyBmaWxlISAgICAgICAgICAgICMKI14uX19ffiItLS5fICAgIH4teyAgLi1+IC4gIGBcIFkgLiAvICAgIHwgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIwojIDxfXyB+Ii0uICB+ICAgICAgIC9fLyAgIFwgICBcSSAgWSAgIDogfCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAjCiMgICBeLS5fXyAgICAgICAgICAgfihfLyAgIFwgICA+Ll86ICAgfCBsX19fX19fICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgICAgICBeLS0uLF9fXy4tfiIgIC9fLyAgICEgIGAtLn4iLS1sXyAvICAgICB+Ii0uICAgICAgICAgICAgICAgICAgICAgICAgIwojICAgICAgICAgICAgICAoXy8gLiAgfiggICAvJyAgICAgIn4iLS0sWSAgIC09Yi0uIF8pICAgICAgICAgICAgICAgICAgICAgICAjCiMgICAgICAgICAgICAgICAoXy8gLiAgXCAgOiAgICAgICAgICAgLyBsICAgICAgYyJ+byBcICAgICAgICAgICAgICAgICAgICAgICMKIyAgICAgICAgICAgICAgICBcIC8gICAgYC4gICAgLiAgICAgLl4gICBcXy4tfiJ+LS0uICApICAgICAgICAgICAgICAgICAgICAgIwojICAgICAgICAgICAgICAgICAoXy8gLiAgIGAgIC8gICAgIC8gICAgICAgISAgICAgICApLyAgICAgICAgICAgICAgICAgICAgICAjCiMgICAgICAgICAgICAgICAgICAvIC8gXy4gICAnLiAgIC4nOiAgICAgIC8gICAgICAgICcgICAgICAgICAgICAgICAgICAgICAgICMKIyAgICAgICAgICAgICAgICAgIH4oXy8gLiAgIC8gICAgXyAgYCAgLi08XyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIwojICAgICAgICAgICAgICAgICAgICAvXy8gLiAnIC4tfiIgYC4gIC8gXCAgXCAgICAgICAgICAsej0uICBTdXJmYWNpbmd4ICAgICAjCiMgICAgICAgICAgICAgICAgICAgIH4oIC8gICAnICA6ICAgfCBLICAgIi0ufi0uX19fX19fLy8gICBPcmlnaW5hbCBBdXRob3IgICMKIyAgICAgICAgICAgICAgICAgICAgICAiLSwuICAgIGwgICBJLyBcXyAgICBfX3stLS0+Ll8oPT0uICAgICAgICAgICAgICAgICAgIwojICAgICAgICAgICAgICAgICAgICAgICAvLyggICAgIFwgIDwgICAgfiJ+IiAgICAgLy8gICAgICAgICAgICAgICAgICAgICAgICAjCiMgICAgICAgICAgICAgICAgICAgICAgLycgL1wgICAgIFwgIFwgICAgICx2PS4gICgoICAgICBGaXJlIFRWIEd1cnUgICAgICAgICMKIyAgICAgICAgICAgICAgICAgICAgLl4uIC8gL1wgICAgICIgIH1fXyAvLz09PS0gIGAgICAgUHlYQk1DdCBMYVlPVXQgICAgICAgIwojICAgICAgICAgICAgICAgICAgIC8gLyAnICcgICItLixfXyB7LS0tKD09LSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAjCiMgICAgICAgICAgICAgICAgIC5eICcgICAgICAgOiAgVCAgfiIgICBsbCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgICAgICAgICAgICAgICAvIC4gIC4gIC4gOiB8IDohICAgICAgICBcICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIwojICAgICAgICAgICAgICAgKF8vICAvICAgfCB8IGotIiAgICAgICAgICB+XiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAjCiMgICAgICAgICAgICAgICAgIH4tPF8oXy5eLX4iICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIwojICAgICAgICAgICAgICAgICAgQ29weXJpZ2h0IChDKSBPbmUgb2YgdGhvc2UgWWVhcnMuLi4uICAgICAgICAgICAgICAgICAgICAjCiMgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgVGhpcyBwcm9ncmFtIGlzIGZyZWUgc29mdHdhcmU6IHlvdSBjYW4gcmVkaXN0cmlidXRlIGl0IGFuZC9vciBtb2RpZnkgICAgIwojICBpdCB1bmRlciB0aGUgdGVybXMgb2YgdGhlIEdOVSBHZW5lcmFsIFB1YmxpYyBMaWNlbnNlIGFzIHB1Ymxpc2hlZCBieSAgICAjCiMgIHRoZSBGcmVlIFNvZnR3YXJlIEZvdW5kYXRpb24sIGVpdGhlciB2ZXJzaW9uIDMgb2YgdGhlIExpY2Vuc2UsIG9yICAgICAgICMKIyAgKGF0IHlvdXIgb3B0aW9uKSBhbnkgbGF0ZXIgdmVyc2lvbi4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIwojICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAjCiMgIFRoaXMgcHJvZ3JhbSBpcyBkaXN0cmlidXRlZCBpbiB0aGUgaG9wZSB0aGF0IGl0IHdpbGwgYmUgdXNlZnVsLCAgICAgICAgICMKIyAgYnV0IFdJVEhPVVQgQU5ZIFdBUlJBTlRZOyB3aXRob3V0IGV2ZW4gdGhlIGltcGxpZWQgd2FycmFudHkgb2YgICAgICAgICAgIwojICBNRVJDSEFOVEFCSUxJVFkgb3IgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UuICBTZWUgdGhlICAgICAgICAgICAjCiMgIEdOVSBHZW5lcmFsIFB1YmxpYyBMaWNlbnNlIGZvciBtb3JlIGRldGFpbHMuICAgICAgICAgICAgICAgICAgICAgICAgICAgICMKIyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIwojIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCgppbXBvcnQgeGJtYywgeGJtY2FkZG9uLCB4Ym1jZ3VpLCB4Ym1jcGx1Z2luLCBvcywgc3lzLCB4Ym1jdmZzLCBnbG9iCmltcG9ydCBzaHV0aWwKaW1wb3J0IHVybGxpYjIsdXJsbGliCmltcG9ydCByZQppbXBvcnQgdXNlcnZhcgpmcm9tIGRhdGV0aW1lIGltcG9ydCBkYXRlLCBkYXRldGltZSwgdGltZWRlbHRhCmZyb20gcmVzb3VyY2VzLmxpYnMgaW1wb3J0IGV4dHJhY3QsIGRvd25sb2FkZXIsIG5vdGlmeSwgbG9naW5pdCwgZGVicmlkaXQsIGFsbHVjaXQsIHRyYWt0aXQsIHNraW5Td2l0Y2gsIHVwbG9hZExvZywgd2l6YXJkIGFzIHdpegoKQURET05fSUQgICAgICAgPSB1c2VydmFyLkFERE9OX0lECkFERE9OVElUTEUgICAgID0gdXNlcnZhci5BRERPTlRJVExFCkFERE9OICAgICAgICAgID0gd2l6LmFkZG9uSWQoQURET05fSUQpClZFUlNJT04gICAgICAgID0gd2l6LmFkZG9uSW5mbyhBRERPTl9JRCwndmVyc2lvbicpCkFERE9OUEFUSCAgICAgID0gd2l6LmFkZG9uSW5mbyhBRERPTl9JRCwncGF0aCcpCkFERE9OSUQgICAgICAgID0gd2l6LmFkZG9uSW5mbyhBRERPTl9JRCwnaWQnKQpESUFMT0cgICAgICAgICA9IHhibWNndWkuRGlhbG9nKCkKRFAgICAgICAgICAgICAgPSB4Ym1jZ3VpLkRpYWxvZ1Byb2dyZXNzKCkKSE9NRSAgICAgICAgICAgPSB4Ym1jLnRyYW5zbGF0ZVBhdGgoJ3NwZWNpYWw6Ly9ob21lLycpClBST0ZJTEUgICAgICAgID0geGJtYy50cmFuc2xhdGVQYXRoKCdzcGVjaWFsOi8vcHJvZmlsZS8nKQpLT0RJSE9NRSAgICAgICA9IHhibWMudHJhbnNsYXRlUGF0aCgnc3BlY2lhbDovL3hibWMvJykKQURET05TICAgICAgICAgPSBvcy5wYXRoLmpvaW4oSE9NRSwgICAgICdhZGRvbnMnKQpLT0RJQURET05TICAgICA9IG9zLnBhdGguam9pbihLT0RJSE9NRSwgJ2FkZG9ucycpClVTRVJEQVRBICAgICAgID0gb3MucGF0aC5qb2luKEhPTUUsICAgICAndXNlcmRhdGEnKQpQTFVHSU4gICAgICAgICA9IG9zLnBhdGguam9pbihBRERPTlMsICAgQURET05fSUQpClBBQ0tBR0VTICAgICAgID0gb3MucGF0aC5qb2luKEFERE9OUywgICAncGFja2FnZXMnKQpBRERPTkRBVEEgICAgICA9IG9zLnBhdGguam9pbihVU0VSREFUQSwgJ2FkZG9uX2RhdGEnLCBBRERPTl9JRCkKVEVYVENBQ0hFICAgICAgPSBvcy5wYXRoLmpvaW4oQURET05EQVRBLCAnQ2FjaGUnKQpGQU5BUlQgICAgICAgICA9IG9zLnBhdGguam9pbihBRERPTlBBVEgsJ2ZhbmFydC5qcGcnKQpJQ09OICAgICAgICAgICA9IG9zLnBhdGguam9pbihBRERPTlBBVEgsJ2ljb24ucG5nJykKQVJUICAgICAgICAgICAgPSBvcy5wYXRoLmpvaW4oQURET05QQVRILCdyZXNvdXJjZXMnLCAnYXJ0JykKU0tJTiAgICAgICAgICAgPSB4Ym1jLmdldFNraW5EaXIoKQpUSFVNQlMgICAgICAgICA9IG9zLnBhdGguam9pbihVU0VSREFUQSwgICdUaHVtYm5haWxzJykKQlVJTEROQU1FICAgICAgPSB3aXouZ2V0UygnYnVpbGRuYW1lJykKREVGQVVMVFNLSU4gICAgPSB3aXouZ2V0UygnZGVmYXVsdHNraW4nKQpERUZBVUxUTkFNRSAgICA9IHdpei5nZXRTKCdkZWZhdWx0c2tpbm5hbWUnKQpERUZBVUxUSUdOT1JFICA9IHdpei5nZXRTKCdkZWZhdWx0c2tpbmlnbm9yZScpCkJVSUxEVkVSU0lPTiAgID0gd2l6LmdldFMoJ2J1aWxkdmVyc2lvbicpCkJVSUxETEFURVNUICAgID0gd2l6LmdldFMoJ2xhdGVzdHZlcnNpb24nKQpCVUlMRENIRUNLICAgICA9IHdpei5nZXRTKCdsYXN0YnVpbGRjaGVjaycpCkRJU0FCTEVVUERBVEUgID0gd2l6LmdldFMoJ2Rpc2FibGV1cGRhdGUnKQpBVVRPQ0xFQU5VUCAgICA9IHdpei5nZXRTKCdhdXRvY2xlYW4nKQpBVVRPQ0FDSEUgICAgICA9IHdpei5nZXRTKCdjbGVhcmNhY2hlJykKQVVUT1BBQ0tBR0VTICAgPSB3aXouZ2V0UygnY2xlYXJwYWNrYWdlcycpCkFVVE9USFVNQlMgICAgID0gd2l6LmdldFMoJ2NsZWFydGh1bWJzJykKQVVUT0ZFUSAgICAgICAgPSB3aXouZ2V0UygnYXV0b2NsZWFuZmVxJykKQVVUT05FWFRSVU4gICAgPSB3aXouZ2V0UygnbmV4dGF1dG9jbGVhbnVwJykKVFJBS1RTQVZFICAgICAgPSB3aXouZ2V0UygndHJha3RsYXN0c2F2ZScpClJFQUxTQVZFICAgICAgID0gd2l6LmdldFMoJ2RlYnJpZGxhc3RzYXZlJykKQUxMVUNTQVZFICAgICAgPSB3aXouZ2V0UygnYWxsdWNsYXN0c2F2ZScpCkxPR0lOU0FWRSAgICAgID0gd2l6LmdldFMoJ2xvZ2lubGFzdHNhdmUnKQpLRUVQVFJBS1QgICAgICA9IHdpei5nZXRTKCdrZWVwdHJha3QnKQpLRUVQUkVBTCAgICAg'
love = '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'
god = 'ZGVvKCk6Cgl4Ym1jLnNsZWVwKDEwMDApCgppZiBLT0RJViA+PSAxNzoKCU5PVyA9IGRhdGV0aW1lLm5vdygpCgl0ZW1wID0gd2l6LmdldFMoJ2tvZGkxN2lzY3JhcCcpCglpZiBub3QgdGVtcCA9PSAnJzoKCQlpZiB0ZW1wID4gc3RyKE5PVyAtIHRpbWVkZWx0YShtaW51dGVzPTIpKToKCQkJd2l6LmxvZygiS2lsbGluZyBTdGFydCBVcCBTY3JpcHQiKQoJCQlzeXMuZXhpdCgpCgl3aXoubG9nKCIlcyIgJSAoTk9XKSkKCXdpei5zZXRTKCdrb2RpMTdpc2NyYXAnLCBzdHIoTk9XKSkKCXhibWMuc2xlZXAoMTAwMCkKCWlmIG5vdCB3aXouZ2V0Uygna29kaTE3aXNjcmFwJykgPT0gc3RyKE5PVyk6CgkJd2l6LmxvZygiS2lsbGluZyBTdGFydCBVcCBTY3JpcHQiKQoJCXN5cy5leGl0KCkKCWVsc2U6CgkJd2l6LmxvZygiQ29udGludWluZyBTdGFydCBVcCBTY3JpcHQiKQoKd2l6LmxvZygiW1BhdGggQ2hlY2tdIFN0YXJ0ZWQiLCB4Ym1jLkxPR05PVElDRSkKcGF0aCA9IG9zLnBhdGguc3BsaXQoQURET05QQVRIKQppZiBub3QgQURET05JRCA9PSBwYXRoWzFdOiBESUFMT0cub2soQURET05USVRMRSwgJ1tDT0xPUiAlc11QbGVhc2UgbWFrZSBzdXJlIHRoYXQgdGhlIHBsdWdpbiBmb2xkZXIgaXMgdGhlIHNhbWUgYXMgdGhlIEFERE9OX0lELlsvQ09MT1JdJyAlIENPTE9SMiwgJ1tDT0xPUiAlc11QbHVnaW4gSUQ6Wy9DT0xPUl0gW0NPTE9SICVzXSVzWy9DT0xPUl0nICUgKENPTE9SMiwgQ09MT1IxLCBBRERPTklEKSwgJ1tDT0xPUiAlc11QbHVnaW4gRm9sZGVyOlsvQ09MT1JdIFtDT0xPUiAlc10lc1svQ09MT1JdJyAlIChDT0xPUjIsIENPTE9SMSwgcGF0aCkpOyB3aXoubG9nKCJbUGF0aCBDaGVja10gQURET05fSUQgYW5kIHBsdWdpbiBmb2xkZXIgZG9lc250IG1hdGNoLiAlcyAvICVzICIgJSAoQURET05JRCwgcGF0aCkpCmVsc2U6IHdpei5sb2coIltQYXRoIENoZWNrXSBHb29kISIsIHhibWMuTE9HTk9USUNFKQoKaWYgS09ESUFERE9OUyBpbiBBRERPTlBBVEg6Cgl3aXoubG9nKCJDb3B5aW5nIHBhdGggdG8gYWRkb25zIGRpciIsIHhibWMuTE9HTk9USUNFKQoJaWYgbm90IG9zLnBhdGguZXhpc3RzKEFERE9OUyk6IG9zLm1ha2VkaXJzKEFERE9OUykKCW5ld3BhdGggPSB4Ym1jLnRyYW5zbGF0ZVBhdGgob3MucGF0aC5qb2luKCdzcGVjaWFsOi8vaG9tZS9hZGRvbnMvJywgQURET05JRCkpCglpZiBvcy5wYXRoLmV4aXN0cyhuZXdwYXRoKToKCQl3aXoubG9nKCJGb2xkZXIgYWxyZWFkeSBleGlzdHMsIGNsZWFuaW5nIEhvdXNlIiwgeGJtYy5MT0dOT1RJQ0UpCgkJd2l6LmNsZWFuSG91c2UobmV3cGF0aCkKCQl3aXoucmVtb3ZlRm9sZGVyKG5ld3BhdGgpCgl0cnk6CgkJd2l6LmNvcHl0cmVlKEFERE9OUEFUSCwgbmV3cGF0aCkKCWV4Y2VwdCBFeGNlcHRpb24sIGU6CgkJcGFzcwoJd2l6LmZvcmNlVXBkYXRlKFRydWUpCgp0cnk6CglteWJ1aWxkcyA9IHhibWMudHJhbnNsYXRlUGF0aChNWUJVSUxEUykKCWlmIG5vdCBvcy5wYXRoLmV4aXN0cyhteWJ1aWxkcyk6IHhibWN2ZnMubWtkaXJzKG15YnVpbGRzKQpleGNlcHQ6CglwYXNzCgp3aXoubG9nKCJbQXV0byBJbnN0YWxsIFJlcG9dIFN0YXJ0ZWQiLCB4Ym1jLkxPR05PVElDRSkKaWYgQVVUT0lOU1RBTEwgPT0gJ1llcycgYW5kIG5vdCBvcy5wYXRoLmV4aXN0cyhvcy5wYXRoLmpvaW4oQURET05TLCBSRVBPSUQpKToKCXdvcmtpbmd4bWwgPSB3aXoud29ya2luZ1VSTChSRVBPQURET05YTUwpCglpZiB3b3JraW5neG1sID09IFRydWU6CgkJdmVyID0gd2l6LnBhcnNlRE9NKHdpei5vcGVuVVJMKFJFUE9BRERPTlhNTCksICdhZGRvbicsIHJldD0ndmVyc2lvbicsIGF0dHJzID0geydpZCc6IFJFUE9JRH0pCgkJaWYgbGVuKHZlcikgPiAwOgoJCQlpbnN0YWxsemlwID0gJyVzLSVzLnppcCcgJSAoUkVQT0lELCB2ZXJbMF0pCgkJCXdvcmtpbmdyZXBvID0gd2l6LndvcmtpbmdVUkwoUkVQT1pJUFVSTCtpbnN0YWxsemlwKQoJCQlpZiB3b3JraW5ncmVwbyA9PSBUcnVlOgoJCQkJRFAuY3JlYXRlKEFERE9OVElUTEUsJ0Rvd25sb2FkaW5nIFJlcG8uLi4nLCcnLCAnUGxlYXNlIFdhaXQnKQoJCQkJaWYgbm90IG9zLnBhdGguZXhpc3RzKFBBQ0tBR0VTKTogb3MubWFrZWRpcnMoUEFDS0FHRVMpCgkJCQlsaWI9b3MucGF0aC5qb2luKFBBQ0tBR0VTLCBpbnN0YWxsemlwKQoJCQkJdHJ5OiBvcy5yZW1vdmUobGliKQoJCQkJZXhjZXB0OiBwYXNzCgkJCQlkb3dubG9hZGVyLmRvd25sb2FkKFJFUE9aSVBVUkwraW5zdGFsbHppcCxsaWIsIERQKQoJCQkJZXh0cmFjdC5hbGwobGliLCBBRERPTlMsIERQKQoJCQkJdHJ5OgoJCQkJCWYgPSBvcGVuKG9zLnBhdGguam9pbihBRERPTlMsIFJFUE9JRCwgJ2FkZG9uLnhtbCcpLCBtb2RlPSdyJyk7IGcgPSBmLnJlYWQoKTsgZi5jbG9zZSgpCgkJCQkJbmFtZSA9IHdpei5wYXJzZURPTShnLCAnYWRkb24nLCByZXQ9J25hbWUnLCBhdHRycyA9IHsnaWQnOiBSRVBPSUR9KQoJCQkJCXdpei5Mb2dOb3RpZnkoIltDT0xPUiAlc10lc1svQ09MT1JdIiAlIChDT0xPUjEsIG5hbWVbMF0pLCAiW0NPTE9SICVzXUFkZC1vbiB1cGRhdGVkWy9DT0xPUl0iICUgQ09MT1IyLCBpY29uPW9zLnBhdGguam9pbihBRERPTlMsIFJFUE9JRCwgJ2ljb24ucG5nJykpCgkJCQlleGNlcHQ6CgkJCQkJcGFzcwoJCQkJaWYgS09ESVYgPj0gMTc6IHdpei5hZGRvbkRhdGFiYXNlKFJFUE9JRCwgMSkKCQkJCURQLmNsb3NlKCkKCQkJCXhibWMuc2xlZXAoNTAwKQoJCQkJd2l6LmZvcmNlVXBkYXRlKFRydWUpCgkJCQl3aXoubG9nKCJbQXV0byBJbnN0YWxsIFJlcG9dIFN1Y2Nlc3NmdWxseSBJbnN0YWxsZWQiLCB4Ym1jLkxPR05PVElDRSkKCQkJZWxzZTogCgkJCQl3aXouTG9nTm90aWZ5KCJbQ09MT1IgJXNdUmVwbyBJbnN0YWxsIEVycm9yWy9DT0xPUl0iICUgQ09MT1IxLCAiW0NPTE9SICVzXUludmFsaWQgdXJsIGZvciB6aXAhWy9DT0xPUl0iICUgQ09MT1IyKQoJCQkJd2l6LmxvZygiW0F1dG8gSW5zdGFsbCBSZXBvXSBXYXMgdW5hYmxlIHRvIGNyZWF0ZSBhIHdvcmtpbmcgdXJsIGZvciByZXBvc2l0b3J5LiAlcyIgJSB3b3JraW5ncmVwbywgeGJtYy5MT0dFUlJPUikKCQllbHNlOgoJCQl3aXoubG9nKCJJbnZhbGlkIFVSTCBmb3IgUmVwbyBaaXAiLCB4Ym1jLkxPR0VSUk9SKQoJZWxzZTogCgkJd2l6LkxvZ05vdGlmeSgiW0NPTE9SICVzXVJlcG8gSW5zdGFsbCBFcnJvclsvQ09MT1JdIiAlIENPTE9SMSwgIltDT0xPUiAlc11JbnZhbGlkIGFkZG9uLnhtbCBmaWxlIVsvQ09MT1JdIiAlIENPTE9SMikKCQl3aXoubG9nKCJbQXV0byBJbnN0YWxsIFJlcG9dIFVuYWJsZSB0byByZWFkIHRoZSBhZGRvbi54bWwgZmlsZS4iLCB4Ym1jLkxPR0VSUk9SKQplbGlmIG5vdCBBVVRPSU5TVEFMTCA9PSAnWWVzJzogd2l6LmxvZygiW0F1dG8gSW5zdGFsbCBSZXBvXSBOb3QgRW5hYmxlZCIsIHhibWMuTE9HTk9USUNFKQplbGlmIG9zLnBhdGguZXhpc3RzKG9zLnBhdGguam9pbihBRERPTlMsIFJFUE9JRCkpOiB3aXoubG9nKCJbQXV0byBJbnN0YWxsIFJlcG9dIFJlcG9zaXRvcnkgYWxyZWFkeSBpbnN0YWxsZWQiKQoKd2l6LmxvZygiW0F1dG8gVXBkYXRlIFdpemFyZF0gU3RhcnRlZCIsIHhibWMuTE9HTk9USUNFKQppZiBBVVRPVVBEQVRFID09ICdZZXMnOgoJd2l6LndpemFyZFVwZGF0ZSgnc3RhcnR1cCcpCmVsc2U6IHdpei5sb2coIltBdXRvIFVwZGF0ZSBXaXphcmRdIE5vdCBFbmFibGVkIiwgeGJtYy5MT0dOT1RJQ0UpCgp3aXoubG9nKCJbTm90aWZpY2F0aW9uc10gU3RhcnRlZCIsIHhibWMuTE9HTk9USUNFKQppZiBFTkFCTEUgPT0gJ1llcyc6CglpZiBub3QgTk9USUZZID09ICd0cnVlJzoKCQl1cmwgPSB3aXoud29ya2luZ1VSTChOT1RJRklDQVRJT04pCgkJaWYgdXJsID09IFRydWU6CgkJCWlkLCBtc2cgPSB3aXouc3BsaXROb3RpZnkoTk9USUZJQ0FUSU9OKQoJCQlpZiBub3QgaWQgPT0gRmFsc2U6CgkJCQl0cnk6CgkJCQkJaWQgPSBpbnQoaWQpOyBOT1RFSUQgPSBpbnQoTk9URUlEKQoJCQkJCWlmIGlkID09IE5PVEVJRDoKCQkJCQkJaWYgTk9URURJU01JU1MgPT0gJ2ZhbHNlJzoKCQkJCQkJCW5vdGlmeS5ub3RpZmljYXRpb24obXNnKQoJCQkJCQllbHNlOiB3aXoubG9nKCJbTm90aWZpY2F0aW9uc10gaWRbJXNdIERpc21pc3NlZCIgJSBpbnQoaWQpLCB4Ym1jLkxPR05PVElDRSkKCQkJCQllbGlmIGlkID4gTk9URUlEOgoJCQkJCQl3aXoubG9nKCJbTm90aWZpY2F0aW9uc10gaWQ6ICVzIiAlIHN0cihpZCksIHhibWMuTE9HTk9USUNFKQoJCQkJCQl3aXouc2V0Uygnbm90ZWlkJywgc3RyKGlkKSkKCQkJCQkJd2l6LnNldFMoJ25vdGVkaXNtaXNzJywgJ2ZhbHNlJykKCQkJCQkJbm90aWZ5Lm5vdGlmaWNhdGlvbihtc2c9bXNnKQoJCQkJCQl3aXoubG9nKCJbTm90aWZpY2F0aW9uc10gQ29tcGxldGUiLCB4Ym1jLkxPR05PVElDRSkKCQkJCWV4Y2VwdCBFeGNlcHRpb24sIGU6CgkJCQkJd2l6LmxvZygiRXJyb3Igb24gTm90aWZpY2F0aW9ucyBXaW5kb3c6ICVzIiAlIHN0cihlKSwgeGJtYy5MT0dFUlJPUikKCQkJZWxzZTogd2l6LmxvZygiW05vdGlmaWNhdGlvbnNdIFRleHQgRmlsZSBub3QgZm9ybWF0ZWQgQ29ycmVjdGx5IikKCQllbHNlOiB3aXoubG9nKCJbTm90aWZpY2F0aW9uc10gVVJMKCVzKTogJXMiICUgKE5PVElGSUNBVElPTiwgdXJsKSwgeGJtYy5MT0dOT1RJQ0UpCgllbHNlOiB3aXoubG9nKCJbTm90aWZpY2F0aW9uc10gVHVybmVkIE9mZiIsIHhibWMuTE9HTk9USUNFKQplbHNlOiB3aXoubG9nKCJbTm90aWZpY2F0aW9uc10gTm90IEVuYWJsZWQiLCB4Ym1jLkxPR05PVElDRSkKCndpei5sb2coIltJbnN0YWxsZWQgQ2hlY2tdIFN0YXJ0ZWQiLCB4Ym1jLkxPR05PVElDRSkKaWYgSU5TVEFMTEVEID09ICd0cnVlJzoKCWlmIEtPRElWID49IDE3OgoJCXdpei5rb2RpMTdGaXgoKQoJCWlmIFNLSU4gaW4gWydza2luLmNvbmZsdWVuY2UnLCAnc2tpbi5lc3R1YXJ5J106CgkJCWNoZWNrU2tpbigpCgkJRkFJTEVEID0gVHJ1ZQoJZWxpZiBub3QgRVhUUkFDVCA9PSAnMTAwJyBhbmQgbm90IEJVSUxETkFNRSA9PSAiIjoKCQl3aXoubG9nKCJbSW5zdGFsbGVkIENoZWNrXSBCdWlsZCB3YXMgZXh0cmFjdGVkICVzLzEwMCB3aXRoIFtFUlJPUlM6ICVzXSIgJSAoRVhUUkFDVCwgRVhURVJST1IpLCB4Ym1jLkxPR05PVElDRSkKCQl5ZXM9RElBTE9HLnllc25vKEFERE9OVElUTEUsICdbQ09MT1IgJXNdJXNbL0NPTE9SXSBbQ09MT1IgJXNdd2FzIG5vdCBpbnN0YWxsZWQgY29ycmVjdGx5IScgJSAoQ09MT1IxLCBDT0xPUjIsIEJVSUxETkFNRSksICdJbnN0YWxsZWQ6IFtDT0xPUiAlc10lc1svQ09MT1JdIC8gRXJyb3IgQ291bnQ6IFtDT0xPUiAlc10lc1svQ09MT1JdJyAlIChDT0xPUjEsIEVYVFJBQ1QsIENPTE9SMSwgRVhURVJST1IpLCAnV291bGQgeW91IGxpa2UgdG8gdHJ5IGFnYWluP1svQ09MT1JdJywgbm9sYWJlbD0nW0JdTm8gVGhhbmtzIVsvQl0nLCB5ZXNsYWJlbD0nW0JdUmV0cnkgSW5zdGFsbFsvQl0nKQoJCXdpei5jbGVhclMoJ2J1aWxkJykKCQlGQUlMRUQgPSBUcnVlCgkJaWYgeWVzOiAKCQkJd2l6LmViaSgiUGxheU1lZGlhKHBsdWdpbjovLyVzLz9tb2RlPWluc3RhbGwmbmFtZT0lcyZ1cmw9ZnJlc2gpIiAlIChBRERPTl9JRCwgdXJsbGliLnF1b3RlX3BsdXMoQlVJTEROQU1FKSkpCgkJCXdpei5sb2coIltJbnN0YWxsZWQgQ2hlY2tdIEZyZXNoIEluc3RhbGwgUmUtYWN0aXZhdGVkIiwgeGJtYy5MT0dOT1RJQ0UpCgkJZWxzZTogd2l6LmxvZygiW0luc3RhbGxlZCBDaGVja10gUmVpbnN0YWxsIElnbm9yZWQiKQoJZWxpZiBTS0lOIGluIFsnc2tpbi5jb25mbHVlbmNlJywgJ3NraW4uZXN0dWFyeSddOgoJCXdpei5sb2coIltJbnN0YWxsZWQgQ2hlY2tdIEluY29ycmVjdCBza2lu'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))