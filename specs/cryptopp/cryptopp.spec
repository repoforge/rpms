# $Id$
# Authority: matthias

%define real_version 552

Summary: Free C++ class library of cryptographic schemes
Name: cryptopp
Version: 5.5.2
Release: 1%{?dist}
License: Public Domain
Group: System Environment/Libraries
URL: http://www.cryptopp.com/

Source: http://dl.sf.net/cryptopp/cryptopp%{real_version}.zip
Patch0: cryptopp-5.5.2-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildrequires: dos2unix
Buildrequires: gcc-c++
Buildrequires: unzip

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
%patch0 -p0

### All files have ^M end of lines, fix that for the gcc4 patch to apply
find . -type f -exec dos2unix {} \;

%build
#configure --disable-static
%ifarch X86_64
%{__make} %{?_smp_mflags} shared CXXFLAGS="%{optflags} -DNDEBUG -fPIC"
%else
%{__make} %{?_smp_mflags} shared CXXFLAGS="%{optflags} -DNDEBUG"
%endif

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" PREFIX="%{_prefix}" LIBDIR="%{_libdir}"

%{__ln_s} -f libcryptopp.so.1.0 %{buildroot}%{_libdir}/libcryptopp.so.1
%{__ln_s} -f libcryptopp.so.1.0 %{buildroot}%{_libdir}/libcryptopp.so

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc License.txt Readme.txt
%{_libdir}/libcryptopp.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/cryptopp/
%{_libdir}/libcryptopp.so
#%exclude %{_libdir}/libcryptopp.a
#%exclude %{_libdir}/libcryptopp.la

%files progs
%defattr(-, root, root, 0755)
%{_bindir}/cryptest
%{_datadir}/cryptopp/

%changelog
* Wed Sep 17 2008 Dag Wieers <dag@wieers.com> - 5.5.2-1
- Updated to release 5.5.2.

* Fri Oct 28 2005 Matthias Saou <http://freshrpms.net/> 5.2.1-3
- Include gcc4 patch, and convert all files to UNIX line breaks.

* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 5.2.1-2
- Use optflags, but replace -O? with -O1, since it breaks otherwise.

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
