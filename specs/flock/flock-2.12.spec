# $Id$
# Authority: dag
# Upstream: Adrian Bunk <bunk@kernel.org>

# ExclusiveDist: el2 rh7 rh9 el3 el4

%{?dtag: %{expand: %%define %dtag 1}}

%{?el3:%define _without_gettextdevel 1}
%{?rh9:%define _without_gettextdevel 1}
%{?rh7:%define _without_gettextdevel 1}
%{?el2:%define _without_gettextdevel 1}

%define real_name util-linux

Summary: Manage locks from shell scripts
Name: flock
Version: 2.12r
Release: 0.1%{?dist}
License: distributable
Group: System Environment/Base
URL: ftp://ftp.kernel.org/pub/linux/utils/util-linux/

Source: ftp://ftp.kernel.org/pub/linux/utils/util-linux/util-linux-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_gettextdevel:BuildRequires: gettext-devel}
%{?_without_gettextdevel:BuildRequires: gettext}

Conflicts: util-linux > 2.12i

%description
flock is a tool to manage flock(2) locks from within shell scripts or the
command line.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 sys-utils/flock %{buildroot}%{_bindir}/flock
%{__install} -Dp -m0755 sys-utils/flock.1 %{buildroot}%{_mandir}/man1/flock.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc HISTORY MAINTAINER README
%doc %{_mandir}/man1/flock.1*
%{_bindir}/flock

%changelog
* Mon Nov 10 2008 Dag Wieers <dag@wieers.com> - 2.12r-0.1
- Initial package. (using DAR)
