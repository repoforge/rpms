# $Id$
# Authority: dag
# Upstream: Chris Kuklewicz <chrisk$mit,edu>

%define xmms_generaldir %(xmms-config --general-plugin-dir)

Summary: Enhanced playlist plugin for the Linux XMMS music player
Name: xmms-gtk-playlist
Version: 2.0
Release: 0.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://web.mit.edu/chrisk/www/

Source: http://web.mit.edu/chrisk/www/xmms-gtk-playlist-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel >= 1.2.0, xmms-devel


%description
xmms-gtk-playlist is an enhanced playlist for the Linux XMMS music player.
You can load and save playlists, and perform regular expressions on your
playlists.


%prep
%setup


%build
#configure
./configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall \
	libdir="%{buildroot}%{xmms_generaldir}"

%{__mv} -f %{buildroot}%{xmms_generaldir}/*.so.0.0.0 %{buildroot}%{xmms_generaldir}/*.so


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*
%{xmms_generaldir}/*.so
%exclude %{xmms_generaldir}/*.a
%exclude %{xmms_generaldir}/*.la
%exclude %{xmms_generaldir}/*.so.*


%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.0-0.2
- Rebuild for Fedora Core 5.

* Sun Feb 16 2003 Dag Wieers <dag@wieers.com> - 2.0-0
- Initial package. (using DAR)
