# $Id$
# Authority: matthias

Summary: Library for working with files using the mp4 container format
Name: libmp4v2
Version: 1.5.0.1
Release: 3
License: MPL
Group: System Environment/Libraries
URL: http://resare.com/libmp4v2/
Source0: http://resare.com/libmp4v2/dist/libmp4v2-%{version}.tar.bz2
# Only here to be in the source package, "just in case, and FYI"
Source1: http://resare.com/libmp4v2/mklibmp4v2/mklibmp4v2-r51.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++

%description
The libmp4v2 library provides an abstraction layer for working with files
using the mp4 container format. This library is developed by mpeg4ip project
and is an exact copy of the library distributed in the mpeg4ip package.


%package devel
Summary: Development files for the mp4v2 library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Development files and documentation needed to develop and compile programs
using the libmp4v2 library.


%prep
%setup -q 


%build
%configure \
    --disable-static \
    --disable-dependency-tracking
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%{__rm} -rf %{buildroot}%{_mandir}/manm/


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,0755)
%doc COPYING
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,0755)
%doc README TODO INTERNALS API_CHANGES
%{_includedir}/*.h
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_mandir}/man?/*


%changelog
* Fri Dec 15 2006 Matthias Saou <http://freshrpms.net/> 1.5.0.1-3
- Spec file cleanup (habits, mostly) preparing to submit for Extras inclusion.

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 1.5.0.1-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Jul 18 2006 Noa Resare <noa@resare.com> 1.5.0.1-1
- new upstream release

* Sat May 13 2006 Noa Resare <noa@resare.com> 1.4.1-3
- disabled static lib
- use DESTDIR
- disable-dependency-tracking for faster builds
- removed a manpage template file apt.mpt.gz

* Mon May 08 2006 Noa Resare <noa@resare.com> 1.4.1-2
- specfile cleanups

* Fri May 05 2006 Noa Resare <noa@resare.com> 1.4.1-1.lvn5
- initial release
