# $Id: $

# Authority: dries
# Screenshot: http://pwp.netcabo.pt/users/51/0251296501/tagtool/tt_edit.png
# ScreenshotURL: http://pwp.netcabo.pt/users/51/0251296501/tagtool/Default.htm#shots

Summary: Manage the information fields in MP3 and Ogg Vorbis files
Name: tagtool
Version: 0.11.1
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://pwp.netcabo.pt/paol/tagtool/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/tagtool/tagtool-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: automake, autoconf, glib2-devel, gtk2-devel, libglade2-devel
BuildRequires: id3lib-devel, libogg-devel, libvorbis-devel

%description
Audio Tag Tool is a program to manage the information fields in MP3 and Ogg
Vorbis files.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
# make it available to both
%{__install} -d %{buildroot}%{_datadir}/applications
%{__mv} %{buildroot}%{_datadir}/gnome/apps/Multimedia/tagtool.desktop %{buildroot}%{_datadir}/applications/
echo "Categories=Application;AudioVideo;X-Red-Hat-Base;" >> %{buildroot}%{_datadir}/applications/tagtool.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%{_bindir}/*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop
%{_datadir}/tagtool

%changelog
* Thu Jan 06 2005 Dries Verachtert <dries@ulyssis.org> - 0.11.1
- Initial package.
