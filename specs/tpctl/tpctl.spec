# Authority: dag

Summary: IBM ThinkPad configuration tools.
Name: tpctl
Version: 4.8
Release: 0
License: GPL
Group: System Environment/Base
URL: http://tpctl.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://download.sf.net/tpctl/%{name}_%{version}.tar.gz
Patch: tpctl-4.8-rpm.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: ncurses-devel, perl
Requires: kernel-module-thinkpad >= 3.2, perl

Obsoletes: tpctl-apmiser

%description
tpctl is a package of IBM ThinkPad configuration tools for Linux.

%prep
%setup
%patch0 -b .rpm

%build
%{__make} %{?_smp_mflags} all
%{__cp} -av apmiser/README ./README.apmiser

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_mandir}/man1
%makeinstall \
	PATH_SBIN="%{buildroot}%{_sbindir}/" \
	PATH_BIN="%{buildroot}%{_bindir}/" \
	PATH_LIB="%{buildroot}%{_libdir}/" \
	PATH_MAN="%{buildroot}%{_mandir}/"

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README* SUPPORTED* TROUBLE* VGA-MODES
%doc %{_mandir}/man?/*
%{_sbindir}/*
%{_libdir}/*
%{_bindir}/*

%changelog
* Thu Dec 04 2003 Dag Wieers <dag@wieers.com> - 4.8-0
- Updated to release 4.8.

* Fri Apr 11 2003 Dag Wieers <dag@wieers.com> - 4.4-0
- Updated to release 4.4.

* Tue Mar 11 2003 Dag Wieers <dag@wieers.com> - 4.3-0
- Initial package. (using DAR)
