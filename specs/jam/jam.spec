# $Id$
# Authority: dag

Summary: Replacement for make
Name: jam
Version: 2.5
Release: 1%{?dist}
License: BSD-like
Group: Development/Tools
URL: http://public.perforce.com/public/jam/

Source: ftp://ftp.perforce.com/pub/jam/jam-%{version}.tar
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: byacc
Conflicts: boost-jam

%description
This is the Jam/MR program as published by Perforce. 

A powerful and highly customizable utility to build programs
and other things, that can run on Un*x, Nt, VMS, OS/2 and
Macintosh MPW, using portable Jamfiles. It can build large
projects spread across many directories in one pass. 

It takes some time to fully apprehend, especially when one's
already accustomed to make(1), but there's no comparison in
power when comparing these 2 tools.

%prep
%setup

%build
%{__make} CC="%{__cc}" CFLAGS="%{optflags}" CCFLAGS="%{optflags}" %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 bin.linux*/jam %{buildroot}%{_bindir}/jam
%{__install} -Dp -m0755 bin.linux*/mkjambase %{buildroot}%{_bindir}/mkjambase

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.html Porting README RELNOTES
%{_bindir}/jam
%{_bindir}/mkjambase

%changelog
* Mon Jul 27 2009 Dag Wieers <dag@wieers.com> - 2.5-1
- Initial package. (using DAR)
