# $Id$
# Authority: dag
# Upstream: Gavin Brown <jodrell$spod,uk,net>

Summary: Graphical whois client
Name: greenwich
Version: 0.8.1
Release: 1
License: GPL
Group: Applications/System
URL: http://jodrell.net/projects/greenwich/

#Source: http://jodrell.net/download.html?file=/files/greenwich-%{version}.tar.gz
Source: http://jodrell.net/files/greenwich/greenwich-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.00503, gettext
Requires: perl >= 0:5.00503
Requires: Gtk-Perl, perl(IP::Authority), perl(Locale::Maketext)
Requires: perl(ExtUtils::Depends), perl(Gnome2), perl(Gtk2)
AutoReq: no

%description
Greenwich is a graphical whois client for GNOME. It is written in Perl and
makes use of the GNOME bindings for Perl.

Greenwich transparently handles almost all gTLDs, first- and second-level
ccTLDs and whois servers run by private domain registries (like CentralNic).
It can also do lookups against IP addresses.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	mandir="%{buildroot}%{_mandir}/man1"
%{__install} -Dp -m0644 src/redhat-whois.png %{buildroot}%{_datadir}/icons/Bluecurve/greenwich.png

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/Greenwich/
%{_datadir}/gnome/apps/Internet/*.desktop
%{_datadir}/icons/Bluecurve/*.png
%{_datadir}/pixmaps/*.png

%changelog
* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Updated to release 0.8.1.

* Thu Apr 29 2004 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Updated to release 0.7.0.

* Wed Dec 31 2003 Dag Wieers <dag@wieers.com> - 0.6.2-0
- Updated to release 0.6.2.

* Sun Jul 21 2003 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Updated to release 0.6.1.

* Sun Jul 20 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Updated to release 0.6.0.

* Thu Apr 10 2003 Dag Wieers <dag@wieers.com> - 0.5.2-0
- Updated to release 0.5.2.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 0.5.1-0
- Updated to release 0.5.1.

* Sun Jan 19 2003 Dag Wieers <dag@wieers.com> - 0.5.0-0
- Initial package. (using DAR)
