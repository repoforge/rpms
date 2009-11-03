# $Id$
# Authority: dag

Summary: Packet watcher, dumper and logger.
Name: exdump
Version: 0.2
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://packetstormsecurity.org/sniffers/exdump/

Source: http://packetstormsecurity.org/sniffers/exdump/exdump-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Exdump is a packet watcher, dumper and logger. TCP, UDP and ICMP packets
that pass a computer on which Exdump resides and runs are logged.

Exdump allows output to be directed to the console/adm or to a user-defined
file. Exdump also has an option to only display packets that are sent to a
specified port, and the program can actually show you the data that was in
the packet. 

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install-exec bindir="%{buildroot}%{_bindir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ABOUT HISTORY OUTPUT README
%{_bindir}/exdump

%changelog
* Thu Feb 22 2007 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)
