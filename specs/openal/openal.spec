# $Id$

# Authority: newrpms

Summary: Open Audio Library
Name: openal
Version: 0.0.0
Release: 0.20031006
License: LGPL
Group: System Environment/Libraries
URL: http://www.openal.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: openal-20031006.tar.bz2
Source1: openalrc
Source2: acinclude.m4
Source9999: openal-20030131-32.spec.bak
Patch0: openal-conf.patch
Patch1: openal-etc_openalrc.patch
Patch2: openal-incl.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: SDL-devel, arts-devel, esound-devel, libogg-devel, libvorbis-devel
BuildRequires: texinfo
Requires(post,preun): info

%description
OpenAL is an audio library designed in the spirit of OpenGL--machine
independent, cross platform, and data format neutral, with a clean,
simple C-based API.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}
%{__rm} -f linux/acinclude.m4 linux/aclocal.m4
install -p -D %{SOURCE2} linux/aclocal.m4
%patch0 -p1
%patch1
%patch2 -p1

%build
cd linux
aclocal
autoconf 
autoheader configure.in
%configure --enable-arts \
           --enable-esd \
           --enable-vorbis \
           --enable-sdl \
           --disable-smpeg \
           --enable-capture	
%{__make} %{?_smp_mflags}
%{__make} -C doc

%install
%{__rm} -rf %{buildroot}
%makeinstall -C linux \
	DESTDIR="%{buildroot}%{_prefix}" \
	DESTLIB="%{buildroot}%{_libdir}"

%{__install} -d -m0755 %{buildroot}%{_sysconfdir} \
			%{buildroot}%{_infodir}
%{__install} -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/openalrc
%{__install} -m0644 linux/doc/openal.info %{buildroot}%{_infodir}

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig &>/dev/null
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir 2>/dev/null || :

%preun
if [ "$1" -eq 0 ]; then
  /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir 2>/dev/null || :
fi

%postun
/sbin/ldconfig &>/dev/null

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING CREDITS README 
%doc %{_infodir}/*.info*
%config(noreplace) %{_sysconfdir}/openalrc
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc README
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/AL/

%changelog
* Mon Feb 09 2004 Dag Wieers <dag@wieers.com> - 0.0.0-0.20031006
- Initial package. (using DAR)
