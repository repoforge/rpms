# $Id$
# Authority: dag

Summary: Program for converting DAA files to ISO
Name: daa2iso
Version: 0.1.7b
Release: 1
License: GPL
Group: Applications/Archiving
URL: http://aluigi.altervista.org/mytoolz.htm

Source: http://aluigi.altervista.org/mytoolz/daa2iso.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel

%description
DAA2ISO is an open source command-line/GUI tool for converting single and
multipart DAA images to the original ISO format.

The DAA image (Direct Access Archive) in fact is just a compressed CD/DVD ISO
which can be created through the commercial program PowerISO.

%prep
%setup -c

%{__perl} -pi -e 's|\r||g' daa2iso.txt

%build
%{__make} -C src %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 src/daa2iso %{buildroot}%{_bindir}/daa2iso

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc daa2iso.txt
%{_bindir}/daa2iso

%changelog
* Tue Feb 03 2009 Dag Wieers <dag@wieers.com> - 0.1.7b-1
- Updated to release 0.1.7b.

* Mon Nov 17 2008 Dag Wieers <dag@wieers.com> - 0.1.7a-1
- Updated to release 0.1.7a.

* Sat Nov 08 2008 Dag Wieers <dag@wieers.com> - 0.1.6-1
- Initial package. (using DAR)
