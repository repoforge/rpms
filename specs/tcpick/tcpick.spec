# $Id$
# Authority: dag
# Upstream: <tcpick-project$lists,sourceforge,net>

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: TCP stream sniffer and connection tracker
Name: tcpick
Version: 0.2.1
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://tcpick.sourceforge.net/

Source: http://dl.sf.net/tcpick/tcpick-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
tcpick is a textmode sniffer that can track tcp streams and saves the data
captured in files or displays them in the terminal. Useful for picking
files in a passive way.

It can store all connections in different files, or it can display all the
stream on the terminal. It is useful to keep track of what users of a network
are doing, and is usable with textmode tools like grep, sed, awk.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL KNOWN-BUGS NEWS README THANKS TODO
%doc %{_mandir}/man8/tcpick.8*
%exclude %{_mandir}/man8/tcpick_italian.8*
%{_bindir}/tcpick

%changelog
* Wed Jan 19 2005 Dag Wieers <dag@wieers.com> - 0.2.1-1
- Updated to release 0.2.1.

* Wed Jan 12 2005 Dag Wieers <dag@wieers.com> - 0.2.0-1
- Updated to release 0.2.0.

* Sun Aug 29 2004 Dag Wieers <dag@wieers.com> - 0.1.24-1
- Updated to release 0.1.24.

* Fri Jun 04 2004 Dag Wieers <dag@wieers.com> - 0.1.23-1
- Updated to release 0.1.23.

* Fri Apr 09 2004 Dag Wieers <dag@wieers.com> - 0.1.22-1
- Updated to release 0.1.22.

* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 0.1.21-1
- Initial package. (using DAR)
