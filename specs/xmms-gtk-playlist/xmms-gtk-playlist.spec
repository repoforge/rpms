# $Id$

# Authority: dag

# Upstream: Chris Kuklewicz <chrisk@mit.edu>

%define plugindir %(xmms-config --general-plugin-dir)

Summary: An enhanced playlist plugin for the Linux XMMS music player.
Name: xmms-gtk-playlist
Version: 2.0
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://web.mit.edu/chrisk/www/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://web.mit.edu/chrisk/www/%{name}-%{version}.tar.gz
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
	libdir="%{buildroot}%{plugindir}"

%{__mv} -f %{buildroot}%{plugindir}/*.so.0.0.0 %{buildroot}%{plugindir}/*.so

### Clean up buildroot
%{__rm} -f %{buildroot}%{plugindir}/*.a \
		%{buildroot}%{plugindir}/*.la \
		%{buildroot}%{plugindir}/*.so.*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{plugindir}/*.so
%{_bindir}/*
#exclude %{plugindir}/*.la

%changelog
* Sun Feb 16 2003 Dag Wieers <dag@wieers.com> - 2.0-0
- Initial package. (using DAR)
