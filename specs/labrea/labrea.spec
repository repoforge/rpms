# $Id$
# Authority: dag
# Upstream: lorgor <lorgor$users,sourceforge,net>

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

%define real_version 2.5-stable-1

Summary: "Sticky" Honeypot and IDS
Name: labrea
Version: 2.5
Release: 2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://labrea.sourceforge.net/

Source: http://dl.sf.net/labrea/labrea-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap, libdnet-devel
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
LaBrea takes over unused IP addresses, and creates virtual servers that
are attractive to worms, hackers, and other denizens of the Internet.
The program answers connection attempts in such a way that the machine
at the other end gets "stuck", sometimes for a very long time.

%prep
%setup -n %{name}-%{real_version}

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/labrea.1*
%doc %{_mandir}/man5/labrea.conf.5*
%config(noreplace) %{_sysconfdir}/labrea.conf
%{_sbindir}/labrea

%changelog
* Fri Jan 26 2007 Dag Wieers <dag@wieers.com> - 2.5-2
- Rebuild for fixing group on older packages (<fc3).

* Fri Jul 02 2004 Dag Wieers <dag@wieers.com> - 2.5-1
- Initial package. (using DAR)
