# $Id$
# Authority: dag
# Upstream: Sergey Zhitomirsky <szh$7ka,mipt,ru>

Summary: Execute programs chrooted, with dropped privileges and as another user/group
Name: dreamland
Version: 0.1
Release: 0.2%{?dist}
Group: System Environment/Daemons
License: GPL
URL: http://www.7ka.mipt.ru/~szh/dreamland/

Source: http://www.7ka.mipt.ru/~szh/dreamland/dreamland.c
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Dreamland executes programs chrooted, with dropped privileges and as
another user/group. Besides it can also impose resource limits, and
other nice ( renice :) features. I'm trying to provide ability to drop
all kinds of privileges, defined in Linux.

%prep

%build
${CC:-%{__cc}} %{optflags} -o dreamland %{SOURCE0}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 dreamland %{buildroot}%{_bindir}/dreamland

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/dreamland

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.1-0.2
- Rebuild for Fedora Core 5.

* Sun May 04 2003 Dag Wieers <dag@wieers.com> - 0.1-0
- Initial package. (using DAR)
