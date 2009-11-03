# $Id$

# Authority: dag
# Upstream: Michal Zalewski <lcamtuf$coredump,cx>

Summary: Dump the memory of a running process.
Name: memfetch
Version: 0.05
Release: 0.b.2%{?dist}
License: GPL
Group: Applications/System
URL: http://lcamtuf.coredump.cx/

Source: http://lcamtuf.coredump.cx/soft/memfetch.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
memfetch is a handy utility for dumping the memory of a running process
(either immediately or on fault). It is a quite valuable addition to the
shell command armory of an average hacker, helping you recover information
that would otherwise be lost, and making it easier to check the integrity
or internals of a running process.

Most debuggers are good at accessing small portions of memory at once,
whereas memfetch is a quick way of getting it all, ready to be processed
in any way you like.

%prep
%setup -n %{name}

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 memfetch %{buildroot}%{_bindir}/memfetch

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README mffind.pl
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.05-0.b.2
- Rebuild for Fedora Core 5.

* Mon Mar 29 2004 Dag Wieers <dag@wieers.com> - 0.05-0.b
- Initial package. (using DAR)
