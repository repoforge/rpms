# $Id$
# Authority: matthias

%define real_version 521

Summary: Free C++ class library of cryptographic schemes
Name: cryptopp
Version: 5.2.1
Release: 1
License: Public Domain
Group: System Environment/Libraries
URL: http://www.cryptopp.com/
Source: http://www.eskimo.com/~weidai/cryptopp%{real_version}.zip
Patch: crypto-5.2.patch.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Buildrequires: unzip, gcc-c++

%description
Crypto++ Library is a free C++ class library of cryptographic schemes. 
Currently the library consists of the following, some of which are other 
people's code, repackaged into classes.

One purpose of Crypto++ is to act as a repository of public domain 
(not copyrighted) source code. Although the library is copyrighted as a 
compilation, the individual files in it (except for a few exceptions listed
in the license) are in the public domain.


%package devel
Summary: Files for development of applications which will use Crypto++
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
Crypto++ Library is a free C++ class library of cryptographic schemes.
Currently the library consists of the following, some of which are other
people's code, repackaged into classes.

This package contains the header files and static libraries for Crypto++.


%package progs
Summary: Programs for manipulating Crypto++ routines
Group: Development/Tools
Requires: %{name} = %{version}

%description progs
Crypto++ Library is a free C++ class library of cryptographic schemes.
Currently the library consists of the following, some of which are other
people's code, repackaged into classes.

This package contains programs for manipulating Crypto++ routines.


%prep
%setup -c -n %{name}-%{version}
%patch -p1 -b .autotools
%{__chmod} 755 configure


%build
%configure
# For 5.1 at least :
# Don't optimize with -O2, it BREAKS the lib: running 'cryptest v' fails
%{__make} %{?_smp_mflags} CXXFLAGS="-DNDEBUG"


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc License.txt Readme.txt
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/cryptopp/
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so

%files progs
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_datadir}/cryptopp/


%changelog
* Mon Nov 15 2004 Matthias Saou <http://freshrpms.net/> 5.2.1-1
- Update to 5.2.1, with newer patch from Mandrake Cooker.

* Wed May 26 2004 Matthias Saou <http://freshrpms.net/> 5.1-1
- Fedora Core package based on the Mandrake one.

* Mon Mar 01 2004 Lenny Cartier <lenny@mandrakesoft.com> 5.1-1mdk
- from Pierre-Michel Theveny <pmth@free.fr> :
	- Fixed problem with broken library (do not use -O2 !)
	- Added patch for GNU autotools and libtool support
	- Added package progs

* Wed Feb 19 2004 Pierre-Michel Theveny <pmth@free.fr> 5.1-1mdk
- Ported to Mandrake 9.2
- Added shared library

* Tue Feb 18 2004 Ariano Bertacca <ariano@hirnriss.net> 5.1-1
- released libcryptopp-5.1-1
