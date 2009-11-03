# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Red Hat compilers for distccd
Name: distcc-compilers-redhat
Version: 0.7.2
Release: 2%{?dist}
License: GPL
Group: Development/Tools
URL: http://dag.wieers.com/home-made/distcc/

Source0: ftp://ftp.redhat.com/pub/redhat/linux/6.2/en/os/i386/RedHat/RPMS/egcs-1.1.2-30.i386.rpm
Source1: ftp://ftp.redhat.com/pub/redhat/linux/6.2/en/os/i386/RedHat/RPMS/egcs-c++-1.1.2-30.i386.rpm
Source2: ftp://ftp.redhat.com/pub/redhat/linux/as2.1/en/os/i386/RedHat/RPMS/gcc-2.96-124.7.2.i386.rpm
Source3: ftp://ftp.redhat.com/pub/redhat/linux/as2.1/en/os/i386/RedHat/RPMS/gcc-c++-2.96-124.7.2.i386.rpm
Source4: ftp://ftp.redhat.com/pub/redhat/linux/8.0/en/os/i386/RedHat/RPMS/gcc-3.2-7.i386.rpm
Source5: ftp://ftp.redhat.com/pub/redhat/linux/8.0/en/os/i386/RedHat/RPMS/gcc-c++-3.2-7.i386.rpm
Source6: ftp://ftp.redhat.com/pub/redhat/linux/9/en/os/i386/RedHat/RPMS/gcc-3.2.2-5.i386.rpm
Source7: ftp://ftp.redhat.com/pub/redhat/linux/9/en/os/i386/RedHat/RPMS/gcc-c++-3.2.2-5.i386.rpm
Source8: ftp://ftp.redhat.com/pub/redhat/linux/el3/en/os/i386/RedHat/RPMS/gcc-3.2.3-20.i386.rpm
Source9: ftp://ftp.redhat.com/pub/redhat/linux/el3/en/os/i386/RedHat/RPMS/gcc-c++-3.2.3-20.i386.rpm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: rpm, cpio, binutils
%{?fc1:Requires: compat-gcc, compat-gcc-c++, gcc32}
%{?el3:Requires: gcc, gcc-c++, compat-gcc, compat-gcc-c++}
%{?rh9:Requires: gcc, gcc-c++, compat-gcc, compat-gcc-c++}
%{?rh8:Requires: gcc, gcc-c++, compat-gcc, compat-gcc-c++}
%{?rh7:Requires: gcc, gcc-c++}
%{?el2:Requires: gcc, gcc-c++}
%{?rh6:Requires: egcs, egcs-c++}

%description
distcc-compilers-redhat contains de stock Red Hat compilers for Red Hat 6.2,
Red Hat Advanced Server 2.1, Red Hat 7.3, Red Hat 8.0, Red Hat 9 and
Red Hat Enterprise Linux 3 for use on nodes in a distcc cluster.

If you use this package you have to make sure that you're compiling for the
right compiler on your distcc cluster.

%prep
%build
%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_libdir}/distcc/bin \
			%{buildroot}%{_libdir}/ccache/bin
cd %{buildroot}

### Red Hat 6.2 compilers
%if %{?rh6:1}%{!?rh6:0}
	%{__ln_s} -f i386-redhat-linux-gcc .%{_bindir}/i386-redhat-linux-cc-2.91.6
	%{__ln_s} -f i386-redhat-linux-gcc .%{_bindir}/i386-redhat-linux-gcc-2.91.6
	%{__ln_s} -f g++ .%{_bindir}/i386-redhat-linux-c++-2.91.6
	%{__ln_s} -f g++ .%{_bindir}/i386-redhat-linux-g++-2.91.6
%else
	rpm2cpio %{SOURCE0} | cpio -ivd *i386-redhat-linux-gcc *cc1
	rpm2cpio %{SOURCE1} | cpio -ivd *g++ *cc1plus
	%{__mv} -f .%{_bindir}/i386-redhat-linux-gcc .%{_bindir}/i386-redhat-linux-gcc-2.91.6
	%{__mv} -f .%{_bindir}/g++ .%{_bindir}/i386-redhat-linux-g++-2.91.6
	ln -f .%{_bindir}/i386-redhat-linux-gcc-2.91.6 .%{_bindir}/i386-redhat-linux-cc-2.91.6
	ln -f .%{_bindir}/i386-redhat-linux-g++-2.91.6 .%{_bindir}/i386-redhat-linux-c++-2.91.6
%endif

### Red Hat 7.3 and AS2.1 compilers
%{?rh7:%define has_gcc296 1}
%{?el2:%define has_gcc296 1}
%if %{?has_gcc296:1}%{!?has_gcc296:0}
	%{__ln_s} -f i386-redhat-linux-gcc .%{_bindir}/i386-redhat-linux-cc-2.96
	%{__ln_s} -f i386-redhat-linux-gcc .%{_bindir}/i386-redhat-linux-gcc-2.96
	%{__ln_s} -f i386-redhat-linux-g++ .%{_bindir}/i386-redhat-linux-c++-2.96
	%{__ln_s} -f i386-redhat-linux-g++ .%{_bindir}/i386-redhat-linux-g++-2.96
%else
### Red Hat 8.0, 9, EL3 and RHFC1 have compatible C compilers in compat-gcc
%{?fc1:%define has_compat_gcc296 1}
%{?el3:%define has_compat_gcc296 1}
%{?rh9:%define has_compat_gcc296 1}
%{?rh8:%define has_compat_gcc296 1}
%if %{?has_compat_gcc296:1}%{!?has_compat_gcc296:0}
	%{__ln_s} -f i386-redhat-linux7-gcc .%{_bindir}/i386-redhat-linux-cc-2.96
	%{__ln_s} -f i386-redhat-linux7-gcc .%{_bindir}/i386-redhat-linux-gcc-2.96
	%{__ln_s} -f i386-redhat-linux7-g++ .%{_bindir}/i386-redhat-linux-c++-2.96
	%{__ln_s} -f i386-redhat-linux7-g++ .%{_bindir}/i386-redhat-linux-g++-2.96
%else
	rpm2cpio %{SOURCE2} | cpio -ivd *i386-redhat-linux-gcc *cc1
	rpm2cpio %{SOURCE3} | cpio -ivd *i386-redhat-linux-g++ *cc1plus
	%{__mv} -f .%{_bindir}/i386-redhat-linux-gcc .%{_bindir}/i386-redhat-linux-gcc-2.96
	%{__mv} -f .%{_bindir}/i386-redhat-linux-g++ .%{_bindir}/i386-redhat-linux-g++-2.96
	ln -f .%{_bindir}/i386-redhat-linux-gcc-2.96 .%{_bindir}/i386-redhat-linux-cc-2.96
	ln -f .%{_bindir}/i386-redhat-linux-g++-2.96 .%{_bindir}/i386-redhat-linux-c++-2.96
%endif
%endif

### Red Hat 8.0 compilers
%if %{?rh8:1}%{!?rh8:0}
	%{__ln_s} -f i386-redhat-linux-gcc .%{_bindir}/i386-redhat-linux-cc-3.2
	%{__ln_s} -f i386-redhat-linux-gcc .%{_bindir}/i386-redhat-linux-gcc-3.2
	%{__ln_s} -f i386-redhat-linux-g++ .%{_bindir}/i386-redhat-linux-c++-3.2
	%{__ln_s} -f i386-redhat-linux-g++ .%{_bindir}/i386-redhat-linux-g++-3.2
%else
	rpm2cpio %{SOURCE4} | cpio -ivd *i386-redhat-linux-gcc *cc1
	rpm2cpio %{SOURCE5} | cpio -ivd *i386-redhat-linux-g++ *cc1plus
	%{__mv} -f .%{_bindir}/i386-redhat-linux-gcc .%{_bindir}/i386-redhat-linux-gcc-3.2
	%{__mv} -f .%{_bindir}/i386-redhat-linux-g++ .%{_bindir}/i386-redhat-linux-g++-3.2
	ln -f .%{_bindir}/i386-redhat-linux-gcc-3.2 .%{_bindir}/i386-redhat-linux-cc-3.2
	ln -f .%{_bindir}/i386-redhat-linux-g++-3.2 .%{_bindir}/i386-redhat-linux-c++-3.2
%endif

### Red Hat 9 compilers
%if %{?rh9:1}%{!?rh9:0}
	%{__ln_s} -f i386-redhat-linux-gcc .%{_bindir}/i386-redhat-linux-cc-3.2.2
	%{__ln_s} -f i386-redhat-linux-gcc .%{_bindir}/i386-redhat-linux-gcc-3.2.2
	%{__ln_s} -f i386-redhat-linux-g++ .%{_bindir}/i386-redhat-linux-c++-3.2.2
	%{__ln_s} -f i386-redhat-linux-g++ .%{_bindir}/i386-redhat-linux-g++-3.2.2
%else
	rpm2cpio %{SOURCE6} | cpio -ivd *i386-redhat-linux-gcc *cc1
	rpm2cpio %{SOURCE7} | cpio -ivd *i386-redhat-linux-g++ *cc1plus
	%{__mv} -f .%{_bindir}/i386-redhat-linux-gcc .%{_bindir}/i386-redhat-linux-gcc-3.2.2
	%{__mv} -f .%{_bindir}/i386-redhat-linux-g++ .%{_bindir}/i386-redhat-linux-g++-3.2.2
	ln -f .%{_bindir}/i386-redhat-linux-gcc-3.2.2 .%{_bindir}/i386-redhat-linux-cc-3.2.2
	ln -f .%{_bindir}/i386-redhat-linux-g++-3.2.2 .%{_bindir}/i386-redhat-linux-c++-3.2.2
%endif

### Red Hat EL3 compilers
%if %{?el3:1}%{!?el3:0}
	%{__ln_s} -f i386-redhat-linux-gcc .%{_bindir}/i386-redhat-linux-cc-3.2.3
	%{__ln_s} -f i386-redhat-linux-gcc .%{_bindir}/i386-redhat-linux-gcc-3.2.3
	%{__ln_s} -f i386-redhat-linux-g++ .%{_bindir}/i386-redhat-linux-c++-3.2.3
	%{__ln_s} -f i386-redhat-linux-g++ .%{_bindir}/i386-redhat-linux-g++-3.2.3
%else
### Red Hat FC1 includes this one in the gcc32 package (not the c++)
%{?fc1:%define has_gcc323 1}
%if %{?has_gcc323:1}%{!?has_gcc323:0}
	%{__ln_s} -f gcc32 .%{_bindir}/i386-redhat-linux-cc-3.2.3
	%{__ln_s} -f gcc32 .%{_bindir}/i386-redhat-linux-gcc-3.2.3
	rpm2cpio %{SOURCE9} | cpio -ivd *i386-redhat-linux-g++ *cc1plus
	%{__mv} -f .%{_bindir}/i386-redhat-linux-g++ .%{_bindir}/i386-redhat-linux-g++-3.2.3
	ln -f .%{_bindir}/i386-redhat-linux-g++-3.2.3 .%{_bindir}/i386-redhat-linux-c++-3.2.3
%else
	rpm2cpio %{SOURCE8} | cpio -ivd *i386-redhat-linux-gcc *cc1
	rpm2cpio %{SOURCE9} | cpio -ivd *i386-redhat-linux-g++ *cc1plus
	%{__mv} -f .%{_bindir}/i386-redhat-linux-gcc .%{_bindir}/i386-redhat-linux-gcc-3.2.3
	%{__mv} -f .%{_bindir}/i386-redhat-linux-g++ .%{_bindir}/i386-redhat-linux-g++-3.2.3
	ln -f .%{_bindir}/i386-redhat-linux-gcc-3.2.3 .%{_bindir}/i386-redhat-linux-cc-3.2.3
	ln -f .%{_bindir}/i386-redhat-linux-g++-3.2.3 .%{_bindir}/i386-redhat-linux-c++-3.2.3
%endif
%endif

### Set up links for distcc-server and ccache
cd .%{_bindir}
for compiler in *; do
	%{__ln_s} -f %{_bindir}/distcc %{buildroot}%{_libdir}/distcc/bin/$compiler
	%{__ln_s} -f %{_bindir}/ccache %{buildroot}%{_libdir}/ccache/bin/$compiler
done

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_libdir}/gcc-lib/
%{_libdir}/distcc/bin/*
%{_libdir}/ccache/bin/*

%changelog
* Tue Feb 03 2004 Dag Wieers <dag@wieers.com> - 0.7.2-2
- Fix gcc-c++ 3.2.3 package for RHFC1.

* Sun Jan 25 2004 Dag Wieers <dag@wieers.com> - 0.7.2-1
- RHFC1 requires gcc32 package, so don't include the compiler. (Rudolf Kastl)
- Added RHAS21 gcc 2.96 compiler instead of RH73.

* Sat Oct 25 2003 Dag Wieers <dag@wieers.com> - 0.7.1-0
- Added RHEL3 compilers.

* Wed Aug 13 2003 Dag Wieers <dag@wieers.com> - 0.7-0
- Get rid of distcc requirement.

* Thu May 15 2003 Dag Wieers <dag@wieers.com> - 0.6-0
- Small fixes.

* Tue May 13 2003 Dag Wieers <dag@wieers.com> - 0.5-0
- Added cc to the list.
- Added gcc and gcc-c++ Requires.

* Wed May 07 2003 Dag Wieers <dag@wieers.com> - 0.3-0
- Fixed the link to the local compiler.
- Added ccache links.

* Tue May 06 2003 Dag Wieers <dag@wieers.com> - 0.1-0
- Initial package. (using DAR)
