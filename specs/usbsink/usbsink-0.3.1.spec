# $Id$
# Authority: dag

Summary: Program for automatic file synchronization over USB
Name: usbsink
Version: 0.3.1
Release: 1%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://usbsink.sourceforge.net/

Source: http://dl.sf.net/sourceforge/usbsink/usbsink-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, pcre-devel, gamin-devel, gnome-doc-utils, scrollkeeper
BuildRequires: gtkmm24-devel, libglademm24-devel, gnome-vfsmm26-devel
Requires: scrollkeeper

%description
USBSink is a GNOME program for automatic file synchronization with removable
drives. In USBSink you define a task associated to a particular flash drive,
and then have a complete automation of data transfers. With file monitoring
and hardware detection features, the program is able to act and respond
according to relevant events on the desktop. 

%prep
%setup

%build
%configure --disable-scrollkeeper
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%post
scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
scrollkeeper-update -q || :
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING COPYRIGHT NEWS README
%{_bindir}/usbsink
%{_datadir}/usbsink/
%{_datadir}/applications/usbsink.desktop
%{_datadir}/gnome/help/usbsink/
%{_datadir}/icons/hicolor/48x48/apps/usbsink.png
%{_datadir}/icons/hicolor/scalable/apps/usbsink.svg
%{_datadir}/omf/usbsink/

%changelog
* Mon Sep 10 2007 Dag Wieers <dag@wieers.com> - 0.3.1-1
- Initial package. (using DAR)
