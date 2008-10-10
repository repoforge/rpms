# $Id$
# Authority: dag
# Upstream: Philippe Biondi <biondi$cartel-securite,fr>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Interactive packet manipulation tool and network scanner
Name: scapy
Version: 2.0.0.10
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.secdev.org/projects/scapy/

Source: http://www.secdev.org/projects/scapy/files/scapy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: python >= 2.2, nmap

%description
Scapy is a powerful interactive packet manipulation tool, packet generator,
network scanner, network discovery, packet sniffer, etc. It can for the
moment replace hping, 85% of nmap, arpspoof, arp-sk, arping, tcpdump,
tethereal, p0f, ....

Scapy uses the python interpreter as a command board. That means that you
can use directly python language (assign variables, use loops, define
functions, etc.) If you give a file as parameter when you run scapy, your
session (variables, functions, intances, ...) will be saved when you leave
the interpretor, and restored the next time you launch scapy.

%prep
%setup

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
#%{__install} -Dp -m0755 scapy.py %{buildroot}%{_bindir}/scapy
#%{__install} -Dp -m0644 scapy.1 %{buildroot}%{_mandir}/man1/scapy.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
#%doc AUTHORS changelog* COPYING README
%doc %{_mandir}/man1/scapy.1*
%{_bindir}/scapy
%{_bindir}/UTscapy
%{python_sitelib}

%changelog
* Sat Oct 11 2008 Dag Wieers <dag@wieers.com> - 2.0.0.10-1
- Updated to release 2.0.0.10.

* Tue Apr 17 2007 Dries Verachtert <dries@ulyssis.org> - 1.1.1-1
- Updated to release 1.1.1.

* Fri Oct 20 2006 Dag Wieers <dag@wieers.com> - 1.0.5-1
- Updated to release 1.0.5.

* Fri Mar 17 2006 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Updated to release 1.0.4.

* Sat Jan 28 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.3-1
- Updated to release 1.0.3.

* Sun Nov 27 2005 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Wed Aug 10 2005 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Fri Sep 03 2004 Dag Wieers <dag@wieers.com> - 0.9.17-1
- Updated to release 0.9.17.

* Fri Aug 01 2003 Dag Wieers <dag@wieers.com> - 0.9.14-0
- Added nmap as a dependency.
- Updated to release 0.9.14.

* Sat May 17 2003 Dag Wieers <dag@wieers.com> - 0.9.13-0.beta
- Initial package. (using DAR)
