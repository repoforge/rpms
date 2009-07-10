# $Id$
# Authority: dag
# Upstream: Glenn Randers-Pehrson <glennrp$users,sf,net>

Summary: Optimizer for PNG (Portable Network Graphics) files
Name: pngcrush
Version: 1.6.19
Release: 1
License: GPL
Group: Applications/File
URL: http://pmt.sourceforge.net/pngcrush/

Source: http://dl.sf.net/pmt/pngcrush-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpng-devel, zlib-devel

%description
pngcrush is an optimizer for PNG (Portable Network Graphics) files. It can be
run from a commandline in an MSDOS window, or from a UNIX or LINUX commandline.

Its main purpose is to reduce the size of the PNG IDAT datastream by trying
various compression levels an PNG filter methods. It also can be used to
remove unwanted ancillary chunks, or to add certain chunks including gAMA,
tRNS, iCCP, and textual chunks. 

%prep
%setup

%build
%{__make} %{?_smp_mflags} CC="%{__cc}" LD="%{__cc}"

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -D -m0755 pngcrush %{buildroot}%{_bindir}/pngcrush

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.html
%{_bindir}/pngcrush

%changelog
* Thu Jun 18 2009 Dag Wieers <dag@wieers.com> - 1.6.19-1
- Updated to release 1.6.19.

* Sun May 10 2009 Dag Wieers <dag@wieers.com> - 1.6.17-1
- Updated to release 1.6.17.

* Sun Feb 22 2009 Dag Wieers <dag@wieers.com> - 1.6.14-1
- Updated to release 1.6.14.

* Wed Aug 27 2008 Dag Wieers <dag@wieers.com> - 1.6.10-1
- Updated to release 1.6.10.

* Mon Jun 16 2008 Dag Wieers <dag@wieers.com> - 1.6.7-1
- Updated to release 1.6.7.

* Thu May 22 2008 Dag Wieers <dag@wieers.com> - 1.6.6-1
- Updated to release 1.6.6.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.6.5-1
- Updated to release 1.6.5.

* Mon Jun 12 2006 Dag Wieers <dag@wieers.com> - 1.6.4-1
- Initial package. (using DAR)
