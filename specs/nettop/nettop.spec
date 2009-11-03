# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Top like program for network activity
Name: nettop
Version: 0.2.3
Release: 1%{?dist}
License: BSD
Group: Applications/System
URL: http://srp.portico.org/scripts/

Source: http://srparish.net/software/nettop-%{version}.tar.gz
Patch0: nettop-0.2.3-gcc3.patch
Patch1: nettop-0.2.3-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{?_with_libpcapdevel:BuildRequires:libpcap-devel}
BuildRequires: libpcap, slang-devel
Requires: slang, libpcap

%description
This program was written as a top like program for
network activity. It is licensed under a BSD type
license, so you are free to do pretty much as you
like with this.

%prep
%setup
%patch0 -p0
%patch1 -p1

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 nettop %{buildroot}%{_sbindir}/nettop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README THANKS README
%{_sbindir}/nettop

%changelog
* Thu Dec 22 2006 Dag Wieers <dag@wieers.com> - 0.2.3-1
- Initial package. (using DAR)
