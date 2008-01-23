# $Id$
# Authority: dries
# Upstream: Enrico Troeger <enrico,troeger$uvena,de>

Summary: Small C editor
Name: geany
Version: 0.12
Release: 1
License: GPL
Group: Applications/Editors
URL: http://geany.uvena.de/

Source: http://dl.sf.net/geany/geany-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gettext, gtk2-devel >= 2.6, perl(XML::Parser), intltool

%description
Geany is a small C editor using GTK2 with basic features of an integrated 
development environment. It features syntax highlighting, code completion, 
call tips, many supported filetypes (including C, Java, PHP, HTML, DocBook, 
Perl, LateX, and Bash), and symbol lists.

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
%doc INSTALL THANKS rpmdocs/*
%doc %{_mandir}/man1/geany*
%{_bindir}/geany
%{_libdir}/geany/
%{_datadir}/geany/
%{_datadir}/icons/*/*/apps/classviewer*.png
%{_datadir}/pixmaps/geany.*
%{_datadir}/applications/geany.desktop

%changelog
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
