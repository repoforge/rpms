# $Id$
# Authority: dag
# Upstream: 

Summary: I/O generator
Name: iogen
Version: 2.2
Release: 1
License: GPL
Group: Applications/
URL: http://www.peereboom.us/iogen/

Source: http://www.peereboom.us/iogen/iogen_%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#Buildarch: noarch
#BuildRequires: 
#Requires:

%description
iogen is an I/O generator. It forks child processes that each run a mix
of reads and writes. The idea is to generate heavily fragmented files
to make the hardware suffer as much as possible. This tool has been
used to test filesystems, drivers, firmware, and hardware devices.

It is by no means meant as a performance measuring tool since it tries
to recreate the worst case scenario I/O.

%prep
%setup -n %{name}_%{version}

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 iogen %{buildroot}%{_bindir}/iogen
%{__install} -Dp -m0644 src/iogen.8 %{buildroot}%{_mandir}/man8/iogen.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man8/iogen.8*
%{_bindir}/iogen

%changelog
* Sun Feb 11 2007 Dag Wieers <dag@wieers.com> - 2.2-1
- Initial package. (using DAR)
