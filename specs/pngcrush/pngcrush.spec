# $Id$
# Authority: dag
# Upstream: Glenn Randers-Pehrson <glennrp$users,sf,net>

Summary: Optimizer for PNG (Portable Network Graphics) files
Name: pngcrush
Version: 1.6.4
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
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -D -m0755 pngcrush %{buildroot}%{_bindir}/pngcrush

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt
%{_bindir}/pngcrush

%changelog
* Mon Jun 12 2006 Dag Wieers <dag@wieers.com> - 
- Initial package. (using DAR)
