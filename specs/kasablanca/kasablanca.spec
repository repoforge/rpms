# $Id: $

# Authority: dries

Summary: Ftp/fxp client
Name: kasablanca
Version: 0.3.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://kasablanca.berlios.de/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.tuxforge.de/kasablanca/kasablanca-%{version}.tar.gz 
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc-c++, XFree86-devel, qt-devel, openssl-devel
Requires: kdelibs, openssl

# Screenshot: http://kasablanca.berlios.de/images/screenshots/sshot031.png

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

%changelog
* Mon Mar 22 2004 Dries Verachtert <dries@ulyssis.org> 0.3-1
- Initial package
