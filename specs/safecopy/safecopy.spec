# $Id$
# Authority: dag

Summary: Data recovery tool
Name: safecopy
Version: 1.1
Release: 1
License: GPL
Group: Applications/System
URL: http://safecopy.sourceforge.net/

Source: http://dl.sf.net/safecopy/safecopy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
safecopy is a data recovery tool which tries to extract as much data a
possible from a seekable but problematic (i.e., damaged sectors) source like
floppy drives, hard disk partitions, CDs, etc., where other tools like dd 
would fail due to I/O errors.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/safecopy %{buildroot}%{_bindir}/safecopy

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/safecopy

%changelog
* Sun Feb 22 2009 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

* Sun Feb 08 2009 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Thu Nov 01 2007 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial packages. (using DAR)
