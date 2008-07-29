# $Id$
# Authority: dries

Summary: Film collection manager application
Name: griffith
Version: 0.9.7.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://griffith.vasconunes.net/

Source: http://download.berlios.de/griffith/griffith-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: 
Requires: python-imaging, python-reportlab, gnome-python2-gtkspell, python-sqlalchemy

%description
Griffith is a film collection manager application. Adding items to the
movie collection is as quick and easy as typing the film title and
selecting a supported source. Griffith will then try to fetch all the
related information from the Web.  

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall DESTDIR=%{buildroot}
%{__rm} -f %{buildroot}%{_bindir}/griffith
%{__ln_s} %{_datadir}/griffith/lib/griffith %{buildroot}%{_bindir}/griffith
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%doc %{_mandir}/man1/griffith*
%doc %{_mandir}/*/man1/griffith*
%{_bindir}/griffith
%{_datadir}/griffith/
%{_datadir}/pixmaps/griffith.*
%{_datadir}/applications/griffith.desktop

%changelog
* Tue Jul 29 2008 Dries Verachtert <dries@ulyssis.org> - 0.9.7.1-1
- Updated to release 0.9.7.1.

* Mon Jul 28 2008 Dries Verachtert <dries@ulyssis.org> - 0.9.7-1
- Updated to release 0.9.7.

* Tue Jan 29 2008 Dries Verachtert <dries@ulyssis.org> - 0.9.6-1
- Updated to release 0.9.6.

* Mon Sep  3 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.5-1
- Updated to release 0.9.5.

* Mon Aug 13 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.4-1
- Updated to release 0.9.4.

* Sun Jul 08 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.3.1-1
- Updated to release 0.9.3.1.

* Wed Feb 21 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.2-1
- Updated to release 0.9.2.

* Sat Jan 27 2007 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Updated to release 0.9.

* Wed May 31 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.1-2
- Added missing requirements, thanks to Malte Tiedje.

* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.1-1
- Initial package.
