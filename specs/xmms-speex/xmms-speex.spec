# $Id: xmms-speex.spec,v 1.1 2004/02/26 17:54:31 thias Exp $

%define _xmmsinputdir %(xmms-config --input-plugin-dir)

Summary: X MultiMedia System input plugin to play speex files
Name: xmms-speex
Version: 0.9.1
Release: 1.fr
License: GPL
Group: Applications/Multimedia
URL: http://jzb.rapanden.dk/projects/speex-xmms
Source: http://jzb.rapanden.dk/pub/speex-xmms-%{version}.tar.gz
Patch: speex-xmms-0.9.1.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: xmms >= 1.0.0, glib >= 1.2.7, gtk+ >= 1.2.7, speex, libogg
BuildRequires: xmms-devel, gtk+-devel, speex-devel, libogg-devel

%description
X MultiMedia System input plugin to play speex files.

%prep
%setup -q -n speex-xmms
%patch -p1

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc COPYING README
%{_xmmsinputdir}/libspeex.so

%changelog
* Mon Jan  5 2004 Matthias Saou <http://freshrpms.net/> 0.9.1-1.fr
- Initial rpm package.

