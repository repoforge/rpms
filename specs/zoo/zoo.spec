# $Id$

# Authority: dag

# Archs: i386 i686

Summary: file archiving utility with compression
Name: zoo
Version: 2.10
Release: 1
License: Distributable
Group: Applications/Archiving

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}-%{version}.tar.gz
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
%{__install} -d -m0755 %{buildroot}%{_bindir} \
	%{buildroot}%{_mandir}/man1

%{__install} -m0755 fiz zoo %{buildroot}%{_bindir}/
%{__install} -m0644 fiz.1 zoo.1 %{buildroot}%{_mandir}/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/*
%{_bindir}/*

%changelog
* Sat Dec 06 2003 Dag Wieers <dag@wieers.com> - 2.10-1
- Patch to build on RHFC1.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 2.10-0
- Initial package. (using DAR)
