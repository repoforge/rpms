# $Id$
# Authority: dag
# Upstream: Chris Mason <mason$suse,com>

Summary: AIO benchmark tool
Name: aio-stress
Version: 0.21
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://fsbench.filesystems.org/

Source: http://fsbench.filesystems.org/bench/aio-stress.c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
aio-stress is a AIO benchmark tool.

%prep
%{__cp} -v %{SOURCE0} aio-stress.c

%build
%{__cc} -Wall -laio -lpthread -o aio-stress aio-stress.c

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 aio-stress %{buildroot}%{_bindir}/aio-stress

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/aio-stress

%changelog
* Tue Jun 08 2010 Dag Wieers <dag@wieers.com> - 0.21-1
- Initial package. (using DAR)
