# $Id: $

# Authority: dries
# Screenshot: http://kasablanca.berlios.de/images/screenshots/sshot031.png

Summary: Ftp/fxp client
Name: kasablanca
Version: 0.3.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://kasablanca.berlios.de/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://download.berlios.de/kasablanca/kasablanca-%{version}.tar.gz 
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: gettext, libart_lgpl-devel
BuildRequires: libjpeg-devel, libpng-devel
BuildRequires: arts-devel, zlib-devel
BuildRequires: kdelibs-devel, gcc-c++
BuildRequires: qt-devel, openssl-devel
%{?fc2:BuildRequires: xorg-x11-devel}
%{?fc1:BuildRequires: XFree86-devel}

%description
Kasablanca is an ftp client, written in c++, using the kde libraries. among
its features are currently encryption (auth tls) support, fxp, site 
bookmarks, and queued transfers.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_datadir}/applnk/Utilities/kasablanca.desktop
%{_datadir}/apps/kasablanca
%{_datadir}/doc/HTML/en/kasablanca
%{_datadir}/icons/*/*/apps/kasablanca.png

%changelog
* Wed Jul 14 2004 Dries Verachtert <dries@ulyssis.org> 0.4-1
- Update to version 0.4.

* Mon Mar 22 2004 Dries Verachtert <dries@ulyssis.org> 0.3-1
- Initial package
