# $Id: cabextract.spec,v 1.1 2004/02/26 12:32:02 thias Exp $

Summary: A program to extract Microsoft Cabinet files.
Name: cabextract
Version: 0.6
Release: 3.fr
Group: Applications/Archiving
License: GPL
Source: http://www.kyz.uklinux.net/downloads/%{name}-%{version}.tar.gz
URL: http://www.kyz.uklinux.net/cabextract.php3
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Cabinet (.CAB) files are a form of archive, which Microsoft use to
distribute their software, and things like Windows Font Packs. The
cabextract program simply unpacks such files.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.6-3.fr
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Tue Jan  7 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

