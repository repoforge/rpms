# $Id$

# Authority: dag

# Upstream: Sergey Zhitomirsky <szh@7ka.mipt.ru>

Summary: Execute programs chrooted, with dropped privileges and as another user/group.
Name: dreamland
Version: 0.1
Release: 0
Group: System Environment/Daemons
License: GPL
URL: http://www.7ka.mipt.ru/~szh/dreamland/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.7ka.mipt.ru/~szh/dreamland/dreamland.c
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
Dreamland executes programs chrooted, with dropped privileges and as
another user/group. Besides it can also impose resource limits, and
other nice ( renice :) features. I'm trying to provide ability to drop
all kinds of privileges, defined in Linux.

%prep

%build
gcc %{optflags} -o dreamland %{SOURCE0}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -m0755 dreamland %{buildroot}%{_bindir}/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*

%changelog
* Sun May 04 2003 Dag Wieers <dag@wieers.com> - 0.1-0
- Initial package. (using DAR)
