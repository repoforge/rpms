# $Id$

Summary: GnuPG Made Easy.
Name: gpgme
Version: 0.3.15
Release: 4.fr
License: GPL
Group: Applications/System
Source: ftp://ftp.gnupg.org/gcrypt/alpha/gpgme/gpgme-%{version}.tar.gz
URL: http://www.gnupg.org/gpgme.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Obsoletes: libgpgme <= 0.3.15
Provides: libgpgme = %{version}-%{release}
Requires: gnupg >= 1.2.0
BuildRequires: gnupg >= 1.2.0, info

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG easier
for applications. It provides a High-Level Crypto API for encryption,
decryption, signing, signature verification and key management. Currently it
uses GnuPG as its backend but the API isn't restricted to this engine


%package devel
Summary: Static libraries and header files from GPGME, GnuPG Made Easy.
Group: Development/Libraries
Requires: %{name} = %{version}
Provides: libgpgme-devel = %{version}-%{release}

%description devel
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG easier
for applications. It provides a High-Level Crypto API for encryption,
decryption, signing, signature verification and key management. Currently it
uses GnuPG as its backend but the API isn't restricted to this engine

Static libraries and header files from GPGME, GnuPG Made Easy.


%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall
rm -f %{buildroot}%{_infodir}/dir || :

%clean
rm -rf %{buildroot}

%post devel
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir

%preun devel
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir
fi

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_bindir}/%{name}-config
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_datadir}/aclocal/%{name}.m4
%{_infodir}/%{name}.info*

%changelog
* Mon Nov 17 2003 Matthias Saou <http://freshrpms.net/> 0.3.15-4.fr
- Exclude the dir info file.
- Added scriplets for info file install.

* Wed Nov 12 2003 Matthias Saou <http://freshrpms.net/> 0.3.15-3.fr
- Added missing gnupg build requirement.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.3.15-2.fr
- Revert to latest semi-stable for now.
- Rebuild for Fedora Core 1.

* Thu Aug 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.0 (as 0.4.1 and 0.4.2 require libgpg-error).
- Added provides and obsoletes for libgpgme.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.15.
- Exclude .la files.
- Rebuilt for Red Hat Linux 9.

* Tue Feb  4 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.14.

* Sun Sep 29 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.11.
- Rebuilt against Red Hat Linux 8.0.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Mon Apr 22 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.5.

* Wed Sep 19 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.2.3.

* Thu Aug 30 2001 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

