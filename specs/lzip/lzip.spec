# $Id$
# Authority: dag

Summary: Lossless LZMA-based data compression
Name: lzip
Version: 1.4
Release: 1
License: GPL
Group: Applications/File
URL: http://www.nongnu.org/lzip/lzip.html

Source: http://download.savannah.gnu.org/releases/lzip/lzip-%{version}.tar.gz
Patch1: lzip-0.3-fix_types.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-%{_arch}-root

BuildRequires: gcc-c++

%description
Lzip is a lossless data compressor based on the LZMA algorithm, with very safe
integrity checking and a user interface almost identical to the one of
bzip2. Lzip is only a data compressor, not an archiver. It has no facilities
for multiple files, encryption, or archive-splitting, but, in the Unix
tradition, relies instead on separate external utilities such as GNU Tar for
these tasks.

%prep
%setup
%patch1

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 doc/lzip.1 %{buildroot}%{_mandir}/man1/lzip.1

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir

%preun
/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_infodir}/lzip.info*
%doc %{_mandir}/man1/lzip.1*
%{_bindir}/lzip

%changelog
* Mon Jan 26 2009 Dag Wieers <dag@wieers.com> - 1.4-1
- Updated to release 1.4.

* Mon Dec 22 2008 Dag Wieers <dag@wieers.com> - 1.3-1
- Updated to release 1.3.

* Tue Nov 18 2008 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

* Tue Oct 14 2008 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Tue Sep 23 2008 Dag Wieers <dag@wieers.com> - 0.4-1
- Updated to release 0.4.

* Sat Sep 20 2008 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
