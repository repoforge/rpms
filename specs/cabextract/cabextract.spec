# $Id$
# Authority: matthias
# Upstream: Stuart Caie <kyzer$4u,net>

Summary: Program to extract Microsoft Cabinet files
Name: cabextract
Version: 1.3
Release: 1%{?dist}
License: GPL
Group: Applications/Archiving
URL:  http://www.cabextract.org.uk/

Source: http://www.cabextract.org.uk/cabextract-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Cabinet (.CAB) files are a form of archive, which Microsoft use to
distribute their software, and things like Windows Font Packs. The
cabextract program simply unpacks such files.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README
%doc %{_mandir}/man1/cabextract.1*
%{_bindir}/cabextract

%changelog
* Sat Jul 24 2010 Dag Wieers <dag@wieers.com> - 1.3-1
- Updated to release 1.3.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Updated to release 1.2.

* Mon Oct 18 2004 Matthias Saou <http://freshrpms.net/> 1.1-1
- Update to 1.1.

* Mon Mar 15 2004 Matthias Saou <http://freshrpms.net/> 1.0-1
- Update to 1.0.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.6-3
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Tue Jan  7 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

