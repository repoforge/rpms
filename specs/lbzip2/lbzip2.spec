# $Id$
# Authority: dag

Summary: Parallel implementation of the bzip2 file compressor
Name: lbzip2
Version: 0.20
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://phptest11.atw.hu/

### FIXME: Unique Source URL, remove and redownload file every time :-/
Source: lbzip2.tar.gz
Patch: lbzip2-0.10-oldgcc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bzip2-devel

%description
Lbzip2 is a pthreads-based parallel bzip2/bunzip2 filter, passable to
GNU tar with the --use-compress-program option. It isn't restricted
to regular files on input, nor output. Successful splitting for
decompression isn't guaranteed, just very likely (failure is detected).
Splitting in both modes and compression itself occur with an
approximate 900k block size. On an Athlon-64 X2 6000+, lbzip2 was
92% faster than standard bzip2 when compressing, and 45% faster when
decompressing (based on wall clock time). Lbzip2 strives to be
portable by requiring UNIX 98 APIs only, besides an unmodified libbz2.

%prep
%setup -n %{name}
%patch0 -p1 -b .oldgcc

%build
%{__make} CFLAGS="%{optflags} -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64 -D_XOPEN_SOURCE=500"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 lbzip2 %{buildroot}%{_bindir}/lbzip2
%{__install} -Dp -m0644 lbzip2.1 %{buildroot}%{_mandir}/man1/lbzip2.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog GPL-2.0 GPL-3.0 README
%doc %{_mandir}/man1/lbzip2.1*
%{_bindir}/lbzip2

%changelog
* Thu Dec 31 2009 Dag Wieers <dag@wieers.com> - 0.20-1
- Updated to release 0.20.

* Sat Dec 26 2009 Dag Wieers <dag@wieers.com> - 0.19-1
- Initial package. (using DAR)
