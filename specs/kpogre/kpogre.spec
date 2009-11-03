# $Id$

# Authority: dries
# Upstream: Lumir Vanek <lvanek$eanet,cz>
# Screenshot: http://kpogre.sourceforge.net/kpogre1.png
# ScreenshotURL: http://kpogre.sourceforge.net/screenshots.htm

%define real_version 1.3.5


Summary: PostgreSQL graphical frontend
Name: kpogre
Version: 1.3.5
Release: 2%{?dist}
License: GPL
Group: Applications/Databases
URL: http://kpogre.sourceforge.net/

Source: http://dl.sf.net/kpogre/kpogre-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# Patch: fc2-compile-fixes.patch

BuildRequires: gcc, make, libpng-devel, libart_lgpl-devel
BuildRequires: arts-devel, gcc-c++, gettext
BuildRequires: zlib-devel, qt-devel, libjpeg-devel, kdelibs-devel >= 3.3
BuildRequires: postgresql-devel, libpqxx, libpqxx-devel, libacl-devel

%description
KPoGre is a graphical client for PostgreSQL databases. All important
information such as users, databases, types, domains, functions, sequences,
tables and views is easily accessible in a tree view.

%prep
%setup -n kpogre-%{real_version}

%build
source /etc/profile.d/qt.sh
%configure LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
%{__perl} -pi -e "s|-Iincludedir\@| |g; s|-Llibdir\@| |g;" $(find . -type f | grep Makefile)
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source /etc/profile.d/qt.sh
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
* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.5-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Mon Aug 15 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.5-1
- Update to release 1.3.5.

* Mon Jan 03 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.7-1
- Update to release 1.2.7.

* Sun Nov 28 2004 Dries Verachtert <dries@ulyssis.org> - 1.2.6-1
- Update to release 1.2.6.

* Fri Oct 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.2.4-1
- Update to release 1.2.4.

* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.9.8-1
- Initial package.
