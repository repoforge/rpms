# $Id$
# Authority: dag

Summary: Stylus oriented notetaking
Name: xournal
Version: 0.4.5
Release: 2%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://xournal.sourceforge.net/

Source: http://dl.sf.net/xournal/xournal-%{version}.tar.gz
Patch0:		xournal-0.4.5-xoprint-len.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: freetype-devel
BuildRequires: glib2-devel >= 2.6
BuildRequires: libgnomeprintui22-devel
BuildRequires: poppler-devel
BuildRequires: poppler-glib-devel

%description
Xournal is an application for notetaking, sketching, keeping a journal using 
a stylus. It is free software (GNU GPL) and runs on Linux (recent 
distributions) and other GTK+/Gnome platforms. It is similar to Microsoft 
Windows Journal or to other alternatives such as Jarnal, Gournal, and NoteLab.

%prep
%setup
%patch0 -p1

%build
./autogen.sh --prefix="%{_prefix}"
#configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install desktop-install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README 
%{_bindir}/xournal
%{_datadir}/applications/xournal.desktop
%{_datadir}/icons/hicolor/scalable/apps/xournal.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/gnome-mime-application-x-xoj.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/xoj.svg
%{_datadir}/mime/packages/xournal.xml
%{_datadir}/mimelnk/application/x-xoj.desktop
%{_datadir}/xournal/

%post
update-desktop-database %{_datadir}/applications &>/dev/null || :
touch --no-create %{_datadir}/hicolor &>/dev/null || : 
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    update-desktop-database %{_datadir}/applications &>/dev/null ||:
    touch --no-create %{_datadir}/hicolor &>/dev/null || :
    gtk-update-icon-cache %{_datadir}/hicolor &>/dev/null || :
fi

%changelog
* Wed Apr 25 2012 He Jian <hejian.he@gmail.com> 0.4.5-2
- Added xournal-0.4.5-xoprint-len.patch to fix 64 bit systems

* Sun Nov 21 2010 Dag Wieers <dag@wieers.com> - 0.4.5-1
- Updated to release 0.4.5.

* Fri Mar 28 2008 Dag Wieers <dag@wieers.com> - 0.4.2.1-1
- Updated to release 0.4.2.1.

* Wed Mar 26 2008 Dag Wieers <dag@wieers.com> - 0.4.2-1
- Updated to release 0.4.2.

* Sat Sep 22 2007 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Updated to release 0.4.1.

* Wed Sep 09 2007 R P Herrold <info@owlriver.com> - 0.4.0.1-1
- Initial packaging.
