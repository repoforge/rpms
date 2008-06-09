# $Id$
# Authority: dag

Summary: File manager for the GNOME desktop
Name: gnome-commander
Version: 1.2.6
Release: 2
License: GPL
Group: Applications/File
URL: http://www.nongnu.org/gcmd/

Source: http://ftp.gnome.org/pub/GNOME/sources/gnome-commander/1.2/gnome-commander-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: scrollkeeper, gettext >= 0.10.36, intltool
BuildRequires: gnome-vfs2-devel >= 2.0, libgnomeui-devel >= 2.0
BuildRequires: gnome-doc-utils >= 0.3.2, exiv2-devel
BuildRequires: glib2-devel >= 2.6, gcc-c++

Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires(post): scrollkeeper
Requires(postun): scrollkeeper

%description
GNOME Commander is a nice and fast file manager for the GNOME desktop.
In addition to performing the basic filemanager functions the program
is also an FTP-client and it can browse SMB-networks.

%prep
%setup

%build
%configure \
	--disable-scrollkeeper
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%post
scrollkeeper-update -q -o %{_datadir}/omf/gnome-commander/ || :
/usr/bin/update-desktop-database -q || :

%postun
scrollkeeper-update -q || :
/usr/bin/update-desktop-database -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING INSTALL NEWS README TODO doc/*.txt
%doc %{_mandir}/man1/gnome-commander.1*
%doc %{_datadir}/gnome/help/gnome-commander/
%{_bindir}/gcmd-block
%{_bindir}/gnome-commander
%{_libdir}/gnome-commander/
%{_datadir}/applications/gnome-commander.desktop
%{_datadir}/omf/gnome-commander/
%{_datadir}/pixmaps/gnome-commander/
%{_datadir}/pixmaps/gnome-commander.png

%changelog
* Mon Jun 09 2008 Dag Wieers <dag@wieers.com> - 1.2.6-2
- Rebuild against exiv2-0.17.

* Sun Jun 01 2008 Heiko Adams <info-2K8@ha-software.de> - 1.2.6-1
- Updated to release 1.2.6.

* Fri Feb 29 2008 Heiko Adams <info-2007@ha-software.de> - 1.2.5-1
- Updated to release 1.2.5.

* Sun Jun 10 2007 Dag Wieers <dag@wieers.com> - 1.2.4-1
- Updated to release 1.2.4.

* Mon Dec 11 2006 Dag Wieers <dag@wieers.com> - 1.2.2-1
- Initial package. (using DAR)
