# $Id$
# Authority: dries
# Upstream: Enrico Troeger <enrico,troeger$uvena,de>

Summary: Small C editor
Name: geany
Version: 0.18.1
Release: 1%{?dist}
License: GPL
Group: Applications/Editors
URL: http://geany.org

Source: http://download.geany.org/geany-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gettext, gtk2-devel >= 2.6, perl(XML::Parser), intltool
BuildRequires: vte-devel

%description
Geany is a small C editor using GTK2 with basic features of an integrated 
development environment. It features syntax highlighting, code completion, 
call tips, many supported filetypes (including C, Java, PHP, HTML, DocBook, 
Perl, LateX, and Bash), and symbol lists.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
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
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}
%{__mv} %{buildroot}%{_datadir}/doc/geany rpmdocs

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog ChangeLog.pre-0-17 HACKING INSTALL NEWS 
%doc README.* rpmdocs/* 
%doc %{_mandir}/man?/*
%{_bindir}/geany
%{_libdir}/geany/
%{_datadir}/geany/
%{_datadir}/icons/*/*/apps/*
%{_datadir}/locale/*/LC_MESSAGES/*
%{_datadir}/applications/geany.desktop

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/geany/
%{_libdir}/pkgconfig/geany.pc

%changelog
* Sun Feb 28 2010 Steve Huff <shuff@vecna.org> - 0.18-1
- Updated to release 0.18.1.

* Sun Apr 20 2008 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Updated to release 0.14.

* Tue Oct 16 2007 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Mon Jun 25 2007 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Updated to release 0.11.

* Tue Apr 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.10.2-1
- Updated to release 0.10.2.

* Sat Feb 24 2007 Dries Verachtert <dries@ulyssis.org> - 0.10.1-1
- Updated to release 0.10.1.

* Sat Dec 23 2006 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Mon Oct 02 2006 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Updated to release 0.9.

* Fri Aug 11 2006 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Initial package.
