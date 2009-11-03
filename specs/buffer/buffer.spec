# $Id$
# Authority: dag

Summary: buffer program to speed up writing to tapes
Name: buffer
Version: 1.19
Release: 2%{?dist}
License: GPL
Group: Applications/Archiving
URL: http://hello-penguin.com/software.htm

Source: http://hello-penguin.com/software/buffer/buffer-%{version}.tar.gz
Patch0: buffer-1.19-destdir.patch
Patch1: buffer-1.19-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: i386 ia64 x86_64

%description
buffer is a program designed to speed up writing tapes on remote tape
drives.  Requirements are shared memory and locks which normally
means that these are supported in your kernel.

%prep
%setup
%patch0 -p0 -b .destdir
%patch1 -p0 -b .build

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%doc %{_mandir}/man1/buffer.1*
%{_bindir}/buffer

%changelog
* Sun Nov 11 2007 Dag Wieers <dag@wieers.com> - 1.19-2
- Fix group tag.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.19-1
- Initial package. (using DAR)
