# $Id$
# Authority: dag

### EL6 ships with wireless-tools-29-5.1.1.el6
### EL5 ships with wireless-tools-28-2.el5
### EL4 ships with wireless-tools-28-0.pre16.3.3.EL4
### EL3 ships with wireless-tools-26-2
### EL2 ships with wireless-tools-21-3
# ExclusiveDist: el2
# Tag: rfx

%define _sbindir /sbin
%define _libdir /lib
%define real_name wireless_tools

Summary: Wireless ethernet configuration tools
Name: wireless-tools
Version: 26
Release: 0.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/Tools.html

Source: http://pcmcia-cs.sf.net/ftp/contrib/wireless_tools.%{version}.tar.gz
#Patch0: wireless-tools-26-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
This package contain the Wireless tools, used to manipulate
the Wireless Extensions. The Wireless Extension is an interface
allowing you to set Wireless LAN specific parameters and get the
specific stats for wireless networking equipment.

%prep
%setup -n %{real_name}.%{version}
#patch0

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
%defattr(-, root, root, 0755)
%doc *.txt README
%doc %{_mandir}/man?/*
%{_sbindir}/*
%{_libdir}/*.so*
%{_includedir}/*.h

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 26-0.2
- Rebuild for Fedora Core 5.

* Sat Jul 12 2003 Dag Wieers <dag@wieers.com> - 26-0
- Initial package. (using DAR)
