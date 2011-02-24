# $Id$
# Authority: shuff
# Upstream: Colomban Wendling <ban$herbesfolles,org>
# ExcludeDist: el4 el5
# Rationale: glib2-devel in el<6 doesn't have a sufficient GIO

Summary: C Template Parser Library
Name: ctpl
Version: 0.3.2
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://ctpl.tuxfamily.org/

Source: http://download.tuxfamily.org/ctpl/releases/ctpl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: gtk-doc
BuildRequires: make
BuildRequires: rpm-macros-rpmforge

%description
CTPL is a template library written in C. It allows fast and easy parsing of
templates from many sources (including in-memory data and local and remote
streaming, thanks to GIO) and fine control over template parsing environment. 

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
    --disable-dependency-tracking \
    --disable-static \
    --enable-gtk-doc
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# pkgconfig files in the wrong place
%{__install} -m0755 -d %{buildroot}%{_datadir}/pkgconfig
%{__mv} %{buildroot}%{_libdir}/pkgconfig/*.pc %{buildroot}%{_datadir}/pkgconfig
%{__rm}dir %{buildroot}%{_libdir}/pkgconfig

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING HACKING INSTALL NEWS README THANKS TODO
%doc docs/reference/ctpl/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_datadir}/pkgconfig
%{_includedir}/ctpl
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Thu Feb 24 2011 Steve Huff <shuff@vecna.org> - 0.3.2-1
- Initial package.
