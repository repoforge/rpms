# $Id$
# Authority: matthias
# Dist: nodist

Summary: Sound files for the Asterisk PBX and telephony application and toolkit
Name: asterisk-sounds
Version: 1.2.1
Release: 5%{?dist}
License: BSD
Group: Applications/Internet
URL: http://www.asterisk.org/
Source: http://ftp.digium.com/pub/asterisk/asterisk-sounds-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: asterisk >= 1.2.15
BuildArch: noarch

%description
Asterisk is an Open Source PBX and telephony development platform that
can both replace a conventional PBX and act as a platform for developing
custom telephony applications for delivering dynamic content over a
telephone similarly to how one can deliver dynamic content through a
web browser using CGI and a web server.

Asterisk talks to a variety of telephony hardware including BRI, PRI,
POTS, and IP telephony clients using the Inter-Asterisk eXchange
protocol (e.g. gnophone or miniphone).

This package contains freely usable recorded sounds that were meant to be
used with Asterisk.


%prep
%setup


%build


%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_PREFIX=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(0644, root, root, 0755)
%doc README.txt sounds-extra.txt
%{_var}/lib/asterisk/sounds/
# Exclude files already present in the main asterisk package (conflict)
%exclude %{_var}/lib/asterisk/sounds/conf-hasleft.gsm
%exclude %{_var}/lib/asterisk/sounds/conf-leaderhasleft.gsm
%exclude %{_var}/lib/asterisk/sounds/conf-placeintoconf.gsm
%exclude %{_var}/lib/asterisk/sounds/conf-thereare.gsm
%exclude %{_var}/lib/asterisk/sounds/conf-userswilljoin.gsm
%exclude %{_var}/lib/asterisk/sounds/conf-userwilljoin.gsm
%exclude %{_var}/lib/asterisk/sounds/conf-waitforleader.gsm
%exclude %{_var}/lib/asterisk/sounds/invalid.gsm
%exclude %{_var}/lib/asterisk/sounds/minutes.gsm
%exclude %{_var}/lib/asterisk/sounds/seconds.gsm
%exclude %{_var}/lib/asterisk/sounds/letters/
%exclude %{_var}/lib/asterisk/sounds/silence/


%changelog
* Mon Feb 12 2007 Matthias Saou <http://freshrpms.net/> 1.2.1-5
- Exclude "silence" (only numbers), which are included in asterisk 1.2.15.

* Fri Nov 24 2006 Matthias Saou <http://freshrpms.net/> 1.2.1-4
- Exclude seconds.gsm, minutes.gsm which are included in asterisk 1.2.13.

* Thu Mar  9 2006 Matthias Saou <http://freshrpms.net/> 1.2.1-3
- Exclude some more sounds that are part of asterisk 1.2.5, so require that.

* Fri Jan 27 2006 Matthias Saou <http://freshrpms.net/> 1.2.1-2
- Update to 1.2.1.
- Exclude letters from sounds (they're also in the main asterisk package).

* Fri Nov 25 2005 Matthias Saou <http://freshrpms.net/> 1.2.0-1
- Update to 1.2.0.
- Update list of excluded conflicting sounds (+conf-hasleft, +conf-thereare).

* Tue Aug 23 2005 Matthias Saou <http://freshrpms.net/> 1.0.9-1
- Update to 1.0.9.

* Tue Apr  5 2005 Matthias Saou <http://freshrpms.net/> 1.0.7-1
- Update to 1.0.7.

* Wed Feb  2 2005 Matthias Saou <http://freshrpms.net/> 1.0.1-1
- Minor cleanups.

* Mon Oct 18 2004 Matthias Saou <http://freshrpms.net/> 1.0.1-0
- Update to 1.0.1.

* Thu Aug 26 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.RC2.0
- Update to 1.0-RC2.

* Mon Jul 26 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.RC1.1
- Initial RPM release.

