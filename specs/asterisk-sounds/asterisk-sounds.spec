# $Id$
# Authority: matthias

# For pre-versions
%define prever RC1

Summary: Sound files for the Asterisk PBX and telephony application and toolkit
Name: asterisk-sounds
Version: 1.0
Release: %{?prever:0.%{prever}.}1
License: BSD
Group: Applications/Internet
URL: http://www.asterisk.org/
Source: ftp://ftp.asterisk.org/pub/telephony/asterisk/asterisk-sounds-%{version}%{?prever:-%{prever}}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: asterisk

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
%{_localstatedir}/lib/asterisk/sounds


%changelog
* Mon Jul 26 2004 Matthias Saou <http://freshrpms.net> 1.0-0.RC1.1
- Initial RPM release.

