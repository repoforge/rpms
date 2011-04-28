# $Id$
# Authority: shuff
# Upstream: Lars-Dominik Braun <lars$6xq,net>

Summary: console Pandora.com client
Name: pianobar
Version: 2011.04.27
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://6xq.net/html/00/17.html

Source: http://6xq.net/media/00/16/pianobar-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: libao-devel
BuildRequires: libmad-devel
BuildRequires: make
BuildRequires: rpm-macros-rpmforge

%description
Features:

* Create, delete, rename stations and add more music
* Rate and temporary ban tracks as well as move them to another station
* “Shared stations”

and some that pandora does not have (yet):

* last.fm scrobbling (using an external scrobbler)
* Proxy support for non-americans

%package -n libpiano
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description -n libpiano
This package contains the runtime components of the libpiano shared library.

# %package -n libpiano-devel
# Summary: Header files, libraries and development documentation for %{name}.
# Group: Development/Libraries
# Requires: %{name} = %{version}-%{release}
# 
# %description -n libpiano-devel
# This package contains the header files, static libraries and development
# documentation for libpiano. If you like to develop programs using %{name},
# you will need to install libpiano-devel.

%prep
%setup

%build
%{__make} %{?_smp_mflags} all DISABLE_FAAD=1
%{__make} %{?_smp_mflags} libpiano.so.0 DISABLE_FAAD=1

%install
%{__rm} -rf %{buildroot}
%{__make} install PREFIX="%{_usr}" LIBDIR="%{_libdir}" DESTDIR="%{buildroot}"
%{__make} install-libpiano PREFIX="%{_usr}" LIBDIR="%{_libdir}" DESTDIR="%{buildroot}"

# install the man page
%{__install} -m0755 -d %{buildroot}%{_mandir}/man1
%{__install} -m0755 contrib/pianobar.1 %{buildroot}%{_mandir}/man1
%{__rm} -f contrib/pianobar.1

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%post -n libpiano -p /sbin/ldconfig

%postun -n libpiano -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL README contrib/
%doc %{_mandir}/man?/*
%{_bindir}/*

%files -n libpiano
%defattr(-, root, root, 0755)
%{_libdir}/*.so.*
%exclude %{_includedir}/piano.h
%exclude %{_libdir}/libpiano.a
%{_libdir}/libpiano.so


# %files -n libpiano-devel
# %defattr(-, root, root, 0755)
# %{_includedir}/*.h
# %{_libdir}/*.so
# %exclude %{_libdir}/*.a
# %exclude %{_libdir}/*.la

%changelog
* Wed Apr 27 2011 Philip Durbin <philipdurbin@gmail.com> - 2011.04.27-1
- updated to pianobar-2011.04.27
- put version macro in Source
- make libpiano.so.0 separately (no longer built by "make all")

* Mon Jan 31 2011 Steve Huff <shuff@vecna.org> - 2011.01.24-1
- Initial package.
- Doesn't currently build/install libpiano-devel.
