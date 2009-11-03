# $Id$
# Authority: dag

Summary: Displays a live list of active connections and what files are being transferred
Name: pktstat
Version: 1.8.4
Release: 1%{?dist}
License: BSD
Group: Applications/Internet
URL: http://www.adaptive-enterprises.com.au/~d/software/pktstat/

Source: http://www.adaptive-enterprises.com.au/~d/software/pktstat/pktstat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap

%description
Display a real-time list of active connections seen on a network
interface, and how much bandwidth is being used by what. Partially
decodes HTTP and FTP protocols to show what filename is being
transferred. X11 application names are also shown. Entries hang around
on the screen for a few seconds so you can see what just happened. Also
accepts filter expressions like tcpdump.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
#%{__install} -D -m0755 pktstat %{buildroot}%{_bindir}/pktstat
#%{__install} -D -m0644 pktstat.1 %{buildroot}%{_mandir}/man1/pktstat.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man1/pktstat.1*
%{_bindir}/pktstat

%changelog
* Tue Sep  4 2007 Dries Verachtert <dries@ulyssis.org> - 1.8.4-1
- Updated to release 1.8.4.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.8.3-1
- Updated to release 1.8.3.

* Sat Nov 11 2006 Dag Wieers <dag@wieers.com> - 1.8.2-1
- Updated to release 1.8.2.

* Sun Feb 12 2006 Dag Wieers <dag@wieers.com> - 1.8.1-1
- Updated to release 1.8.1.

* Sun Jan 29 2006 Dag Wieers <dag@wieers.com> - 1.8.0-1
- Initial package. (using DAR)
