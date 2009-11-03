# $Id$
# Authority: dag


Summary: Red Hat Fedora compilers for distccd
Name: distcc-compilers-fedora
Version: 0.7.2
Release: 0%{?dist}
License: GPL
Group: Development/Tools
URL: http://dag.wieers.com/home-made/distcc/

Source0: ftp://ftp.redhat.com/pub/redhat/linux/el3/en/os/i386/RedHat/RPMS/gcc-3.3.2-1.i386.rpm
Source1: ftp://ftp.redhat.com/pub/redhat/linux/el3/en/os/i386/RedHat/RPMS/cpp-3.3.2-1.i386.rpm
Source2: ftp://ftp.redhat.com/pub/redhat/linux/el3/en/os/i386/RedHat/RPMS/gcc-c++-3.3.2-1.i386.rpm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: rpm, cpio, binutils
%{?fc1:Requires: gcc, gcc-c++, compat-gcc, compat-gcc-c++, gcc32}

%description
distcc-compilers-fedora contains de stock Fedora compilers for Fedora Core 1
for use on nodes in a distcc cluster.

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

### Fedora Core 1 compilers
%if %{?fc1:1}%{!?fc1:0}
	%{__ln_s} -f i386-redhat-linux-gcc .%{_bindir}/i386-redhat-linux-cc-3.3.2
	%{__ln_s} -f i386-redhat-linux-gcc .%{_bindir}/i386-redhat-linux-gcc-3.3.2
	%{__ln_s} -f i386-redhat-linux-g++ .%{_bindir}/i386-redhat-linux-c++-3.3.2
	%{__ln_s} -f i386-redhat-linux-g++ .%{_bindir}/i386-redhat-linux-g++-3.3.2
%else
	rpm2cpio %{SOURCE0} | cpio -ivd *i386-redhat-linux-gcc
	rpm2cpio %{SOURCE1} | cpio -ivd *cc1
	rpm2cpio %{SOURCE2} | cpio -ivd *i386-redhat-linux-g++ *cc1plus
	%{__mv} -f .%{_bindir}/i386-redhat-linux-gcc .%{_bindir}/i386-redhat-linux-gcc-3.3.2
	%{__mv} -f .%{_bindir}/i386-redhat-linux-g++ .%{_bindir}/i386-redhat-linux-g++-3.3.2
	ln -f .%{_bindir}/i386-redhat-linux-gcc-3.3.2 .%{_bindir}/i386-redhat-linux-cc-3.3.2
	ln -f .%{_bindir}/i386-redhat-linux-g++-3.3.2 .%{_bindir}/i386-redhat-linux-c++-3.3.2
%endif

### Set up links for distcc and ccache
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
%{!?fc1:%{_libdir}/gcc-lib/}
%{_libdir}/distcc/bin/*
%{_libdir}/ccache/bin/*

%changelog
* Sun Jan 25 2004 Dag Wieers <dag@wieers.com> - 0.7.2-0
- Fixed requirements.

* Mon Nov 10 2003 Dag Wieers <dag@wieers.com> - 0.7.1-0
- Added RHFC1 compilers.
- Initial package. (using DAR)
