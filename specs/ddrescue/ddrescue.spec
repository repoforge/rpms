# $Id$
# Authority: dag
# Upstream: Kurt Garloff <kurt$garloff,de>

%define real_name dd_rescue

Summary: Fault tolerant "dd" utility for rescueing data from bad media
Name: ddrescue
Version: 1.11
Release: 1
License: GPL
Group: Applications/System
URL: http://www.garloff.de/kurt/linux/ddrescue/

Source: http://www.garloff.de/kurt/linux/ddrescue/dd_rescue-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
ddrescue is a utility similar to the system utility "dd" which copies
data from a file or block device to another. ddrescue does however
not abort on errors in the input file. This makes it suitable for
rescuing data from media with errors, e.g. a disk with bad sectors.

%prep
%setup -n %{real_name}

### Remove binary object
%{__rm} -f %{real_name}

### Rename default README
%{__mv} -f README.dd_rescue README

%build
%{__make} %{?_smp_mflags} \
	EXTRA_CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 dd_rescue %{buildroot}%{_bindir}/dd_rescue

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README*
%{_bindir}/dd_rescue

%changelog
* Fri Mar 04 2005 Dag Wieers <dag@wieers.com> - 1.11-1
- Updated to release 1.11.

* Mon Dec 20 2004 Dag Wieers <dag@wieers.com> - 1.10-1
- Updated to release 1.10.

* Sun Aug 29 2004 Dag Wieers <dag@wieers.com> - 1.04-1
- Updated to release 1.04.

* Tue Jan 27 2004 Dag Wieers <dag@wieers.com> - 1.03-0
- Initiale package. (using DAR)
