# $Id$
# Authority: dries
# Upstream: Pawel Stolowski <yogin$linux,bydg,org>

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?fc4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}

Summary: Viewer for comic book archives
Name: qcomicbook
Version: 0.4.3
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://linux.bydg.org/~yogin/

Source: http://linux.bydg.org/~yogin/qcomicbook/qcomicbook-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gettext, gcc-c++, imlib2-devel
%{!?_without_modxorg:BuildRequires: libXmu-devel, libXi-devel}

%description
QComicBook is a viewer for rar, zip, cbr, and cbz format comic book
archives containing JPEG or PNG images. Its features include
automatic handling of archives, full-screen mode, page scaling, and
mouse or keyboard navigation.

%prep
%setup

%build
%{expand: %%define optflags -O2}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%doc %{_mandir}/man1/qcomicbook*
%{_bindir}/qcomicbook
%{_datadir}/applications/*qcomicbook.desktop
%{_datadir}/qcomicbook/
%{_datadir}/pixmaps/qcomicbook.png

%changelog
* Mon Sep 14 2009 Dries Verachtert <dries@ulyssis.org> - 0.4.3-1
- Updated to release 0.4.3.

* Mon Aug 31 2009 Dries Verachtert <dries@ulyssis.org> - 0.4.1-1
- Updated to release 0.4.1.

* Thu Nov 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.4-1
- Updated to release 0.3.4.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.3-1
- Updated to release 0.3.3.

* Tue Aug 15 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.0-1
- Updated to release 0.3.0.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.7-1.2
- Rebuild for Fedora Core 5.

* Sun Mar 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.7-1
- Updated to release 0.2.7.

* Thu Dec 29 2005 Dries Verachtert <dries@ulyssis.org> - 0.2.6-1
- Updated to release 0.2.6.

* Fri Dec 02 2005 Dries Verachtert <dries@ulyssis.org> - 0.2.5-1
- Initial package.
