# $Id$
# Authority: dag

Summary: File archiving utility with compression
Name: zoo
Version: 2.10
Release: 2.2%{?dist}
License: Distributable
Group: Applications/Archiving
URL: ftp://sunsite.unc.edu/pub/Linux/utils/compress/

Source: http://slackware.cs.utah.edu/slackware_source/a/bin/zoo-%{version}.tar.gz
Patch0: http://ftp.debian.org/debian/pool/non-free/z/zoo/zoo_2.10-9.diff.gz
Patch1: zoo-2.10-tempfile.patch
Patch2: zoo-2.10-gcc4.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
zoo is a file archiving utility for maintaining collections of files.
It uses Lempel-Ziv compression to provide space savings in the
range of 20 to 80 percent depending on the type of data. Written by
Rahul Dhesi, and posted to the USENET newsgroup comp.sources.misc.

%prep
%setup
%patch0 -p1 -b .debian
%patch1 -p1 -b .tempfile
%patch2 -p1 -b .gcc4

%build
%{__make} %{?_smp_mflags} linux OPTIM="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 fiz %{buildroot}%{_bindir}/fiz
%{__install} -Dp -m0755 zoo %{buildroot}%{_bindir}/zoo
%{__install} -Dp -m0644 fiz.1 %{buildroot}%{_mandir}/man1/fiz.1
%{__install} -Dp -m0644 zoo.1 %{buildroot}%{_mandir}/man1/zoo.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Copyright Install
%doc %{_mandir}/man1/fiz.1*
%doc %{_mandir}/man1/zoo.1*
%{_bindir}/fiz
%{_bindir}/zoo

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.10-2.2
- Rebuild for Fedora Core 5.

* Tue Apr 05 2005 Dag Wieers <dag@wieers.com> - 2.10-2
- Added gcc4 patch. (Adrian Reber)

* Sat Dec 06 2003 Dag Wieers <dag@wieers.com> - 2.10-1
- Patch to build on FC1.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 2.10-0
- Initial package. (using DAR)
