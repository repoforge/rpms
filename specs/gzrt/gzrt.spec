# $Id$
# Authority: dag

Summary: Gzip recovery toolkit
Name: gzrt
Version: 0.5
Release: 1
License: GPL
Group: Applications/Archiving
URL: http://www.urbanophile.com/arenn/hacking/gzrt/gzrt.html

Source: http://www.urbanophile.com/arenn/hacking/gzrt/gzrt-%{version}.tar.gz
BuildRequires: zlib-devel

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The gzip recovery toolkit attempts to automate the recovery of data
from corrupted gzip files through a program called gzrecover.  This
package is very experimental at this point.

%prep
%setup

%build
%{__cc} %{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -lz -o gzrecover gzrecover.c

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 gzrecover %{buildroot}%{_bindir}/gzrecover

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%{_bindir}/gzrecover

%changelog
* Wed Nov 05 2008 Dag Wieers <dag@wieers.com> - 0.5-1
- Initial package. (using DAR)
