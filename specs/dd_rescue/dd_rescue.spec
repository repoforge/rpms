# $Id$
# Authority: dag
# Upstream: Kurt Garloff <kurt$garloff,de>

Summary: Fault tolerant "dd" utility for rescueing data from bad media
Name: dd_rescue
Version: 1.12
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.garloff.de/kurt/linux/ddrescue/

Source: http://www.garloff.de/kurt/linux/ddrescue/dd_rescue-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
dd_rescue is a utility similar to the system utility "dd" which copies
data from a file or block device to another. dd_rescue does however
not abort on errors in the input file. This makes it suitable for
rescuing data from media with errors, e.g. a disk with bad sectors.

%prep
%setup -n %{name}

### Remove binary object
#%{__rm} -f dd_rescue

%build
%{__make} %{?_smp_mflags} clean dd_rescue \
	EXTRA_CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 dd_rescue %{buildroot}%{_bindir}/dd_rescue

### Rename default README
%{__mv} -f README.dd_rescue README

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README*
%{_bindir}/dd_rescue

%changelog
* Sun Aug 13 2006 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Fri Mar 04 2005 Dag Wieers <dag@wieers.com> - 1.11-1
- Updated to release 1.11.

* Mon Dec 20 2004 Dag Wieers <dag@wieers.com> - 1.10-1
- Updated to release 1.10.

* Sun Aug 29 2004 Dag Wieers <dag@wieers.com> - 1.04-1
- Updated to release 1.04.

* Tue Jan 27 2004 Dag Wieers <dag@wieers.com> - 1.03-0
- Initial package. (using DAR)
