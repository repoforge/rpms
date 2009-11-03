# $Id$
# Authority: dries
# Upstream: <asselsm$gmail,com>

Summary: Flickr uploader
Name: kflickr
Version: 0.9
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://kflickr.sourceforge.net/

Source: http://dl.sf.net/kflickr/kflickr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gettext, kdelibs-devel
BuildRequires: automake, autoconf

%description
kFlickr is a standalone Flickr uploader for KDE. It allows for easy
upload with drag and drop. Common attributes can be edited before
sending the photo. Multiple users are supported.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/kflickr*
%{_bindir}/kflickr
%{_datadir}/applnk/Graphics/kflickr.desktop
%{_datadir}/apps/kflickr/
%{_datadir}/apps/kflickrpart/
%{_datadir}/apps/konqueror/servicemenus/kflickr_servicemenu.desktop
%{_datadir}/services/kflickrpart.desktop
%{_datadir}/doc/HTML/en/kflickr/
%{_datadir}/icons/hicolor/*/apps/kflickr.png
%{_libdir}/kde3/libkflickrpart.*

%changelog
* Sat Jul 28 2007 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Updated to release 0.9.

* Wed Mar 28 2007 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Updated to release 0.8.

* Thu Aug 24 2006 Dries Verachtert <dries@ulyssis.org> - 0.7-1
- Updated to release 0.7.

* Sat Aug 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Updated to release 0.6.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.5-1.2
- Rebuild for Fedora Core 5.

* Sun Nov 27 2005 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Updated to release 0.5.

* Fri Nov 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.4-1
- Updated to release 0.4.

* Tue Oct 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Initial package.
