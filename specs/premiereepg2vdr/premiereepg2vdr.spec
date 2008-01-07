# $Id$
# Authority: dag
# Upstream: Axel Katzur <software@katzur.de>

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_kernelheaders 1}
%{?el3:%define _without_kernelheaders 1}
%{?rh9:%define _without_kernelheaders 1}
%{?rh7:%define _without_kernelheaders 1}
%{?el2:%define _without_kernelheaders 1}

Summary: Read EPG information for Premiere TV channels
Name: premiereepg2vdr
Version: 0.0.5
Release: 1
License: GPL
Group: Applications/
URL: http://www.vdr-wiki.de/wiki/index.php/Premiereepg2vdr

#Source: http://deela.cc.fh-lippe.de/files/premiereepg2vdr/premiereepg2vdr-%{version}.tar.gz
Source: http://www.katzur.de/download/premiereepg2vdr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_kernelheaders:BuildRequires: kernel-headers >= 2.4-9}
%{?_without_kernelheaders:BuildRequires: glibc-kernheaders >= 2.4-9}

%description
premiereepg2vdr is a tool to read Electronic Program Guid (EPG) information
for the Premiere TV channels and use it with VDR.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README* *.conf
%{_bindir}/premiereepg2vdr

%changelog
* Sat Jan 05 2008 Dag Wieers <dag@wieers.com> - 0.0.5-1
- Initial package. (using DAR)
