# $Id$
# Authority: atrpms
# Upstream: <gnupg-devel@gnupg.org>

# Distcc: 0

Summary: GnuPG Made Easy
Name: gpgme
Version: 0.4.3
Release: 1
License: GPL
Group: Applications/System
URL: http://www.gnupg.org/gpgme.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.gnupg.org/GnuPG/alpha/gpgme/gpgme-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: libgpgme <= 0.4.0
Requires: gnupg >= 1.0.6

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications. It provides a High-Level Crypto API for
encryption, decryption, signing, signature verification and key
management.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_infodir}/dir \
		%{buildroot}%{_libdir}/*.la

%post devel
/sbin/install-info --info-dir="%{_infodir}" %{_infodir}/%{name}.info.gz

%preun devel
if [ $1 -eq 0 ]; then
	/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%doc %{_infodir}/*
%{_bindir}/*
#%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*.h
%{_datadir}/aclocal/*.m4

%changelog
* Tue Apr 06 2004 Dag Wieers <dag@wieers.com> - 0.4.3-1
- Updated to release 0.4.3.

* Sun Aug 24 2003 Dag Wieers <dag@wieers.com> - 0.4.0-0
- Make work without atrpms package.

* Fri Jan 17 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de> 0.4.0-0at2
- Update to 0.4.0.
- Synced with embedded specfile.
- Added info files.

* Sun Sep 29 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.3.11.
- Rebuilt against Red Hat Linux 8.0.

* Thu May  2 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Mon Apr 22 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.3.5.

* Wed Sep 19 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.2.3.

* Thu Aug 30 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Initial RPM release.
