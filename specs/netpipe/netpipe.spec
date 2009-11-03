# $Id$
# Authority: dag
# Upstream: <netpipe$scl,ameslab,gov>
# Upstream: Dave Turner <turner$ameslab,gov>

%define real_name NetPIPE

Summary: Protocol independent performance tool
Name: netpipe
Version: 3.6.2
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.scl.ameslab.gov/netpipe/

Source: http://www.scl.ameslab.gov/netpipe/code/NetPIPE_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: NetPIPE <= %{version}-%{release}, netpipe-tcp <= %{version}-%{release}

%description
NetPIPE is a protocol independent performance tool that visually represents
the network performance under a variety of conditions. It performs simple
ping-pong tests, bouncing messages of increasing size between two processes,
whether across a network or within an SMP system. Message sizes are chosen
at regular intervals, and with slight perturbations, to provide a complete
test of the communication system. Each data point involves many ping-pong
tests to provide an accurate timing. Latencies are calculated by dividing
the round trip time in half for small messages ( < 64 Bytes ).

%prep
%setup -n %{real_name}_%{version}

%build
%{__make} %{?_smp_mflags} memcpy tcp \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 NPmemcpy %{buildroot}%{_bindir}/NPmemcpy
%{__install} -Dp -m0755 NPtcp %{buildroot}%{_bindir}/NPtcp
%{__install} -Dp -m0644 dox/netpipe.1 %{buildroot}%{_mandir}/man1/netpipe.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc bin/* dox/README
#%doc dox/*.pdf dox/*.ps
%doc %{_mandir}/man1/netpipe.1*
%{_bindir}/NPmemcpy
%{_bindir}/NPtcp

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.6.2-1.2
- Rebuild for Fedora Core 5.

* Mon Aug 02 2004 Dag Wieers <dag@wieers.com> - 3.6.2-1
- Initial package. (using DAR)
