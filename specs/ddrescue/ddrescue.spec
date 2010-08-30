# $Id$
# Authority: dag
# Upstream: Antonio Diaz Diaz <ant_diaz$teleline,es>

Summary: Data recovery tool
Name: ddrescue
### Epoch to override Fedora Extras stupid decision to NOT ADHERE TO THEIR OWN NAMING CONVENTION
Epoch: 1
Version: 1.13
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.gnu.org/software/ddrescue/ddrescue.html

Source: http://ftp.gnu.org/gnu/ddrescue/ddrescue-%{version}.tar.gz
#Source: http://savannah.gnu.org/download/ddrescue/ddrescue-%{version}.tar.gz
Patch0: ddrescue-1.7-unistd.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
GNU ddrescue is a data recovery tool. It copies data from one file or block
device (hard disc, cdrom, etc) to another, trying hard to rescue data in
case of read errors.

Ddrescue does not truncate the output file if not asked to. So, every time
you run it on the same output file, it tries to fill in the gaps.

The basic operation of ddrescue is fully automatic. That is, you don't have
to wait for an error, stop the program, read the log, run it in reverse mode,
etc.

%prep
%setup
%patch0 -p0

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0644 doc/ddrescue.1 %{buildroot}%{_mandir}/man1/ddrescue.1

%post
if [ -e %{_infodir}/ddrescue.info.gz ]; then
    /sbin/install-info %{_infodir}/ddrescue.info.gz %{_infodir}/dir
fi

%preun
if [ -e %{_infodir}/ddrescue.info.gz ]; then
    /sbin/install-info --delete %{_infodir}/ddrescue.info.gz %{_infodir}/dir
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_infodir}/ddrescue.info.*
%doc %{_mandir}/man1/ddrescue.1*
%{_bindir}/ddrescue

%changelog
* Sun Aug 29 2010 Dag Wieers <dag@wieers.com> - 1.13-1
- Updated to release 1.13.

* Wed Apr 07 2010 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Tue Jul 14 2009 Dag Wieers <dag@wieers.com> - 1.11-1
- Updated to release 1.11.

* Mon Mar 02 2009 Dag Wieers <dag@wieers.com> - 1.10-1
- Updated to release 1.10.

* Tue Nov 18 2008 Dag Wieers <dag@wieers.com> - 1.9-1
- Updated to release 1.9.

* Tue Feb 26 2008 Dag Wieers <dag@wieers.com> - 1.8-1
- Updated to release 1.8.

* Mon Jan 07 2008 Dag Wieers <dag@wieers.com> - 1.7-1
- Updated to release 1.7.

* Fri Nov 16 2007 Dag Wieers <dag@wieers.com> - 1.6-1
- Updated to release 1.6.

* Mon Jul 02 2007 Dag Wieers <dag@wieers.com> - 1.5-1
- Updated to release 1.5.

* Wed Jun 20 2007 Dag Wieers <dag@wieers.com> - 1.4-1
- Updated to release 1.4.

* Tue Dec 19 2006 Dag Wieers <dag@wieers.com> - 1.3-1
- Updated to release 1.3.

* Thu Dec 08 2005 Dag Wieers <dag@wieers.com> - 1.0-2
- Added epoch to override Fedora Extras ddrescue (which really is dd_rescue).

* Fri Jul 15 2005 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
