# $Id$
# Authority: dag

##Archs: i386 i686 x86_64

Summary: file archiving utility with compression
Name: zoo
Version: 2.10
Release: 1
License: Distributable
Group: Applications/Archiving

Source: ftp://sunsite.unc.edu/pub/Linux/utils/compress/zoo-%{version}.tar.gz
Patch0: http://ftp.debian.org/debian/pool/non-free/z/zoo/zoo_2.10-9.diff.gz
Patch1: zoo-2.10-tempfile.patch
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

%build
%{__make} %{?_smp_mflags} OPTIM="%{optflags}" linux

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
%doc %{_mandir}/man1/*
%{_bindir}/*

%changelog
* Sat Dec 06 2003 Dag Wieers <dag@wieers.com> - 2.10-1
- Patch to build on FC1.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 2.10-0
- Initial package. (using DAR)
