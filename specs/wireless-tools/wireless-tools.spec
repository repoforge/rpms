# $Id$

# Authority: dag

%define _sbindir /sbin
%define _libdir /lib
%define rname wireless_tools

Summary: Wireless ethernet configuration tools.
Name: wireless-tools
Version: 26
Release: 0
License: GPL
Group: System Environment/Base
URL: http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/Tools.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://pcmcia-cs.sourceforge.net/ftp/contrib/wireless_tools.%{version}.tar.gz
Patch0: wireless-tools-26-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
This package contain the Wireless tools, used to manipulate
the Wireless Extensions. The Wireless Extension is an interface
allowing you to set Wireless LAN specific parameters and get the
specific stats for wireless networking equipment. 

%prep
%setup -n %{rname}.%{version}
%patch0

%build
%{__make} clean
%{__make} %{?_smp_mflags} \
	OPT_FLAGS="%{optflags}" \
	BUILD_SHARED="1"

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	INSTALL_DIR="%{buildroot}%{_sbindir}" \
	INSTALL_LIB="%{buildroot}%{_libdir}" \
	INSTALL_INC="%{buildroot}%{_includedir}" \
	INSTALL_MAN="%{buildroot}%{_mandir}"
#mkdir -p $RPM_BUILD_ROOT{/sbin,/%{_lib},%{_mandir}/man8,%{_includedir},%{_libdir}}

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/libiw.a
%{__ln_s} -f %{_libdir}/libiw.so.%{version} %{buildroot}%{_libdir}/libiw.so

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-,root,root)
%doc *.txt README
%doc %{_mandir}/man?/*
%{_sbindir}/*
%{_libdir}/*.so*
%{_includedir}/*.h

%changelog
* Sat Jul 12 2003 Dag Wieers <dag@wieers.com> - 26-0
- Initial package. (using DAR)
