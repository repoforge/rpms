# $Id$

# Authority: dag
# Distcc: 0

%define plugindir %(xmms-config --output-plugin-dir)
%define rname DBMix

Summary: Digital Audio Mixing System.
Name: dbmix
Version: 0.9.8
Release: 3
License: GPL
Group: Applications/Multimedia
URL: http://dbmix.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/DBMix/DBMix-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: xmms >= 1.2.0
Obsoletes: DBMix <= %{version}
Provides: DBMix = %{version}-%{release}

%description
DBMix is a software DJ mixing system for digital audio. DBMix allows a user
to output multiple simultaneous audio streams on a single sound device, and
to transform/modify each stream independently.

%prep 
%setup -n %{rname}-%{version}

### FIXME: Fix the errno problem on RH9
%{__perl} -pi.orig -e 's|^(\s*extern int errno;\s*)$|#include <errno.h>\n\n\1|' dbaudiolib/dbaudiolib.c dbaudiolib/DBAudio_Volume.c dbaudiolib/DBAudio_Mute.c

%build
#configure
./configure \
	--prefix="%{_prefix}" \
	--bindir="%{_bindir}" \
	--libdir="%{_libdir}"
%{__make} %{?_smp_mflags} \
	LDFLAGS="-L%{_builddir}/%{buildsubdir}/dbaudiolib/.libs"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -d %{buildroot}%{plugindir}
%{__mv} -f %{buildroot}%{_libdir}/libdbmix.* %{buildroot}%{plugindir}

### Clean up buildroot
%{__rm} -f %{buildroot}%{plugindir}/*.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README Readme.*
%{_bindir}/*
%{_libdir}/libdbaudiolib.*
%{plugindir}/*
     
%changelog
* Tue Feb 24 2004 Dag Wieers <dag@wieers.com> - 0.9.8-3
- Renamed package to lowercase 'dbmix'.

* Fri Aug 01 2003 Dag Wieers <dag@wieers.com> - 0.9.8-2
- Removed the remaining .la file and use plugindir macro.

* Thu Jun 27 2002 Dag Wieers <dag@wieers.com> - 0.9.8-0
- Initial package.
