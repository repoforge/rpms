# $Id$
# Authority: dag
# Upstream: Folkert Van Heusden <folkert$vanheusden,com>

Summary: Replacement for tee program
Name: memtee
Version: 0.3
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://www.vanheusden.com/memtee/

Source: http://www.vanheusden.com/memtee/memtee-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
memtee is a replacement for 'tee' in situations were no read-write mounted
filesystem is available. In such a case memtee buffers all output into memory
and when it receives the TERM-signal, it writes that buffered data into a file.

This way one can have for example the output of fsck in the startup-scripts
buffered and when a filesystem is mounted rw, one can signal memtee the flush
that fsck-output onto disk by sending it a TERM signal.

%prep
%setup

%build
%{__make} %{?_smp_mflags} DEBUG="%{optflags}"

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 memtee %{buildroot}%{_bindir}/memtee

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc license.txt
%{_bindir}/*

%changelog
* Sun Nov 19 2006 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
