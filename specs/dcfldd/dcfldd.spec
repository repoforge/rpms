# $Id$
# Authority: dag

Summary: Improved dd, useful for forensics and security
Name: dcfldd
%define real_version 1.3.4-1
Version: 1.3.4.1
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://dcfldd.sourceforge.net/

Source: http://dl.sf.net/dcfldd/dcfldd-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, libstdc++-devel

%description
dcfldd is an enhanced version of GNU dd with features useful for forensics
and security. dcfldd has the following additional features:

   * Hashing on-the-fly - dcfldd can hash the input data as it is being
     transferred, helping to ensure data integrity.
   * Status output - dcfldd can update the user of its progress in terms of
     the amount of data transferred and how much longer operation will take.
   * Flexible disk wipes - dcfldd can be used to wipe disks quickly
     and with a known pattern if desired.
   * Image/wipe Verify - dcfldd can verify that a target drive is a
     bit-for-bit match of the specified input file or pattern.
   * Multiple outputs - dcfldd can output to multiple files or disks at
     the same time.
   * Split output - dcfldd can split output to multiple files with more
     configurability than the split command.
   * Piped output and logs - dcfldd can send all its log data and output
     to commands as well as files natively.

%prep
%setup -n %{name}-%{real_version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/dcfldd.1*
%{_bindir}/dcfldd

%changelog
* Thu Nov 01 2007 Dag Wieers <dag@wieers.com> - 1.3.4.1-1
- Initial package. (using DAR)
