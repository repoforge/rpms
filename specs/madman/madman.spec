# $Id$
# Authority: matthias
# Upstream: <madman-discuss@lists.sourceforge.net>

Summary: Madman Administrates Digital Music Archives Neatly
Name: madman
Version: 0.93
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://madman.sourceforge.net/
Source: http://dl.sf.net/madman/madman-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xmms
BuildRequires: XFree86-devel, libpng-devel, libjpeg-devel, glib-devel
BuildRequires: qt-devel, xmms-devel, id3lib-devel, libogg-devel, libvorbis-devel
# libtool, *sigh*
BuildRequires: gcc-c++
# xmms-devel, *sigh (bis)*
BuildRequires: gtk+-devel

%description
Madman is a music manager application that allows you to easily keep your
music database organized and tidy, and it helps you listen to better music,
be happier, brighten your teeth and quickly restore world peace.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/%{name}
%{_libdir}/%{name}


%changelog
* Thu May 20 2004 Matthias Saou <http://freshrpms.net/> 0.93-1
- Update to 0.93.

* Fri Apr  2 2004 Matthias Saou <http://freshrpms.net/> 0.91.1-1
- Initial RPM release.

