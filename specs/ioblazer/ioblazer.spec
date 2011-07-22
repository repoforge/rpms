# $Id$
# Authority: yury
# Upstream: http://labs.vmware.com/flings/ioblazer

Name: ioblazer
Version: 1.01
Release: 1%{?dist}
Group: Applications/System
Summary: Multi-platform storage stack micro-benchmark
License: MIT
URL: http://labs.vmware.com/flings/ioblazer

Source: http://download3.vmware.com/software/vmw-tools/ioblazer/ioblazer-%{version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libaio-devel

%description
IOBlazer is a multi-platform storage stack micro-benchmark. IOBlazer
runs on Linux, Windows and OSX and it is capable of generating a highly
customizable workload.

%prep
%setup -c

%build
%{__make} ioblazer.o %{?_smp_mflags} CFLAGS="%{optflags} -D__LINUX__ -D_GNU_SOURCE -D_LARGEFILE64_SOURCE -pthread -laio -o ioblazer"

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -m 0755 ioblazer %{buildroot}/%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}

%changelog
* Fri Jul 22 2011 Yury V. Zaytsev <yury@shurup.com> - 1.01-1
- Initial package import into RepoForge.
- Thanks to Sergio Rubio for the pull request!
