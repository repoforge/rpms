# $Id$
# Authority: dag

Summary: The Ultimate Packer for eXecutables
Name: upx
Version: 1.25
Release: 1.2%{?dist}
License: GPL
Group: Applications/File
URL: http://upx.sourceforge.net/

Source: http://upx.sf.net/download/upx-%{version}-src.tar.gz
#Source: http://dl.sf.net/upx/upx-%{version}-src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ucl-devel, perl, gcc-c++

%description
UPX is a free, portable, extendable, high-performance executable packer for
several different executable formats. It achieves an excellent compression
ratio and offers very fast decompression. Your executables suffer no memory
overhead or other drawbacks.

Programs and libraries compressed by UPX are completely self-contained
and run exactly as before, with no runtime or memory penalty for most
of the supported formats.

UPX supports a number of different executable formats, including
Win95/98/ME/NT/2000 programs and DLLs, DOS programs, and Linux executables.

%prep
%setup

%build
# Makefile is very fucked up.. so, let hack it even more :(
%{__perl} -pi.orig -e '
		s|\s+-Werror||;
		s|CC \+= -march=i386 -mcpu=i586|CFLAGS = %{optflags} -fexceptions|;
	' src/Makefile

export UCLDIR="%{_prefix}"
export CFLAGS="%{optflags}"
export LDFLAGS="%{optflags}"

%{__make} %{?_smp_mflags} -C src target="linux"
%{__make} -C doc

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/upx %{buildroot}%{_bindir}/upx
%{__install} -Dp -m0444 doc/upx.1 %{buildroot}%{_mandir}/man1/upx.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS COPYING LICENSE NEWS PROJECTS README* THANKS
%doc doc/upx.doc doc/upx.html
%doc %{_mandir}/man1/upx.1*
%{_bindir}/upx

%changelog
* Thu Jul 01 2004 Dag Wieers <dag@wieers.com> - 1.25-1
- Updated to release 1.25.

* Wed Oct 08 2003 Dag Wieers <dag@wieers.com> - 1.24-0
- Initial package. (using DAR)
