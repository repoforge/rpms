# $Id$
# Authority: matthias
# Dist: nodist

# For pre-versions
#define prever RC2

Summary: Sound files for the Asterisk PBX and telephony application and toolkit
Name: asterisk-sounds
Version: 1.0.1
Release: %{?prever:0.%{prever}.}1
License: BSD
Group: Applications/Internet
URL: http://www.asterisk.org/
Source: ftp://ftp.asterisk.org/pub/asterisk/asterisk-sounds-%{version}%{?prever:-%{prever}}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: asterisk
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
%setup -n asterisk-sounds-%{version}%{?prever:-%{prever}}


%build


%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_PREFIX=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(0644, root, root, 0755)
%doc README.txt sounds-extra.txt
%{_var}/lib/asterisk/sounds


%changelog
* Wed Feb  2 2005 Matthias Saou <http://freshrpms.net> 1.0.1-1
- Minor cleanups.

* Mon Oct 18 2004 Matthias Saou <http://freshrpms.net> 1.0.1-0
- Update to 1.0.1.

* Thu Aug 26 2004 Matthias Saou <http://freshrpms.net> 1.0-0.RC2.0
- Update to 1.0-RC2.

* Mon Jul 26 2004 Matthias Saou <http://freshrpms.net> 1.0-0.RC1.1
- Initial RPM release.

