# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: Simple sound converter application
Name: soundconverter
Version: 1.3.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://soundconverter.berlios.de/

Source: http://download.berlios.de/soundconverter/soundconverter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python-devel >= 2.3.3, gstreamer-python >= 0.10
BuildRequires: intltool, perl(XML::Parser)
Requires: python >= 2.3.3, pygtk2, gstreamer-python >= 0.10, gnome-python2-gconf

%description
A simple sound converter application. It can convert from and to all
gstreamer supported formats.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README TODO
%doc %{_mandir}/man1/soundconverter.1*
%{_bindir}/soundconverter
%{_datadir}/applications/soundconverter.desktop
%{_datadir}/icons/hicolor/scalable/apps/soundconverter.svg
%{_datadir}/icons/hicolor/*/apps/soundconverter.png
%{_datadir}/soundconverter/

%changelog
* Tue Jun 24 2008 Dag Wieers <dag@wieers.com> - 1.3.1-1
- Updated to release 1.3.1.

* Tue Jun 24 2008 Dag Wieers <dag@wieers.com> - 1.3.0-1
- Updated to release 1.3.0.

* Sun Apr  6 2008 Dries Verachtert <dries@ulyssis.org> - 1.0.0-1
- Updated to release 1.0.0.

* Thu Jan 10 2008 Dag Wieers <dag@wieers.com> - 0.9.8-1
- Updated to release 0.9.8.

* Sun Apr 01 2007 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.

* Fri Jun 02 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.6-1
- Updated to release 0.8.6.

* Sun May 28 2006 Dag Wieers <dag@wieers.com> - 0.8.5-1
- Updated to release 0.8.5.

* Sat Jan 07 2006 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Initial package. (using DAR)
