# $Id$
# Authority: dries
# Upstream: Quar <quar$vitea,pl>

Summary: Development environment for children
Name: littlewizard
Version: 1.2.1
Release: 1
License: GPL
Group: Applications/Education
URL: http://littlewizard.sourceforge.net/

Source: http://dl.sf.net/littlewizard/littlewizard-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, pkgconfig, gtk2-devel, libxml2-devel, gettext

%description
Little Wizard is a development environment for children. Little Wizard
can be programmed without using keyboard, just by using drag and drop.
It works under Linux and Windows 2000/XP (using GTK). Even children in
primary school can understand how it works. 

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
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/littlewizard
%{_bindir}/littlewizardtest
%{_libdir}/liblanguage.so.*
%{_libdir}/liblw.so.*
%{_datadir}/pixmaps/littlewizard/
%{_datadir}/applications/littlewizard.desktop
%{_datadir}/icons/gnome/*/mimetypes/gnome-mime-application-x-littlewizard.png
%{_datadir}/icons/gnome/scalable/mimetypes/gnome-mime-application-x-littlewizard.svg
%{_datadir}/mime/packages/littlewizard.xml
%{_datadir}/littlewizard/
%exclude %{_prefix}/doc/littlewizard/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/littlewizard/
%{_libdir}/liblanguage.so
%{_libdir}/liblw.so
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%changelog
* Mon Aug 18 2008 Dries Verachtert <dries@ulyssis.org> - 1.2.1-1
- Updated to release 1.2.1.

* Sun Jul  6 2008 Dries Verachtert <dries@ulyssis.org> - 1.2.0-1
- Updated to release 1.2.0.

* Sat Jul 28 2007 Dries Verachtert <dries@ulyssis.org> - 1.1.5-1
- Updated to release 1.1.5.

* Sun Mar 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.2-1
- Updated to release 1.1.2.

* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.1-1
- Updated to release 1.1.1.

* Tue Dec 06 2005 Dries Verachtert <dries@ulyssis.org> - 1.1.0-0.rc2
- Initial package.
