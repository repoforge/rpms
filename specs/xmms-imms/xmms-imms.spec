# $Id$
# Authority: dag
# Upstream: Michael Grigoriev <mag$luminal,org>

%define xmms_generaldir %(xmms-config --general-plugin-dir)

%define real_name imms

Summary: Intelligent Multimedia Management System plugin for XMMS.
Name: xmms-imms
Version: 1.1
Release: 2.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.luminal.org/phpwiki/index.php/IMMS

Source: http://dl.sf.net/imms/imms-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: XFree86-devel, glib-devel, gtk+-devel, id3lib-devel
BuildRequires: libogg-devel, pcre-devel, libstdc++-devel,
BuildRequires: libvorbis-devel, xmms-devel, sqlite-devel, zlib-devel
BuildRequires: automake, autoconf, gcc-c++, xmms-devel

%description
IMMS is an adaptive playlist plug-in for XMMS designed to simplify management
and prioritization of large collections of music.

Some of the key features include:
* Rating and playlist adjustment is done completely transparently to the user.
  IMMS is super easy to use!
* Files are indentified by paths and checksums. Even if you move them they
  still keep their ratings.
* Though mostly "good" songs will be played, ocasionally less popular songs
  will sneak in to give them a chance to earn user's favour.
* IMMS does a better job of shuffling than XMMS. It is able to recognise
  different versions of the same song and not play them in quick succession.

%prep
%setup -n %{real_name}-%{version}

%build
%{__aclocal}
%{__autoheader}
%{__autoconf}
%configure
%{__make} %{?_smp_mflags} \
	LDFLAGS="-lm"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 libimms.so %{buildroot}%{xmms_generaldir}/libimms.so

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README
%{xmms_generaldir}/libimms.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1-2.2
- Rebuild for Fedora Core 5.

* Thu Oct 07 2004 Dag Wieers <dag@wieers.com> - 1.1-2
- Fix permissions of library to include missing dependencies. (Mike Traum)

* Fri Apr 16 2004 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

* Mon Dec 15 2003 Dag Wieers <dag@wieers.com> - 0.9.9-0
- Updated to release 0.9.9.

* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 0.9.4-0
- Initial package. (using DAR)
