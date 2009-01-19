# $Id$
# Authority: dag
# Upstream: Christophe Grenier <grenier$cgsecurity,org>

Summary: Decrypts password stored in cmos used to access BIOS SETUP
Name: cmospwd
Version: 5.0
Release: 1
License: GPL
Group: Applications/File
URL: http://www.cgsecurity.org/wiki/CmosPwd

Source: http://www.cgsecurity.org/cmospwd-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
cmospwd decrypts password stored in cmos used to access BIOS SETUP.
cmospwd works with the following BIOSes:

    ACER/IBM BIOS,
    AMI BIOS,
    AMI WinBIOS 2.5,
    Award 4.5x/4.6x/6.0,
    Compaq,
    IBM (PS/2, Activa, Thinkpad),
    Packard Bell,
    Phoenix (1.00.09.AC0 1994, a486 1.03, 1.04, 1.10 A03, 4.05 rev 1.02.943, 4.06 rev 1.13.1107, 4 release 6),
    Gateway Solo (Phoenix 4.0 release 6),
    Toshiba and
    Zenith AMI

With cmospwd, you can also backup, restore and erase/kill cmos. 

%prep
%setup

%build
%{__cc} %{optflags} -o cmospwd src/cmospwd.c


%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 cmospwd %{buildroot}%{_sbindir}/cmospwd

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING *.txt
%{_sbindir}/cmospwd

%changelog
* Thu May 22 2008 Dag Wieers <dag@wieers.com> - 5.0-1
- Updated to release 5.0.

* Wed Nov 08 2006 Dag Wieers <dag@wieers.com> - 4.8-1
- Initial package. (using DAR)
