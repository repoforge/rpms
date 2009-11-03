# $Id$
# Authority: dag
# Upstream: Nick Harbour <nickharbour$gmail,com>

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Tool for extracting files from network traffic
Name: tcpxtract
Version: 1.0.1
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://tcpxtract.sourceforge.net/

Source: http://downloads.sourceforge.net/tcpxtract/tcpxtract-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: flex, libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
tcpxtract is a tool for extracting files from network traffic based on file
signatures. Extracting files based on file type headers and footers
(sometimes called "carving") is an age old data recovery technique.

Tools like Foremost employ this technique to recover files from arbitrary
data streams. Tcpxtract uses this technique specifically for the application
of intercepting files transmitted across a network.

Other tools that fill a similar need are driftnet and EtherPEG. driftnet and
EtherPEG are tools for monitoring and extracting graphic files on a network
and is commonly used by network administrators to police the internet activity
of their users. The major limitations of driftnet and EtherPEG is that they
only support three filetypes with no easy way of adding more.

The search technique they use is also not scalable and does not search across
packet boundries. tcpxtract features the following:

 * Supports 26 popular file formats out-of-the-box. New formats can be added
   by simply editing its config file.
 * With a quick conversion, you can use your old Foremost config file with
   tcpxtract.
 * Custom written search algorithm is lightning fast and very scalable.
 * Search algorithm searches across packet boundaries for total coverage and
   forensic quality.
 * Uses libpcap, a popular, portable and stable library for network data
   capture.
 * Can be used against a live network or a tcpdump formatted capture file.

%prep
%setup
%{__perl} -pi.path -e 's|/usr/local/etc|%{_sysconfdir}|' tcpxtract.c

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALL="%{__install} -p"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING
%doc %{_mandir}/man1/tcpxtract.1*
%config(noreplace) %{_sysconfdir}/tcpxtract.conf
%{_bindir}/tcpxtract

%changelog
* Wed Jun 06 2007 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Initial package. (using DAR)
