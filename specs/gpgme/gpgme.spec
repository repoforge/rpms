# $Id$
# Authority: matthias
# Upstream: <gnupg-devel$gnupg,org>

Summary: GnuPG Made Easy
Name: gpgme
Version: 1.1.6
Release: svn1258
License: GPL
Group: Applications/System
#Source: ftp://ftp.gnupg.org/gcrypt/gpgme/gpgme-%{version}-%{release}.tar.bz2
Source: ftp://ftp.gnupg.ca/alpha/gpgme/gpgme-%{version}-%{release}.tar.bz2
URL: http://www.gnupg.org/related_software/gpgme/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Obsoletes: libgpgme <= 0.3.15
Provides: lib%{name} = %{version}-%{release}
Requires: gnupg >= 1.2.2, libgpg-error >= 0.5
BuildRequires: gnupg >= 1.2.2, libgpg-error-devel >= 0.5, info, gcc-c++

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG easier
for applications. It provides a High-Level Crypto API for encryption,
decryption, signing, signature verification and key management. Currently it
uses GnuPG as its backend but the API isn't restricted to this engine


%package devel
Summary: Static libraries and header files from GPGME, GnuPG Made Easy
Group: Development/Libraries
Requires: %{name} = %{version}
Requires(post): info
Requires(preun): info
Requires: libgpg-error-devel >= 0.5
Provides: lib%{name}-devel = %{version}-%{release}

%description devel
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG easier
for applications. It provides a High-Level Crypto API for encryption,
decryption, signing, signature verification and key management. Currently it
uses GnuPG as its backend but the API isn't restricted to this engine

Static libraries and header files from GPGME, GnuPG Made Easy.


%prep
%setup -n gpgme-%{version}-%{release}


%build
%configure --enable-static
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{_infodir}/dir || :

%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig
chcon -t texrel_shlib_t %{_infodir}/libgpgme.so.11

%postun
/sbin/ldconfig


%post devel
/sbin/install-info %{_infodir}/gpgme.info.gz %{_infodir}/dir

%preun devel
if [ $1 -eq 0 ]; then
    /sbin/install-info --delete %{_infodir}/gpgme.info.gz %{_infodir}/dir
fi


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_libdir}/*.so.*
/usr/share/common-lisp/source/gpgme/*.lisp
/usr/share/common-lisp/source/gpgme/gpgme.asd

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/gpgme-config
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_datadir}/aclocal/gpgme.m4
%{_infodir}/gpgme.info*

%changelog
* Thu Jan 01 2008 Heiko Adams <info-2007@fedora-blog.de> - 1.1.6-svn1258
- Update to 1.1.6-svn1258

* Mon Aug 15 2005 Matthias Saou <http://freshrpms.net/> 1.0.3-1
- Update to 1.0.3.

* Mon Jan  3 2005 Matthias Saou <http://freshrpms.net/> 1.0.2-1
- Update to 1.0.2.
- Re-enable static libs by explicitely requesting them to configure.

* Wed May 19 2004 Matthias Saou <http://freshrpms.net/> 0.4.7-1
- Update to 0.4.7, as libgpg-error is in Fedora Core 2 at last.

* Mon Nov 17 2003 Matthias Saou <http://freshrpms.net/> 0.3.15-4
- Exclude the dir info file.
- Added scriplets for info file install.

* Wed Nov 12 2003 Matthias Saou <http://freshrpms.net/> 0.3.15-3
- Added missing gnupg build requirement.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.3.15-2
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

