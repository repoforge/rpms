# $Id: $

# Authority: dries
# Upstream: Lumir Vanek <lvanek$eanet,cz>
# Screenshot: http://kpogre.sourceforge.net/kpogre1.png
# ScreenshotURL: http://kpogre.sourceforge.net/screenshots.htm

%define real_version 0.98

Summary: PostgreSQL graphical frontend
Name: kpogre
Version: 0.9.8
Release: 1
License: GPL
Group: Applications/Databases
URL: http://kpogre.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/kpogre/kpogre-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Patch: fc2-compile-fixes.patch

BuildRequires: gcc, make, libpng-devel, libart_lgpl-devel
BuildRequires: arts-devel, gcc-c++, gettext, XFree86-devel
BuildRequires: zlib-devel, qt-devel, libjpeg-devel, kdelibs-devel
BuildRequires: postgresql-devel, libpqxx, libpqxx-devel

%description
KPoGre is a graphical client for PostgreSQL databases. All important
information such as users, databases, types, domains, functions, sequences, 
tables and views is easily accessible in a tree view.

%prep
%setup -n kpogre-%{real_version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_bindir}/*
%{_datadir}/icons/*/*/apps/kpogre.png
%{_datadir}/apps/kpogre
%{_datadir}/applnk/Applications/kpogre.desktop
%{_datadir}/doc/HTML/en/kpogre

%changelog
* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.9.8-1
- Initial package.
