# $Id: upx.spec 4308 2006-04-21 22:20:20Z dries $
# Authority: dag

Summary: The Ultimate Packer for eXecutables
Name: upx
Version: 3.03
Release: 1
License: GPL
Group: Applications/File
URL: http://upx.sourceforge.net/

Source: http://upx.sf.net/download/upx-%{version}-src.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ucl-devel >= 1.01
BuildRequires: perl
BuildRequires: gcc-c++
BuildRequires: make >= 3.80

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
%setup -n %{name}-%{version}-src
%{__perl} -pi -e ' s| -O2| |; s| -Werror||;' src/Makefile

%build
export CXXFLAGS="%{optflags}"
%{__make} %{?_smp_mflags} -C src
%{__make} -C doc

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/upx.out %{buildroot}%{_bindir}/upx
%{__install} -Dp -m0444 doc/upx.1 %{buildroot}%{_mandir}/man1/upx.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS COPYING LICENSE NEWS PROJECTS README* THANKS TODO doc/*.txt
%doc doc/upx.doc doc/upx.html
%doc %{_mandir}/man1/upx.1*
%{_bindir}/upx

%changelog
* Sun Nov 02 2008 Dag Wieers <dag@wieers.com> - 3.03-1
- Updated to release 3.03.

* Sat Nov 11 2006 Dag Wieers <dag@wieers.com> - 2.03-1
- Updated to release 2.03.

* Wed Oct 11 2006 Dag Wieers <dag@wieers.com> - 2.02-1
- Updated to release 2.02.

* Thu Jul 01 2004 Dag Wieers <dag@wieers.com> - 1.25-1
- Updated to release 1.25.

* Wed Oct 08 2003 Dag Wieers <dag@wieers.com> - 1.24-0
- Initial package. (using DAR)
