# $Id: $

# Authority: dries
# Upstream: 

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

# The file isn't yet available on all sf mirrors
Source: http://osdn.dl.sourceforge.net/sourceforge/kpogre/kpogre-%{real_version}.tar.gz
#Source: http://dl.sf.net/kpogre/kpogre-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc, make, libpng-devel, libart_lgpl-devel, arts-devel, gcc-c++, gettext, XFree86-devel, zlib-devel, qt-devel, libjpeg-devel, kdelibs-devel, postgresql-devel

# Screenshot: http://kpogre.sourceforge.net/kpogre1.png
# ScreenshotURL: http://kpogre.sourceforge.net/screenshots.htm

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
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL LICENSE NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%changelog
* Sat May 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.9.7-1
- Initial package.

