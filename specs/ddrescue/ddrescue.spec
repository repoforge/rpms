# $Id$
# Authority: dag

%define real_name dd_rescue

Summary: Fault tolerant "dd" utility for rescueing data from bad media
Name: ddrescue
Version: 1.04
Release: 1
License: GPL
Group: Applications/System
URL: http://www.garloff.de/kurt/linux/ddrescue/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

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
%{__install} -D -m0755 dd_rescue %{buildroot}%{_bindir}/dd_rescue
%{__ln_s} -f dd_rescue %{buildroot}%{_bindir}/ddrescue

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/dd_rescue

%changelog
* Sun Aug 29 2004 Dag Wieers <dag@wieers.com> - 1.04-1
- Updated to release 1.04.

* Tue Jan 27 2004 Dag Wieers <dag@wieers.com> - 1.03-0
- Initiale package. (using DAR)
