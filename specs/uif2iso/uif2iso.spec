# $Id$
# Authority: dag

Summary: Convert MagicISO UIF Files to ISO9660
Name: uif2iso
Version: 0.1.7c
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://aluigi.org/mytoolz.htm#uif2iso

Source: http://aluigi.org/mytoolz/uif2iso.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel
BuildRequires: unzip
BuildRequires: zlib-devel

%description
uif2iso is an open source command-line/GUI tool for converting single and
multipart UIF images to the original ISO format.

The UIF image (Universal Image Format) in fact is just a compressed CD/DVD
image which can be created through the commercial program MagicISO.

%prep
%setup -c %{name}-%{version}
%{__rm} -f *.exe

%build
%{__make} -C src %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/uif2iso %{buildroot}%{_bindir}/uif2iso

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc uif2iso.txt
%{_bindir}/uif2iso

%changelog
* Sun May 17 2009 Dag Wieers <dag@wieers.com> - 0.1.7c-1
- Updated to release 0.1.7c.

* Sat Nov 08 2008 Dag Wieers <dag@wieers.com> - 0.1.7-1
- Updated to release 0.1.7.

* Wed Nov 05 2008 Dag Wieers <dag@wieers.com> - 0.1.6-1
- Initial package. (using DAR)
